import pygame
import math


class MickeyHand:
    """
    Represents a Mickey Mouse-style gloved hand used as a clock hand.
    Drawn programmatically using geometric shapes.
    """

    def __init__(self, color=(255, 255, 255), glove_color=(255, 255, 255)):
        self.color = color
        self.glove_color = glove_color

    def draw(self, surface, center, angle_deg, length):
        """
        Draw a Mickey Mouse hand rotated around center point.
        angle_deg: 0 = pointing up, increases clockwise
        length: length of the arm in pixels
        """
        # Convert angle: 0=up, clockwise positive -> math angle
        angle_rad = math.radians(-angle_deg + 90)

        # Arm end point (tip of the hand)
        tip_x = center[0] + length * math.cos(angle_rad)
        tip_y = center[1] - length * math.sin(angle_rad)

        # Draw arm (thick line)
        arm_width = 8
        pygame.draw.line(surface, (80, 50, 30), center, (int(tip_x), int(tip_y)), arm_width)

        # Draw Mickey-style glove (circle with finger bumps)
        glove_radius = 22
        gx, gy = int(tip_x), int(tip_y)

        # Main glove circle (white)
        pygame.draw.circle(surface, self.glove_color, (gx, gy), glove_radius)
        pygame.draw.circle(surface, (0, 0, 0), (gx, gy), glove_radius, 2)  # outline

        # Finger bumps - 4 small circles on top of main glove
        finger_positions = [-20, -7, 7, 20]
        finger_perp_rad = math.radians(-angle_deg + 90 + 90)  # perpendicular direction

        for offset in finger_positions:
            fx = gx + offset * math.cos(finger_perp_rad) + 10 * math.cos(angle_rad)
            fy = gy - offset * math.sin(finger_perp_rad) - 10 * math.sin(angle_rad)
            pygame.draw.circle(surface, self.glove_color, (int(fx), int(fy)), 10)
            pygame.draw.circle(surface, (0, 0, 0), (int(fx), int(fy)), 10, 2)

        # Stitch lines on glove (decorative)
        stitch1_x = gx + 8 * math.cos(finger_perp_rad)
        stitch1_y = gy - 8 * math.sin(finger_perp_rad)
        stitch2_x = gx - 8 * math.cos(finger_perp_rad)
        stitch2_y = gy + 8 * math.sin(finger_perp_rad)
        pygame.draw.line(surface, (180, 180, 180), (int(stitch1_x), int(stitch1_y)),
                         (int(stitch2_x), int(stitch2_y)), 1)


class MickeysClock:
    """
    Mickey Mouse Clock - displays minutes and seconds using Mickey's hands.
    Right hand = minutes hand
    Left hand = seconds hand
    """

    def __init__(self, screen_width=600, screen_height=600):
        self.width = screen_width
        self.height = screen_height
        self.center = (screen_width // 2, screen_height // 2)
        self.clock_radius = 220

        # Hand lengths
        self.minute_hand_length = 160
        self.second_hand_length = 180

        # Create hand objects
        self.minute_hand = MickeyHand(glove_color=(255, 255, 255))
        self.second_hand = MickeyHand(glove_color=(255, 220, 50))

        # Load font for digital time display
        pygame.font.init()
        self.font_large = pygame.font.SysFont("Arial", 48, bold=True)
        self.font_small = pygame.font.SysFont("Arial", 24)

    def _draw_clock_face(self, surface):
        """Draw the main clock face with Mickey Mouse style."""
        cx, cy = self.center
        r = self.clock_radius

        # Outer glow effect
        for i in range(5):
            glow_color = (255, 200 - i * 30, 50 - i * 5)
            pygame.draw.circle(surface, glow_color, self.center, r + 15 - i * 2, 3)

        # Main clock face - cream/yellow Mickey style
        pygame.draw.circle(surface, (255, 250, 220), self.center, r)
        pygame.draw.circle(surface, (0, 0, 0), self.center, r, 4)

        # Decorative inner ring
        pygame.draw.circle(surface, (200, 180, 100), self.center, r - 15, 2)

        # Hour markers (12 markers)
        for i in range(60):
            marker_angle = math.radians(i * 6 - 90)
            if i % 5 == 0:
                # Hour marker - longer
                inner = r - 30
                outer = r - 10
                width = 4
                color = (50, 30, 10)
            else:
                # Minute marker - shorter
                inner = r - 18
                outer = r - 8
                width = 1
                color = (150, 130, 80)

            x1 = cx + inner * math.cos(marker_angle)
            y1 = cy + inner * math.sin(marker_angle)
            x2 = cx + outer * math.cos(marker_angle)
            y2 = cy + outer * math.sin(marker_angle)
            pygame.draw.line(surface, color, (int(x1), int(y1)), (int(x2), int(y2)), width)

        # Hour numbers
        hour_font = pygame.font.SysFont("Arial", 28, bold=True)
        for i in range(1, 13):
            angle = math.radians(i * 30 - 90)
            num_r = r - 55
            nx = cx + num_r * math.cos(angle)
            ny = cy + num_r * math.sin(angle)
            num_surf = hour_font.render(str(i), True, (40, 20, 5))
            num_rect = num_surf.get_rect(center=(int(nx), int(ny)))
            surface.blit(num_surf, num_rect)

        # Mickey Mouse ears (two circles on top)
        ear_radius = 55
        left_ear_center = (cx - 145, cy - 175)
        right_ear_center = (cx + 145, cy - 175)

        pygame.draw.circle(surface, (20, 20, 20), left_ear_center, ear_radius)
        pygame.draw.circle(surface, (20, 20, 20), right_ear_center, ear_radius)

        # Mickey face elements
        # Eyes
        pygame.draw.circle(surface, (20, 20, 20), (cx - 45, cy - 35), 15)
        pygame.draw.circle(surface, (20, 20, 20), (cx + 45, cy - 35), 15)
        pygame.draw.circle(surface, (255, 255, 255), (cx - 40, cy - 40), 6)
        pygame.draw.circle(surface, (255, 255, 255), (cx + 50, cy - 40), 6)

        # Nose
        pygame.draw.ellipse(surface, (20, 20, 20),
                            (cx - 18, cy - 8, 36, 22))

        # Smile
        pygame.draw.arc(surface, (20, 20, 20),
                        (cx - 55, cy, 110, 50), math.pi, 2 * math.pi, 4)

        # "MM" text on clock
        mm_surf = self.font_small.render("MICKEY", True, (180, 100, 0))
        mm_rect = mm_surf.get_rect(center=(cx, cy + 65))
        surface.blit(mm_surf, mm_rect)

    def _draw_labels(self, surface):
        """Draw labels for hands."""
        cx, cy = self.center
        # Minutes label
        min_label = self.font_small.render("MIN →", True, (255, 255, 255))
        surface.blit(min_label, (20, self.height - 80))

        # Seconds label
        sec_label = self.font_small.render("SEC →", True, (255, 220, 50))
        surface.blit(sec_label, (20, self.height - 50))

        # Glove legend
        pygame.draw.circle(surface, (255, 255, 255), (100, self.height - 72), 10)
        pygame.draw.circle(surface, (255, 220, 50), (100, self.height - 42), 10)

    def draw(self, surface, minutes, seconds):
        """
        Main draw method. 
        minutes: 0-59
        seconds: 0-59
        """
        # Calculate rotation angles
        # 0 minutes/seconds = pointing up (12 o'clock)
        # Full rotation = 60 steps
        minute_angle = minutes * 6  # 360/60 = 6 degrees per minute
        second_angle = seconds * 6  # 6 degrees per second

        # Draw clock face
        self._draw_clock_face(surface)

        # Draw second hand (yellow glove) - behind minute hand
        self.second_hand.draw(surface, self.center, second_angle, self.second_hand_length)

        # Draw minute hand (white glove) - on top
        self.minute_hand.draw(surface, self.center, minute_angle, self.minute_hand_length)

        # Center cap (black circle)
        pygame.draw.circle(surface, (20, 20, 20), self.center, 12)
        pygame.draw.circle(surface, (80, 80, 80), self.center, 12, 2)

        # Draw labels
        self._draw_labels(surface)

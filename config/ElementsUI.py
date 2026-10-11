import pygame

COLOR_BG = (24, 28, 36)
COLOR_PANEL = (32, 38, 50)
COLOR_PANEL_HEADER = (42, 50, 66)
COLOR_ACCENT = (0, 160, 255)
COLOR_ACCENT_HOVER = (40, 180, 255)
COLOR_TEXT = (235, 240, 245)
COLOR_MUTED = (150, 160, 175)
COLOR_SUCCESS = (45, 200, 120)
COLOR_WARNING = (255, 170, 0)
COLOR_DANGER = (240, 70, 70)


class Button:
    def __init__(self, rect, text, callback=None, color=COLOR_PANEL_HEADER, hover_color=COLOR_ACCENT, text_color=COLOR_TEXT, active=False, font_size=14):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.callback = callback
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.active = active
        self.font = pygame.font.Font(None, font_size)
        self.is_hovered = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.callback:
                    self.callback()
                return True
        return False

    def draw(self, surface):
        bg = self.hover_color if (self.is_hovered or self.active) else self.color
        pygame.draw.rect(surface, bg, self.rect, border_radius=5)
        border_col = COLOR_ACCENT if self.active else ((100, 120, 150) if self.is_hovered else (60, 70, 90))
        pygame.draw.rect(surface, border_col, self.rect, width=1, border_radius=5)

        lbl = self.font.render(self.text, True, self.text_color)
        lbl_rect = lbl.get_rect(center=self.rect.center)
        surface.blit(lbl, lbl_rect)


class Checkbox:
    def __init__(self, rect, label, initial_val=False, callback=None):
        self.rect = pygame.Rect(rect)
        self.box_rect = pygame.Rect(self.rect.x, self.rect.y + 2, 16, 16)
        self.label = label
        self.checked = initial_val
        self.callback = callback
        self.font = pygame.font.Font(None, 14)
        self.is_hovered = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.checked = not self.checked
                if self.callback:
                    self.callback(self.checked)
                return True
        return False

    def draw(self, surface):
        bg = COLOR_ACCENT if self.checked else (40, 48, 62)
        pygame.draw.rect(surface, bg, self.box_rect, border_radius=3)
        pygame.draw.rect(surface, COLOR_ACCENT if self.is_hovered else (80, 95, 120), self.box_rect, width=1, border_radius=3)

        if self.checked:
            pygame.draw.line(surface, (255, 255, 255), (self.box_rect.x + 3, self.box_rect.y + 8), (self.box_rect.x + 6, self.box_rect.y + 12), 2)
            pygame.draw.line(surface, (255, 255, 255), (self.box_rect.x + 6, self.box_rect.y + 12), (self.box_rect.x + 12, self.box_rect.y + 4), 2)

        lbl = self.font.render(self.label, True, COLOR_TEXT)
        surface.blit(lbl, (self.box_rect.right + 8, self.rect.y + 2))


class Slider:
    def __init__(self, rect, min_val, max_val, initial_val, label="", step=0.1, callback=None):
        self.rect = pygame.Rect(rect)
        self.min_val = min_val
        self.max_val = max_val
        self.value = initial_val
        self.label = label
        self.step = step
        self.callback = callback
        self.is_dragging = False
        self.font = pygame.font.Font(None, 14)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.is_dragging = True
                self.update_val_from_mouse(event.pos[0])
                return True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.is_dragging:
                self.is_dragging = False
                return True
        elif event.type == pygame.MOUSEMOTION and self.is_dragging:
            self.update_val_from_mouse(event.pos[0])
            return True
        return False

    def update_val_from_mouse(self, mouse_x):
        rel_x = max(0, min(self.rect.width, mouse_x - self.rect.x))
        ratio = rel_x / float(self.rect.width)
        raw_val = self.min_val + ratio * (self.max_val - self.min_val)
        if self.step > 0:
            raw_val = round(raw_val / self.step) * self.step
        self.value = max(self.min_val, min(self.max_val, raw_val))
        if self.callback:
            self.callback(self.value)

    def draw(self, surface):
        lbl_str = f"{self.label}: {self.value:.1f}" if isinstance(self.value, float) else f"{self.label}: {int(self.value)}"
        lbl = self.font.render(lbl_str, True, COLOR_TEXT)
        surface.blit(lbl, (self.rect.x, self.rect.y - 14))

        # Track line
        track_y = self.rect.y + self.rect.height // 2
        pygame.draw.line(surface, (50, 60, 80), (self.rect.x, track_y), (self.rect.right, track_y), 4)

        ratio = (self.value - self.min_val) / float(self.max_val - self.min_val) if self.max_val > self.min_val else 0
        handle_x = int(self.rect.x + ratio * self.rect.width)
        pygame.draw.line(surface, COLOR_ACCENT, (self.rect.x, track_y), (handle_x, track_y), 4)
        pygame.draw.circle(surface, COLOR_ACCENT_HOVER if self.is_dragging else COLOR_TEXT, (handle_x, track_y), 6)


class TextInput:
    def __init__(self, rect, initial_text="", placeholder="Enter text...", callback=None):
        self.rect = pygame.Rect(rect)
        self.text = initial_text
        self.placeholder = placeholder
        self.callback = callback
        self.active = False
        self.font = pygame.font.Font(None, 14)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.active = self.rect.collidepoint(event.pos)
            return self.active
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.active = False
                if self.callback:
                    self.callback(self.text)
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                if len(event.unicode) > 0 and event.unicode.isprintable():
                    self.text += event.unicode
            return True
        return False

    def draw(self, surface):
        bg = (40, 50, 65) if self.active else (30, 36, 48)
        pygame.draw.rect(surface, bg, self.rect, border_radius=4)
        border = COLOR_ACCENT if self.active else (60, 75, 95)
        pygame.draw.rect(surface, border, self.rect, width=1, border_radius=4)

        disp_text = self.text if self.text else self.placeholder
        color = COLOR_TEXT if self.text else COLOR_MUTED
        lbl = self.font.render(disp_text, True, color)
        surface.blit(lbl, (self.rect.x + 6, self.rect.y + (self.rect.height - lbl.get_height()) // 2))

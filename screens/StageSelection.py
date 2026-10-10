from config import constants
import pygame
from config.constants import SCREEN_SIZE, FONT_SIZE_LARGE, FONT_SIZE_NORMAL


class StageSelection(pygame.surface.Surface):
    def __init__(self):
        super().__init__(SCREEN_SIZE)
        self.title_font = pygame.font.Font(None, 48)
        self.subtitle_font = pygame.font.Font(None, 22)
        self.card_title_font = pygame.font.Font(None, 26)
        self.desc_font = pygame.font.Font(None, 18)
        self.button_font = pygame.font.Font(None, 20)
        self.badge_font = pygame.font.Font(None, 16)

        self.back_button = pygame.Rect(50, 35, 120, 42)
        self.back_hovered = False

        self.stage_one_thumb = None
        try:
            img = pygame.image.load("./assets/StageOneMap.png").convert()
            self.stage_one_thumb = pygame.transform.smoothscale(img, (300, 150))
        except Exception:
            self.stage_one_thumb = None

        self.stages = [
            {
                "id": "stage_one",
                "stage_num": "STAGE 01",
                "name": "Warants",
                "difficulty": "EASY",
                "diff_color": (46, 204, 113),
                "description": "The war has begun, defend the first battlefield.",
                "rect": pygame.Rect(90, 130, 340, 480),
                "play_btn": pygame.Rect(110, 540, 300, 48),
                "hovered": False,
                "btn_hovered": False,
                "accent_color": 'royalblue1',
                "bg_accent": 'royalblue4',
                "thumb_type": "one"
            },
            {
                "id": "stage_two",
                "stage_num": "STAGE 02",
                "name": "Waraid",
                "difficulty": "MEDIUM",
                "diff_color": (241, 196, 15),
                "description": "Aid the royal guards from the raid.",
                "rect": pygame.Rect(470, 130, 340, 480),
                "play_btn": pygame.Rect(490, 540, 300, 48),
                "hovered": False,
                "btn_hovered": False,
                "accent_color": 'orange1',
                "bg_accent": 'orange4',
                "thumb_type": "two"
            },
            {
                "id": "stage_three",
                "stage_num": "STAGE 03",
                "name": "Warpath",
                "difficulty": "HARD",
                "diff_color": (231, 76, 60),
                "description": "The war has reached its peak. Defend the last and only path. ",
                "rect": pygame.Rect(850, 130, 340, 480),
                "play_btn": pygame.Rect(870, 540, 300, 48),
                "hovered": False,
                "btn_hovered": False,
                "accent_color": 'tomato1',
                "bg_accent": 'tomato4',
                "thumb_type": "three"
            }
        ]

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            pos = event.pos
            self.back_hovered = self.back_button.collidepoint(pos)
            for stage in self.stages:
                stage["hovered"] = stage["rect"].collidepoint(pos)
                stage["btn_hovered"] = stage["play_btn"].collidepoint(pos)

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = event.pos
            if self.back_button.collidepoint(pos):
                return "main_menu"

            for stage in self.stages:
                if stage["play_btn"].collidepoint(pos) or stage["rect"].collidepoint(pos):
                    return stage["id"]

        return "stage_selection"

    def _render_thumbnail(self, stage, thumb_rect):
        if stage["thumb_type"] == "one" and self.stage_one_thumb:
            self.blit(self.stage_one_thumb, thumb_rect.topleft)
            pygame.draw.rect(self, (60, 80, 100), thumb_rect, width=1, border_radius=4)
            return

        pygame.draw.rect(self, stage["bg_accent"], thumb_rect, border_radius=6)

        pygame.draw.rect(self, 'grey', thumb_rect, width=1, border_radius=6)

    def draw(self):
        self.fill((18, 22, 28))

        for x in range(0, SCREEN_SIZE[0], 40):
            for y in range(0, SCREEN_SIZE[1], 40):
                self.set_at((x, y), (30, 36, 46))

        title_surface = self.title_font.render("SELECT STAGE", True, 'white')
        title_rect = title_surface.get_rect(center=(SCREEN_SIZE[0] // 2, 50))
        self.blit(title_surface, title_rect)

        subtitle_surface = self.subtitle_font.render("Choose your path to defend against the red colony", True, 'lightgray')
        subtitle_rect = subtitle_surface.get_rect(center=(SCREEN_SIZE[0] // 2, 85))
        self.blit(subtitle_surface, subtitle_rect)

        btn_bg = 'gray20' if self.back_hovered else 'gray20'
        btn_border = 'cyan' if self.back_hovered else 'gray30'
        pygame.draw.rect(self, btn_bg, self.back_button, border_radius=6)
        pygame.draw.rect(self, btn_border, self.back_button, width=2, border_radius=6)
        back_text = self.button_font.render("Back", True, 'white')
        back_text_rect = back_text.get_rect(center=self.back_button.center)
        self.blit(back_text, back_text_rect)

        for stage in self.stages:
            card_rect = stage["rect"]
            is_hovered = stage["hovered"]
            is_btn_hovered = stage["btn_hovered"]

            card_bg = (38, 46, 60) if is_hovered else (28, 34, 46)
            pygame.draw.rect(self, card_bg, card_rect, border_radius=12)

            border_color = stage["accent_color"] if is_hovered else (55, 68, 88)
            border_width = 2 if is_hovered else 1
            pygame.draw.rect(self, border_color, card_rect, width=border_width, border_radius=12)

            num_surface = self.desc_font.render(stage["stage_num"], True, stage["accent_color"])
            self.blit(num_surface, (card_rect.x + 20, card_rect.y + 18))

            difficulty_text = self.badge_font.render(stage["difficulty"], True, (255, 255, 255))
            badge_w = difficulty_text.get_width() + 16
            badge_h = 22
            badge_rect = pygame.Rect(card_rect.right - badge_w - 20, card_rect.y + 14, badge_w, badge_h)
            pygame.draw.rect(self, stage["diff_color"], badge_rect, border_radius=4)
            diff_text_rect = difficulty_text.get_rect(center=badge_rect.center)
            self.blit(difficulty_text, diff_text_rect)

            thumb_rect = pygame.Rect(card_rect.x + 20, card_rect.y + 45, 300, 150)
            self._render_thumbnail(stage, thumb_rect)

            name_surface = self.card_title_font.render(stage["name"], True, (240, 245, 250))
            self.blit(name_surface, (card_rect.x + 20, card_rect.y + 210))

            pygame.draw.line(self, (50, 62, 80), (card_rect.x + 20, card_rect.y + 242), (card_rect.right - 20, card_rect.y + 242), 1)

            words = stage["description"].split(" ")
            line = ""
            desc_y = card_rect.y + 260
            for word in words:
                test_line = f"{line} {word}".strip()
                test_surface = self.desc_font.render(test_line, True, (160, 175, 195))
                if test_surface.get_width() > 300:
                    rendered_line = self.desc_font.render(line, True, (160, 175, 195))
                    self.blit(rendered_line, (card_rect.x + 20, desc_y))
                    desc_y += 20
                    line = word
                else:
                    line = test_line
            if line:
                rendered_line = self.desc_font.render(line, True, (160, 175, 195))
                self.blit(rendered_line, (card_rect.x + 20, desc_y))

            # Play Button
            play_btn_rect = stage["play_btn"]
            btn_color = stage["accent_color"] if (is_btn_hovered or is_hovered) else (45, 55, 72)
            pygame.draw.rect(self, btn_color, play_btn_rect, border_radius=8)
            if not (is_btn_hovered or is_hovered):
                pygame.draw.rect(self, stage["accent_color"], play_btn_rect, width=1, border_radius=8)

            btn_label_color = (255, 255, 255) if (is_btn_hovered or is_hovered) else (200, 215, 230)
            btn_surface = self.button_font.render("PLAY", True, btn_label_color)
            btn_surface_rect = btn_surface.get_rect(center=play_btn_rect.center)
            self.blit(btn_surface, btn_surface_rect)

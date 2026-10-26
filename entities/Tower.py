import pygame

class TowerOptions(pygame.surface.Surface):
    def __init__(self, position):
        super().__init__((400, 200))
        self.is_open = False

        self.tower_icons_assets = ["./assets/bow-frame.png"]
        self.bow_frame_img = pygame.image.load(self.tower_icons_assets[0]).convert_alpha()
        self.bow_frame_img = pygame.transform.scale(self.bow_frame_img, (50, 50))
        self.bow_frame_rect = self.bow_frame_img.get_rect(midtop=position)

    def set_position(self, position):
        self.bow_frame_rect.midtop = position

    def draw(self, screen):
        if not self.is_open:
            return
        screen.blit(self.bow_frame_img, self.bow_frame_rect)

class Tower(pygame.sprite.Sprite):
    current_open_options_surface = None

    def __init__(self, slot_id, position):
        super().__init__()
        self.tower_slot_assets = ["./assets/tower_slot-1.png","./assets/tower_slot-2.png"]
        self.frames = [pygame.image.load(self.tower_slot_assets[frame]).convert_alpha() for frame in range(len(self.tower_slot_assets))]
        self.animation_index = 0
        self.animation_speed = 0.1

        self.name = 'none'
        self.damage = 0
        self.range = 0
        self.cooldown = 0

        self.last_shot_time = 0
        self.image = self.frames[self.animation_index]

        self.rect = self.image.get_rect()
        self.rect.center = position

        self.options_surface = TowerOptions((self.rect.centerx, self.rect.bottom + 5))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                print(f"Tower slot {self.rect.center} clicked.")

                if Tower.current_open_options_surface:
                    Tower.current_open_options_surface.is_open = False
                    
                self.options_surface.is_open = True
                Tower.current_open_options_surface = self.options_surface

    def set_tower_properties(self, name, damage, range, cooldown):
        self.name = name
        self.damage = damage
        self.range = range
        self.cooldown = cooldown

    def show_options(self, screen):
        if self.options_surface.is_open and Tower.current_open_options_surface == self.options_surface:
            self.options_surface.draw(screen)

    def is_enemy_in_range(self, enemy):
        distance = ((self.rect.x - enemy.rect.x) ** 2 + (self.rect.y - enemy.rect.y) ** 2) ** 0.5
        return distance <= self.range

    def update(self, enemies,  *args, **kwargs):
        current_time = pygame.time.get_ticks()
        self.animation_index += self.animation_speed
        if self.animation_index >= len(self.frames):
            self.animation_index = 0

        self.image = self.frames[int(self.animation_index)]
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect(center=self.rect.center)
        self.options_surface.set_position((self.rect.centerx, self.rect.bottom - 40))

        if self.name == 'none':
            return
        
        for enemy in enemies:
            if not self.is_enemy_in_range(enemy):
                continue
                
            if current_time - self.last_shot_time >= self.cooldown:
                print(f"{self.name} shooting at {enemy.name}")
                enemy.take_damage(self.damage)
                self.last_shot_time = current_time
class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        # self.bg_color = (230, 230, 230) # grey screen background
        # self.bg_color = (70, 140, 70) # dark-green screen background
        self.bg_color = (48, 20, 58) # dark-violet screen background
        
        # Bullet settings
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (200, 0, 14)
        self.bullets_allowed = 3
        
        # Alien settings
        self.fleet_drop_speed = 6
        
        # Ship settings
        self.ship_limit = 3

        # How quickly the game speed up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 0.5

        # fleet_direction of 1 represents right: -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien points values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)


class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        # self.bg_color = (230, 230, 230) # grey screen background
        # self.bg_color = (70, 140, 70) # dark-green screen background
        self.bg_color = (48, 20, 58) # dark-violet screen background
        
        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (200, 0, 14)
        self.bullets_allowed = 3
        
        # Alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 6
        # fleet_direction of 1 represents right: -1 represents left.
        self.fleet_direction = 1

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3
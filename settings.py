class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        # self.bg_color = (230, 230, 230) # grey screen background
        self.bg_color = (70, 140, 70) # dark-green screen background
        
        # Ship settings
        self.ship_speed = 1.5
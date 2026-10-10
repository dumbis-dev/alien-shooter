class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1080
        self.screen_height = 800
        self.bg_color = (55,50,185)

        # Ship's settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (255, 24, 1)
        self.bullets_allowed = 5

        # Alien settings
        self.fleet_drop_speed = 10
    
        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quikcly the alien points values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 7
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        # fleet_direction of 1 represetns right; -1 represents left
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        

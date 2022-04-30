class Settings:
    #a class to store all settings for Alien invasion"

    def __init__(self):
        #initialize game settings

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed = 1.5
        self.ship_limit = 3

            #bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 4.5
        self.bullet_height = 20
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 100

        #alien settings
        self.alien_speed = 1.0 
        self.fleet_drop_speed = 5
        #fleet direction of 1 represents right -1 left
        self.fleet_direction = 1

        #how qickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #initialize settings throughout the game
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1
        
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
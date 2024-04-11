import math
class Rover:
    def __init__(self, initial_x=0, initial_y=0, initial_heading=0):
        self.x = initial_x  # Initial x-coordinate
        self.y = initial_y  # Initial y-coordinate
        self.heading = initial_heading  # Initial heading (in degrees)

    def move(self, distance, angle):
        # Update position based on distance moved and angle turned
        self.x += distance * math.cos(math.radians(self.heading + angle))
        self.y += distance * math.sin(math.radians(self.heading + angle))

    def update_heading(self, new_heading):
        # Update heading
        self.heading = new_heading % 360
    def locate(self):
        rovposition=[self.x,self.y]
        rovheading=self.heading
        return rovposition, rovheading
        

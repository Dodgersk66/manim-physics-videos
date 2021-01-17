from manimlib.imports import *
import random

class Intro(Scene):
    def construct(self):
        Logo = ImageMobject("./Images/StelloGoldenrodLogo.png")
        Logo.scale(2.4)
        

        for i in range(0,20):
            star = ImageMobject("./Images/star.png")
            star.scale(0.05)
            star.move_to(random.randrange(-8,8) * RIGHT + random.randrange(-4,4) * UP)
            self.add(star)
            self.wait(0.2)
        
        self.add(Logo)
        self.wait(1)
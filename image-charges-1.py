from manimlib.imports import *

class Charge(VGroup):
    CONFIG = {
        "radius": 0.5,
        "stroke_width" : 0,
        "fill_opacity": 1.0,
        "color" : "#D63647",
        "sheen_direction": UL,
        "sheen_factor": 0.8,
    }
    def __init__(self, point = ORIGIN, positive = True,**kwargs):
        super().__init__(**kwargs)
        charge = Circle(arc_center = point, radius = self.radius, stroke_width = self.stroke_width, fill_opacity = self.fill_opacity, color = self.color, sheen_direction = self.sheen_direction, sheen_factor = self.sheen_factor)
        
        
        symbol = TextMobject("+")
        if(positive):
            symbol = TextMobject("+",stroke_width = 2.0)
        else:
            symbol = TextMobject("-",stroke_width=2.0)
        
        symbol.set_color(BLACK)
        symbol.move_to(point)
        
        VGroup.__init__(self,charge, symbol)

#class LineOfCharge(VGroup):


class InIntroPhysics(Scene):
    def construct(self):
        for i in range(-7,8):
                for j in range(-4,5):
                    locDot = Dot()
                    locDot.move_to(RIGHT*i + UP*j)
                    self.add(locDot)
        
        force1 = Arrow(start = 4 * LEFT, end = 2* LEFT)
        force2 = Arrow(start = 4 * RIGHT, end = 2* RIGHT)
        
        charge1 = Charge(4 * RIGHT, True)
        charge2 = Charge(4 * LEFT, False)

        

        coulombLaw = TexMobject("\\vec{F}", "= \\frac{1}{4\\pi \\epsilon_0}","\\frac{q_1 q_2}{r^2}","\\hat{r}")
        coulombLaw.move_to(2 * DOWN)
        coulombLaw.set_color_by_tex_to_color_map({
            "\\vec{F}" : YELLOW,
            "\\frac{q_1 q_2}{r^2}" : BLUE,
            "\\hat{r}" : YELLOW
        })

        
        self.play(GrowArrow(force1),GrowArrow(force2),FadeIn(charge1),FadeIn(charge2),run_time = 1.5,rate_func = rush_from)
        self.wait(0.5)
        self.play(Write(coulombLaw),run_time = 5)

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

class LineOfCharge(VGroup):
    CONFIG = {
        "width" : 1.0,
        "height": 4.0,
        "fill_opacity" : 1.0,
        "color" : "#D63647",
        "sheen_direction": LEFT,
        "sheen_factor": 0.8,
    }
    def __init__(self, bro = ORIGIN, direction = UP, positive =  True, **kwargs):
        super().__init__(**kwargs)
        if(all(direction == UP)):
            line = Rectangle(stroke_width = 0, fill_color = self.color, height = self.height * 2, width =self.width,fill_opacity = self.fill_opacity, sheen_direction = self.sheen_direction, sheen_factor = self.sheen_factor)
            line.move_to(bro)
            chargeLabels =  []
            for i  in range(int(-1 * self.height),int(self.height)):
                symbol = TextMobject("+")
                if(positive):
                    symbol = TextMobject("+",stroke_width = 2.0)
                else:
                    symbol = TextMobject("-",stroke_width=2.0)
                
                symbol.set_color(BLACK)
                symbol.move_to(bro + i * UP + 0.5 * UP)
                chargeLabels.append(symbol)
            VGroup.__init__(self, line, *chargeLabels)
        else:
            line = Rectangle(stroke_width = 0, fill_color = self.color, height = self.width, width =self.height * 2,fill_opacity = self.fill_opacity, sheen_direction = self.sheen_direction, sheen_factor = self.sheen_factor)
            line.move_to(bro)
            chargeLabels =  []
            for i  in range(int(-1 * self.height),int(self.height)):
                symbol = TextMobject("+")
                if(positive):
                    symbol = TextMobject("+",stroke_width = 2.0)
                else:
                    symbol = TextMobject("-",stroke_width=2.0)
                
                symbol.set_color(BLACK)
                symbol.move_to(bro + i * RIGHT+ 0.5 * RIGHT)
                chargeLabels.append(symbol)
            VGroup.__init__(self, line, *chargeLabels)
class PlaneOfCharge(LineOfCharge):
    CONFIG = {
        "width" : 1.0,
        "height": 4.0,
        "fill_opacity" : 1.0,
        "color" : "#EBA49B",
        "sheen_direction": LEFT,
        "sheen_factor": 0,
    }
    def __init__(self,point = ORIGIN, pos = True, direc = RIGHT,**kwargs):
        LineOfCharge.__init__(self,bro = point, direction = direc, positive = pos, **kwargs)


class InIntroPhysics(Scene):
    def construct(self):
        for i in range(-7,8):
                for j in range(-4,5):
                    locDot = Dot()
                    locDot.move_to(RIGHT*i + UP*j)
                    self.add(locDot)
        
        force1 = Arrow(start = 4 * LEFT, end = 2* LEFT)
        force2 = Arrow(start = 4 * RIGHT, end = 2* RIGHT)
        force3 = Arrow(start = ORIGIN, end = 2* RIGHT)
        force4 = Arrow(start = 3 * DOWN, end = DOWN)
        force5 = Arrow(start = 3 * UP, end = UP)
        
        charge1 = Charge(4 * RIGHT, True)
        charge2 = Charge(4 * LEFT, False)
        charge3 = Charge(3 * UP,True)

        

        coulombLaw = TexMobject("\\vec{F}", "= \\frac{1}{4\\pi \\epsilon_0}","\\frac{q_1 q_2}{r^2}","\\hat{r}")
        coulombLaw.move_to(2 * DOWN)
        coulombLaw.set_color_by_tex_to_color_map({
            "\\vec{F}" : YELLOW,
            "\\frac{q_1 q_2}{r^2}" : BLUE,
            "\\hat{r}" : YELLOW
        })

        gaussLaw = TexMobject("\\oiint","\\vec{E}", "\cdot d", "\\vec{A}", "=","\\frac{q_{enc}}{\\epsilon_0}")
        gaussLaw.move_to(4 * LEFT)
        gaussLaw.set_color_by_tex_to_color_map({
            "\\vec{E}" : YELLOW,
            "\\vec{A}" : RED,
            "\\frac{q_{enc}}{\\epsilon_0}" : BLUE
        })

        lineCharge = LineOfCharge(positive = False)
        plane = PlaneOfCharge(height = 8,pos = False, point = 3 * DOWN)


        
        self.play(GrowArrow(force1),GrowArrow(force2),FadeIn(charge1),FadeIn(charge2),run_time = 1.5,rate_func = rush_from)
        self.wait(0.5)
        
        self.play(Write(coulombLaw),run_time = 5)
        self.play(ReplacementTransform(force1,force3),ReplacementTransform(charge2, lineCharge),ReplacementTransform(coulombLaw,gaussLaw),run_time = 3)
        self.wait(0.6)
        self.play(ReplacementTransform(force3, force4),ReplacementTransform(force2,force5),FadeIn(plane),FadeOut(lineCharge),ReplacementTransform(charge1,charge3),run_time = 3)
        


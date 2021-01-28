from manimlib.imports import *


class Container(VMobject):
    CONFIG = {
        "color" : WHITE,
        "stroke_width" : 5,
        "fill_color" : BLUE,
        "fill_opacity" : 1.0,
        "sheen_factor" : 0.5,
        "sheen_direction" : UP
    }
    def __init__(self, *vertices, **kwargs):
        VMobject.__init__(self, **kwargs)
        self.set_points_as_corners(vertices)

class Ion(VGroup):
    def __init__(self,text,scale,**kwargs):
        bruh1 = Circle(radius = 0.3, color = BLACK)
        bruh2 = TexMobject(text)
        bruh2.set_color(BLACK)
        bruh2.scale(scale)
        super().__init__(bruh1,bruh2,**kwargs)

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
        symbol.scale(0.5)
        
        symbol.set_color(BLACK)
        symbol.move_to(point)
        
        VGroup.__init__(self,charge, symbol)


class Bruh(Scene):
    def construct(self):
        # self.add(Dot(ORIGIN))
        # for i in range(-8,9):
        #     self.add(Line(4 * DOWN + i * RIGHT, 4 * UP + i * RIGHT))
        #     self.add(DashedLine(4 * DOWN + (i + 0.5) * RIGHT, 4 * UP + (i + 0.5) * RIGHT))
        # for i in range(-4,5):
        #     self.add(Line(i * UP + 8 * LEFT, -8 * LEFT + i * UP))
        #     self.add(DashedLine((i + 0.5) * UP + 8 * LEFT, -8 * LEFT + (i + 0.5) * UP))
        # self.wait(1)
        
        tub=  Container(4 * LEFT + 1 * UP, 4 * LEFT +  3.5 * DOWN, 4* RIGHT + 3.5 * DOWN, 4 * RIGHT + 1 * UP,color= "#888888")
        tubBound = Container(4 * LEFT + 1 * UP, 4 * LEFT +  3.5 * DOWN, 4* RIGHT + 3.5 * DOWN, 4 * RIGHT + 1 * UP,color= "#888888")
        # tubLeft=  Container( * LEFT + 1 * UP, 5 * LEFT +  3.5 * DOWN, -1* RIGHT + 3.5 * DOWN, -1 * RIGHT + 1 * UP,color= "#888888",sheen_factor = 0, fill_opacity = 0)
        # tubLBound = Container(5 * LEFT + 1 * UP, 5 * LEFT +  3.5 * DOWN, -1* RIGHT + 3.5 * DOWN, -1 * RIGHT + 1 * UP,color= "#888888",sheen_factor = 0, fill_opacity = 0)
        # tubRight=  Container(5 * RIGHT + 1 * UP, 5 * RIGHT +  3.5 * DOWN, 1* RIGHT + 3.5 * DOWN, 1 * RIGHT + 1 * UP,color= "#888888")
        # tubRBound=  Container(5 * RIGHT + 1 * UP, 5 * RIGHT +  3.5 * DOWN, 1* RIGHT + 3.5 * DOWN, 1 * RIGHT + 1 * UP,color= "#888888",sheen_factor = 0, fill_opacity = 0)
        cap = Polygon(4.25 * LEFT + 1 * UP, 4.25 * LEFT + 1.25 * UP, 4.25 * RIGHT + 1.25 * UP, 4.25 * RIGHT + 1 * UP,color = "#888888",fill_color = "#888888",fill_opacity = 1)

        leftBar = Polygon(3 * LEFT + 2.5 * UP, 2.5 * LEFT + 2.5 * UP, DOWN + 2.5 * LEFT, 3 * LEFT + DOWN, fill_color = RED, fill_opacity = 1, color= RED)
        rightBar = Polygon(3 * RIGHT + 2.5 * UP, 2.5 * RIGHT + 2.5 * UP, DOWN + 2.5 * RIGHT, 3 * RIGHT + DOWN, fill_color = GREEN_B, fill_opacity = 1, color= GREEN_B)

        dotLeft = Dot(point = 2.75 * LEFT + 2.25 * UP,color= GRAY)
        dotRight=  Dot(point = 2.75 * RIGHT + 2.25 * UP, color = GRAY)
        wire = VMobject(color = GRAY)
        wire.set_points_smoothly([2.75 * RIGHT + 2.25 * UP, RIGHT + 3.5 * UP, LEFT + 2.5 * UP, 2 * LEFT + 3 * UP,2.75 * LEFT + 2.25 * UP])
           

        leadOxide = TexMobject("\\textsf{PbO}_2")
        leadOxide.rotate(PI/2)
        leadOxide.move_to(2.75 * LEFT)
        leadOxide.set_color(BLACK)

        leadOxideCharge = TexMobject("\\textsf{Pb}^{4+}\\textsf{O}^{2-}_2")
        leadOxideCharge.rotate(PI/2)
        leadOxideCharge.move_to(2.75 * LEFT)
        leadOxideCharge.set_color(BLACK)
        leadOxideCharge.align_to(leadOxide,direction = DOWN)

        lead = TexMobject("\\textsf{Pb}")
        lead.rotate(PI/2)
        lead.move_to(2.75 * RIGHT)
        lead.set_color(BLACK)

        leadSulfate = TexMobject("\\textsf{PbSO}_4")
        leadSulfate.rotate(PI/2)
        leadSulfate.move_to(2.75 * RIGHT)
        leadSulfate.align_to(lead,direction = DOWN)
        leadSulfate.set_color(BLACK)

        leadSulfate2 = TexMobject("\\textsf{PbSO}_4")
        leadSulfate2.rotate(PI/2)
        leadSulfate2.move_to(2.75 * LEFT)
        leadSulfate2.align_to(lead,direction = DOWN)
        leadSulfate2.set_color(BLACK)


        H = []
        sulfate = []

        for i in range(0,4):
            H.append(Ion("\\textsf{H}^+",0.5))
            sulfate.append(Ion("\\textsf{SO}_4^{2-}",0.35))
        H[0].move_to( 0.2 * UP + 1.2 * RIGHT)
        H[1].move_to(-2 * UP - 2* RIGHT)
        H[2].move_to( -1.9 * UP + 2.8 * RIGHT)
        H[3].move_to( -2.8 * UP + 0 * RIGHT)
        sulfate[1].move_to(1.5 * RIGHT + 1.5 * DOWN)
        sulfate[2].move_to(1.3 * DOWN)
        sulfate[3].move_to(3 * LEFT + 2.7 * DOWN)


        self.add(tub,tubBound,cap)
        for i in range(0,4):
            self.add(H[i])
            self.wait(0.2)
        for i in range(0,4):
            self.add(sulfate[i])
            self.wait(0.2)
        self.wait(1)
        self.play(FadeInFrom(leftBar,direction = UP),FadeInFrom(rightBar,direction = UP),FadeInFrom(lead,direction = UP),FadeInFrom(leadOxide,direction = UP),run_time = 1.5)

        self.play(FadeIn(dotLeft),FadeIn(dotRight),FadeIn(wire),run_time = 1.5)
        
        self.wait(1)

        electron1 = Charge(2.75 * RIGHT, positive = False,radius=  0.1)
        electron2 = Charge(3 * RIGHT, positive = False,radius = 0.1)

        def move_over(x,y,z,t):
            return[x + 2.2 * t,y + t,z]
        self.play(Homotopy(move_over,sulfate[2]))
        self.add(electron1,electron2)
        self.wait(1)
        self.play(FadeOut(sulfate[2]),ReplacementTransform(lead,leadSulfate))
        self.play(MoveAlongPath(electron1,wire),run_time = 1)
        self.play(MoveAlongPath(electron2,wire),run_time = 1)
        self.wait(1)

        def moveH1(x,y,z,t):
            return[x-0.3 * t, y + 0.9 * t, z]
        def moveH3(x,y,z,t):
            return[]


        h1=  Ion("\\textsf{H}^+",0.5)
        h1.move_to(2 * LEFT)
        h2=  Ion("\\textsf{H}^+",0.5)
        h2.move_to(1.4 * LEFT)
        h3=  Ion("\\textsf{H}^+",0.5)
        h3.move_to(2 * LEFT + 0.7 * DOWN)
        h4=  Ion("\\textsf{H}^+",0.5)
        h4.move_to(1.4 * LEFT + 0.7 * DOWN)
        s = Ion("\\textsf{SO}_4^{2-}",0.35)
        s.move_to(2.75 * LEFT + 1.5 * DOWN)

        water1 = Ion("\\textsf{H}_2\\textsf{O}",0.35)
        water2 = Ion("\\textsf{H}_2\\textsf{O}",0.35)
        water1.move_to(1.7 * LEFT)
        water2.move_to(1.7 * LEFT + 0.7 * DOWN)

        self.play(FadeIn(h1),FadeIn(h2),FadeIn(h3),FadeIn(h4),FadeIn(s))
        self.wait(1)
        self.play(ReplacementTransform(leadOxide,leadOxideCharge))
        self.wait(1)
        self.play(ReplacementTransform(leadOxideCharge,leadSulfate2),FadeIn(water1),FadeIn(water2),FadeOut(h1),FadeOut(h2),FadeOut(h3),FadeOut(h4),FadeOut(s),FadeOut(electron1),FadeOut(electron2))

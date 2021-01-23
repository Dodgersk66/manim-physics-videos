from manimlib.imports import *


class Logo(Scene):
    def construct(self):
        dur=0.75
        def homotopyTest(x,y,z,t):
            Rotate(mainHexagon,PI*0.1)
            if(t<dur):
                return[x+4*t+2*t*t,y-2*t-t*t,z]
            else:
                return[x+4*dur+2*dur*dur+1.5*(t-dur),y-2*dur-dur*dur-3*(t-dur)*(t-dur)-5*(t-dur),z]
        
        mainHexagon = Polygon(ORIGIN,RIGHT,RIGHT*1.5+UP*math.sqrt(0.75),RIGHT+UP*math.sqrt(3),UP*math.sqrt(3),0.5*LEFT+UP*math.sqrt(0.75),color=WHITE)
        plane = Polygon(LEFT*4+UP*2,LEFT*4+DOWN*2,RIGHT*4+DOWN*2,color=LIGHT_GRAY,fill_color=LIGHT_GRAY,fill_opacity=1,stroke_width=0)
        t = TextMobject("Slipping Hexagons")
        t.scale(2)
        t.move_to(DOWN*1.4)
        title = TextMobject("Hydrostatic Solutions!")
        title.scale(2)

        logo = ImageMobject("./Images/logo4.0.png")
        logo.scale(1.5)
        logo.move_to(UP*0.8)

        subtitle = TextMobject("Ep. 6: Problems 14-16")
        subtitle.scale(1.2)
        subtitle.set_color(YELLOW)
        subtitle.move_to(DOWN*1.3)

        self.play(FadeIn(plane),run_time=1.2)
        self.play(FadeInFrom(mainHexagon,direction=3*UP),rate_func=rush_into,run_time=0.8);
        self.add_sound("./sound/hitSound.wav",gain=10);
        #self.play(Homotopy(homotopyTest,mainHexagon)        
        self.play(Rotate(mainHexagon,-1*PI*26.57/180,about_point=ORIGIN),run_time=0.2)
        self.add_sound("./sound/hitSound.wav",gain=10);
        # for i in range(1,3):
        #     self.play(Rotate(mainHexagon,-1*PI/3,about_point=i*2/math.sqrt(5)*RIGHT + i/math.sqrt(5)*DOWN),run_time=0.6)
        #     self.add_sound("./hitSound.wav",gain=10);
        #self.add_sound("./Recording (17).m4a",gain=10,time_offset=0.5)
        self.add_sound("./sound/Recording (21).m4a",gain=10,time_offset=0.33)
        #self.play(Homotopy(homotopyTest,mainHexagon))
        self.play(Homotopy(homotopyTest,mainHexagon))
        self.play(FadeOut(mainHexagon),FadeOut(plane),run_time=0.6)
        self.wait(0.2)
        # #self.wait(1.2)
        # self.play(FadeOut(plane))
        # #self.play(ReplacementTransform(plane,t))
        # # #self.play(FadeOut(plane))
        #self.play(FadeIn(logo),FadeIn(t))
        #self.wait(0.8)
        #self.play(FadeOut(logo),FadeOut(t))
        self.play(FadeIn(title))
        self.wait(0.4)
        #self.play(Write(subtitle),run_time=5)
        self.wait(0.8)
        self.play(FadeOut(title))



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

class HydrostaticParadox(Scene):
    def construct(self):
        
        for i in range(-8, 9):
            for j in range(-4,5):
                if(i == 0 and j == 0):
                    self.add(Dot(color = RED))
                    continue;
                self.add(Dot(i * RIGHT + j * UP))

        title = TextMobject("Solution 1: ", "Hydrostatic Paradox")
        title.set_color_by_tex_to_color_map({
            "Solution 1: " : YELLOW,
            "Hydrostatic Paradox" : WHITE
        })
        title.scale(1.6)

        titleScaledAndMoved = TextMobject("Solution 1: ", "Hydrostatic Paradox")
        titleScaledAndMoved.set_color_by_tex_to_color_map({
            "Solution 1: " : YELLOW,
            "Hydrostatic Paradox" : WHITE
        })
        titleScaledAndMoved.move_to(3.3 * UP + 3 * LEFT)
        titleScaledAndMoved.align_to(6.5 * LEFT, LEFT)
        self.add(title)
        self.play(ReplacementTransform(title,titleScaledAndMoved))
        self.wait(1)

        #wide
        container1 = Container(5.3 * LEFT + UP, 5 * LEFT + 2 * DOWN, 3 * LEFT + 2 * DOWN, 2.7 * LEFT + UP,fill_opacity= 0)


        #normal
        container2 = Container(LEFT + UP, LEFT + 2 * DOWN, RIGHT + 2 * DOWN, RIGHT + UP,fill_opacity= 0)
        water2 = Container(LEFT +2 * DOWN + UP * ( 2.6),LEFT + 2 * DOWN, RIGHT + 2 * DOWN,RIGHT +2 * DOWN + UP * ( 2.6))
        water1 = Container(5 * LEFT +2 * DOWN + UP * ( 2.6 - 2.6 * 0) + (0.3 * 2.6/3- 0.3* 2.6/3 * 0) * LEFT,5 * LEFT + 2 * DOWN, 3 * LEFT + 2 * DOWN,3 * LEFT +2 * DOWN + UP * ( 2.6 - 2.6 * 0) + (0.3 * 2.6/3 - 0.3 * 2.6/3* 0) * RIGHT)
        water3 = Container(3 * RIGHT +2 * DOWN + UP * ( 2.6 - 2.6 * 0) + (0.3 * 2.6/3 - 0.3* 2.6/3 * 0) * RIGHT, 3 * RIGHT + 2 * DOWN, 5 * RIGHT + 2 * DOWN,5 * RIGHT +2 * DOWN + UP * ( 2.6 - 2.6 * 0) + (0.3* 2.6/3 - 0.3 * 2.6/3* 0) * LEFT)
        
        #thin
        container3 = Container(3.3 * RIGHT + UP, 3 * RIGHT + 2 * DOWN, 5* RIGHT +  2 * DOWN, 4.7 * RIGHT + UP,fill_opacity= 0)
        
        table = Polygon(8 * LEFT + 2.02 * DOWN, 8 * RIGHT + 2.02 * DOWN, 8 * RIGHT + 5.2 * DOWN, 8 * LEFT + 5.2 * DOWN,fill_opacity = 1, fill_color = "#222222", stroke_width = 0, sheen_factor=  0.6, sheen_direction = UP)

        waterLine = DashedLine(6 * LEFT + 0.6 * UP, 6 * RIGHT + 0.6 * UP)

        hydroEq = TexMobject("\\frac{\\mathrm d P}{\mathrm d z} = - \\rho g")
        hydroEq2 = TexMobject("\\Delta P = - \\rho g \\Delta z")
        pressureEq = TexMobject("F = PA")
        hydroEq.move_to(3 * UP + 4 * RIGHT)
        hydroEq2.move_to(3 * UP + 4 * RIGHT)
        pressureEq.move_to(2 * UP + 4 * RIGHT)

        relation2 = TexMobject("F_1 \\,\\, \\,\\qquad\\, = \\,\\qquad \\,\\,\\, F_2\\, \\,\\,\\,\\qquad = \\,\\,\\,\\, \\qquad F_3 ")

        f1 = Line(4 * LEFT + DOWN, 4 * LEFT + 2 * DOWN,color = GREEN)
        f2 = Line(DOWN, 2 * DOWN,color = GREEN)
        f3 = Line(4 * RIGHT + DOWN, 4 * RIGHT + 2 * DOWN,color = GREEN)
        f1.add_tip()
        f2.add_tip()
        f3.add_tip()


        relation2.move_to(3 * DOWN)

        question = TextMobject("If the volumes are different,") 
        question2 = TextMobject("how can the forces at the bottoms be the same?")
        question.scale(0.8)
        question2.scale(0.8)
        question.move_to(2.3 * UP)
        question.align_to(6 * LEFT,LEFT)
        
        question2.move_to(1.9 * UP)
        question2.align_to(6 * LEFT, LEFT)


        self.play(FadeIn(table),FadeIn(container1),FadeIn(container2),FadeIn(container3),FadeIn(water1),FadeIn(water2),FadeIn(water3),FadeIn(waterLine),FadeIn(hydroEq2),
                    FadeIn(pressureEq),FadeIn(relation2),FadeIn(f1),FadeIn(f2),FadeIn(f3),FadeIn(question),FadeIn(question2))
        self.wait(1)

        ### Solution from here ###

        


    

        


class Problem2(Scene):
    def construct(self):
        for i in range(-16, 17):
            for j in range(-8,9):
                if(i == 0 and j == 0):
                    self.add(Dot(color = RED))
                    continue;
                self.add(Dot(i / 2 * RIGHT + j / 2 * UP))

        title = TextMobject("Problem 2: ", "A famous see-saw")
        title.set_color_by_tex_to_color_map({
            "Problem 2: " : YELLOW,
            "Hydrostatic Paradox" : WHITE
        })
        title.scale(1.6)

        titleScaledAndMoved = TextMobject("Problem 2: ", "A famous see-saw")
        titleScaledAndMoved.set_color_by_tex_to_color_map({
            "Problem 2: " : YELLOW,
            "Hydrostatic Paradox" : WHITE
        })
        titleScaledAndMoved.move_to(3.3 * UP + 3.4 * LEFT)
        titleScaledAndMoved.align_to(6.5 * LEFT, LEFT)
        

        table = Polygon(8 * LEFT + 2.02 * DOWN, 8 * RIGHT + 2.02 * DOWN, 8 * RIGHT + 5.2 * DOWN, 8 * LEFT + 5.2 * DOWN,fill_opacity = 1, fill_color = "#222222", stroke_width = 0, sheen_factor=  0.6, sheen_direction = UP)

        
        fulcrum = Polygon(LEFT + 2 * DOWN, DOWN, RIGHT + 2 * DOWN, fill_color = "#333333", fill_opacity = 1,sheen_direction = UL, sheen_factor = 0.6,color = WHITE)
        

        balance = Container(3 * LEFT + 0.25 * DOWN, 3 * LEFT + DOWN, 3 * RIGHT + DOWN, 3 * RIGHT + 0.25 * DOWN,fill_opacity = 0)
        
        

        plate1 = Polygon(4.2 * LEFT + 0.54 * DOWN, 1.8 * LEFT + 0.54 * DOWN, 1.8 * LEFT + 0.29 * DOWN, 4.2 * LEFT + 0.29 * DOWN,fill_color = "#555555",fill_opacity = 1,sheen_factor = 0.4,sheen_direction = UL,color = WHITE)
        plate2 = Polygon(4.2 * RIGHT + 0.54 * DOWN, 1.8 * RIGHT + 0.54 * DOWN, 1.8 * RIGHT + 0.29 * DOWN, 4.2 * RIGHT + 0.29 * DOWN,fill_color = "#555555",fill_opacity = 1,sheen_factor = 0.4,sheen_direction = UL,color = WHITE)
        
        
        
        container1 = Container(1.5 * UP + 4 * LEFT,4 * LEFT + 0.25 * DOWN, 2 * LEFT+ 0.25 * DOWN, 2 * LEFT + 1.5 * UP,fill_opacity = 0)
        container2 = Container(1.5 * UP + 4 * RIGHT,4 * RIGHT+ 0.25 * DOWN, 2 * RIGHT+ 0.25 * DOWN, 2 * RIGHT + 1.5 * UP,fill_opacity = 0)
        water1 = Container(1.25 * UP + 4 * LEFT,4 * LEFT + 0.25 * DOWN, 2 * LEFT+ 0.25 * DOWN, 2 * LEFT + 1.25 * UP)
        water2 = Container(1.25 * UP + 4 * RIGHT,4 * RIGHT+ 0.25 * DOWN, 2 * RIGHT+ 0.25 * DOWN, 2 * RIGHT + 1.25 * UP)
        
        
        
        
        pingPong = Circle( fill_color = WHITE, fill_opacity = 1,radius = 0.35,color = BLACK)
        rock = Circle(color = WHITE, fill_color = LIGHT_GRAY, fill_opacity = 1, radius = 0.35)
        pingPong.move_to(3 * LEFT + 0.6 * UP)
        rock.move_to(3 * RIGHT + 0.6 * UP)

        stand = Polygon(5 * RIGHT + 2 * DOWN,  5.5 * RIGHT + 2 * DOWN, 5.5 * RIGHT + 3 * UP, 2.75 * RIGHT + 3 * UP, 2.75 * RIGHT + 2 * UP, 3.25 * RIGHT + 2 * UP ,3.25 * RIGHT + 2.5 * UP, 5 * RIGHT + 2.5 * UP,5 * RIGHT + 2 * DOWN,color = WHITE, stroke_width = 4, fill_color = "#666666",sheen_factor = 0.4, sheen_direction = UL,fill_opacity = 1)

        stringPing = Line(3 * LEFT + 0.25 * DOWN, 3 * LEFT + 0.25 * UP,color = GREEN)
        stringRock = Line(3 * RIGHT + 2 * UP,3 * RIGHT + 0.95 * UP,color = GREEN)


        question = TextMobject("Does the balance tip ", "right")
        question.move_to(2.25 * UP + 2.9 * LEFT)
        question.set_color_by_tex_to_color_map({
            "Does the balance tip " : WHITE,
            "right" : YELLOW
        })
        questionPart2 = TextMobject("Does the balance tip ", "right ", "or ", "left", "?")
        questionPart2.align_to(question,LEFT)
        questionPart2.align_to(question,UP)
        questionPart2.set_color_by_tex_to_color_map({
            "Does the balance tip " : WHITE,
            "right " : YELLOW,
            "or " : WHITE,
            "left" : YELLOW
        })

        


        self.add(title)
        self.play(ReplacementTransform(title,titleScaledAndMoved))
        self.wait(1)


        self.play(FadeIn(table),FadeIn(fulcrum),FadeIn(balance),FadeIn(plate1),FadeIn(plate2),FadeIn(container1),FadeIn(container2),FadeIn(water1),FadeIn(water2),
                   FadeIn(pingPong),FadeIn(rock),FadeIn(stand),FadeIn(stringPing),FadeIn(stringRock),FadeIn(questionPart2))
        
        ### Solution from here ###

        larr1 = Line(3.5 * LEFT + 0.7 * UP, 3.5 * LEFT + 0.25 * DOWN,color = BLACK)
        larr2 = Line(3 * LEFT+ 0.7 * UP, 3 * LEFT + 0.25 * DOWN,color = BLACK)
        larr3 = Line(2.5 * LEFT + 0.7 * UP, 2.5 * LEFT + 0.25 * DOWN,color = BLACK)
        rarr1 = Line(3.5 * RIGHT + 0.7 * UP, 3.5 * RIGHT + 0.25 * DOWN,color = BLACK)
        rarr2 = Line(3 * RIGHT+ 0.7 * UP, 3 * RIGHT + 0.25 * DOWN,color = BLACK)
        rarr3 = Line(2.5 * RIGHT + 0.7 * UP, 2.5 * RIGHT + 0.25 * DOWN,color = BLACK)

        larr1.add_tip()
        larr2.add_tip()
        larr3.add_tip()
        rarr1.add_tip()
        rarr2.add_tip()
        rarr3.add_tip()
        
        self.play(Indicate(container1),Indicate(container2))
        self.wait(1)
        self.play(GrowFromPoint(larr1,larr1.get_top()),GrowFromPoint(larr2,larr2.get_top()),GrowFromPoint(larr3,larr3.get_top()),GrowFromPoint(rarr1,rarr1.get_top()),GrowFromPoint(rarr2,rarr2.get_top()),GrowFromPoint(rarr3,rarr3.get_top()))       

        waterLine = DashedLine(4.8 * LEFT + 1.25 * UP, 4.8 * RIGHT + 1.25 * UP)

        self.wait(1)
        self.play(Indicate(pingPong))
        self.wait(1)
        self.play(Indicate(rock))
        self.wait(1)
        self.play(DrawBorderThenFill(waterLine))
        self.wait(1)
        
    
        leftEq = TexMobject("F_L = F_P - F_T")
        rightEq = TexMobject("F_R = F_P")
        ineq = TexMobject("F_L < F_R")

        self.play(FadeOut(larr1),FadeOut(larr2),FadeOut(larr3),FadeOut(rarr1),FadeOut(rarr2),FadeOut(rarr3))

        tension = Line(3 * LEFT + 0.25 * DOWN, 3 * LEFT + 0.25 * UP,color = BLACK)
        tension.add_tip()
        self.play(GrowFromPoint(tension,tension.get_bottom()))
        

        correct = Ellipse(width = 1.3, height = 0.7,color = GREEN)
        correct.move_to(2.25 * UP + 0.6 * LEFT)

        self.play(DrawBorderThenFill(correct))



class Perpet(Scene):
    def construct(self):
        title = TextMobject("Problem 3: ", "A Perpetual Motion Machine")
        title.set_color_by_tex_to_color_map({
            "Problem 3: " : YELLOW,
            "Hydrostatic Paradox" : WHITE
        })
        title.scale(1.3)

        titleScaledAndMoved = TextMobject("Problem 3: ", "A Perpetual Motion Machine")
        titleScaledAndMoved.set_color_by_tex_to_color_map({
            "Problem 3: " : YELLOW,
            "Hydrostatic Paradox" : WHITE
        })
        titleScaledAndMoved.move_to(3.3 * UP + 3.4 * LEFT)
        titleScaledAndMoved.align_to(6.5 * LEFT, LEFT)
        # self.add(Dot(ORIGIN))
        # for i in range(-8,9):
        #     self.add(Line(4 * DOWN + i * RIGHT, 4 * UP + i * RIGHT))
        #     self.add(DashedLine(4 * DOWN + (i + 0.5) * RIGHT, 4 * UP + (i + 0.5) * RIGHT))
        # for i in range(-4,5):
        #     self.add(Line(i * UP + 8 * LEFT, -8 * LEFT + i * UP))
        #     self.add(DashedLine((i + 0.5) * UP + 8 * LEFT, -8 * LEFT + (i + 0.5) * UP))

        pulleyTop = VGroup(Line(ORIGIN, 0.8 * np.cos(1.26) * RIGHT + 0.8 * np.sin(1.26) *UP,color = GRAY),Line(ORIGIN, 0.8 * np.cos(1.26 + 2 * PI / 5) * RIGHT + 0.8 * np.sin(1.26 + 2 * PI / 5) *UP,color = GRAY),Line(ORIGIN, 0.8 * np.cos(1.26 + 4 * PI / 5) * RIGHT + 0.8 * np.sin(1.26 + 4 * PI / 5) *UP,color = GRAY),
                    Line(ORIGIN, 0.8 * np.cos(1.26 + 6 * PI / 5) * RIGHT + 0.8 * np.sin(1.26 + 6 * PI / 5) *UP,color = GRAY), Line(ORIGIN, 0.8 * np.cos(1.26 + 8 * PI / 5) * RIGHT + 0.8 * np.sin(1.26 + 8 * PI / 5) *UP,color = GRAY),
                    Circle(radius = 0.55, fill_color=  LIGHT_GRAY, color = LIGHT_GRAY, fill_opacity = 1), Circle(radius=  0.4, color = BLACK,stroke_width = 2), Circle(radius = 0.2, color = BLACK,stroke_width = 2),Line(-0.07 * UP, 0.07 * UP,color = BLACK),Line(-0.07 * RIGHT, 0.07 * RIGHT,color = BLACK))
        pulleyTop.move_to(1.9 * LEFT + 1.5 * UP)
        pulleyBot = VGroup(Line(ORIGIN, 0.8 * np.cos( -1 * 1.26) * RIGHT + 0.8 * np.sin( -1 * 1.26) *UP,color = GRAY),Line(ORIGIN, 0.8 * np.cos( -1 * 1.26 + 2 * -1 * PI / 5) * RIGHT + 0.8 * np.sin( -1 * 1.26 + 2 * -1 * PI / 5) *UP,color = GRAY),Line(ORIGIN, 0.8 * np.cos( -1 * 1.26 + 4 * -1 * PI / 5) * RIGHT + 0.8 * np.sin( -1 * 1.26 + 4 * -1 * PI / 5) *UP,color = GRAY),
                    Line(ORIGIN, 0.8 * np.cos( -1 * 1.26 + 6 * -1 * PI / 5) * RIGHT + 0.8 * np.sin( -1 * 1.26 + 6 * -1 * PI / 5) *UP,color = GRAY), Line(ORIGIN, 0.8 * np.cos( -1 * 1.26 + 8 * -1 * PI / 5) * RIGHT + 0.8 * np.sin( -1 * 1.26 + 8 * -1 * PI / 5) *UP,color = GRAY),Circle(radius = 0.55, fill_color=  LIGHT_GRAY, color = LIGHT_GRAY, fill_opacity = 1), Circle(radius=  0.4, color = BLACK,stroke_width = 2), Circle(radius = 0.2, color = BLACK,stroke_width = 2),Line(-0.07 * UP, 0.07 * UP,color = BLACK),Line(-0.07 * RIGHT, 0.07 * RIGHT,color = BLACK))
        pulleyBot.move_to(1.9 * LEFT + 1.5 * DOWN)

        containerPart1 = Container(3.75 * LEFT + 1.5 * UP, 3.75  * LEFT + DOWN,3.75 * LEFT + DOWN, 3.75 * LEFT + 1.5 * DOWN,3.75 * LEFT + 1.5 * DOWN, 2.75 * LEFT+ 1.25 * DOWN, 1.75 * LEFT + 1.5 * DOWN,1.75 * LEFT + 1.5 * DOWN, 1.75 * LEFT + 1.5 * UP)
        mask = Container(2.5 * LEFT +  1.25 * DOWN + DOWN / 16,2.75 * LEFT + 1.25 * DOWN,3 * LEFT + 1.25 * DOWN + 1/16 * DOWN, 2.75 * LEFT + 1.25 * DOWN,color = BLACK,stroke_width = 4.85,sheen_factor = 0)

        #string = Polygon(2.75 * LEFT + 1.5 * DOWN, 1.5 * UP + 2.75 * LEFT, 1.9 * LEFT + 2.45 * UP,1.05 * LEFT + 1.5 * UP, 1.05 * LEFT, 1.05 * LEFT+ 1.5 * DOWN,2.45 * DOWN + 1.9 * LEFT)
        #string.make_smooth()
        string = Polygon(2.75 * LEFT + 1.5 * DOWN, 1.5 * UP + 2.75 * LEFT)
        string.add_cubic_bezier_curve(1.5 * UP + 2.75 * LEFT,1.5 * UP + 2.75 * LEFT + 0.5 *  UP, 1.9 * LEFT + 2.4 * UP + 0.5 * LEFT,1.9 * LEFT + 2.4 * UP)
        string.add_cubic_bezier_curve(1.9 * LEFT + 2.4 * UP, + 1.9 * LEFT + 2.4 * UP + 0.5 *  RIGHT,1.05 * LEFT + 1.5 * UP + 0.5 * UP, 1.05 * LEFT + 1.5 * UP)
        string.add_cubic_bezier_curve(1.05 * LEFT + 1.5 * UP,1.05 * LEFT, 1.05 * LEFT, 1.05 * LEFT+ 1.5 * DOWN)
        string.add_cubic_bezier_curve(1.05 * LEFT+ 1.5 * DOWN, 1.05 * LEFT + 2 * DOWN, 2.4  *DOWN + 1.4 * LEFT,2.4 * DOWN + 1.9 * LEFT )
        string.add_cubic_bezier_curve(2.4 * DOWN + 1.9 * LEFT, 2.4 * DOWN + 2.4 * LEFT, 2.75 * LEFT + 2 * DOWN, 2.75 * LEFT + 1.5 * DOWN)
        
        pingPongs = []

        for i  in range(0,12):
            pingPongs.append(Circle(radius = 0.25, fill_opacity = 1, fill_color = WHITE, color = WHITE))
            pingPongs[i].move_to(1.05 * LEFT)
            pingPongs[i].speed = 0.2
            pingPongs[i].acc = 0.6
        pingPongs[1].move_to(DOWN + 1.05 * LEFT)
        pingPongs[2].move_to(UP + 1.05 * LEFT)
        pingPongs[3].move_to(1.5 * DOWN + 1.9 * LEFT + 0.8 * np.cos(0.625) * RIGHT + np.sin(0.625) * DOWN * 0.8)
        pingPongs[4].move_to(1.5 * DOWN + 1.9 * LEFT + RIGHT * np.cos(1.875) * 0.8 + DOWN * 0.8 * np.sin(1.875))
        pingPongs[5].move_to(1.5 * DOWN + 1.9 * LEFT + RIGHT * np.cos(3.125) * 0.8 + DOWN * 0.8 * np.sin(3.125))
        pingPongs[6].move_to(2.75 * LEFT + 1.5 * DOWN + 0.9867258771 * UP)
        pingPongs[7].move_to(2.75 * LEFT + 1.5 * DOWN + 1.9867258771 * UP)
        pingPongs[8].move_to(2.75 * LEFT + 1.5 * DOWN + 2.9867258771 * UP)
        pingPongs[9].move_to(1.5 * UP + 1.9 * LEFT + 0.8 * np.cos(0.625) * RIGHT + np.sin(0.625) * UP * 0.8)
        pingPongs[10].move_to(1.5 *  UP+ 1.9 * LEFT + RIGHT * np.cos(1.875) * 0.8 + UP * 0.8 * np.sin(1.875))
        pingPongs[11].move_to(1.5 * UP + 1.9 * LEFT + RIGHT * np.cos(3.125) * 0.8 + UP * 0.8 * np.sin(3.125))

        # for i in range(0,12):
        #     pingPongs[i].move_to(pingPongs[i].get_center() + 0.05 * LEFT)

        def ping_pong_updater(d,dt):
            d.speed += d.acc * dt;
            if(d.get_center()[1] <= -1.5):
                d.rotate(-1 * d.speed / 0.8 * dt,axis = OUT, about_point = 1.5 * DOWN + 1.9 * LEFT)
            
            elif(d.get_center()[1] >= 1.5):
                d.rotate(-1 * d.speed / 0.8 * dt,axis = OUT, about_point = 1.5 * UP + 1.9 * LEFT)
         
            else:
                if(d.get_center()[0] <= -2):
                    d.move_to(d.get_center() + d.speed * dt * UP)
                else:
                    d.move_to(d.get_center() - d.speed * dt * UP)


        def disc_rotate(d,dt):
            rotSpeed = pingPongs[0].speed / 0.8
            d.rotate(rotSpeed * dt * -1, axis = OUT, about_point = d.get_center())
        


        self.add(title)
        self.play(ReplacementTransform(title,titleScaledAndMoved))
        self.wait(1)
        self.add(containerPart1, mask)
        self.add(pulleyTop,pulleyBot,string)
        self.wait(1)
        for i in range(0, 12):
            pingPongs[i].add_updater(ping_pong_updater)
        for i in range(0,12):
            self.add(pingPongs[i])
        pulleyTop.add_updater(disc_rotate)
        pulleyBot.add_updater(disc_rotate)
        self.add(pulleyBot,pulleyTop)
        self.wait(8)

        enArrow = Arrow(ORIGIN, 2 * RIGHT)
        energyTxt = TexMobject("\\infty")
        energyTxt.move_to(3 * RIGHT)
        energyTxt.scale(3)
        energy = SVGMobject("./images/lightning-bolt.svg",fill_color = YELLOW)
        energy.move_to(5 * RIGHT)
        energy.scale(1.5)

        self.play(GrowArrow(enArrow))
        self.play(Write(energyTxt),DrawBorderThenFill(energy))

        for i in range(0,12):
            pingPongs[i].remove_updater(ping_pong_updater)

        pulleyBot.remove_updater(disc_rotate)
        pulleyTop.remove_updater(disc_rotate)

        for i in range(0,12):
            self.remove(pingPongs[i])
        
        self.wait(1)
        
        deny = Line(5.5 * RIGHT + 2 * DOWN, 2.5 * RIGHT+ 2 * UP, color = RED,stroke_width = 6)
        self.play(GrowFromPoint(deny,5.5 * RIGHT + 2 * DOWN))

        question = TextMobject("What's the issue with this perpetual motion machine?")
        question.move_to(3 * DOWN)
        self.play(Write(question),run_time =  2)
        self.wait(1)






        

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
        

        title = TextMobject("Problem 1: ", "Hydrostatic Paradox")
        title.set_color_by_tex_to_color_map({
            "Problem 1: " : YELLOW,
            "Hydrostatic Paradox" : WHITE
        })
        title.scale(1.6)

        titleScaledAndMoved = TextMobject("Problem 1: ", "Hydrostatic Paradox")
        titleScaledAndMoved.set_color_by_tex_to_color_map({
            "Problem 1: " : YELLOW,
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

        forceVecsLeft = []

        for i in range(1, 5):
            bruh = Line(5 * LEFT + 2 * DOWN + 0.5 * i * UP + 0.05 * i * LEFT,5 * LEFT + 2 * DOWN + 0.5 * i * UP + 0.05 * i * LEFT + 0.2 * RIGHT * (5.2-i) + 0.02 * UP * (5.2-i),color = BLACK, tip_length = 0.2)
            bruh.add_tip()
            forceVecsLeft.append(bruh)
        for i in range(1, 5):
            bruh = Line(3 * LEFT + 2 * DOWN + 0.5 * i * UP + 0.05 * i * RIGHT,3 * LEFT + 2 * DOWN + 0.5 * i * UP + 0.05 * i * RIGHT + 0.2 * LEFT * (5.2-i) + 0.02 * UP * (5.2-i),color = BLACK, tip_length = 0.2)
            bruh.add_tip()
            forceVecsLeft.append(bruh)
        arrowsLeft = VGroup(*forceVecsLeft)
        self.play(FadeIn(arrowsLeft))
        self.wait(1)

        forceVecsMid = []
        for i in range(1, 5):
            bruh = Line(LEFT + 2 * DOWN + 0.5 * i * UP,LEFT + 2 * DOWN + 0.5 * i * UP + 0.2 * RIGHT * (5.2-i),color = BLACK, tip_length = 0.2)
            bruh.add_tip()
            forceVecsMid.append(bruh)
        for i in range(1, 5):
            bruh = Line(RIGHT + 2 * DOWN + 0.5 * i * UP,RIGHT + 2 * DOWN + 0.5 * i * UP  + 0.2 * LEFT * (5.2-i) ,color = BLACK, tip_length = 0.2)
            bruh.add_tip()
            forceVecsMid.append(bruh)
        arrowsMid = VGroup(*forceVecsMid)
        self.play(FadeIn(arrowsMid))
        self.wait(1)

        forceVecsRight = []
        
        for i in range(1, 5):
            bruh = Line(5 * RIGHT + 2 * DOWN + 0.5 * i * UP + 0.05 * i * LEFT,5 * RIGHT + 2 * DOWN + 0.5 * i * UP + 0.05 * i * LEFT + 0.2 * LEFT * (5.2-i) + 0.02 * DOWN * (5.2-i),color = BLACK, tip_length = 0.2)
            bruh.add_tip()
            forceVecsRight.append(bruh)
        for i in range(1, 5):
            bruh = Line(3 * RIGHT + 2 * DOWN + 0.5 * i * UP + 0.05 * i * RIGHT,3 *RIGHT + 2 * DOWN + 0.5 * i * UP + 0.05 * i * RIGHT + 0.2 * RIGHT * (5.2-i) + 0.02 * DOWN * (5.2-i),color = BLACK, tip_length = 0.2)
            bruh.add_tip()
            forceVecsRight.append(bruh)
        arrowsRight = VGroup(*forceVecsRight)
        self.play(FadeIn(arrowsRight))
        self.wait(1)

        self.play(Indicate(arrowsLeft))
        self.wait(1)
        self.play(Indicate(arrowsRight))
        self.wait(1)
        self.play(Indicate(arrowsMid))
        self.wait(1)
        self.play(FadeOut(container2),FadeOut(water2),FadeOut(container3),FadeOut(water3),FadeOut(waterLine),FadeOut(question),FadeOut(question2),FadeOut(f2),
                    FadeOut(f3),FadeOut(hydroEq2),FadeOut(pressureEq),FadeOut(table),FadeOut(relation2),FadeOut(arrowsRight),FadeOut(arrowsMid))
        
        self.wait(1)



        netForce = TexMobject("\\vec{F} = \\oint P \\, \\mathrm d \\vec{A}")
        netForce.move_to(2 * UP)
        vertForce = TexMobject("\\implies F_y = \\hat{y} \cdot \\vec{F} = \\oint (P \\hat{y}) \\cdot \\mathrm d \\vec{A}")
        vertForce.move_to(0.6 * UP)
        vertForce.align_to(netForce,LEFT)
        vertForcePressure=  TexMobject("\\implies F_y = \\oint (P_{atm} - \\rho g y )\\hat{y} \\cdot \\mathrm d \\vec{A}")
        vertForcePressure.move_to(0.6 * UP)
        vertForcePressure.align_to(vertForce,LEFT)

        divergTheorem = TexMobject("\\oint \\vec{E} \\cdot \\mathrm d A = \\int_V \\nabla \\cdot \\vec{E}\\,  \\mathrm d V")
        divergTheorem.move_to(2.5 * RIGHT + 0.8 * DOWN)

        divergTheoremApply = TexMobject("F_y = \\oint P\\hat{y} \\cdot \\mathrm d \\vec{A} = \\int_V - \\nabla \\cdot P\\hat{y} \\, \\mathrm d V")
        divergTheoremApply.move_to(0.8 * DOWN)
        divergTheoremApply.align_to(vertForcePressure,LEFT)
        
        divergTheoremCalc = TexMobject("\\implies F_y = \\int_V -(-\\rho g)\\, \\mathrm d V")
        divergTheoremCalc.move_to(2.2 * DOWN)
        divergTheoremCalc.align_to(divergTheoremApply,LEFT)
        final = TexMobject("\\implies F_y = \\int_V \\rho g\\, \\mathrm d V = \\rho g V")
        divergTheoremCalc.move_to(2.2 * DOWN)
        divergTheoremCalc.align_to(divergTheoremApply,LEFT)

        final.move_to(2.2 * DOWN)
        final.align_to(divergTheoremCalc,LEFT)

        self.play(Write(netForce),run_time = 1.5)
        self.wait(1)
        self.play(Write(vertForce),run_time = 1.5)
        self.wait(1)
        self.play(ReplacementTransform(vertForce,vertForcePressure),run_time = 1.5)
        self.wait(1)
        self.play(Write(divergTheorem))
        self.wait(1)
        self.play(ReplacementTransform(divergTheorem,divergTheoremApply),run_time = 1.5)
        self.wait(1)
        self.play(Write(divergTheoremCalc),run_time = 1.5)
        self.wait(1)
        self.play(ReplacementTransform(divergTheoremCalc,final),run_time = 1.5)
        self.wait(1)


        




    

        


class Problem2(Scene):
    def construct(self):
        # for i in range(-16, 17):
        #     for j in range(-8,9):
        #         if(i == 0 and j == 0):
        #             self.add(Dot(color = RED))
        #             continue;
        #         self.add(Dot(i / 2 * RIGHT + j / 2 * UP))

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

        larr1 = Line(3.5 * LEFT + 0.7 * UP, 3.5 * LEFT + 0.25 * DOWN,color = BLACK,tip_length = 0.2)
        larr2 = Line(3 * LEFT+ 0.7 * UP, 3 * LEFT + 0.25 * DOWN,color = BLACK,tip_length = 0.2)
        larr3 = Line(2.5 * LEFT + 0.7 * UP, 2.5 * LEFT + 0.25 * DOWN,color = BLACK,tip_length = 0.2)
        rarr1 = Line(3.5 * RIGHT + 0.7 * UP, 3.5 * RIGHT + 0.25 * DOWN,color = BLACK,tip_length = 0.2)
        rarr2 = Line(3 * RIGHT+ 0.7 * UP, 3 * RIGHT + 0.25 * DOWN,color = BLACK,tip_length = 0.2)
        rarr3 = Line(2.5 * RIGHT + 0.7 * UP, 2.5 * RIGHT + 0.25 * DOWN,color = BLACK,tip_length = 0.2)

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
        leftEq.move_to(3 * DOWN + 3 * LEFT)
        rightEq = TexMobject("F_R = F_P")
        rightEq.move_to(3 * DOWN + 3 * RIGHT)
        ineq = TexMobject("<")
        ineq.set_color(YELLOW)
        ineq.move_to(3 * DOWN)

        self.play(FadeOut(larr1),FadeOut(larr2),FadeOut(larr3),FadeOut(rarr1),FadeOut(rarr2),FadeOut(rarr3))

        tension = Line(3 * LEFT + 0.25 * DOWN, 3 * LEFT + 0.4 * UP,color = DARK_BLUE,tip_length = 0.2)
        tension.add_tip()
        self.wait(1)
        self.play(GrowFromPoint(tension,tension.get_bottom()))

        self.wait(1)
        
        self.play(Write(leftEq),run_time = 2)
        self.play(Write(rightEq),run_time = 2)
        self.play(Write(ineq))
        self.wait(1)


        correct = Ellipse(width = 1.3, height = 0.7,color = GREEN)
        correct.move_to(2.25 * UP + 0.6 * LEFT)

        self.play(DrawBorderThenFill(correct))
        self.wait(1)
        self.play(FadeOut(tension),FadeOut(ineq),FadeOut(leftEq),FadeOut(rightEq))
        self.wait(1)

        outline1 = Polygon(1.5 * UP + 4 * LEFT,4 * LEFT + 0.25 * DOWN, 2 * LEFT+ 0.25 * DOWN, 2 * LEFT + 1.5 * UP,fill_opacity = 0,color = GREEN)
        outline2 = Polygon(1.5 * UP + 4 * RIGHT,4 * RIGHT+ 0.25 * DOWN, 2 * RIGHT+ 0.25 * DOWN, 2 * RIGHT + 1.5 * UP,fill_opacity = 0,color = GREEN)

        self.play(DrawBorderThenFill(outline1))
        self.play(DrawBorderThenFill(outline2))
        self.play(FadeOut(outline1),FadeOut(outline2))
        self.wait(1)

        gravPing = Line(pingPong.get_center(),pingPong.get_center() + DOWN, color = GREEN_C, tip_length = 0.2)
        gravPing.add_tip()
        gravRock = Line(rock.get_center(),rock.get_center() + 1.6 * DOWN, color = GREEN_C, tip_length = 0.2)
        gravRock.add_tip()

        tenRock = Line(rock.get_center(), rock.get_center() + 0.8 * UP, color = DARK_BLUE, tip_length = 0.2)
        tenRock.add_tip()

        self.play(GrowFromPoint(gravPing,gravPing.get_top()))
        self.wait(1)
        self.play(GrowFromPoint(gravRock,gravRock.get_top()))
        self.wait(1)
        self.play(GrowFromPoint(tenRock,tenRock.get_bottom()))
        self.wait(1)

        leftEq2 = TexMobject("F_L = W_P")
        leftEq2.move_to(3 * DOWN + 3 * LEFT)
        
        leftEq3 = TexMobject("F_L = \\rho_P V g")
        leftEq3.move_to(3 * DOWN + 3 * LEFT)

        rightEq2 = TexMobject("F_R = W_R - F_T")
        rightEq2.move_to(3 * DOWN + 3 * RIGHT)
        rightEq3 = TexMobject("F_R = \\rho_RVg - F_T")
        rightEq3.move_to(3 * DOWN + 3 * RIGHT)
        rightEq4 = TexMobject("F_R = \\rho_RVg - (\\rho_R V g - \\rho_wVg)")
        rightEq4.move_to(3 * DOWN + 3 * RIGHT)
        rightEq5 = TexMobject("F_R = \\rho_wVg)")
        rightEq5.move_to(3 * DOWN + 3 * RIGHT)
        ineq2 = TexMobject("<")
        ineq2.set_color(YELLOW)
        ineq2.move_to(3 * DOWN)

        self.play(Write(leftEq2),run_time = 2)
        self.play(Write(rightEq2),run_time = 2)
        self.wait(1)

        self.play(ReplacementTransform(leftEq2,leftEq3),ReplacementTransform(rightEq2,rightEq3))
        self.wait(1)
        self.play(ReplacementTransform(rightEq3,rightEq4))
        self.wait(1)
        self.play(ReplacementTransform(rightEq4,rightEq5))
        self.wait(1)
        self.play(Write(ineq2))





        





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
        

        enArrow = Arrow(ORIGIN, 2 * RIGHT)
        energyTxt = TexMobject("\\infty")
        energyTxt.move_to(3 * RIGHT)
        energyTxt.scale(3)
        energy = SVGMobject("./images/lightning-bolt.svg",fill_color = YELLOW)
        energy.move_to(5 * RIGHT)
        energy.scale(1.5)

        self.add(enArrow)
        self.add(energyTxt,energy)

   

        
        deny = Line(5.5 * RIGHT + 2 * DOWN, 2.5 * RIGHT+ 2 * UP, color = RED,stroke_width = 6)
        self.add(deny)

        question = TextMobject("What's the issue with this perpetual motion machine?")
        question.move_to(3 * DOWN)
        self.add(question)

        for i in range(0, 12):
            pingPongs[i].add_updater(ping_pong_updater)
        for i in range(0,12):
            self.add(pingPongs[i])
        pulleyTop.add_updater(disc_rotate)
        pulleyBot.add_updater(disc_rotate)
        self.add(pulleyBot,pulleyTop)
        self.wait(8)

        self.wait(1)
        
        for i in range(0,12):
            pingPongs[i].remove_updater(ping_pong_updater)
        
        pulleyBot.remove_updater(disc_rotate)
        pulleyTop.remove_updater(disc_rotate)

        for i in range(0,12):
            self.remove(pingPongs[i])
        
        self.wait(1)

        newPingPong = Circle(radius = 0.25, fill_opacity = 1, fill_color = WHITE, color = WHITE)
        newPingPong.move_to(1.05 * LEFT)
        newPingPong.speed = 0.2
        newPingPong.acc = 0.6

        ### Solutions from here ###

        newPingPong.add_updater(ping_pong_updater)
        self.add(newPingPong)
        self.wait(3.4)
        newPingPong.remove_updater(ping_pong_updater)
        self.wait(1)
        self.play(FadeOut(enArrow),FadeOut(energyTxt),FadeOut(energy),FadeOut(deny))
        self.wait(1)

        changeEnergy = TexMobject("\\Delta E")
        changeEnergy2 = TexMobject("= W_g + W_b + W_{in}")
        changeEnergy.move_to(0.5 * RIGHT + 2 * UP)
        changeEnergy2.next_to(changeEnergy,direction = RIGHT, buff = 0.62, aligned_edge=  LEFT)
        changeEnergy2.align_to(changeEnergy,direction = UP)
        self.play(Write(changeEnergy))
        self.wait(1)
        self.play(Write(changeEnergy2))

        bruh = TexMobject("= 0 + \\rho V g h + W_{in}")
        bruh.move_to(UP)
        bruh.align_to(changeEnergy2,LEFT)
        bruh2 = TexMobject("W_{in} = (-PA)d = -PV")
        bruh2.move_to(0 * UP + 1.5 * 1.3 * RIGHT)
        bruh3 = TexMobject("= 0 + \\rho V g h - P V")
        bruh3.move_to(0 * DOWN)
        bruh3.align_to(changeEnergy2,LEFT)
        bruh4 = TexMobject("=0 + \\rho Vg h - \\rho gh V = 0")
        bruh4.move_to(0 * DOWN)
        bruh4.align_to(changeEnergy2,LEFT)

        def move_ball(x,y,z,t):
            return[x,y + 0.6 * t,z]

        self.wait(1)
        self.play(Write(bruh))
        self.wait(1)
        self.play(Write(bruh2),Homotopy(move_ball,newPingPong),run_time = 2)
        self.wait(1)
        self.play(FadeOut(bruh2))
        self.wait(1)
        self.play(Write(bruh3))
        self.wait(1)
        self.play(ReplacementTransform(bruh3,bruh4))


class Img(Scene):
    def construct(self):
        self.add(Line(ORIGIN, RIGHT + 3 * UP))
        bruh = Line(0.5 * RIGHT + 1.5 * UP, 4 * LEFT + 3 * UP)
        bruh.add_tip()
        self.add(bruh)
        bruh2 = DashedLine(4 * LEFT + 1.5 * UP, 4* LEFT + 3 * UP,color = YELLOW)
        bruh2.add_tip()
        bruh3 = DashedLine(4 * LEFT + 1.5 * UP,1.5 * UP + 0.5 *RIGHT,color = GREEN)
        self.add(bruh2,bruh3)
        self.add(DashedLine(ORIGIN, RIGHT,color = YELLOW),DashedLine(RIGHT, RIGHT + 3 * UP, color = GREEN))

        
        theta1 = TexMobject("\\theta")
        theta1.scale(0.6)
        theta1.move_to(1.5 * LEFT + 1.8 * UP)
        theta2 = TexMobject("\\theta")
        theta2.scale(0.6)
        theta2.move_to(0.8 * RIGHT + 1.6 * UP)
        

        self.add(theta1,theta2)
        self.wait(1)

class Img2(Scene):
    def construct(self):
        self.add(TexMobject("PA\\sin \\theta  = P(A\\sin \\theta) = PA_{h}"))
        self.wait(1)






        

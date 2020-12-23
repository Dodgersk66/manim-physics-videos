from manimlib.imports import *
import math
import numpy

class Intro(Scene):
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
        title = TextMobject("Terminal Velocity of a Pencil")
        title.scale(2)

        logo = ImageMobject("./Images/logo4.0.png")
        logo.scale(1.5)
        logo.move_to(UP*0.8)

        subtitle = TextMobject("Morin 8.66 / IPhO 1998 pr1")
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
        self.play(FadeIn(logo),FadeIn(t))
        self.wait(0.8)
        self.play(FadeOut(logo),FadeOut(t))
        self.play(FadeIn(title))
        self.wait(0.4)
        self.play(Write(subtitle),run_time=5)
        self.wait(0.8)
        self.play(FadeOut(subtitle),FadeOut(title))

class Problem(Scene):
    def construct(self):
        # for i in range(-7,8):
        #         for j in range(-4,5):
        #             locDot = Dot()
        #             locDot.move_to(RIGHT*i + UP*j)
        #             self.add(locDot)
        
        hexagon = RegularPolygon(fill_opacity = 1, fill_color = "#F5F5DC",color=WHITE)
        hexagon.scale(0.8)
        lead = Circle(radius = 0.2,fill_opacity = 1, fill_color = "#555555",sheen_factor = 0.5, sheen_direction = UL,stroke_width = 0)
        leaddup = Circle(radius = 0.2,fill_opacity = 1, fill_color = "#555555",sheen_factor = 0.5, sheen_direction = UL,stroke_width = 0)
        hexagondup = RegularPolygon(fill_opacity = 1, fill_color = "#F5F5DC",color=WHITE)
        hexagondup.scale(0.8)
        pencil = VGroup(hexagon,lead)    
        pencilDup = VGroup(hexagondup,leaddup)     
        pencil.rotate_about_origin(-np.arctan(0.25))
        pencil.move_to(4.22 * LEFT + 0.77 * UP)
        
        #self.add(pencil)


        spokes = []

        for i in range(0,6):
            spoke = Line(ORIGIN,0.8 * np.sin(i * PI/3) * UP + 0.8 * np.cos( i * PI / 3)*RIGHT)
            spokes.append(spoke)


        pencilNewModel = VGroup(*spokes,lead)
        #self.play(Transform(pencil,pencilNewModel))

        #self.play(Transform(pencil,pencilDup))

        plane = Line(2*DOWN + 4 * RIGHT, 2* DOWN + 4 * RIGHT + 12.36931 * LEFT,stroke_width = 7)
        plane2 = Line(2 * DOWN + 4 * RIGHT, 2* DOWN + 8 * RIGHT,stroke_width = 7)
        plane3 = DashedLine(2 * DOWN + 4 * RIGHT, 2 * DOWN + 8 * LEFT,dash_length = 0.25,stroke_width = 7)

        #plane = Line(2 * DOWN + 4 * RIGHT, 8 * LEFT + UP)

        angleLabel = TexMobject("\\theta")
        angleLabel.set_color(YELLOW)
        angleLabel.move_to(0.5 * RIGHT + 1.6 * DOWN)
        angleMark = Arc(PI - np.arctan(0.25),angle = np.arctan(0.25),radius=  3,arc_center = 4 * RIGHT + 2 * DOWN)
        angleMark.set_color(YELLOW)

        kick = Arrow(start = -6.11 * RIGHT + 1.96 * UP, end = -4.68 * RIGHT + 1.6 * UP, color = GREEN)

        self.add(plane,plane2)
        self.wait(0.2)
        self.play(Rotate(plane,angle = -1 * np.arctan(0.25),about_point = 2 * DOWN + 4 * RIGHT),FadeIn(plane3),run_time = 2)
        self.play(Write(angleLabel),FadeIn(angleMark))
        self.play(DrawBorderThenFill(pencil))
        self.play(GrowFromPoint(kick,-6.11 * RIGHT + 1.96 * UP))
        #create updater for stuff rolling down
        pencil.initAngSpeed = 0.8
        pencil.initAngToPlane = PI/3;
        pencil.pointRotate = 4 * LEFT;
        pencil.effLength = 0.795
        def pencil_updater(obj,dt):
            if(pencil.initAngToPlane >= 2 * PI/3):
                pencil.initAngToPlane = PI/3
                pencil.initAngSpeed /= 2
                pencil.pointRotate +=pencil.effLength * 1/np.sqrt(17) * DOWN +  pencil.effLength * 4 / np.sqrt(17) * RIGHT

            angToVert = np.arctan(0.25) + pencil.initAngToPlane - PI/2
            pencil.initAngSpeed += 0.4 * np.sin(angToVert) *dt
            pencil.initAngToPlane += pencil.initAngSpeed * dt
            pencil.rotate(-1 * pencil.initAngSpeed * dt, OUT, about_point = pencil.pointRotate)



        
        pencil.add_updater(pencil_updater)
        self.add(pencil)
        self.wait(1)
        self.play(FadeOut(kick))
        self.wait(5)


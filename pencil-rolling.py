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

class Problem2(Scene):
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
        pencilDup.rotate_about_origin(-np.arctan(0.25))
        pencilDup.move_to(4.22 * LEFT + 0.77 * UP)
        
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
        sideLabel = TexMobject("r")
        sideLabel.move_to(3.9 * LEFT + 1.8 * UP)

        self.add(plane,plane2)
        self.wait(0.2)
        self.play(Rotate(plane,angle = -1 * np.arctan(0.25),about_point = 2 * DOWN + 4 * RIGHT),FadeIn(plane3),run_time = 2)
        self.play(Write(angleLabel),FadeIn(angleMark))
        self.wait(1.2)
        self.play(DrawBorderThenFill(pencil),run_time = 4.2)
        self.wait(1)
        self.play(Write(sideLabel),run_time = 2)
        self.wait(3)
        self.play(GrowFromPoint(kick,-6.11 * RIGHT + 1.96 * UP))
        self.remove(sideLabel)
        #create updater for stuff rolling down
        pencil.initAngSpeed = 1.3
        pencil.initAngToPlane = PI/3;
        pencil.pointRotate = 4 * LEFT;
        pencil.effLength = 0.798
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
        self.wait(0.83)
        self.play(FadeOut(kick),Flash(4 * LEFT + 3.2 * RIGHT / np.sqrt(17) + DOWN * 0.8 / np.sqrt(17)),run_time = 0.2)
        self.add_sound("./sound/hitSound.wav",gain=10);
        self.wait(1.18)
        self.play(Flash(4 * LEFT + 6.4 * RIGHT / np.sqrt(17) + DOWN * 1.6 / np.sqrt(17)),run_time = 0.2)
        self.add_sound("./sound/hitSound.wav",gain=10);
        self.wait(2.43)
        self.play(Flash(4 * LEFT + 9.6 * RIGHT / np.sqrt(17) + DOWN * 2.4 / np.sqrt(17)),run_time = 0.2)
        self.add_sound("./sound/hitSound.wav",gain=10);
        self.wait(2.1)
        pencilDup.remove_updater(pencil_updater)
        pencilDup.initAngSpeed = 1.3
        pencilDup.initAngToPlane = PI/3;
        pencilDup.pointRotate = 4 * LEFT;
        pencilDup.effLength = 0.798
        def pencilDup_updater(obj,dt):
            if(pencilDup.initAngToPlane >= 2 * PI/3):
                pencilDup.initAngToPlane = PI/3
                pencilDup.initAngSpeed /= 2
                pencilDup.pointRotate +=pencilDup.effLength * 1/np.sqrt(17) * DOWN +  pencilDup.effLength * 4 / np.sqrt(17) * RIGHT

            angToVert = np.arctan(0.25) + pencilDup.initAngToPlane - PI/2
            pencilDup.initAngSpeed += 0.4 * np.sin(angToVert) *dt
            pencilDup.initAngToPlane += pencilDup.initAngSpeed * dt
            pencilDup.rotate(-1 * pencilDup.initAngSpeed * dt, OUT, about_point = pencilDup.pointRotate)

        
        self.play(ReplacementTransform(pencil,pencilDup))
        
        self.wait(5)

        self.play(Rotate(pencilDup,-1 * PI/12,about_point = 4 * RIGHT + 2 * DOWN),Rotate(plane,-1 * PI/12,about_point = 4 * RIGHT + 2 * DOWN),run_time=2)
        self.play(Rotate(pencilDup,PI/12,about_point = 4 * RIGHT + 2 * DOWN),Rotate(plane,PI/12,about_point = 4 * RIGHT + 2 * DOWN),run_time=2)
        self.wait(11.2)
        self.play(Rotate(pencilDup,-1 * PI/12, about_point = 4 * LEFT))
        self.play(Rotate(pencilDup,PI/12, about_point = 4 * LEFT))
        self.wait(4)
        self.play(Indicate(leaddup))


        #TODO show the cylinder rolling down with no terminal velocity

        cylinderOut = Circle(radius = 0.8,fill_color = "#F5F5DC", color = WHITE,fill_opacity=1)
        cylinderIn = Circle(radius = 0.2,fill_opacity = 1, fill_color = "#555555",sheen_factor = 0.5, sheen_direction = UL,stroke_width = 0)
        cylinderDot=  SmallDot(color = BLACK)
        cylinderDot.move_to(0.7 * UP)

        cylinder = VGroup(cylinderOut,cylinderIn,cylinderDot)

        cylinder.move_to(9 * LEFT + 2.07 * UP)

        cylinder.initSpeed = 1.5
        cylinder.acc = 0.9
        
        def cylinder_updater(obj,dt):
            cylinder.shift(RIGHT * cylinder.initSpeed * 4/np.sqrt(17) * dt+ DOWN * cylinder.initSpeed /np.sqrt(17) * dt)
            cylinder.initSpeed += cylinder.acc * dt
            cylinder.rotate(-1 * cylinder.initSpeed / 0.8 * dt, about_point = obj.get_center())

        cylinder.add_updater(cylinder_updater)
        self.add(cylinder)
        self.wait(3.7)
        cylinder.remove_updater(cylinder_updater)
        cylinder.suspend_updating()
        self.play(FadeOut(cylinder))

        pencilDup.add_updater(pencilDup_updater)
        self.add(pencilDup)
        self.wait(0.83)
        self.play(Flash(4 * LEFT + 3.2 * RIGHT / np.sqrt(17) + DOWN * 0.8 / np.sqrt(17)),run_time = 0.2)
        self.add_sound("./sound/hitSound.wav",gain=10)
        self.wait(2.26 - 0.84)
        self.play(Flash(4 * LEFT + 6.4 * RIGHT / np.sqrt(17) + DOWN * 1.6 / np.sqrt(17)),run_time = 0.2)
        self.add_sound("./sound/hitSound.wav",gain=10)
        pencilDup.remove_updater(pencilDup_updater)
        pencil.suspend_updating()

        #bruh = LEFT * 4 + pencilDup.effLength * 1/np.sqrt(17) * DOWN +  pencilDup.effLength * 4 / np.sqrt(17) * RIGHT,color = YELLOW

        pivot1 = Dot(4 * LEFT + pencilDup.effLength * 1/np.sqrt(17) * DOWN +  pencilDup.effLength * 4 / np.sqrt(17) * RIGHT,color = GREEN)
        pivot2 = Dot(4 * LEFT + pencilDup.effLength * 1/np.sqrt(17) * DOWN * 2 +  2 * pencilDup.effLength * 4 / np.sqrt(17) * RIGHT,color = BLUE)

        radius1 = Line(4 * LEFT + pencilDup.effLength * 1/np.sqrt(17) * DOWN +  pencilDup.effLength * 4 / np.sqrt(17) * RIGHT,4 * LEFT + pencilDup.effLength * 1/np.sqrt(17) * DOWN +  pencilDup.effLength * 4 / np.sqrt(17) * RIGHT + 0.8 * RIGHT * np.cos(PI/3 - np.arctan(0.25))+ 0.8 * UP * np.sin(PI/3 - np.arctan(0.25)) ,color = GREEN)
        radius2 = Line(4 * LEFT + 2 * pencilDup.effLength * 1/np.sqrt(17) * DOWN +  2 * pencilDup.effLength * 4 / np.sqrt(17) * RIGHT,4 * LEFT + pencilDup.effLength * 1/np.sqrt(17) * DOWN +  pencilDup.effLength * 4 / np.sqrt(17) * RIGHT + 0.8 * RIGHT * np.cos(PI/3 - np.arctan(0.25))+ 0.8 * UP * np.sin(PI/3 - np.arctan(0.25)) ,color = BLUE)

        pauseButton = SVGMobject("./Images/pausebutton.svg")
        pauseButton.scale(0.5)

        pauseButton.move_to(6 * RIGHT + 3* UP)

        self.add(pauseButton)

        self.play(FadeIn(pivot1),FadeIn(radius1))
        
        velocityVector1=  Line(start= 4 * LEFT + pencilDup.effLength * 1/np.sqrt(17) * DOWN +  pencilDup.effLength * 4 / np.sqrt(17) * RIGHT + 0.8 * RIGHT * np.cos(PI/3 - np.arctan(0.25))+ 0.8 * UP * np.sin(PI/3 - np.arctan(0.25)), end = 4 * LEFT + pencilDup.effLength * 1/np.sqrt(17) * DOWN +  pencilDup.effLength * 4 / np.sqrt(17) * RIGHT + 0.8 * RIGHT * np.cos(PI/3 - np.arctan(0.25))+ 0.8 * UP * np.sin(PI/3 - np.arctan(0.25)) + RIGHT * 1 * np.cos(PI/6 + np.arctan(0.25))+ DOWN * 1 * np.sin(PI/6 + np.arctan(0.25))  ,color = GREEN)
        velocityVector1.add_tip(tip_length = 0.2)

        self.wait(1)
        self.play(FadeIn(velocityVector1))

        self.play(FadeIn(pivot2),FadeIn(radius2))
        self.wait(1)
        velocityVector2=  Line(start= 4 * LEFT + pencilDup.effLength * 1/np.sqrt(17) * DOWN +  pencilDup.effLength * 4 / np.sqrt(17) * RIGHT + 0.8 * RIGHT * np.cos(PI/3 - np.arctan(0.25))+ 0.8 * UP * np.sin(PI/3 - np.arctan(0.25)), end = 4 * LEFT + pencilDup.effLength * 1/np.sqrt(17) * DOWN +  pencilDup.effLength * 4 / np.sqrt(17) * RIGHT + 0.8 * RIGHT * np.cos(PI/3 - np.arctan(0.25))+ 0.8 * UP * np.sin(PI/3 - np.arctan(0.25)) + RIGHT * 0.5 * np.cos(PI/6 - np.arctan(0.25))+ UP * 0.5 * np.sin(PI/6 - np.arctan(0.25))  ,color = BLUE)
        velocityVector2.add_tip(tip_length = 0.2)

        self.play(FadeIn(velocityVector2))

        
        self.wait(2)
class Solve(Scene):
    def construct(self):
        # for i in range(-7,8):
        #         for j in range(-4,5):
        #             locDot = Dot()
        #             locDot.move_to(RIGHT*i + UP*j)
        #             self.add(locDot)
        
        hexagon = RegularPolygon(fill_opacity = 1, fill_color = "#F5F5DC",color=WHITE)
        hexagon.scale(0.8)
        lead = Circle(radius = 0.2,fill_opacity = 1, fill_color = "#555555",sheen_factor = 0.5, sheen_direction = UL,stroke_width = 0)
        pencil = VGroup(hexagon,lead)    
        pencil.rotate_about_origin(-np.arctan(0.25))
        pencil.move_to(4.22 * LEFT + 0.77 * UP)

        hexagon2 = RegularPolygon(fill_opacity = 0.5, fill_color = "#F5F5DC",color=WHITE,opacity = 0.5)
        hexagon2.scale(0.8)
        lead2 = Circle(radius = 0.2,fill_opacity = 0.5,opacity=0.5, fill_color = "#555555",sheen_factor = 0.5, sheen_direction = UL,stroke_width = 0)
        pencil2 = VGroup(hexagon2,lead2)
        pencil2.rotate_about_origin(-np.arctan(0.25))
        pencil2.move_to(4.22 * LEFT + 0.77 * UP)
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

        plane.rotate(-1 * np.arctan(0.25),about_point = 2 * DOWN + 4 * RIGHT)
        #plane = Line(2 * DOWN + 4 * RIGHT, 8 * LEFT + UP)

        angleLabel = TexMobject("\\theta")
        angleLabel.set_color(YELLOW)
        angleLabel.move_to(0.5 * RIGHT + 1.6 * DOWN)
        angleMark = Arc(PI - np.arctan(0.25),angle = np.arctan(0.25),radius=  3,arc_center = 4 * RIGHT + 2 * DOWN)
        angleMark.set_color(YELLOW)

        kick = Arrow(start = -6.11 * RIGHT + 1.96 * UP, end = -4.68 * RIGHT + 1.6 * UP, color = GREEN)

        self.add(plane,plane2,plane3,angleLabel,angleMark)

        self.wait(0.2)
        pauseButton = SVGMobject("./Images/pausebutton.svg")
        pauseButton.scale(0.5)

        pauseButton.move_to(6 * RIGHT + 3* UP)
        
        self.add(pencil,pauseButton)

        pencil.initAngSpeed = 1.3
        pencil.initAngToPlane = PI/3;
        pencil.pointRotate = 4 * LEFT;
        pencil.effLength = 0.798
        def pencil_updater(obj,dt):
            if(pencil.initAngToPlane >= 2 * PI/3):
                pencil.initAngToPlane = PI/3
                pencil.initAngSpeed /= 2
                pencil.pointRotate +=pencil.effLength * 1/np.sqrt(17) * DOWN +  pencil.effLength * 4 / np.sqrt(17) * RIGHT

            angToVert = np.arctan(0.25) + pencil.initAngToPlane - PI/2
            pencil.initAngSpeed += 0.4 * np.sin(angToVert) *dt
            pencil.initAngToPlane += pencil.initAngSpeed * dt
            pencil.rotate(-1 * pencil.initAngSpeed * dt, OUT, about_point = pencil.pointRotate)

        #TODO Draw velocity vectors

        velocityVector3=  Line(start= 4 * LEFT + 0.8 * RIGHT * np.cos(PI/3 - np.arctan(0.25))+ 0.8 * UP * np.sin(PI/3 - np.arctan(0.25)), end = 4 * LEFT + 0.8 * RIGHT * np.cos(PI/3 - np.arctan(0.25))+ 0.8 * UP * np.sin(PI/3 - np.arctan(0.25)) + RIGHT * 1 * np.cos(PI/6 + np.arctan(0.25))+ DOWN * 1 * np.sin(PI/6 + np.arctan(0.25))  ,color = GREEN)
        velocityVector3.add_tip(tip_length = 0.2)
        
        velocityVector4=  Line(start= 4 * LEFT +  0.8 * RIGHT * np.cos(PI/3 - np.arctan(0.25))+ 0.8 * UP * np.sin(PI/3 - np.arctan(0.25)) + 0.8 /np.sqrt(17) * UP + 3.2/np.sqrt(17) * LEFT, 
                            end = 4 * LEFT + 0.8 * RIGHT * np.cos(PI/3 - np.arctan(0.25))+ 0.8 * UP * np.sin(PI/3 - np.arctan(0.25)) +0.8 * UP * np.sin(PI/3 - np.arctan(0.25)) ,color = BLUE)
        velocityVector4.add_tip(tip_length = 0.2)

        pencil.add_updater(pencil_updater)
        self.add(pencil,pencil2)
        self.remove(pauseButton)
        self.wait(0.81)
        pencil.suspend_updating()
        pencil.remove_updater(pencil_updater)
        

        self.add(pauseButton)

        self.play(FadeIn(velocityVector3),FadeIn(velocityVector4))

        fourLabel = TexMobject("v_0")
        threeLabel = TexMobject("v_f")
        fourLabel.move_to(1.5*UP + 3.5 * LEFT)
        threeLabel.move_to(2.3 * LEFT)
        fourLabel.set_color(BLUE)
        threeLabel.set_color(GREEN)

        self.play(Write(fourLabel))
        self.play(Write(threeLabel))

        eqTriangle = Polygon(pencil2.get_center(),pencil2.get_center() + 0.8 * RIGHT * 4/np.sqrt(17) + 0.8 * DOWN / np.sqrt(17),4 * LEFT,color = YELLOW)

        self.play(DrawBorderThenFill(eqTriangle))

        consEnergyEq = TexMobject("\\frac{1}{2}m","v_f^2", "- \\frac{1}{2}m","v_0^2"," =  mgr \\sin","\\theta")
        consEnergyEq.set_color_by_tex_to_color_map({
            "v_f^2":GREEN,
            "v_0^2":BLUE,
            "\\theta":YELLOW
        })
        consEnergyEq.move_to(2 * UP)
        consEnergyEq2 = TexMobject("\\frac{1}{2}m","v_f^2", "- \\frac{1}{2}m","v_0^2"," =  mgr \\sin","\\theta")
        consEnergyEq2.set_color_by_tex_to_color_map({
            "v_f^2":GREEN,
            "v_0^2":BLUE,
            "\\theta":YELLOW
        })
        consEnergyEq2.move_to(3 * LEFT + 3 * UP)

        self.play(Write(consEnergyEq))
        self.play(Indicate(velocityVector3))
        self.play(Indicate(velocityVector4))
        self.play(Transform(consEnergyEq,consEnergyEq2))

        self.play(FadeOut(pencil2),FadeOut(eqTriangle),FadeOut(velocityVector4),FadeOut(velocityVector3),FadeOut(threeLabel),FadeOut(fourLabel))

        pivot1 = Dot(4 * LEFT,color = GREEN)
        pivot2 = Dot(4 * LEFT + pencil.effLength * 1/np.sqrt(17) * DOWN +  pencil.effLength * 4 / np.sqrt(17) * RIGHT,color = BLUE)

        radius1 = Line(4 * LEFT,4 * LEFT + 0.8 * RIGHT * np.cos(PI/3 - np.arctan(0.25))+ 0.8 * UP * np.sin(PI/3 - np.arctan(0.25)) ,color = GREEN)
        radius2 = Line(4 * LEFT + pencil.effLength * 1/np.sqrt(17) * DOWN +  pencil.effLength * 4 / np.sqrt(17) * RIGHT,4 * LEFT + 0.8 * RIGHT * np.cos(PI/3 - np.arctan(0.25))+ 0.8 * UP * np.sin(PI/3 - np.arctan(0.25)) ,color = BLUE)


        self.play(FadeIn(pivot1),FadeIn(radius1))
        
        velocityVector1=  Line(start= 4 * LEFT + 0.8 * RIGHT * np.cos(PI/3 - np.arctan(0.25))+ 0.8 * UP * np.sin(PI/3 - np.arctan(0.25)), end = 4 * LEFT + 0.8 * RIGHT * np.cos(PI/3 - np.arctan(0.25))+ 0.8 * UP * np.sin(PI/3 - np.arctan(0.25)) + RIGHT * 1 * np.cos(PI/6 + np.arctan(0.25))+ DOWN * 1 * np.sin(PI/6 + np.arctan(0.25))  ,color = GREEN)
        velocityVector1.add_tip(tip_length = 0.2)
        self.play(FadeIn(velocityVector1))

        self.play(FadeIn(pivot2),FadeIn(radius2))

        velocityVector2=  Line(start= 4 * LEFT +  0.8 * RIGHT * np.cos(PI/3 - np.arctan(0.25))+ 0.8 * UP * np.sin(PI/3 - np.arctan(0.25)), end = 4 * LEFT + 0.8 * RIGHT * np.cos(PI/3 - np.arctan(0.25))+ 0.8 * UP * np.sin(PI/3 - np.arctan(0.25)) + RIGHT * 0.5 * np.cos(PI/6 - np.arctan(0.25))+ UP * 0.5 * np.sin(PI/6 - np.arctan(0.25))  ,color = BLUE)
        velocityVector2.add_tip(tip_length = 0.2)

        self.play(FadeIn(velocityVector2))

        self.play(Indicate(pivot2))
        grav = Arrow(start = pencil.get_center(), end  =pencil.get_center() + DOWN,color = GREEN)
        self.play(GrowArrow(grav))
        self.wait(2)
        self.play(FadeOut(grav))

        def homotopy_shift_down(x,y,z,t):
            return[x,y-2 * t, z]
        self.play(Homotopy(homotopy_shift_down,pencil),Homotopy(homotopy_shift_down,angleLabel),Homotopy(homotopy_shift_down,angleMark),Homotopy(homotopy_shift_down,plane),Homotopy(homotopy_shift_down,plane2),Homotopy(homotopy_shift_down,plane3),
                    Homotopy(homotopy_shift_down,pivot1),Homotopy(homotopy_shift_down,pivot2),Homotopy(homotopy_shift_down,radius1),Homotopy(homotopy_shift_down,radius2),Homotopy(homotopy_shift_down,velocityVector1),Homotopy(homotopy_shift_down,velocityVector2))
        
        consOfAngMEq1 = TexMobject("\\vec{r_f}\\times \\vec{v_f}", "=","\\vec{r_0}\\times \\vec{v_0}")
        consOfAngMEq1.set_color_by_tex_to_color_map({
            "\\vec{r_f}\\times \\vec{v_f}" : GREEN,
            "\\vec{r_0}\\times \\vec{v_0}" : BLUE
        })

        momentArmInitial = DashedLine(4 * LEFT + pencil.effLength * 1/np.sqrt(17) * DOWN +  pencil.effLength * 4 / np.sqrt(17) * RIGHT,4 * LEFT + pencil.effLength * 1/np.sqrt(17) * DOWN +  pencil.effLength * 4 / np.sqrt(17) * RIGHT + 0.4 * RIGHT * np.cos(PI/3 - np.arctan(0.25))+ 0.4 * UP * np.cos(PI/3 - np.arctan(0.25)),color = GREEN)
        momentArmInitial.shift(2 * DOWN)
        
        consOfAngMEq2 = TexMobject("\\frac{r}{2}v_f", "=","rv_0")
        consOfAngMEq2.set_color_by_tex_to_color_map({
            "\\frac{r}{2}v_f" : GREEN,
            "rv_0" : BLUE
        })

        consOfAngMEq1.move_to(3 * LEFT + 1.8 * UP)
        consOfAngMEq2.move_to(3 * LEFT + 1.8 * UP)

        self.play(Write(consOfAngMEq1))
        self.play(Indicate(radius1))
        self.play(Indicate(velocityVector1))
        self.play(Indicate(radius2))
        self.play(Indicate(velocityVector2))

        self.play(FadeIn(momentArmInitial))
        self.play(Indicate(momentArmInitial))

        self.play(ReplacementTransform(consOfAngMEq1,consOfAngMEq2))

        solveEq = TexMobject("\\frac{1}{2}m","v_f^2", "- \\frac{1}{2}m","v_0^2"," =  mgr \\sin","\\theta")
        solveEq.set_color_by_tex_to_color_map({
            "v_f^2":GREEN,
            "v_0^2":BLUE,
            "\\theta":YELLOW
        })
        solveEq.move_to(3 * LEFT + 0.6 * UP)

        solveEq2 = TexMobject("\\frac{1}{2}m","(4v_0^2)", "- \\frac{1}{2}m","v_0^2"," =  mgr \\sin","\\theta")
        solveEq2.set_color_by_tex_to_color_map({
            "(4v_0^2)":BLUE,
            "v_0^2":BLUE,
            "\\theta":YELLOW
        }) 
        solveEq2.move_to(3 * LEFT+ 0.6 * UP)

        finalEq = TexMobject("\\Longrightarrow","v_0^2","= \\frac{2}{3}gr\\sin","\\theta")
        finalEq.set_color_by_tex_to_color_map({
            "v_0^2" : BLUE,
            "\\theta":YELLOW
        })
        finalEq.move_to(2.8 * RIGHT + 0.6 * UP)

        self.play(Write(solveEq))
        self.play(ReplacementTransform(solveEq,solveEq2))
        self.play(Write(finalEq))
        

        self.wait(2)
class Test(Scene):
    def construct(self):
        bruh = RegularPolygon()
        self.play(Flash(ORIGIN))

class Terminal(Scene):
    def construct(self):
        hexagon = RegularPolygon(fill_opacity = 1, fill_color = "#F5F5DC",color=WHITE)
        hexagon.scale(0.8)
        lead = Circle(radius = 0.2,fill_opacity = 1, fill_color = "#555555",sheen_factor = 0.5, sheen_direction = UL,stroke_width = 0)
        pencil = VGroup(hexagon,lead)    
        pencil.rotate_about_origin(-np.arctan(0.25))
        pencil.move_to(4.22 * LEFT + 0.77 * UP)

        hexagon2 = RegularPolygon(fill_opacity = 0.5, fill_color = "#F5F5DC",color=WHITE,opacity = 0.5)
        hexagon2.scale(0.8)
        lead2 = Circle(radius = 0.2,fill_opacity = 0.5,opacity=0.5, fill_color = "#555555",sheen_factor = 0.5, sheen_direction = UL,stroke_width = 0)
        pencil2 = VGroup(hexagon2,lead2)
        pencil2.rotate_about_origin(-np.arctan(0.25))
        pencil2.move_to(4.22 * LEFT + 0.77 * UP)
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

        plane.rotate(-1 * np.arctan(0.25),about_point = 2 * DOWN + 4 * RIGHT)
        #plane = Line(2 * DOWN + 4 * RIGHT, 8 * LEFT + UP)

        self.add(plane,plane2,plane3)

        angleLabel = TexMobject("\\theta")
        angleLabel.set_color(YELLOW)
        angleLabel.move_to(0.5 * RIGHT + 1.6 * DOWN)
        angleMark = Arc(PI - np.arctan(0.25),angle = np.arctan(0.25),radius=  3,arc_center = 4 * RIGHT + 2 * DOWN)
        angleMark.set_color(YELLOW)

        kick = Arrow(start = -6.11 * RIGHT + 1.96 * UP, end = -4.68 * RIGHT + 1.6 * UP, color = GREEN)
        self.add(angleLabel,angleMark)

        self.wait(0.2)
        pauseButton = SVGMobject("./Images/pausebutton.svg")
        pauseButton.scale(0.5)

        pauseButton.move_to(6 * RIGHT + 3* UP)
        

        pencil.initAngSpeed = 1.3
        pencil.initAngToPlane = PI/3;
        pencil.pointRotate = 4 * LEFT;
        pencil.effLength = 0.8
        def pencil_updater(obj,dt):
            if(pencil.initAngToPlane >= 2 * PI/3):
                pencil.initAngToPlane = PI/3
                #pencil.initAngSpeed /= 2
                pencil.pointRotate +=pencil.effLength * 1/np.sqrt(17) * DOWN +  pencil.effLength * 4 / np.sqrt(17) * RIGHT

            angToVert = np.arctan(0.25) + pencil.initAngToPlane - PI/2
            #pencil.initAngSpeed += 0.4 * np.sin(angToVert) *dt
            pencil.initAngToPlane += pencil.initAngSpeed * dt
            pencil.rotate(-1 * pencil.initAngSpeed * dt, OUT, about_point = pencil.pointRotate)
        pencil.add_updater(pencil_updater)
        self.add(pencil)

        pencils = []
        velocities = []

        for i in range(0,6):
            if(i % 2 == 0):
                hexagonbruh = RegularPolygon(fill_opacity = 0.5, fill_color = "#FF0012",color=WHITE,opacity = 0.5)
                hexagonbruh.scale(0.8)
                leadbruh = Circle(radius = 0.2,fill_opacity = 0.5,opacity=0.5, fill_color = "#555555",sheen_factor = 0.5, sheen_direction = UL,stroke_width = 0)
                pencilbruh = VGroup(hexagonbruh,leadbruh)
                pencilbruh.rotate_about_origin(-np.arctan(0.25))
                pencilbruh.move_to(4.22 * LEFT + 0.77 * UP + 3.2 * i * RIGHT / np.sqrt(17) + DOWN * 0.8 * i / np.sqrt(17))
                pencils.append(pencilbruh)
            else:
                hexagonbruh = RegularPolygon(fill_opacity = 0.5, fill_color = "#00b32c",color=WHITE,opacity = 0.5)
                hexagonbruh.scale(0.8)
                leadbruh = Circle(radius = 0.2,fill_opacity = 0.5,opacity=0.5, fill_color = "#555555",sheen_factor = 0.5, sheen_direction = UL,stroke_width = 0)
                pencilbruh = VGroup(hexagonbruh,leadbruh)
                pencilbruh.rotate_about_origin(-np.arctan(0.25))
                pencilbruh.move_to(4.22 * LEFT + 0.77 * UP + 3.2 * i * RIGHT / np.sqrt(17) + DOWN * 0.8 * i / np.sqrt(17))
                pencils.append(pencilbruh)
            velBruh=  Line(start= 4 * LEFT +  0.8 * RIGHT * np.cos(PI/3 - np.arctan(0.25))+ 0.8 * UP * np.sin(PI/3 - np.arctan(0.25)) + 0.8 /np.sqrt(17) * UP + 3.2/np.sqrt(17) * LEFT + 3.2 * i * RIGHT / np.sqrt(17) + DOWN * 0.8 * i / np.sqrt(17), 
                            end = 4 * LEFT + 0.8 * RIGHT * np.cos(PI/3 - np.arctan(0.25))+ 0.8 * UP * np.sin(PI/3 - np.arctan(0.25)) +0.8 * UP * np.sin(PI/3 - np.arctan(0.25))+ 3.2/np.sqrt(17) * LEFT + 3.2 * (i+1) * RIGHT / np.sqrt(17) + DOWN * 0.8 * (i+1) / np.sqrt(17) ,color = BLUE)
            velBruh.add_tip(tip_length = 0.2)
            velocities.append(velBruh)

        for i in range (0,6):
            self.add(pencils[i],velocities[i])
            if(not(i == 0)):
                self.play(Flash(4 * LEFT + i * 3.2 * RIGHT / np.sqrt(17) + i * DOWN * 0.8 / np.sqrt(17)),run_time = 0.2)
                self.add_sound("./sound/hitSound.wav",gain=3)
            self.wait(0.71)

        self.add(pauseButton)
        self.play(Flash(4 * LEFT + 6 * 3.2 * RIGHT / np.sqrt(17) + 6 * DOWN * 0.8 / np.sqrt(17)),run_time = 0.2)
        self.add_sound("./sound/hitSound.wav",gain=3)







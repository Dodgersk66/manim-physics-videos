from manimlib.imports import *
import math
import numpy


class Spring(VMobject):
    CONFIG = {
        "color": BLUE,
        "fill_color": BLUE,
    }

    def __init__(self, start,finish,turns,height,**kwargs):
        VMobject.__init__(self, **kwargs)
        pointsArray = [start]

        #Simple for loop to zig zag and get the points
        for i in range(0,turns):
            if(i==0):
                pointsArray.append(start-0.5*height+(finish+(-1)*start)/turns*0.5)
                
            elif(i < turns):
                
                if(i % 2 == 1):
                    pointsArray.append(start+0.5*height+(finish+(-1)*start)/turns*(0.5+i))
                    
                elif(i % 2 == 0):
                    pointsArray.append(start-0.5*height+(finish+(-1)*start)/turns*(0.5+i))
        pointsArray.append(finish)
        self.set_points_as_corners(pointsArray)

    def get_vertices(self):
        return self.get_start_anchors()
    
    def set_start(self,start):
        self.start = start
        self.__init__(self,self.start,self.finish,self.turns,self.height)
        return self

    def set_finish(self,finish):
        self.finish = finish
        self.__init__(self,self.start,self.finish,self.turns,self.height)
        return self

#Intro scene, only adjust title and subtitle
class intro(Scene):
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
        title = TextMobject("Waves and Oscillations")
        title.scale(2)

        logo = ImageMobject("logo4.0.png")
        logo.scale(1.5)
        logo.move_to(UP*0.8)

        subtitle = TextMobject("Ep. 1: Simple Harmonic Motion")
        subtitle.scale(1.2)
        subtitle.set_color(YELLOW)
        subtitle.move_to(DOWN*1.3)

        self.play(FadeIn(plane),run_time=1.2)
        self.play(FadeInFrom(mainHexagon,direction=3*UP),rate_func=rush_into,run_time=0.8);
        self.add_sound("./hitSound.wav",gain=10);
        #self.play(Homotopy(homotopyTest,mainHexagon))
        self.play(Rotate(mainHexagon,-1*PI*26.57/180,about_point=ORIGIN),run_time=0.2)
        self.add_sound("./hitSound.wav",gain=10);
        # for i in range(1,3):
        #     self.play(Rotate(mainHexagon,-1*PI/3,about_point=i*2/math.sqrt(5)*RIGHT + i/math.sqrt(5)*DOWN),run_time=0.6)
        #     self.add_sound("./hitSound.wav",gain=10);
        #self.add_sound("./Recording (17).m4a",gain=10,time_offset=0.5)
        self.add_sound("./Recording (21).m4a",gain=10,time_offset=0.33)
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

class introductionToSeries(Scene):
    def construct(self):
        firstQ = TextMobject("Why waves?")
        firstQ.move_to(UP*3+LEFT*2)
        firstQ.set_color(YELLOW)

        secondQ = TextMobject("Why oscillations?")
        secondQ.move_to(UP*3 + RIGHT*2)
        secondQ.set_color(YELLOW)

        testSpring = Spring(5*LEFT+0.25*DOWN,0.25*DOWN+5*RIGHT,10,0.5*UP,color = WHITE,stroke_width = 3)
        testSpring.counter = 0

        def springUpdater(d,dt):
            time = d.counter/60
            d.set_start((5+np.sin(5*time))*LEFT + 0.25 * DOWN)
            d.set_finish((5+np.sin(5*time))*RIGHT+0.25*DOWN)
            d.counter += 1
            return d
            
        testSpring.add_updater(springUpdater)

        self.add(firstQ)
        self.wait(1)
        self.add(secondQ)
        self.wait(1)
        self.add(testSpring)
        self.wait(3)
#Introducing SHM/Oscillations
class startScene(Scene):
    def construct(self):
        
        #Setting the backdrop
        wallLeft = Line(5*LEFT + DOWN,5*LEFT + 4*UP,stroke_width = 2)
        wallBot = Line(5*LEFT + DOWN,5*RIGHT + DOWN,stroke_width = 2) 
        self.add(wallLeft)
        self.add(wallBot)
        

        
        testRect = Square(side_length =1.5,fill_color="#7d7d7d", fill_opacity=1,stroke_width=2,color=WHITE,sheen_direction=UL,
            sheen_factor=0.5,)
        testRect.move_to(0.75*RIGHT+0.25*DOWN)
        testSpring = Spring(5*LEFT+0.25*DOWN,0.25*DOWN,10,0.5*UP,color = WHITE,stroke_width = 3)
        stifferSpring = Spring(5*LEFT+0.25*DOWN,0.25*DOWN,20,0.5*UP,color = WHITE,stroke_width = 3)
        tallerSpring = Spring(5*LEFT+0.25*DOWN,0.25*DOWN,20,0.9*UP,color = WHITE,stroke_width = 3)

        testRect.counter = 0

        #Polygon(2*RIGHT + 0.5*DOWN, 2.5*RIGHT + 0.5 * DOWN, 2.5*RIGHT + 0.5*UP, 2*RIGHT + 0.5*UP,fill_color = "#7d7d7d",fill_opacity = 1,stroke_width=2,color=WHITE)

        #testSpring.originalLength = testSpring.get_width()
        testSpring.counter = 0

        def rectUpdater(d,dt):
            time = testRect.counter/60
            d.move_to((0.75+2*np.sin(4*time)*np.exp(-time))*RIGHT+0.25*DOWN)
            testRect.counter += 1

        def springUpdater(d,dt):
            time = testSpring.counter/60

            d.stretch_to_fit_width((5+2*np.sin(4*time)*np.exp(-time)))
            d.align_to(5*LEFT+0.25*DOWN,LEFT)

            testSpring.counter += 1

        testRect.add_updater(rectUpdater)
        testSpring.add_updater(springUpdater)
        self.add(testSpring,testRect)
        self.wait(8)
        self.play(ReplacementTransform(testSpring, stifferSpring))
        self.wait(1)
        self.play(ReplacementTransform(stifferSpring,tallerSpring))
        #testShape = Spring(2*LEFT,(2-2.8*math.sin(2*math.pi*i/40))*RIGHT,20,0.5*UP)

        # def springUpdater(d,dt):
        #     d.stretch


        # for i in range(0,80):
        #     testShape = Spring(2*LEFT,(2-2.8*math.sin(2*math.pi*i/40))*RIGHT,20,0.5*UP)
        #     testRect = Polygon((2-2.8*math.sin(2*math.pi*i/40))*RIGHT+0.5*DOWN,(2.5-2.8*math.sin(2*math.pi*i/40))*RIGHT+0.5*DOWN,(2.5-2.8*math.sin(2*math.pi*i/40))*RIGHT+0.5*UP,(2-2.8*math.sin(2*math.pi*i/40))*RIGHT+0.5*UP)
        #     self.add(testRect)
        #     self.add(testShape)
        #     self.wait(0.02)
        #     self.remove(testRect)
        #     self.remove(testShape)
# class complex_solution_explanation(Scene):
#     def construct(self):
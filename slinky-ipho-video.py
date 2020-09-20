from manimlib.imports import *
import math
import numpy

class Spring(VMobject):
    CONFIG = {
        "color": BLUE,
        "fill_color": BLUE,
        "start":3*LEFT,
        "finish":3*RIGHT,
        "turns":10,
        "height":UP,
        "mass":0,
        "spring_constant":5
    }

    def __init__(self,**kwargs):
        VMobject.__init__(self, **kwargs)
        pointsArray = [self.start]

        #Simple for loop to zig zag and get the points
        if(self.mass == 0):
            for i in range(0,self.turns):
                if(i==0):
                    pointsArray.append(self.start-0.5*self.height+(self.finish+(-1)*self.start)/self.turns*0.5)
                    
                elif(i < self.turns):
                    
                    if(i % 2 == 1):
                        pointsArray.append(self.start+0.5*self.height+(self.finish+(-1)*self.start)/self.turns*(0.5+i))
                        
                    elif(i % 2 == 0):
                        pointsArray.append(self.start-0.5*self.height+(self.finish+(-1)*self.start)/self.turns*(0.5+i))
            pointsArray.append(self.finish)
            self.clear_points()
            self.set_points_as_corners(pointsArray)
            self.update()
        else:
            self.construct_with_gravity()
    
    def construct_with_gravity(self):
        pointsArray = [self.start]
        prevPoint = self.start
        height_var = self.height
        
        for i in range(0,self.turns):
            mass_var = self.mass * 9.8 * (self.turns -1-i) / self.turns
            if(i==0):
                prevPoint = self.get_new_point(prevPoint,self.height/2,mass_var)
                pointsArray.append(prevPoint)
            else:
                if(i==self.turns):
                    height_var = self.height/2
                if(i % 2 == 0):
                    prevPoint = self.get_new_point(prevPoint,height_var,mass_var)
                    pointsArray.append(prevPoint)
                else:
                    prevPoint = self.get_new_point(prevPoint,-1*height_var, mass_var)
                    pointsArray.append(prevPoint)
        self.clear_points()
        self.set_points_as_corners(pointsArray)
        self.update()

                
    def get_new_point(self,prevPoint,height,force):
        stretch = force / self.spring_constant
        return prevPoint + height + stretch * DOWN

    def get_vertices(self):
        return self.get_start_anchors()
    
    def set_start(self,start):
        self.start = start
        self.__init__()
        
        return self

    def set_finish(self,finish):
        self.finish = finish
        self.__init__()
        
        return self
    
    def ends_updater(self):
        pointsArray = [self.start]

        #Simple for loop to zig zag and get the points
        for i in range(0,self.turns):
            if(i==0):
                pointsArray.append(self.start-0.5*self.height+(self.finish+(-1)*self.start)/self.turns*0.5)
                
            elif(i < self.turns):
                
                if(i % 2 == 1):
                    pointsArray.append(self.start+0.5*self.height+(self.finish+(-1)*self.start)/self.turns*(0.5+i))
                    
                elif(i % 2 == 0):
                    pointsArray.append(self.start-0.5*self.height+(self.finish+(-1)*self.start)/self.turns*(0.5+i))
        pointsArray.append(self.finish)
        self.clear_points()
        self.set_points_as_corners(pointsArray)



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
        title = TextMobject("Physics of a Slinky")
        title.scale(2)

        logo = ImageMobject("./Images/logo4.0.png")
        logo.scale(1.5)
        logo.move_to(UP*0.8)

        subtitle = TextMobject("Part 1")
        subtitle.scale(1.2)
        subtitle.set_color(YELLOW)
        subtitle.move_to(DOWN*1.3)

        self.play(FadeIn(plane),run_time=1.2)
        self.play(FadeInFrom(mainHexagon,direction=3*UP),rate_func=rush_into,run_time=0.8);
        self.add_sound("./sound/hitSound.wav",gain=10);
        #self.play(Homotopy(homotopyTest,mainHexagon)        self.play(Rotate(mainHexagon,-1*PI*26.57/180,about_point=ORIGIN),run_time=0.2)
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

class introduction_scene(Scene):
    def construct(self):
        starting_question = TextMobject("What exactly is a slinky?")
        starting_question.scale(0.8)
        starting_question.move_to(3.9*LEFT + 3.2*UP)

        starting_answer = TextMobject("  Just a spring!")
        starting_answer.set_color(YELLOW)
        starting_answer.scale(0.8)
        starting_answer.next_to(starting_question)
        
        problem_state_massless = TexMobject("\\text{``Consider the }","\\text{massless}","\\text{ spring...''}")
        problem_state_massive = TextMobject("\\text{``Consider the }","\\text{massive}","\\text{ spring...''}")
        problem_state_massless.set_color_by_tex_to_color_map({"massless" : YELLOW})
        problem_state_massive.set_color_by_tex_to_color_map({"massive" : YELLOW})
        problem_state_massless.move_to(2*UP)
        problem_state_massive.move_to(2*UP)

        question1 = TextMobject("Part 1. ","How much does a slinky stretch when held from one end?")
        question1.set_color_by_tex_to_color_map({"Part 1. " : YELLOW})
        question1.scale(0.8)

        question2 = TextMobject("Part 2. ","How does a slinky drop?")
        question2.set_color_by_tex_to_color_map({"Part 2. " : YELLOW})
        question2.move_to(1*DOWN)
        question2.scale(0.8)

        question3 = TextMobject("Part 3. ","What happens when a slinky is hung from both ends?")
        question3.set_color_by_tex_to_color_map({"Part 3. " : YELLOW})
        question3.move_to(2*DOWN)
        question3.scale(0.8)


        self.play(Write(starting_question))
        self.wait(1.3)
        self.play(Write(starting_answer))
        self.play(Write(problem_state_massless))
        self.wait(0.8)
        self.play(Transform(problem_state_massless,problem_state_massive))
        self.play(FadeIn(question1))
        self.wait(0.9)
        self.play(FadeIn(question2))
        self.wait(0.9)
        self.play(FadeIn(question3))
        self.wait(0.9)



class explain_difference(Scene):
    def construct(self):

        hand1 = ImageMobject("./Images/hand.png")
        hand1.scale(0.5)
        hand1.move_to(3*LEFT+3.3*UP)
        

        hand2 = ImageMobject("./Images/hand.png")
        hand2.scale(0.5)
        hand2.move_to(3*RIGHT + 3.3*UP)
        

        massless_spring = Spring(start = 3*LEFT+3*UP,finish = 3*LEFT,turns = 20,height = 0.6*LEFT)   
        massless_spring_stretched = Spring(start = 3*LEFT + 3*UP, finish = 3*LEFT + DOWN, turns = 20,height = 0.6*LEFT)
        hanging_spring = Spring(mass = 1, start = 3*RIGHT+3*UP,height=0.6*RIGHT,spring_constant = 50,turns=30)
        hanging_spring.make_smooth()
        massless_spring.make_smooth()
        massless_spring_stretched.make_smooth()

        self.add(massless_spring,hand1)
        self.wait(0.6)
        self.add(hanging_spring,hand2)
        self.wait(2)
        self.play(Transform(massless_spring,massless_spring_stretched),run_time = 1.5)
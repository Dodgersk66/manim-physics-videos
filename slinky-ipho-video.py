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

        line = Line(5*LEFT + 1.5*UP,5*RIGHT + 1.5 * UP)

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
        self.wait(0.6)
        self.play(GrowFromCenter(line))

        self.play(FadeIn(question1))
        self.wait(0.9)
        self.play(FadeIn(question2))
        self.wait(0.9)
        self.play(FadeIn(question3))
        self.wait(0.9)


        def topStuffMove(x,y,z,t):
            return[x,y+2.5*t,z]
        def topQuestionMove(x,y,z,t):
            return[x,y+1.9*t,z]
        def midQuestionMove(x,y,z,t):
            return[x,y+1.3*t,z]
        def botQuestionMove(x,y,z,t):
            return[x,y+0.7*t,z]

        self.play(Homotopy(topStuffMove,line),Homotopy(topStuffMove,starting_question),Homotopy(topStuffMove,starting_answer),Homotopy(topStuffMove,problem_state_massless),Homotopy(topQuestionMove,question1),Homotopy(midQuestionMove,question2),Homotopy(botQuestionMove,question3))
        self.wait(1)




class explain_difference(Scene):
    def construct(self):

        hand1 = ImageMobject("./Images/hand.png")
        hand1.scale(0.5)
        hand1.move_to(3*LEFT+3.3*UP)
        

        hand2 = ImageMobject("./Images/hand.png")
        hand2.scale(0.5)
        hand2.move_to(3*RIGHT + 3.3*UP)
        

        massless_spring = Spring(start = 3*LEFT+3*UP,finish = 3*LEFT,turns = 20,height = 0.6*LEFT)   
        massless_spring_zero = Spring(start = 3*LEFT + 3*UP, finish = 3*LEFT + 2.5*UP, turns = 20,height = 0.6*LEFT)
        hanging_spring = Spring(mass = 1, start = 3*RIGHT+3*UP,height=0.6*RIGHT,spring_constant = 50,turns=30)
        hanging_spring.make_smooth()
        massless_spring.make_smooth()
        massless_spring_zero.make_smooth()
        massless_spring.next_to(hand1,direction=DOWN)
        massless_spring.shift(0.25*UP)
        massless_spring_zero.next_to(hand1,direction=DOWN)
        massless_spring_zero.shift(0.25*UP)

        hanging_spring.next_to(hand2,direction=DOWN)
        hanging_spring.shift(0.25*UP)

        rest_length_label = TexMobject("\\ell")
        rest_length_label.scale(0.8)
        rest_length_label.next_to(massless_spring,direction=LEFT)
        zero_label = TexMobject("\\ell = 0")
        zero_label.scale(0.8)
        zero_label.next_to(massless_spring_zero,direction=LEFT)

        

        hanging_length = DoubleArrow(0.8*LEFT + hanging_spring.get_top(),0.8*LEFT +hanging_spring.get_bottom(),stroke_width=0.5)
        hanging_label = TexMobject("L")
        hanging_label.next_to(hanging_length,direction=LEFT)
        hanging_spring_scaled = Spring(mass = 1, start = 3.5*LEFT+3*UP,height=0.6*RIGHT,spring_constant = 50,turns=30)
        hanging_spring_scaled.scale(1.8)
        hanging_spring_scaled.make_smooth()
        hanging_spring_scaled.align_to(5*LEFT + 3.5*UP,UP)

        self.add(massless_spring,hand1)
        self.wait(0.6)
        self.add(hanging_spring,hand2)
        self.wait(2)
        self.play(Write(rest_length_label))
        self.play(Transform(massless_spring,massless_spring_zero),Transform(rest_length_label,zero_label),run_time = 1.5)
        self.wait(1.5)
        self.play(FadeOut(massless_spring),FadeOut(rest_length_label),FadeOut(hand1),FadeOut(hand2))
        self.play(Transform(hanging_spring,hanging_spring_scaled))
        print(hanging_spring_scaled.get_top() - hanging_spring_scaled.get_bottom())
        #self.play(GrowFromCenter(hanging_length),FadeIn(hanging_label))

class SolvingScene(Scene):
    def construct(self):
        hanging_spring_scaled = Spring(mass = 1, start = 3.5*LEFT+3*UP,height=0.6*RIGHT,spring_constant = 50,turns=30)
        

        hanging_spring_scaled.scale(1.8)
        hanging_spring_scaled.make_smooth()
        hanging_spring_scaled.align_to(5*LEFT + 3.5*UP,UP)
        hanging_spring_scaled_line = Line(hanging_spring_scaled.get_bottom(),hanging_spring_scaled.get_top(),color = BLUE)

        for i in range(-7,8):
            for j in range(-4,5):
                locDot = Dot()
                locDot.move_to(RIGHT*i + UP*j)
                self.add(locDot)

        t0 = TextMobject("N")
        t0.align_to(6.5*LEFT,LEFT)
        t0.align_to(3.5*UP,UP)
        t5 = TextMobject("N = 5")
        t5.align_to(6.5*LEFT,LEFT)
        t5.align_to(3.5*UP,UP)
        t6 = TextMobject("N = 6")
        t6.align_to(6.5*LEFT,LEFT)
        t6.align_to(3.5*UP,UP)
        t7 = TextMobject("N = 7")
        t7.align_to(6.5*LEFT,LEFT)
        t7.align_to(3.5*UP,UP)
        t8 = TextMobject("N = 8")
        t8.align_to(6.5*LEFT,LEFT)
        t8.align_to(3.5*UP,UP)
        t9 = TextMobject("N = 9")
        t9.align_to(6.5*LEFT,LEFT)
        t9.align_to(3.5*UP,UP)
        t10 = TexMobject("N \\rightarrow \infty")
        t10.align_to(6.5*LEFT,LEFT)
        t10.align_to(3.5*UP,UP)
        springBot = hanging_spring_scaled.get_bottom()

        n = VGroup()
        n5 = VGroup(*self.return_mass_list(5,5.1156,springBot))
        n6 = VGroup(*self.return_mass_list(6,5.1156,springBot))
        n7 = VGroup(*self.return_mass_list(7,5.1156,springBot))
        n8 = VGroup(*self.return_mass_list(8,5.1156,springBot))
        n9 = VGroup(*self.return_mass_list(9,5.1156,springBot))
        nbig = VGroup(*self.return_mass_list(100,5.1156,springBot))
        
        d = VGroup()
        d5 = VGroup(*self.return_cut_list(5,5.1156,springBot))
        d6 = VGroup(*self.return_cut_list(6,5.1156,springBot))
        d7 = VGroup(*self.return_cut_list(7,5.1156,springBot))
        d8 = VGroup(*self.return_cut_list(8,5.1156,springBot))
        d9 = VGroup(*self.return_cut_list(9,5.1156,springBot))


        singleSpring = Line(3.5 *LEFT + UP,3.5*LEFT + 1.2 * UP,color=BLUE)
        singleMass = Dot(3.5*LEFT + UP,fill_color = YELLOW,radius = 0.04)

        singleSpringMass = VGroup(singleSpring,singleMass)

        scale = 5.1156/15
        labelList = []
        for i in range(1,7):
            label = TexMobject("i = "+ str(i))
            label.scale(i/3.7)
            label.move_to(RIGHT + springBot + (i*(i+1)/4 + i*(i-1)/4)*scale*UP)
            print(i)
            labelList.append(label)
        tempMarker = TexMobject("i = 3")
        tempMarker.scale(3/3.7)
        tempMarker.move_to(RIGHT  +springBot + (3 + 3 * 2 / 4)*scale * UP)
        
        finalMarker = TexMobject("i")
        finalMarker.scale(3/3.7)
        finalMarker.move_to(springBot + (3 + 3 * 2 / 4)*scale * UP)
        finalMarker.align_to(tempMarker,LEFT)

        labelGroup = VGroup(*labelList)
    

        self.add(hanging_spring_scaled)
        self.add(t0)
        self.wait(0.8)
        
        self.add(n)
        self.add(d)
        self.play(Transform(t0,t5),Transform(n,n5),Transform(d,d5))
        self.play(Transform(hanging_spring_scaled,hanging_spring_scaled_line))
        
        self.wait(0.4)
        self.play(Transform(n,n6),Transform(d,d6),Transform(t0,t6))

        self.wait(0.4)
        self.play(Transform(n,n7),Transform(d,d7),Transform(t0,t7))

        self.wait(0.4)
        self.play(Transform(n,n8),Transform(d,d8),Transform(t0,t8))
        
                
        self.wait(0.4)
        self.play(Transform(n,n9),Transform(d,d9),Transform(t0,t9))
        
        self.wait(0.4)
        self.remove(d)
        self.play(Transform(n,nbig),Transform(t0,t10))
        self.wait(1)
        
        self.play(Transform(n,n5),Transform(t0,t5))
        self.add(d5)
        self.wait(0.4)

        self.play(ShowIncreasingSubsets(labelGroup,run_time = 7))
        self.add(tempMarker,finalMarker)
        self.wait(0.6)
        self.play(FadeOut(labelGroup))
        self.play(FadeOut(tempMarker))


        massMarker = TexMobject("M")
        massMarker.move_to(5 * LEFT + UP)

        forceEquation = TexMobject("F_T = img")
        forceEquation2 = TexMobject("F_T = \\frac{iMg}{N}")
        forceHooke = TexMobject("F_T = k_i\\Delta x_i = \\frac{iMg}{N}")
        forceHooke2 = TexMobject("F_T = k_i\\Delta x_i = \\frac{iMg}{N}")

        displacementEq = TexMobject("\\Delta x_i = \\frac{iMg}{k_iN}")


        forceEquation.move_to(2* RIGHT + 2*UP)
        forceEquation2.move_to(2* RIGHT + 2*UP)
        forceHooke.move_to(2.6 * RIGHT + 0.9 * UP)
        forceHooke.align_to(forceEquation2, direction = LEFT, alignment_vect=  RIGHT)

        forceHooke2.move_to(2.6 * RIGHT + 0.9 * UP)
        forceHooke2.align_to(forceEquation2, direction = LEFT, alignment_vect=  RIGHT)
        displacementEq.move_to(-0.2 * UP)
        displacementEq.align_to(forceHooke,direction = RIGHT, alignment_vect = RIGHT)


        self.play(Write(massMarker))
        self.play(Write(forceEquation))
        self.play(Transform(forceEquation, forceEquation2))
        self.play(Write(forceHooke))
        self.add(forceHooke2)
        self.play(Transform(forceHooke2,displacementEq))
        self.wait(0.5)

        totalDisplaceEq = TexMobject("\\Delta X = \\sum_{i = 1}^{N} \\frac{iMg}{k_iN}")
        totalDisplaceEq2 = TexMobject("\\Delta X = \\sum_{i = 1}^{N} \\frac{iMg}{k_iN} = \\frac{(N+1)Mg}{2k_i}")
        totalDisplaceEq.move_to(0.5 * RIGHT + 2 * UP)
        totalDisplaceEq2.move_to(2  * UP)
        totalDisplaceEq2.align_to(totalDisplaceEq,direction = LEFT,alignment_vect = LEFT)
        
        self.play(FadeOut(forceEquation),FadeOut(forceHooke),FadeOut(forceHooke2))

        self.play(Write(totalDisplaceEq))
        self.wait(0.3)
        self.play(Write(totalDisplaceEq2))
        self.play(FadeOut(totalDisplaceEq),run_time=0.1)

        divideLine = Line(1 * LEFT + UP, 5 * RIGHT + UP)
        subtitle = TexMobject("\\text{Finding }k_i")
        subtitle.set_color(YELLOW)
        subtitle.move_to(0.5 * UP + 0.5 * RIGHT)

        self.play(GrowFromCenter(divideLine),FadeIn(subtitle))

        def shiftUp(x,y,z,t):
            return[x,y+3*t,z]
        self.play(Homotopy(shiftUp, divideLine),Homotopy(shiftUp, subtitle),Homotopy(shiftUp, totalDisplaceEq2))
        self.wait(2)

        def shiftLeft(x,y,z,t):
            return[x-t,y,z]

        vertDiv = Line(2*LEFT + 3.5*UP,2*LEFT+DOWN)

        floor = Polygon(2*LEFT+DOWN,8*RIGHT+DOWN,8*RIGHT+DOWN*4,2*LEFT+DOWN*4,fill_opacity=1,fill_color=DARK_GRAY,sheen_direction = DOWN,stroke_width = 0,sheen_factor=0.6)


        self.play(Homotopy(shiftLeft,subtitle),FadeIn(vertDiv))
        self.add(floor)
        self.wait(1.5)






        # self.play(GrowFromCenter(singleSpringMass),run_time = 2)
        # #Put marking the generalized coordinate stuff here!!!!!
        
        # self.play(FadeOut(n5),FadeOut(t0),FadeOut(hanging_spring_scaled),ScaleInPlace(singleSpringMass,6))

    

    def return_mass_list(self,N,reqLength,bottomPoint):
        initialMass = Dot(bottomPoint,radius = 0.04)
        massList = [initialMass]
        length = N * (N+1)/2
        scale = reqLength/length
        for i in range(1,N+1):
            coord = bottomPoint + scale * i * (i+1) / 2 * UP
            massList.append(Dot(coord,radius = 0.04))
        return massList
    
    def return_cut_list(self,N,reqLength,bottomPoint):
        initialMass = DashedLine(bottomPoint+0.5*LEFT, bottomPoint + 0.5 * RIGHT)
        massList = [initialMass]
        length = N * (N+1)/2
        scale = reqLength/length
        for i in range(1,N):
            coord = bottomPoint + scale * i * (i+1) / 2 * UP
            massList.append(DashedLine(coord+0.5*LEFT,coord + 0.5 * RIGHT))
        return massList


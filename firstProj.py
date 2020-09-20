from manimlib.imports import *
import math
import numpy

class Pendulum(VGroup):
    CONFIG = {
        "length": 3,
        "gravity": 9.8,
        "weight_diameter": 0.5,
        "initial_theta": 0.3,
        "omega": 0,
        "damping": 0.1,
        "top_point": 2 * UP,
        "rod_style": {
            "stroke_width": 3,
            "stroke_color": LIGHT_GREY,
            "sheen_direction": UP,
            "sheen_factor": 1,
        },
        "weight_style": {
            "stroke_width": 0,
            "fill_opacity": 1,
            "fill_color": GREY_BROWN,
            "sheen_direction": UL,
            "sheen_factor": 0.5,
            "background_stroke_color": BLACK,
            "background_stroke_width": 3,
            "background_stroke_opacity": 0.5,
        },
        "dashed_line_config": {
            "num_dashes": 25,
            "stroke_color": WHITE,
            "stroke_width": 2,
        },
        "angle_arc_config": {
            "radius": 1,
            "stroke_color": WHITE,
            "stroke_width": 2,
        },
        "velocity_vector_config": {
            "color": RED,
        },
        "theta_label_height": 0.25,
        "set_theta_label_height_cap": False,
        "n_steps_per_frame": 100,
        "include_theta_label": True,
        "include_velocity_vector": False,
        "velocity_vector_multiple": 0.5,
        "max_velocity_vector_length_to_length_ratio": 0.5,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_fixed_point()
        self.create_rod()
        self.create_weight()
        self.rotating_group = VGroup(self.rod, self.weight)
        self.create_dashed_line()
        self.create_angle_arc()
        if self.include_theta_label:
            self.add_theta_label()
        if self.include_velocity_vector:
            self.add_velocity_vector()

        self.set_theta(self.initial_theta)
        self.update()

    def create_fixed_point(self):
        self.fixed_point_tracker = VectorizedPoint(self.top_point)
        self.add(self.fixed_point_tracker)
        return self

    def create_rod(self):
        rod = self.rod = Line(UP, DOWN)
        rod.set_height(self.length)
        rod.set_style(**self.rod_style)
        rod.move_to(self.get_fixed_point(), UP)
        self.add(rod)

    def create_weight(self):
        weight = self.weight = Circle()
        weight.set_width(self.weight_diameter)
        weight.set_style(**self.weight_style)
        weight.move_to(self.rod.get_end())
        self.add(weight)

    def create_dashed_line(self):
        line = self.dashed_line = DashedLine(
            self.get_fixed_point(),
            self.get_fixed_point() + self.length * DOWN,
            **self.dashed_line_config
        )
        line.add_updater(
            lambda l: l.move_to(self.get_fixed_point(), UP)
        )
        self.add_to_back(line)

    def create_angle_arc(self):
        self.angle_arc = always_redraw(lambda: Arc(
            arc_center=self.get_fixed_point(),
            start_angle=-90 * DEGREES,
            angle=self.get_arc_angle_theta(),
            **self.angle_arc_config,
        ))
        self.add(self.angle_arc)

    def get_arc_angle_theta(self):
        # Might be changed in certain scenes
        return self.get_theta()

    def add_velocity_vector(self):
        def make_vector():
            omega = self.get_omega()
            theta = self.get_theta()
            mvlr = self.max_velocity_vector_length_to_length_ratio
            max_len = mvlr * self.rod.get_length()
            vvm = self.velocity_vector_multiple
            multiple = np.clip(
                vvm * omega, -max_len, max_len
            )
            vector = Vector(
                multiple * RIGHT,
                **self.velocity_vector_config,
            )
            vector.rotate(theta, about_point=ORIGIN)
            vector.shift(self.rod.get_end())
            return vector

        self.velocity_vector = always_redraw(make_vector)
        self.add(self.velocity_vector)
        return self

    def add_theta_label(self):
        self.theta_label = always_redraw(self.get_label)
        self.add(self.theta_label)

    def get_label(self):
        label = TexMobject("\\theta")
        label.set_height(self.theta_label_height)
        if self.set_theta_label_height_cap:
            max_height = self.angle_arc.get_width()
            if label.get_height() > max_height:
                label.set_height(max_height)
        top = self.get_fixed_point()
        arc_center = self.angle_arc.point_from_proportion(0.5)
        vect = arc_center - top
        norm = get_norm(vect)
        vect = normalize(vect) * (norm + self.theta_label_height)
        label.move_to(top + vect)
        return label

    #
    def get_theta(self):
        theta = self.rod.get_angle() - self.dashed_line.get_angle()
        theta = (theta + PI) % TAU - PI
        return theta

    def set_theta(self, theta):
        self.rotating_group.rotate(
            theta - self.get_theta()
        )
        self.rotating_group.shift(
            self.get_fixed_point() - self.rod.get_start(),
        )
        return self

    def get_omega(self):
        return self.omega

    def set_omega(self, omega):
        self.omega = omega
        return self

    def get_fixed_point(self):
        return self.fixed_point_tracker.get_location()

    #
    def start_swinging(self):
        self.add_updater(Pendulum.update_by_gravity)

    def end_swinging(self):
        self.remove_updater(Pendulum.update_by_gravity)

    def update_by_gravity(self, dt):
        theta = self.get_theta()
        omega = self.get_omega()
        nspf = self.n_steps_per_frame
        for x in range(nspf):
            d_theta = omega * dt / nspf
            d_omega = op.add(
                -self.damping * omega,
                -(self.gravity / self.length) * np.sin(theta),
            ) * dt / nspf
            theta += d_theta
            omega += d_omega
        self.set_theta(theta)
        self.set_omega(omega)
        return self

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

class spring_with_gravity(Scene):
    def construct(self):   
        hanging_spring = Spring(mass = 1, start = 3*UP,height=0.5*RIGHT,spring_constant = 50,turns=30)
        hanging_spring.make_smooth()
        self.add(hanging_spring)

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
        #self.play(Homotopy(homotopyTest,mainHexagon)        self.play(Rotate(mainHexagon,-1*PI*26.57/180,about_point=ORIGIN),run_time=0.2)
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

        testSpring = Spring(start = 5*LEFT+0.25*DOWN,finish =0.25*DOWN+5*RIGHT,turns=10,height=0.5*UP,color = WHITE,stroke_width = 3)
        testSpring.counter = 0

        def springUpdater(d,dt):
            #print("bruh")
            time = d.counter/60

            
            d.set_start((5-np.sin(time))*LEFT)
            d.set_finish((3+np.sin(time))*RIGHT)
            pointsArray = [d.start]

            #Simple for loop to zig zag and get the points
            for i in range(0,d.turns):
                if(i==0):
                    pointsArray.append(d.start-0.5*d.height+(d.finish+(-1)*d.start)/d.turns*0.5)
                    
                elif(i < d.turns):
                    
                    if(i % 2 == 1):
                        pointsArray.append(d.start+0.5*d.height+(d.finish+(-1)*d.start)/d.turns*(0.5+i))
                        
                    elif(i % 2 == 0):
                        pointsArray.append(d.start-0.5*d.height+(d.finish+(-1)*d.start)/d.turns*(0.5+i))
            pointsArray.append(d.finish)
            d.clear_points()
            d.set_points_as_corners(pointsArray)

            d.counter += 1
            #if(d.counter <= 45):
                #print(time)
        def spring_update(obj,dt):
            time = testSpring.counter/60
            testSpring.move_to(time*2*RIGHT)

            testSpring.counter += 1
            
        testSpring.add_updater(springUpdater)
        testSpring.add_updater(spring_update)
        print(len(testSpring.get_updaters()))
        if(len(testSpring.get_updaters())>0):
            print("yay")
        else:
            print("bruh")

        testPend = Pendulum(top_point = 2*UP + 3*RIGHT,length = 2)

        self.add(firstQ)
        self.wait(1)
        self.add(secondQ)
        self.wait(1)
        self.add(testSpring)
        self.wait(1)
        testSpring.clear_updaters()
        testSpring.set_start(6*LEFT)
        testSpring.ends_updater()
        self.add(testSpring)
        self.wait(0.5)
        testSpring.set_finish(6*RIGHT)
        testSpring.ends_updater()
        self.add(testSpring)
        self.wait(0.5)
        # self.add(testPend)
        # testPend.start_swinging()
        # self.wait(2)
    
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
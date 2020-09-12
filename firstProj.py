from manimlib.imports import *
import math
import numpy


class Spring(VMobject):
    CONFIG = {
        "color": BLUE,
        "fill_color": BLUE
    }

    def __init__(self, start,finish,turns,height,**kwargs):
        VMobject.__init__(self, **kwargs)
        pointsArray = [start]

        
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
        # self.set_points_as_corners(
        #     [*vertices, start]
        # )

    def get_vertices(self):
        return self.get_start_anchors()

class start(Scene):
    def construct(self):
        
        #Setting the backdrop
        wallLeft = Line(5*LEFT + DOWN,5*LEFT + 4*UP,stroke_width = 2)
        wallBot = Line(5*LEFT + DOWN,5*RIGHT + DOWN,stroke_width = 2) 
        self.add(wallLeft)
        self.add(wallBot)
        

        
        testRect = Square(side_length =1.5,fill_color="#7d7d7d", fill_opacity=1,stroke_width=2,color=WHITE)
        testRect.move_to(0.75*RIGHT+0.25*DOWN)
        testSpring = Spring(5*LEFT+0.25*DOWN,0.25*DOWN,10,0.5*UP,color = WHITE,stroke_width = 3)
        stifferSpring = Spring(5*LEFT+0.25*DOWN,0.25*DOWN,20,0.5*UP,color = WHITE,stroke_width = 3)

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
        replacement_transformation
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

Polygon
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

class HydrostaticParadox(Scene):
    def construct(self):
        
        for i in range(-8, 9):
            for j in range(-4,5):
                if(i == 0 and j == 0):
                    self.add(Dot(color = RED))
                    continue;
                self.add(Dot(i * RIGHT + j * UP))

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
        botLength1 = Line(start = 5 * LEFT + 2.3 * DOWN, end = 3 * LEFT + 2.3 *DOWN)
        botLength1.add_tip(at_start=  True)
        botLength1.add_tip()
        botLength1.set_color(BLUE)
        botLength1Label = DecimalNumber(4.00)
        botLength1Label.scale(0.6)
        botLength1Label.move_to(2.6 * DOWN + 4 * LEFT)
        
        def label_updater(d,dt):
            botLength1Label.set_value(2 * (botLength1.get_right() - botLength1.get_left())[0])
            botLength1Label.align_to(botLength1.get_bottom() - 0.2 * UP, direction = UP)
        def arrow_updater(d,dt):
            if(d.get_width() <= 2.7):
                d.move_to(d.get_center() + dt * UP * 2)
                d.stretch_to_fit_width(d.get_width() + 0.6 * dt / 3 * 2)


        #normal
        container2 = Container(LEFT + UP, LEFT + 2 * DOWN, RIGHT + 2 * DOWN, RIGHT + UP,fill_opacity= 0)
        water2 = Container(LEFT + UP, LEFT + 2 * DOWN, RIGHT + 2 * DOWN, RIGHT + UP)
        water2.time = 0
        water1 = Container(LEFT + UP, LEFT + 2 * DOWN, RIGHT + 2 * DOWN, RIGHT + UP)
        water1.time = 0
        water3 = Container(LEFT + UP, LEFT + 2 * DOWN, RIGHT + 2 * DOWN, RIGHT + UP)
        water3.time = 0

        def water2Update(d,dt):
            tim = water2.time / 12
            water2.set_points_as_corners([LEFT +2 * DOWN + UP * ( 2.6 - 2.6 * np.exp(-tim)),LEFT + 2 * DOWN, RIGHT + 2 * DOWN,RIGHT +2 * DOWN + UP * ( 2.6- 2.6 * np.exp(-tim))])
            water2.time += 1
        def water1Update(d,dt):
            tim = water1.time / 12
            water1.set_points_as_corners([5 * LEFT +2 * DOWN + UP * ( 2.6 - 2.6 * np.exp(-tim)) + (0.3 * 2.6/3- 0.3* 2.6/3 * np.exp(-tim)) * LEFT,5 * LEFT + 2 * DOWN, 3 * LEFT + 2 * DOWN,3 * LEFT +2 * DOWN + UP * ( 2.6 - 2.6 * np.exp(-tim)) + (0.3 * 2.6/3 - 0.3 * 2.6/3* np.exp(-tim)) * RIGHT])
            water1.time += 1
        def water3Update(d,dt):
            tim = water3.time / 12
            water3.set_points_as_corners([3 * RIGHT +2 * DOWN + UP * ( 2.6 - 2.6 * np.exp(-tim)) + (0.3 * 2.6/3 - 0.3* 2.6/3 * np.exp(-tim)) * RIGHT, 3 * RIGHT + 2 * DOWN, 5 * RIGHT + 2 * DOWN,5 * RIGHT +2 * DOWN + UP * ( 2.6 - 2.6 * np.exp(-tim)) + (0.3* 2.6/3 - 0.3 * 2.6/3* np.exp(-tim)) * LEFT])
            water3.time += 1

        botLength2 = Line(start = LEFT+ 2.3 * DOWN, end = RIGHT + 2.3 *DOWN)
        botLength2.add_tip(at_start=  True)
        botLength2.add_tip()
        botLength2.set_color(BLUE)
        botLength2Label = DecimalNumber(4.00)
        botLength2Label.scale(0.6)
        botLength2Label.move_to(2.6 * DOWN)

        def label_updater2(d,dt):
            
            botLength2Label.align_to(botLength2.get_bottom() - 0.2 * UP, direction = UP)
        def arrow_updater2(d,dt):
            if(botLength1.get_width() <= 2.7):
                d.move_to(d.get_center() + dt * UP * 2)
                #d.stretch_to_fit_width(d.get_width() + 0.6 * dt / 3 * 2)

        #thin
        container3 = Container(3.3 * RIGHT + UP, 3 * RIGHT + 2 * DOWN, 5* RIGHT +  2 * DOWN, 4.7 * RIGHT + UP,fill_opacity= 0)
        
        
        botLength3 = Line(start = 3 * RIGHT+ 2.3 * DOWN, end = 5 * RIGHT + 2.3 *DOWN)
        botLength3.add_tip(at_start=  True)
        botLength3.add_tip()
        botLength3.set_color(BLUE)
        botLength3Label = DecimalNumber(4.00)
        botLength3Label.scale(0.6)
        botLength3Label.move_to(4 * RIGHT + 2.6 * DOWN)

        table = Polygon(8 * LEFT + 2.02 * DOWN, 8 * RIGHT + 2.02 * DOWN, 8 * RIGHT + 5.2 * DOWN, 8 * LEFT + 5.2 * DOWN,fill_opacity = 1, fill_color = "#222222", stroke_width = 0, sheen_factor=  0.6, sheen_direction = UP)

        def label_updater3(d,dt):
            botLength3Label.set_value(2 * (botLength3.get_right() - botLength3.get_left())[0])
            botLength3Label.align_to(botLength3.get_bottom() - 0.2 * UP, direction = UP)
        def arrow_updater3(d,dt):
            if(botLength1.get_width() <= 2.7):
                d.move_to(d.get_center() + dt * UP * 2)
                d.stretch_to_fit_width(d.get_width() - 0.6 * dt / 3 * 2)


        self.play(DrawBorderThenFill(table))

        self.play(DrawBorderThenFill(container1),DrawBorderThenFill(container2),DrawBorderThenFill(container3))
        self.wait(1)
        botLength1Label.add_updater(label_updater)
        botLength1.add_updater(arrow_updater)
        botLength2Label.add_updater(label_updater2)
        botLength2.add_updater(arrow_updater2)
        botLength3Label.add_updater(label_updater3)
        botLength3.add_updater(arrow_updater3)

        self.add(botLength1Label,botLength1,botLength2Label,botLength2,botLength3Label,botLength3)
        self.wait(3)
        self.play(FadeOut(botLength1Label),FadeOut(botLength1),FadeOut(botLength2Label),FadeOut(botLength2),FadeOut(botLength3Label),FadeOut(botLength3))
        water2.add_updater(water2Update)
        water3.add_updater(water3Update)
        water1.add_updater(water1Update)
        self.add(water2,water1,water3)
        self.wait(3)
        waterLine = DashedLine(6 * LEFT + 0.6 * UP, 6 * RIGHT + 0.6 * UP)
        self.play(DrawBorderThenFill(waterLine))



        


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
        self.play(DrawBorderThenFill(table))
        self.wait(1)
        self.play(DrawBorderThenFill(fulcrum))
        self.wait(1)
        self.play(FadeIn(balance))
        self.play(FadeIn(plate1),FadeIn(plate2))
        self.wait(1)
        self.play(DrawBorderThenFill(container1),DrawBorderThenFill(container2))
        self.wait(1)
        self.play(FadeIn(water1),FadeIn(water2))
        self.wait(1)
        self.play(DrawBorderThenFill(pingPong))
        self.wait(1)
        self.play(DrawBorderThenFill(rock))
        self.wait(1)
        
        pingForce = Arrow(pingPong.get_center()+ 0.3 * DOWN,pingPong.get_center() + 1.3 * UP+ 0.3 * DOWN,color = GREEN)
        rockForce = Arrow(rock.get_center() + 0.3 * UP,rock.get_center() + 1.3 * DOWN+ 0.3 * UP,color = GREEN)

        self.play(GrowFromPoint(pingForce,pingPong.get_center()),GrowFromPoint(rockForce,rock.get_center()))

        self.wait(1)
        self.play(FadeOut(pingForce),FadeOut(rockForce))
        self.play(DrawBorderThenFill(stand))
        self.wait(1)
        self.play(GrowFromPoint(stringPing,stringPing.get_bottom()),FadeIn(stringRock,stringRock.get_top()))
        self.play(Write(question))
        self.play(Rotate(balance, angle = -PI/22, about_point = DOWN),Rotate(plate1, angle = -PI/22, about_point = DOWN),Rotate(balance, angle = -PI/22, about_point = DOWN),
                Rotate(plate2, angle = -PI/22, about_point = DOWN),Rotate(container1, angle = -PI/22, about_point = DOWN),Rotate(container2, angle = -PI/22, about_point = DOWN),
                Rotate(water1, angle = -PI/22, about_point = DOWN),Rotate(water2, angle = -PI/22, about_point = DOWN),Rotate(stringPing, angle = -PI/22, about_point = DOWN),Rotate(pingPong, angle = -PI/22, about_point = DOWN))
        self.play(Rotate(balance, angle = PI/22, about_point = DOWN),Rotate(plate1, angle = PI/22, about_point = DOWN),Rotate(balance, angle = PI/22, about_point = DOWN),
                Rotate(plate2, angle = PI/22, about_point = DOWN),Rotate(container1, angle = PI/22, about_point = DOWN),Rotate(container2, angle = PI/22, about_point = DOWN),
                Rotate(water1, angle = PI/22, about_point = DOWN),Rotate(water2, angle = PI/22, about_point = DOWN),Rotate(stringPing, angle = PI/22, about_point = DOWN),Rotate(pingPong, angle = PI/22, about_point = DOWN))
        
        self.wait(1)
        self.play(Write(questionPart2))
        self.play(Rotate(balance, angle = PI/22, about_point = DOWN),Rotate(plate1, angle = PI/22, about_point = DOWN),Rotate(balance, angle = PI/22, about_point = DOWN),
                Rotate(plate2, angle = PI/22, about_point = DOWN),Rotate(container1, angle = PI/22, about_point = DOWN),Rotate(container2, angle = PI/22, about_point = DOWN),
                Rotate(water1, angle = PI/22, about_point = DOWN),Rotate(water2, angle = PI/22, about_point = DOWN),Rotate(stringPing, angle = PI/22, about_point = DOWN),Rotate(pingPong, angle = PI/22, about_point = DOWN))
        self.play(Rotate(balance, angle = -PI/22, about_point = DOWN),Rotate(plate1, angle = -PI/22, about_point = DOWN),Rotate(balance, angle = -PI/22, about_point = DOWN),
                Rotate(plate2, angle = -PI/22, about_point = DOWN),Rotate(container1, angle = -PI/22, about_point = DOWN),Rotate(container2, angle = -PI/22, about_point = DOWN),
                Rotate(water1, angle = -PI/22, about_point = DOWN),Rotate(water2, angle = -PI/22, about_point = DOWN),Rotate(stringPing, angle = -PI/22, about_point = DOWN),Rotate(pingPong, angle = -PI/22, about_point = DOWN))

class Perpet(Scene):
    def construct(self):
        bruh = Circle()
        title = TextMobject("Problem 3: ", "A Perpetual Motion Machine")
        title.set_color_by_tex_to_color_map({
            "Problem 3: " : YELLOW,
            "Hydrostatic Paradox" : WHITE
        })
        title.scale(1.6)

        titleScaledAndMoved = TextMobject("Problem 3: ", "A Perpetual Motion Machine")
        titleScaledAndMoved.set_color_by_tex_to_color_map({
            "Problem 3: " : YELLOW,
            "Hydrostatic Paradox" : WHITE
        })
        titleScaledAndMoved.move_to(3.3 * UP + 3.4 * LEFT)
        titleScaledAndMoved.align_to(6.5 * LEFT, LEFT)
        
        




        

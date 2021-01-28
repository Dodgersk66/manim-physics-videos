from manimlib.imports import *

class twod_orbit(Scene):
    def construct(self):
        orbitEllipse = Ellipse(width = 10,height =6,color=DARK_GRAY,sheen_factor = 0.7,fill_color = DARK_GRAY,fill_opacity = 0,sheen_direction = RIGHT)
        sun = Circle(color = YELLOW,fill_color = YELLOW,fill_opacity=1,radius=0.5,sheen_factor = 0.9,sheen_direction = UR)
        sun.move_to(4*RIGHT)

        sattelite = Circle(color = DARK_GRAY,fill_opacity = 1,fill_color = DARK_GRAY,sheen_factor = 0.9,sheen_direction = UR,radius=0.2)
        sattelite.move_to(5*LEFT)
        sattelite.velVec = UP*1.3
        
        sattelite.angle = 0
        sattelite.adjustable_constant = 100

        orbitEllipse.count_time = 0

        gravitation_force_vector = Vector(direction = sun.get_center() - sattelite.get_center())
        gravitation_force_vector.put_start_and_end_on(sattelite.get_center(), sattelite.get_center() + (sun.get_center() - sattelite.get_center())*0.5)

        # def ellipse_updater(mob,dt):
        #     time = orbitEllipse.count_time/60
        #     mob.set_sheen_direction =(3*np.sin(time)*UP+5*np.cos(time)*RIGHT)
        
        def force_updater(mob,dt):
            diff_vec  = sun.get_center() - sattelite.get_center()
            diff_vec_mag = np.sqrt(diff_vec[0]*diff_vec[0] + diff_vec[1]*diff_vec[1] + diff_vec[2]*diff_vec[2])
            gravitation_force_vector.put_start_and_end_on(sattelite.get_center(), sattelite.get_center() + 10*(diff_vec)/(diff_vec_mag**3))

        def sattelite_updater(mob,dt):
            diff_vec  = sun.get_center() - sattelite.get_center()
            diff_vec_mag = np.sqrt(diff_vec[0]*diff_vec[0] + diff_vec[1]*diff_vec[1] + diff_vec[2]*diff_vec[2])
            satt_loc = sun.get_center()
            
            x_pos = satt_loc[0]
            y_pos = satt_loc[1]
            satt_mag = np.sqrt(x_pos**2 + y_pos**2)
            angle = sattelite.angle
            
            #vis-viva
            vel_mag = np.sqrt(sattelite.adjustable_constant * (2/diff_vec_mag - 1/5))

            #vel_vec = (vel_mag/satt_mag) * (RIGHT*5 * np.sin(angle)+UP * 3*np.cos(angle))

            mob.move_to((-5 * np.cos(angle + vel_mag/satt_mag * dt))*RIGHT + (3 * np.sin(angle + vel_mag/satt_mag * dt))*UP)
            #print(vel_mag)
            sattelite.angle = angle + vel_mag/satt_mag * dt
            #print("at angle " + str(angle) + ", speed is "+str(vel_mag))

            #mob.move_to(sattelite.get_center() + vel_vec * dt)
        
        gravitation_force_vector.add_updater(force_updater)
        # orbitEllipse.add_updater(ellipse_updater)
        sattelite.add_updater(sattelite_updater)
        quest = TextMobject("Do you enjoy orbital mechanics?")
        
        quest.set_color(YELLOW)
        quest2 = TextMobject("Or just Astronomy in general?")
        
        quest2.set_color(YELLOW)
        ans = TextMobject("Well, then Competitive Astronomy Club")
        ans.move_to(0.3*UP)
        ans2 = TextMobject("is the place for you!")
        ans2.move_to(0.3*DOWN)

        # ioaaPic = ImageMobject("./images/ioaa-logo.png")
        # ioaaPic.scale(8/ioaaPic.getWidth())

        # for i in range(-6,7):
        #     for j in range(-4,5):
        #         locDot = Dot()
        #         locDot.move_to(RIGHT*i + UP*j)
        #         self.add(locDot)
        self.play(Write(quest))
        self.wait(1.5)
        self.play(ReplacementTransform(quest,quest2))
        self.wait(1.5)
        self.play(FadeOut(quest2),FadeOut(quest))
        self.play(GrowFromCenter(ans),GrowFromCenter(ans2))
        self.wait(1)
        self.play(FadeOut(ans),FadeOut(ans2))
        #self.play(FadeOut(ans2))
        
        ioaa_tell = TextMobject("We compete in a series of olympiads")
        ioaa_tell.move_to(3.5*UP)
        ioaa_tell2 = TextMobject("that culminate to the IOAA!")
        ioaa_tell2.next_to(ioaa_tell,direction=DOWN)

        ioaaPic = ImageMobject("./images/ioaa-logo.png")
        ioaaPic.scale(8/ioaaPic.get_width())
        self.play(Write(ioaa_tell))
        self.play(Write(ioaa_tell2))
        self.add(ioaaPic)
        self.wait(2)
        self.play(FadeOut(ioaa_tell),FadeOut(ioaa_tell2),FadeOut(ioaaPic))
        
        astro = TextMobject("So, obviously, we do astronomy:")
        astro.move_to(3.5*UP)

        astroPic = ImageMobject("./images/astro.jpg")
        astroPic.scale(10/astroPic.get_width())

        self.play(GrowFromCenter(astro))
        self.add(astroPic)
        self.wait(2)
        self.play(FadeOut(astroPic),FadeOut(astro))
        
        astroPhys = TextMobject("And we do Astrophysics as well!")
        astroPhys.move_to(3.5*UP)

        self.add(orbitEllipse,sun,sattelite,gravitation_force_vector)
        self.add(astroPhys)
        lineArray = []
        for i in range(0,15):
            newLine = Line(sun.get_center(),sattelite.get_center())
            lineArray.append(newLine)
            self.add(newLine)
            self.wait(0.45)
        self.play(FadeOut(orbitEllipse),FadeOut(sun),FadeOut(sattelite))
        self.clear()
        self.wait(0.2)
        
        final = TextMobject("So, join the newest and coolest club at STEM!")
        final2  = TextMobject("-The Competitive Astronomy Club Team")
        final2.set_color(YELLOW)
        final2.scale(0.6)
        final2.move_to(2.2*RIGHT+0.5*DOWN)
        self.play(Write(final))
        self.play(Write(final2),run_time = 1.5)
        self.wait(1)

        # line1 = Line(sun.get_center(),sattelite.get_center())
        
        # self.add(line1)
        # self.wait(0.4)
        
        # self.add(Line(sun.get_center(),sattelite.get_center()))
        # self.wait(0.4)
        # self.add(Line(sun.get_center(),sattelite.get_center()))
        # self.wait(0.4)
        # self.add(Line(sun.get_center(),sattelite.get_center()))

from manimlib.imports import *

class TestScene(Scene):
    def construct(self):
        t = TextMobject("Hello manim!")
        t.scale(2)
        t2 = TextMobject("$\\dfrac{1}{2}+\\dfrac{1}{3} = \\dfrac{5}{6}$")
        t2.scale(2)
        img = SVGMobject("./weirdThing.svg",SVGMobject_config = {"fill_opacity": 0.5})
        img.scale(2)
        
        line = Arrow(ORIGIN,3*RIGHT + 2*UP)


        self.play(GrowFromPoint(line,ORIGIN))
        self.play(FadeOut(line))
        self.play(Write(t), run_time=1,rate_func=rush_into)
        self.wait(1)
        self.play(ReplacementTransform(t,t2))
        self.play(Transform(t2,img))
        self.play(FadeOut(img))
        self.wait(1)

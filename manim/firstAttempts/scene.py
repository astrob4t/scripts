from manim import *



class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.shift(PI / 4))  # rotate the square
        self.play(Transform(square, circle))  # transform the square into a circle
        self.play(
            square.animate.set_fill(PURPLE, opacity=0.5)
        )  # color the circle on screen

class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2)
        self.wait()

class TwoTransforms(Scene):
    def transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(Transform(a, b))
        Rotate(b, angle = 45, run_time = 2)
        self.play(Transform(a, c))
        self.play(FadeOut(a))

    def replacement_transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(ReplacementTransform(a, b))
        self.play(ReplacementTransform(b, c))
        self.play(FadeOut(c))

    def construct(self):
        self.transform()
        self.wait(0.5)  # wait for 0.5 seconds
        self.replacement_transform()

class CircSquareCircTri(Scene):
    def trans(self):
        a = Circle()
        b = Square()
        c = Circle()
        d = Triangle()
        self.play(ReplacementTransform(a, b))
        self.play(ReplacementTransform(b, c))
        self.play(ReplacementTransform(c, d))
        self.play(FadeOut(d))

    def construct(self):
        self.trans()

class TextTesting(Scene):
    def perfectHatred(self):
        # Preload Shapes
        s1 = Circle(color=PURE_RED)
        s2 = Square(color=PURE_BLUE)
        t1 = Text('Perfect', color = '#8000FF')
        t2 = Text('Hatred', color = '#8000FF')

        # Positioning
        s2.next_to(s1, LEFT)
        s1.shift(RIGHT)
        t1.shift(1.25*LEFT)
        t2.shift(1.25*RIGHT)

        # Run the animation
        self.play(Create(s1), Create(s2))
        self.play(Transform(s1, t1), Transform(s2, t2))

    # Run the previous function
    def construct(self):
        self.perfectHatred()
        self.wait(0.5)
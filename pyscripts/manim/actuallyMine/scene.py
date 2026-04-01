from manim import *

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

class TextShapeText(Scene):
    def Test(self):
        # Preload Shapes and Text
        t1 = Text('Perfect', color = PURE_RED)
        t2 = Text('Hatred', color = PURE_BLUE)
        t2.shift(1.25*RIGHT)

        # Run the animations
        self.play(
            Create(t1)
        )
        self.play(
            t1.animate.shift(1.25*LEFT),
        )
        self.play(
            Create(t2)
        )
        self.play(
            FadeToColor(t1, '#8000FF'),
            FadeToColor(t2, '#8000FF')
        )

    def construct(self):
        self.Test()
        self.wait(0.5)

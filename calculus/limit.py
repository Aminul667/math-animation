from manim import *


class Limit1(Scene):
    def construct(self):
        bangla = Text(
            "In calculus, we apply operations to functions, producing new functions as a result.",
            font="Agency FB",
            font_size=25,
            t2c={'operations to functions': BLUE, 'new functions': BLUE}
        ).to_edge(UP)
        self.play(Write(bangla))
        self.wait()

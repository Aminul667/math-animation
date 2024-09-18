from manim import *


class Limit1(Scene):
    def construct(self):
        calculusText = Text(
            "In calculus, we apply operations to functions, producing new functions as a result.",
            font="Agency FB",
            font_size=25,
            t2c={'operations to functions': BLUE, 'new functions': BLUE}
        ).to_edge(UP)

        self.play(Write(calculusText))
        self.wait()

        calculus = Text(
            "Calculus",
            # font="Agency FB",
            font_size=30
        ).move_to(2*LEFT)

        differentiation = Text(
            "Differentiation",
            # font="Agency FB",
            font_size=30
        ).move_to(DOWN + 2*RIGHT)

        integration = Text(
            "Integration",
            # font="Agency FB",
            font_size=30
        ).move_to(UP + 2*RIGHT)

        rectangle = SurroundingRectangle(calculus, color=RED, buff=0.2)

        # Align "Differentiation" and "Integration" to the left of the scene
        differentiation.align_to(integration, LEFT)

        # Create arrows from "Calculus" to "Differentiation" and "Integration"
        arrow_to_diff = Arrow(
            start=rectangle.get_right(),
            end=differentiation.get_left(),
            buff=0.1,
            color=YELLOW

        )
        arrow_to_integ = Arrow(
            start=rectangle.get_right(),
            end=integration.get_left(),
            buff=0.1,
            color=YELLOW
        )

        self.play(Write(calculus), Write(rectangle))
        self.play(Write(differentiation))
        self.play(Write(integration))
        self.play(Write(arrow_to_diff), Write(arrow_to_integ))
        self.wait()

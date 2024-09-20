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


class LinearFunction(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-5, 5],
            y_range=[-5, 5],
            x_length=7,
            y_length=7,
            axis_config={"color": DARK_BLUE},
            x_axis_config={
                "numbers_to_include": np.arange(-5, 6, 2),
                "numbers_with_elongated_ticks": np.arange(-5, 6, 2),
            },
            tips=False,
        ).shift(3*RIGHT)

        # Create the function y = x - 1
        linear_function_plot = axes.plot(
            lambda x: x - 1,
            color=RED,
            x_range=[-3.5, 5]
        )

        function_equation = MathTex(r"y = f(x) = x - 1", substrings_to_isolate=["x","y"]).to_edge(UL).shift(DOWN + RIGHT)
        function_equation.set_color_by_tex("x", BLUE)
        function_equation.set_color_by_tex("y", YELLOW)

        # Add labels for the axes
        axes_labels = axes.get_axis_labels(
            x_label="x",
            y_label="y"
        )

        # Add everything to the scene
        self.play(Create(axes), Write(axes_labels))
        self.wait()

        self.play(Write(function_equation))
        self.wait()

        self.play(Create(linear_function_plot))
        self.wait()

        # self.add(axes, linear_function, axes_labels)

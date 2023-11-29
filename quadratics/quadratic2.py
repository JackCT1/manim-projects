from manim import *

class SquareWithBraces(Scene):
    def construct(self):

        opening_title = Tex("Quadratic Equations Visualised")
        # Create a square
        square = Square().shift(UP)

        # Create braces for width and height
        brace_height = Brace(square, direction=LEFT)
        brace_width = Brace(square, direction=UP)

        # Create labels for width and height
        label_width = brace_width.get_tex("x", buff=0.1)
        label_height = brace_height.get_tex("x", buff=0.1)
        label_height_copy = label_height.copy()

        # Position the labels
        label_width.next_to(brace_width, UP)
        label_height.next_to(brace_height, LEFT)
        label_height_copy.next_to(brace_height, LEFT)

        # Create a label for the area using MathTex
        label_area = MathTex("x^2").move_to(square)
        label_area_copy = label_area.copy()
        label_area_second_copy = label_area.copy()

        # Define the width transformation
        a = 1.5  # Increase in width
        square_transformed = square.copy().stretch(a, 0, about_point=square.get_left())
        square_transformed_again = square_transformed.copy().stretch(a, 1, about_point=square_transformed.get_top())

        # Create a dashed line representing the original right side of the square
        dashed_line_vertical = DashedLine(square.get_corner(DR), square.get_corner(UR), color=WHITE)
        dashed_line_horizontal = DashedLine(square.get_corner(DL), square_transformed.get_corner(DR), color=WHITE)
        dashed_line_extra_vertical = DashedLine(square.get_corner(DR), square.get_corner(DR) + DOWN)

        # Create a brace for the extra width 'a'
        line_for_extra_width_brace = Line(square.get_corner(UR), square_transformed.get_corner(UR))
        brace_extra_width = Brace(line_for_extra_width_brace, direction=UP)
        label_extra_width = brace_extra_width.get_tex("a", buff=0.1)
        label_extra_width.next_to(brace_extra_width, UP)

        # Create a label for new area 'ax'
        label_new_width_area = MathTex("ax").move_to(square).shift(RIGHT * 1.5)
        label_new_width_area_copy = label_new_width_area.copy()
        label_new_width_area_second_copy = label_new_width_area.copy()

        # Write equations
        equation_initial = MathTex("x^2", "+", "ax", "=", "x", "(", "x + a", ")").next_to(square, DOWN * 3)
        equation_final = MathTex("x^2", '+', 'ax', "+", 'bx', '+', 'ab', '=', '(', 'x + a', ')', '(', 'x + b', ')').next_to(square_transformed_again, DOWN * 3)
        equation_final_simplified = MathTex("x^2", '+', "(", 'a', "+", 'b', ")", "x", "+", 'ab', '=', '(', 'x + a', ')', '(', 'x + b', ')').next_to(square_transformed_again, DOWN * 3)
        changes = [
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),
            (0, 1, 3, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16)
        ]


        # Create brace line and label for x + a
        line_for_combined_width_brace = Line(square.get_corner(UL), square_transformed.get_corner(UR))
        brace_combined_width = Brace(line_for_combined_width_brace, direction=UP)
        label_combined_width = brace_combined_width.get_tex('x + a', buff=0.1)
        label_combined_width.next_to(brace_combined_width, UP)
        label_combined_width_copy = label_combined_width.copy()

        framebox = SurroundingRectangle(equation_initial, buff=0.1)
        framebox2 = SurroundingRectangle(equation_final_simplified, buff=0.1).shift(UP * 1.5)

        # Create brace line for extra height 'b'
        line_for_extra_height_brace = Line(square.get_corner(DL), square_transformed_again.get_corner(DL))
        brace_extra_height = Brace(line_for_extra_height_brace, direction=LEFT)
        label_extra_height = brace_extra_height.get_tex("b", buff=0.1)
        label_extra_height.next_to(brace_extra_height, LEFT)

        # Create a label for new area 'bx'
        label_new_height_area = MathTex("bx").move_to(square).shift(DOWN * 1.5)
        label_new_height_area_copy = label_new_height_area.copy()
        
        # Create a label for new area 'ab'
        label_final_area = MathTex('ab').move_to(square).shift(DOWN * 1.5, RIGHT * 1.5)
        label_final_area_copy = label_final_area.copy()

        # Create brace and label for height 'x + b'
        line_for_combined_height_brace = Line(square.get_corner(UL), square_transformed_again.get_corner(DL))
        brace_combined_height = Brace(line_for_combined_height_brace, direction=LEFT)
        label_combined_height = brace_combined_height.get_tex('x + b', buff=0.1).next_to(brace_combined_height, LEFT)

        # Add the objects to the scene
        self.play(Write(opening_title))
        self.wait()
        self.play(FadeOut(opening_title))

        self.play(Create(square))
        #self.play(square.animate.set_fill(BLUE, opacity=0.5))

        self.play(Create(brace_width), Write(label_width), Create(dashed_line_vertical))
        self.play(Create(brace_height), Write(label_height), Write(label_height_copy))

        self.play(Write(label_area), Write(label_area_copy), Write(label_area_second_copy))

        self.play(Transform(square, square_transformed), Create(dashed_line_horizontal))

        self.play(Create(brace_extra_width), Write(label_extra_width))

        self.play(Write(label_new_width_area), Write(label_new_width_area_copy), Write(label_new_width_area_second_copy))

        self.play(Transform(brace_width, brace_combined_width), 
                  Transform(label_width, label_combined_width), 
                  FadeOut(brace_extra_width), 
                  FadeOut(label_extra_width))
        self.wait()

        self.play(Transform(label_area, equation_initial[0]))
        self.play(Write(equation_initial[1]))
        self.play(Transform(label_new_width_area, equation_initial[2]))
        self.play(Write(equation_initial[3]))
        self.play(Transform(label_height, equation_initial[4]))
        self.wait()
        
        self.play(FadeIn(label_combined_width_copy),
                  Transform(label_combined_width, equation_initial[6]), 
                  Write(equation_initial[5]), 
                  Write(equation_initial[7]))
        self.play(Create(framebox))
        self.wait()

        self.play(Uncreate(framebox), Unwrite(VGroup(equation_initial, label_area, label_new_width_area, label_combined_width, label_height), lag_ratio=0))
        
        self.play(Transform(square, square_transformed_again), Create(dashed_line_extra_vertical))
        self.play(Create(brace_extra_height), Write(label_extra_height))
        
        self.play(Write(label_new_height_area), Write(label_new_height_area_copy))
        self.play(Write(label_final_area), Write(label_final_area_copy))
        
        self.play(Transform(brace_height, brace_combined_height), 
                  Transform(label_height_copy, label_combined_height), 
                  FadeOut(brace_extra_height), 
                  FadeOut(label_extra_height))
        self.wait()

        self.play(Transform(label_area_copy, equation_final[0]))
        self.play(Write(equation_final[1]))
        self.play(Transform(label_new_width_area_copy, equation_final[2]))
        self.play(Write(equation_final[3]))
        self.play(Transform(label_new_height_area, equation_final[4]))
        self.play(Write(equation_final[5]))
        self.play(Transform(label_final_area, equation_final[6]))
        self.play(Write(equation_final[7]))
        self.wait()
        self.play(Transform(label_combined_width_copy, equation_final[9]), Write(equation_final[8]), Write(equation_final[10]))
        self.wait()
        self.play(Transform(label_combined_height, equation_final[12]), Write(equation_final[11]), Write(equation_final[13]))
        self.wait()

        self.play(
            *[ReplacementTransform(equation_final[i], equation_final_simplified[j])
              for i, j in zip(changes[0], changes[1])],
            GrowFromCenter(equation_final_simplified[2]),
            GrowFromCenter(equation_final_simplified[6]),
            GrowFromCenter(equation_final_simplified[7]),
            FadeOut(label_area_copy),
            FadeOut(label_new_width_area_copy),
            FadeOut(label_new_height_area),
            FadeOut(label_final_area),
            FadeOut(label_combined_width_copy),
            FadeOut(label_combined_height),
        )
        self.play(FadeOut(VGroup(
            square,
            square_transformed_again, 
            brace_height, 
            brace_width, 
            label_height_copy,
            label_width,
            label_area_second_copy, 
            label_new_height_area_copy, 
            label_new_width_area_second_copy, 
            label_final_area_copy,
            dashed_line_extra_vertical, dashed_line_horizontal, dashed_line_vertical
        )))
        self.play(equation_final_simplified.animate.shift(UP * 1.5))
        self.play(Create(framebox2))
        self.wait()
        self.play(FadeOut(VGroup(equation_final_simplified, framebox2)))
        self.wait(2)
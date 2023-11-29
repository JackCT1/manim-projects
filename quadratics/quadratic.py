from manim import *

class Intro(Scene):
    def construct(self):
        opening_title = Tex("Quadratic Equations Visualised")
        square = Square(side_length=2).shift(UP * 1)
        square_to_transform = Square(side_length=2).shift(UP * 1)
        
        length = always_redraw(lambda: Brace(square_to_transform, direction=LEFT))
        length_label = always_redraw(lambda: length.get_tex('x'))

        #text_1 = MathTex('Side Length = x').to_edge(DL).shift(UP * 1)
        text_2 = MathTex('Area = x^2').to_edge(DL).shift(UP * 2)

        transformed_square = Square(side_length=3).shift(UP * 0.5, RIGHT * 0.5)
        transformed_label = always_redraw(lambda: length.get_tex('x + a'))
        
        self.play(Write(opening_title))
        self.wait()

        self.play(opening_title.animate.to_edge(UP))
        self.play(Create(VGroup(square, square_to_transform)))
        self.play(Create(length))
        self.play(Write(length_label))
        self.wait()

        self.play(Write(text_2))
        self.wait()

        self.play(
            Transform(square_to_transform, transformed_square),
            Transform(length_label, transformed_label))
        #self.play(square_to_transform.animate.scale(2).shift(RIGHT * 2))

        #self.play(Write(text_2))
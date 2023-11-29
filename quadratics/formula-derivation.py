from manim import *
import numpy as np

class Derivation(Scene):
    def construct(self):
        opening_title = Tex('Deriving the Quadratic Formula')
        
        line1 = Tex('The basic form of a quadratic equation is').to_edge(UP)
        line2 = Tex('We just need to rearrange for x').to_edge(UP)
        line3 = Tex('First subtract c and divide through by a').to_edge(UP)
        line4 = Tex('Now complete the square on the left hand side').to_edge(UP)
        line5 = Tex('We can move over the b squared term').to_edge(UP)
        line6 = Tex('Combining the two fractions on the right...').to_edge(UP)
        line7 = Tex('From here, square root both sides').to_edge(UP)
        line8 = Tex('and rearrange for x').to_edge(UP)
        line9 = Tex('Voila! The quadratic formula').to_edge(UP)

        quadratic1 = MathTex('a','x','^2','+','b','x','+','c','=','0')
        quadratic2 = MathTex('a','x','^2','+','b','x','=','-','c')
        changes1 = [
            (0, 1, 2, 3, 4, 5, 6, 7, 8),
            (0, 1, 2, 3, 4, 5, 7, 8, 6)
        ]
        quadratic3 = MathTex('x','^2','+','{','b','\\over','a','}','x',
                                '=','-','{','c','\\over','a','}')
        changes2 = [
            (0, 1, 2, 3, 4, 5, 6, 7, 8),
            (6, 0, 1, 2, 4, 8, 9, 10, 12)
        ]
        quadratic4 = MathTex('\\left(', 'x', '+', '{', 'b', '\\over', '2', 'a', '}',
                                '\\right)', '^2', '-', '{', 'b', '^2', '\\over', '4', 
                                'a', '^2', '}', '=', '-','{','c','\\over','a','}')
        # need to write positions 6, 7, and 9
        changes3 = [
            (0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15),
            (1, 1, 2, 3, 4, 5, 7, 1, 20, 21, 22, 23, 24, 25, 26)
        ]

        quadratic5 = MathTex('\\left(', 'x', '+', '{', 'b', '\\over', '2', 'a', '}',
                                '\\right)', '^2', '=', '-','{','c','\\over','a','}', 
                                '+', '{', 'b', '^2', '\\over', '4', 'a', '^2', '}')
        changes4 = [
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26),
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 18, 19, 20, 21, 22, 23, 24, 25, 26, 11, 12, 13, 14, 15, 16, 17)
        ]

        quadratic6 = MathTex('\\left(', 'x', '+', '{', 'b', '\\over', '2', 'a', '}', '\\right)',
                                '^2', '=', '{', 'b', '^2', '-', '4', 'a', 'c', '\\over', '4',
                                'a', '^2', '}')

        changes5 = [
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20, 21, 22, 23, 24, 25),
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 18, 17, 13, 14, 19, 20, 21, 22),
            (15, 18),
        ]

        quadratic7 = MathTex('\\sqrt', '{', '\\left(', 'x', '+', '{', 'b', '\\over', '2', 'a', '}',
                                '\\right)', '^2', '}', '=', '\\sqrt', '{', 'b', '^2', '-', '4',
                                'a', 'c', '\\over', '4', 'a', '^2', '}', '}')

        changes6 = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 
                    [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], 
                    [0, 15]]

        quadratic8 = MathTex('x', '+', '{', 'b', '\\over', '2', 'a', '}', '=', '{', '\\pm', '\\sqrt',
                                '{', 'b', '^2', '-', '4', 'a', 'c', '}', '\\over', '\\sqrt', '{',
                                '4', 'a', '^2', '}', '}')

        changes7 = [
            (0, 3, 4, 6, 7, 8, 9, 12, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26),
            (21, 0, 1, 3, 4, 5, 6, 10, 8, 11, 13, 14, 15, 16, 17, 18, 20, 23, 24, 25),
            (2, 11)
        ]

        quadratic9 = MathTex('x', '+', '{', 'b', '\\over', '2', 'a', '}', '=', '{', '\\pm', '\\sqrt',
                                '{', 'b', '^2', '-', '4', 'a', 'c', '}', '\\over', '2', 'a', '}'
                                )

        changes8 = [[23, 24], [21, 22], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]]
        
        quadratic10 = MathTex('x', '=', '{', '-', 'b', '\\pm', '\\sqrt', '{', 'b', '^2', '-',
                                 '4', 'a', 'c', '}', '\\over', '2', 'a', '}')

        changes9 = [
            (0, 1, 3, 5, 6, 8, 10, 11, 13, 14, 15, 16, 17, 18, 20, 21, 22),
            (0, 3, 4, 16, 17, 1, 5, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17)
        ]

        frame_box = SurroundingRectangle(quadratic10, buff=0.2)

        self.play(Write(opening_title))
        self.wait()

        self.play(FadeOut(opening_title))
        self.play(Write(line1))
        self.play(Write(quadratic1))
        self.wait()

        self.play(Transform(line1, line2))
        self.wait(2)

        self.play(Transform(line1, line3))
        self.wait()

        self.play(
            *[
                ReplacementTransform(
                    quadratic1[pre], quadratic2[pos]
                    )
                for pre,pos in zip(changes1[0], changes1[1])
            ],
            FadeOut(quadratic1[9]))
        self.wait()

        self.play(
            *[
                ReplacementTransform(
                    quadratic2[pre2], quadratic3[pos2]
                )
                for pre2,pos2 in zip(changes2[0], changes2[1])
            ],
            ReplacementTransform(quadratic2[0].copy(), quadratic3[14]),
            Write(quadratic3[5]),
            Write(quadratic3[13]))
        self.wait()

        self.play(Transform(line1, line4))
        self.wait()

        self.play(
            *[
                ReplacementTransform(
                    quadratic3[pre3], quadratic4[pos3]
                    )
                for pre3,pos3 in zip(changes3[0], changes3[1])
            ],
            Write(quadratic4[6]),
            #FadeOut(quadratic3[1])
            )
        self.play(Write(VGroup(
            quadratic4[0],
            quadratic4[9],
            quadratic4[10],
            quadratic4[11],
            quadratic4[13],
            quadratic4[14],
            quadratic4[15],
            quadratic4[16],
            quadratic4[17],
            quadratic4[18]))
        )
        self.wait()

        self.play(Transform(line1, line5))
        self.wait()

        self.play(*[
                ReplacementTransform(
                    quadratic4[pre4], quadratic5[pos4]
                    )
                for pre4,pos4 in zip(changes4[0], changes4[1])
            ])
        self.wait()

        self.play(Transform(line1, line6),
                  FadeOut(quadratic4[21]))
        self.wait()


        self.play(
            *[ReplacementTransform(
                quadratic5[i], quadratic6[z])
                for i, z in zip(changes5[0], changes5[1])],
            ShrinkToCenter(quadratic5[18]),
            FadeOut(quadratic4[1]),
            ReplacementTransform(quadratic5[15], quadratic6[16]))
        self.wait()

        self.play(Transform(line1, line7))
        self.wait()


        self.play(
            *[ReplacementTransform(quadratic6[i], quadratic7[i + 2])
              for i in changes6[0]],
            *[ReplacementTransform(quadratic6[i], quadratic7[i + 4])
              for i in changes6[1]],
            ReplacementTransform(quadratic6[11], quadratic7[14]),
            *[GrowFromCenter(quadratic7[i])
              for i in changes6[2]])
        self.wait()

        self.play(
            *[ReplacementTransform(
                quadratic7[i], quadratic8[z])
                for i, z in zip(changes7[0], changes7[1])],
            ShrinkToCenter(quadratic7[2]),
            ShrinkToCenter(quadratic7[11]))
        self.wait()

        self.play(
            *[ReplacementTransform(
                quadratic8[i], quadratic9[z])
                for i, z in zip(changes8[0], changes8[1])],
            *[ReplacementTransform(
                quadratic8[i], quadratic9[i])
                for i in changes8[2]],
            ShrinkToCenter(quadratic8[25]),
            ShrinkToCenter(quadratic8[21]))
        self.wait()

        self.play(Transform(line1, line8))
        self.wait()


        self.play(
            *[ReplacementTransform(
                quadratic9[i], quadratic10[z])
                for i, z in zip(changes9[0], changes9[1])],
            FadeOut(quadratic9[4]))
        self.wait()

        self.play(Transform(line1, line9))
        self.wait()

        self.play(Create(frame_box))
        self.wait()
        self.play(FadeOut(VGroup(line1, quadratic10, frame_box)))
        self.wait(2)

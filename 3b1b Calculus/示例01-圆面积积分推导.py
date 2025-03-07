from manim import *

class CircleArea(Scene):
    def construct(self):
        # ����Բ������ϵ
        circle = Circle(radius=2, color=BLUE)
        axes = Axes(x_range=[0, 3, 1], y_range=[0, 7, 1])
        label = Text("��Բ�ֽ�Ϊ���ޱ�Բ��", font_size=24).to_edge(UP)

        # չʾԲ���ֽ�
        self.play(Create(circle), Write(label))
        self.wait()
        rings = VGroup(*[
            Annulus(inner_radius=r, outer_radius=r+0.1, color=interpolate_color(BLUE, RED, r/2))
            for r in np.arange(0, 2, 0.2)
        ])
        self.play(Transform(circle, rings))
        self.wait()

        # չ��Բ��Ϊ����
        rectangles = VGroup(*[
            Rectangle(height=2*PI*r*0.2, width=0.2, fill_opacity=0.5)
            .move_to(axes.c2p(r, 0), LEFT)
            for r in np.arange(0, 2, 0.2)
        ])
        self.play(Transform(rings, rectangles), Create(axes))
        self.wait()

        # ת��Ϊ����������
        triangle = Polygon(
            axes.c2p(0,0), axes.c2p(2,0), axes.c2p(2,2*PI*2)),
            color=GREEN, fill_opacity=0.3
        )
        formula = MathTex(r"\int_0^R 2\pi r\, dr = \pi R^2").to_edge(DOWN)
        self.play(Create(triangle), Write(formula))
        self.wait(2)
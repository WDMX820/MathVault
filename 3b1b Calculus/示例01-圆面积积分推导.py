from manim import *

class CircleArea(Scene):
    def construct(self):
        # 创建圆和坐标系
        circle = Circle(radius=2, color=BLUE)
        axes = Axes(x_range=[0, 3, 1], y_range=[0, 7, 1])
        label = Text("将圆分解为无限薄圆环", font_size=24).to_edge(UP)

        # 展示圆环分解
        self.play(Create(circle), Write(label))
        self.wait()
        rings = VGroup(*[
            Annulus(inner_radius=r, outer_radius=r+0.1, color=interpolate_color(BLUE, RED, r/2))
            for r in np.arange(0, 2, 0.2)
        ])
        self.play(Transform(circle, rings))
        self.wait()

        # 展开圆环为矩形
        rectangles = VGroup(*[
            Rectangle(height=2*PI*r*0.2, width=0.2, fill_opacity=0.5)
            .move_to(axes.c2p(r, 0), LEFT)
            for r in np.arange(0, 2, 0.2)
        ])
        self.play(Transform(rings, rectangles), Create(axes))
        self.wait()

        # 转换为积分三角形
        triangle = Polygon(
            axes.c2p(0,0), axes.c2p(2,0), axes.c2p(2,2*PI*2)),
            color=GREEN, fill_opacity=0.3
        )
        formula = MathTex(r"\int_0^R 2\pi r\, dr = \pi R^2").to_edge(DOWN)
        self.play(Create(triangle), Write(formula))
        self.wait(2)
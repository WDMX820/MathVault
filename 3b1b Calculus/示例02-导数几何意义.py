class DerivativeVisual(Scene):
    def construct(self):
        # 创建函数曲线
        axes = Axes(x_range=[-1, 3], y_range=[-1, 10])
        curve = axes.plot(lambda x: x**2, color=BLUE)
        dot = Dot(color=RED).move_to(axes.c2p(1, 1))
        label = Text("切线斜率即导数", font_size=24).to_edge(UP)

        # 展示割线变化
        self.play(Create(axes), Create(curve), Write(label))
        self.play(FadeIn(dot))
        
        for h in [0.5, 0.3, 0.1]:
            secant_line = Line(
                axes.c2p(1, 1),
                axes.c2p(1+h, (1+h)**2),
                color=YELLOW
            )
            slope_text = MathTex(r"\frac{\Delta y}{\Delta x} = " + f"{( (1+h)**2 -1 )/h:.2f}").next_to(secant_line, RIGHT)
            self.play(Create(secant_line), Write(slope_text))
            self.wait(0.5)
            self.play(FadeOut(secant_line), FadeOut(slope_text))

        # 显示切线
        tangent_line = axes.get_secant_slope_group(
            1, curve, dx=0.01,
            secant_line_color=GREEN,
            secant_line_length=4)
        derivative_formula = MathTex(r"\frac{d}{dx}x^2 = 2x").next_to(tangent_line, RIGHT)
        self.play(Create(tangent_line), Write(derivative_formula))
        self.wait(2)
class FundamentalTheorem(Scene):
    def construct(self):
        # 创建坐标系和曲线
        axes1 = Axes(x_range=[0, 5], y_range=[0, 10])
        axes2 = Axes(x_range=[0, 5], y_range=[0, 25]).shift(DOWN*2)
        curve = axes1.plot(lambda x: 2*x, color=BLUE)
        area = axes1.get_area(curve, x_range=[0, 3], color=BLUE_E)
        
        # 动画展示面积函数
        self.play(Create(axes1), Create(curve))
        self.play(FadeIn(area))
        self.wait()
        
        # 变换为反导数曲线
        integral_curve = axes2.plot(lambda x: x**2, color=GREEN)
        moving_dot = Dot(color=RED).move_to(axes1.c2p(0,0))
        self.play(
            Transform(area.copy(), integral_curve),
            Create(axes2),
            Create(moving_dot)
        )
        
        # 展示导数关系
        derivative_arrow = Arrow(
            integral_curve.get_end(), 
            curve.get_end(), 
            buff=0, color=YELLOW
        )
        derivative_label = MathTex(r"A'(x) = f(x)").next_to(derivative_arrow, RIGHT)
        self.play(
            Create(derivative_arrow),
            Write(derivative_label)
        )
        self.wait(2)
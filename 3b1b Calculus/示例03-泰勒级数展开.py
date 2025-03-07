class TaylorSeries(Scene):
    def construct(self):
        axes = Axes(x_range=[-4, 4], y_range=[-2, 2])
        cos_curve = axes.plot(np.cos, color=BLUE)
        label = Text("cos(x) 的泰勒多项式逼近", font_size=24).to_edge(UP)
        
        self.play(Create(axes), Create(cos_curve), Write(label))
        self.wait()
        
        # 逐步添加泰勒项
        terms = [
            MathTex(r"1"),
            MathTex(r"1 - \frac{x^2}{2!}"),
            MathTex(r"1 - \frac{x^2}{2!} + \frac{x^4}{4!}"),
            MathTex(r"1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!}")
        ]
        
        approximations = [
            axes.plot(lambda x: 1, color=RED),
            axes.plot(lambda x: 1 - x**2/2, color=YELLOW),
            axes.plot(lambda x: 1 - x**2/2 + x**4/24, color=GREEN),
            axes.plot(lambda x: 1 - x**2/2 + x**4/24 - x**6/720, color=PURPLE)
        ]
        
        for term, approx in zip(terms, approximations):
            term.next_to(approx, UP)
            self.play(
                Create(approx),
                Write(term.to_edge(RIGHT)),
                run_time=1.5
            )
            self.wait()
        
        self.wait(2)
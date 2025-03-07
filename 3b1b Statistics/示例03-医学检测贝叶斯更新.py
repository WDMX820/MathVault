class MedicalTestBayes(Scene):
    def construct(self):
        # 创建基础公式
        formula = MathTex(
            r"P(\text{病}|\text{阳}) = \frac{P(\text{阳}|\text{病})P(\text{病})}{P(\text{阳})}",
            substrings_to_isolate=["P","|"]
        ).scale(1.2)
        
        # 公式分解步骤
        step1 = MathTex(
            r"P(\text{阳}) = P(\text{阳}|\text{病})P(\text{病}) + P(\text{阳}|\text{健})P(\text{健})"
        ).next_to(formula, DOWN)
        
        # 数值代入
        numbers = MathTex(
            r"= \frac{0.9 \times 0.01}{0.9 \times 0.01 + 0.09 \times 0.99} \approx 9.1\%"
        ).next_to(formula, DOWN)
        
        self.play(Write(formula))
        self.wait(1)
        self.play(Transform(formula, formula.copy().to_edge(UP)))
        self.play(Write(step1))
        self.wait(1)
        self.play(Transform(step1, numbers))
        self.wait(2)

# 运行命令: manim -pql medical_bayes.py MedicalTestBayes
class MedicalTestBayes(Scene):
    def construct(self):
        # ����������ʽ
        formula = MathTex(
            r"P(\text{��}|\text{��}) = \frac{P(\text{��}|\text{��})P(\text{��})}{P(\text{��})}",
            substrings_to_isolate=["P","|"]
        ).scale(1.2)
        
        # ��ʽ�ֽⲽ��
        step1 = MathTex(
            r"P(\text{��}) = P(\text{��}|\text{��})P(\text{��}) + P(\text{��}|\text{��})P(\text{��})"
        ).next_to(formula, DOWN)
        
        # ��ֵ����
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

# ��������: manim -pql medical_bayes.py MedicalTestBayes
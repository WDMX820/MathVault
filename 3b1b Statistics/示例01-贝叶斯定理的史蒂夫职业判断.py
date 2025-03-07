from manim import *

class BayesTheoremExample(Scene):
    def construct(self):
        # �������������ռ�
        total_pop = Rectangle(width=6, height=3, color=WHITE)
        self.play(Create(total_pop))
        
        # ����ũ���ͼ�����Ա����
        farmer_rect = Rectangle(width=5.8, height=2.4, color=BLUE).shift(LEFT*2.5)
        librarian_rect = Rectangle(width=0.2, height=2.4, color=GREEN).shift(RIGHT*2.9)
        
        # ��ӱ�ǩ
        farmer_label = Text("ũ�� 200��").scale(0.5).next_to(farmer_rect, UP)
        librarian_label = Text("ͼ�����Ա 10��").scale(0.5).next_to(librarian_rect, UP)
        
        self.play(
            Create(farmer_rect),
            Create(librarian_rect),
            Write(farmer_label),
            Write(librarian_label)
        )
        self.wait(1)

        # ��ӷ�����������Ⱥ
        farmer_feature = Rectangle(width=5.8, height=0.24, color=YELLOW).shift(LEFT*2.5 + DOWN*1)
        librarian_feature = Rectangle(width=0.2, height=0.4, color=YELLOW).shift(RIGHT*2.9 + UP*0.8)
        
        # �������ı�
        result_text = Text("������� = 4/(4+20) �� 16.7%", color=RED).scale(0.8).to_edge(UP)
        
        self.play(
            Create(farmer_feature),
            Create(librarian_feature),
            Write(result_text)
        )
        self.wait(2)

# ��������: manim -pql bayes_example.py BayesTheoremExample
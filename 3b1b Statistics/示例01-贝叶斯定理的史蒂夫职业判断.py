from manim import *

class BayesTheoremExample(Scene):
    def construct(self):
        # 创建总体样本空间
        total_pop = Rectangle(width=6, height=3, color=WHITE)
        self.play(Create(total_pop))
        
        # 划分农民和图书管理员区域
        farmer_rect = Rectangle(width=5.8, height=2.4, color=BLUE).shift(LEFT*2.5)
        librarian_rect = Rectangle(width=0.2, height=2.4, color=GREEN).shift(RIGHT*2.9)
        
        # 添加标签
        farmer_label = Text("农民 200人").scale(0.5).next_to(farmer_rect, UP)
        librarian_label = Text("图书管理员 10人").scale(0.5).next_to(librarian_rect, UP)
        
        self.play(
            Create(farmer_rect),
            Create(librarian_rect),
            Write(farmer_label),
            Write(librarian_label)
        )
        self.wait(1)

        # 添加符合特征的人群
        farmer_feature = Rectangle(width=5.8, height=0.24, color=YELLOW).shift(LEFT*2.5 + DOWN*1)
        librarian_feature = Rectangle(width=0.2, height=0.4, color=YELLOW).shift(RIGHT*2.9 + UP*0.8)
        
        # 计算结果文本
        result_text = Text("后验概率 = 4/(4+20) ≈ 16.7%", color=RED).scale(0.8).to_edge(UP)
        
        self.play(
            Create(farmer_feature),
            Create(librarian_feature),
            Write(result_text)
        )
        self.wait(2)

# 运行命令: manim -pql bayes_example.py BayesTheoremExample
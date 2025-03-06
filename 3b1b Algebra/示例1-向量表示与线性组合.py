# 解释：该动画展示向量的几何表示和线性组合。
# 红色和蓝色箭头分别代表基向量的线性组合，绿色箭头展示合成后的向量，直观体现"缩放再相加"的概念。


from manim import *

class VectorRepresentation(Scene):
    def construct(self):
        # 创建坐标系
        grid = NumberPlane()
        self.play(Create(grid))
        
        # 定义向量v和w
        v = Vector([2, 1], color=RED)
        w = Vector([1, 2], color=BLUE)
        
        # 显示向量标签
        v_label = MathTex(r"\vec{v} = [2,1]").next_to(v, RIGHT)
        w_label = MathTex(r"\vec{w} = [1,2]").next_to(w, UP)
        
        # 动画展示向量
        self.play(GrowArrow(v), Write(v_label))
        self.wait(1)
        self.play(GrowArrow(w), Write(w_label))
        self.wait(2)
        
        # 线性组合 2v + 1.5w
        combo = Vector(2*v.get_vector() + 1.5*w.get_vector(), color=GREEN)
        combo_label = MathTex(r"2\vec{v} + 1.5\vec{w}").next_to(combo, LEFT)
        self.play(GrowArrow(combo), Write(combo_label))
        self.wait(3)
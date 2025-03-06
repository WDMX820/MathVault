# ���ͣ��ö���չʾ�����ļ��α�ʾ��������ϡ�
# ��ɫ����ɫ��ͷ�ֱ�����������������ϣ���ɫ��ͷչʾ�ϳɺ��������ֱ������"���������"�ĸ��


from manim import *

class VectorRepresentation(Scene):
    def construct(self):
        # ��������ϵ
        grid = NumberPlane()
        self.play(Create(grid))
        
        # ��������v��w
        v = Vector([2, 1], color=RED)
        w = Vector([1, 2], color=BLUE)
        
        # ��ʾ������ǩ
        v_label = MathTex(r"\vec{v} = [2,1]").next_to(v, RIGHT)
        w_label = MathTex(r"\vec{w} = [1,2]").next_to(w, UP)
        
        # ����չʾ����
        self.play(GrowArrow(v), Write(v_label))
        self.wait(1)
        self.play(GrowArrow(w), Write(w_label))
        self.wait(2)
        
        # ������� 2v + 1.5w
        combo = Vector(2*v.get_vector() + 1.5*w.get_vector(), color=GREEN)
        combo_label = MathTex(r"2\vec{v} + 1.5\vec{w}").next_to(combo, LEFT)
        self.play(GrowArrow(combo), Write(combo_label))
        self.wait(3)
# ���ͣ�ʹ��LinearTransformationSceneչʾ���б任��
# ����ԭʼ��������͸�����Աȱ任Ч����������ж�Ӧ�µĻ�����λ�ã�ֱ����ʾ"���񱣳�ƽ��"�����ԡ�


class ShearTransform(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True
        )
    
    def construct(self):
        # ��ʼ����Ϊ���о��� [1 1; 0 1]
        shear_matrix = [[1, 1], [0, 1]]
        
        # Ӧ�þ���任
        self.apply_matrix(shear_matrix)
        self.wait()
        
        # ��ʾ�����ǩ
        matrix_label = MathTex(r"\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}").to_edge(UR)
        self.play(Write(matrix_label))
        self.wait(2)
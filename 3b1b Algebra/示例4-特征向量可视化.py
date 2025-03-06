# ���ͣ�չʾ���������ڱ任�б��ַ��򲻱䣨�ƽ��ͷ���������ȱ�����ֵ��=2���š�
# ������������ı��γɶԱȣ�ͻ�����������ĺ������ԡ�

class EigenDemo(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True
        )
    
    def construct(self):
        # ����������������y�ᣩ
        eig_vec = Vector([0, 3], color=GOLD)
        self.play(GrowArrow(eig_vec))
        
        # Ӧ�����ű任���� [1 0; 0 2]
        matrix = [[1, 0], [0, 2]]
        self.apply_matrix(matrix)
        
        # ��ʾ����ֵ��ǩ
        eig_label = MathTex(r"\lambda = 2").next_to(eig_vec, RIGHT)
        self.play(Write(eig_label))
        self.wait(2)
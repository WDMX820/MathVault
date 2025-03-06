# ���ͣ�ͨ����λ�����α任ǰ�������仯��ֱ��չʾ����ʽ��Ϊ����������ӵļ������塣
# ��ɫ���������ԭ��ɫ��2������Ӧ����ʽֵ2��


class DeterminantDemo(Scene):
    def construct(self):
        # ������λ������
        square = Square(side_length=1, color=BLUE, fill_opacity=0.5)
        square.move_to(ORIGIN)
        
        # �任��������ʽ=2��
        matrix = [[2, 1], [0, 1]]
        
        # Ӧ�ñ任
        transformed_square = square.copy()
        transformed_square.apply_matrix(matrix)
        transformed_square.set_color(RED)
        
        # ��ʾ�����ǩ
        det_label = MathTex(r"\text{det} = 2").next_to(transformed_square, UR)
        
        self.play(Create(square))
        self.wait(1)
        self.play(Transform(square, transformed_square), Write(det_label))
        self.wait(2)
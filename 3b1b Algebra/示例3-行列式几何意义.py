# 解释：通过单位正方形变换前后的面积变化，直观展示行列式作为面积缩放因子的几何意义。
# 红色区域面积是原蓝色的2倍，对应行列式值2。


class DeterminantDemo(Scene):
    def construct(self):
        # 创建单位正方形
        square = Square(side_length=1, color=BLUE, fill_opacity=0.5)
        square.move_to(ORIGIN)
        
        # 变换矩阵（行列式=2）
        matrix = [[2, 1], [0, 1]]
        
        # 应用变换
        transformed_square = square.copy()
        transformed_square.apply_matrix(matrix)
        transformed_square.set_color(RED)
        
        # 显示面积标签
        det_label = MathTex(r"\text{det} = 2").next_to(transformed_square, UR)
        
        self.play(Create(square))
        self.wait(1)
        self.play(Transform(square, transformed_square), Write(det_label))
        self.wait(2)
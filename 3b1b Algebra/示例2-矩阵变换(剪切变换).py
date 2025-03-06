# 解释：使用LinearTransformationScene展示剪切变换。
# 保留原始向量（半透明）对比变换效果，矩阵的列对应新的基向量位置，直观演示"网格保持平行"的特性。


class ShearTransform(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True
        )
    
    def construct(self):
        # 初始矩阵为剪切矩阵 [1 1; 0 1]
        shear_matrix = [[1, 1], [0, 1]]
        
        # 应用矩阵变换
        self.apply_matrix(shear_matrix)
        self.wait()
        
        # 显示矩阵标签
        matrix_label = MathTex(r"\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}").to_edge(UR)
        self.play(Write(matrix_label))
        self.wait(2)
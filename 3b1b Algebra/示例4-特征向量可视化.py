# 解释：展示特征向量在变换中保持方向不变（黄金箭头），仅长度被特征值λ=2缩放。
# 其他向量方向改变形成对比，突出特征向量的核心特性。

class EigenDemo(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True
        )
    
    def construct(self):
        # 定义特征向量（沿y轴）
        eig_vec = Vector([0, 3], color=GOLD)
        self.play(GrowArrow(eig_vec))
        
        # 应用缩放变换矩阵 [1 0; 0 2]
        matrix = [[1, 0], [0, 2]]
        self.apply_matrix(matrix)
        
        # 显示特征值标签
        eig_label = MathTex(r"\lambda = 2").next_to(eig_vec, RIGHT)
        self.play(Write(eig_label))
        self.wait(2)
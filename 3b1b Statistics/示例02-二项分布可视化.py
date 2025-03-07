from manim import *
from scipy.stats import binom

class BinomialDistribution(Scene):
    def construct(self):
        n = 50  # 总试验次数
        p = 0.96  # 假设真实概率
        
        # 创建坐标轴
        ax = Axes(
            x_range=[30, 50, 5],
            y_range=[0, 0.2, 0.05],
            axis_config={"color": BLUE},
        )
        labels = ax.get_axis_labels(x_label="成功次数", y_label="概率密度")
        
        # 生成二项分布数据
        x_values = np.arange(30, 51)
        pmf_values = [binom.pmf(k, n, p) for k in x_values]
        
        # 创建柱状图
        bars = VGroup()
        for x, y in zip(x_values, pmf_values):
            bar = Rectangle(
                height=y*10,  # 缩放高度
                width=0.3,
                fill_color=GREEN,
                fill_opacity=0.7,
                stroke_color=WHITE
            ).move_to(ax.c2p(x, y*5))  # 调整位置
            bars.add(bar)
        
        # 标记观测值
        observed_line = DashedLine(
            start=ax.c2p(48, 0),
            end=ax.c2p(48, 0.18),
            color=RED
        )
        observed_label = Text("48次好评", color=RED).scale(0.5).next_to(observed_line, UP)
        
        self.play(Create(ax), Write(labels))
        self.play(LaggedStart(*[Create(bar) for bar in bars], lag_ratio=0.1))
        self.play(Create(observed_line), Write(observed_label))
        self.wait(2)

# 运行命令: manim -pql binomial.py BinomialDistribution
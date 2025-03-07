from manim import *
from scipy.stats import binom

class BinomialDistribution(Scene):
    def construct(self):
        n = 50  # ���������
        p = 0.96  # ������ʵ����
        
        # ����������
        ax = Axes(
            x_range=[30, 50, 5],
            y_range=[0, 0.2, 0.05],
            axis_config={"color": BLUE},
        )
        labels = ax.get_axis_labels(x_label="�ɹ�����", y_label="�����ܶ�")
        
        # ���ɶ���ֲ�����
        x_values = np.arange(30, 51)
        pmf_values = [binom.pmf(k, n, p) for k in x_values]
        
        # ������״ͼ
        bars = VGroup()
        for x, y in zip(x_values, pmf_values):
            bar = Rectangle(
                height=y*10,  # ���Ÿ߶�
                width=0.3,
                fill_color=GREEN,
                fill_opacity=0.7,
                stroke_color=WHITE
            ).move_to(ax.c2p(x, y*5))  # ����λ��
            bars.add(bar)
        
        # ��ǹ۲�ֵ
        observed_line = DashedLine(
            start=ax.c2p(48, 0),
            end=ax.c2p(48, 0.18),
            color=RED
        )
        observed_label = Text("48�κ���", color=RED).scale(0.5).next_to(observed_line, UP)
        
        self.play(Create(ax), Write(labels))
        self.play(LaggedStart(*[Create(bar) for bar in bars], lag_ratio=0.1))
        self.play(Create(observed_line), Write(observed_label))
        self.wait(2)

# ��������: manim -pql binomial.py BinomialDistribution
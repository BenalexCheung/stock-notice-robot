import matplotlib.pyplot as plt
import numpy as np


def plot_histogram(up_count, down_count, volumes, num_days):

    # 计算每日涨跌比
    # changes = [(up - down) / (up + down)
    #            for up, down in zip(up_count, down_count)]

    # 计算涨跌比
    change_ratio = [up / down for up, down in zip(up_count, down_count)]
    # 生成颜色列表
    colors = ['red' if ratio >= 1 else 'green' for ratio in change_ratio]

    # 计算涨跌百分比
    total_count = [up + down for up, down in zip(up_count, down_count)]
    change_percent = [
        (up - down) / total
        for up, down, total in zip(up_count, down_count, total_count)
    ]

    # 定义成交量系数
    up_volume_coef = 0.1  # 上涨成交量系数
    down_volume_coef = 0.05  # 下跌成交量系数

    # 计算加权指标
    weighted_indicator = [(up * up_volume_coef) - (down * down_volume_coef)
                          for up, down in zip(up_count, down_count)]

    print("涨跌比率:", change_ratio)
    print("涨跌百分比:", change_percent)
    print("加权指标:", weighted_indicator)

    # 创建一个图形窗口
    fig, ax1 = plt.subplots(figsize=(8, 6))

    # 绘制每日成交量的直方图
    ax1.bar(num_days, volumes, color=colors, alpha=0.5)
    ax1.set_xlabel('Day')
    ax1.set_ylabel('Volume')

    # 创建第二个纵轴
    ax2 = ax1.twinx()

    # 绘制每日涨跌比的折线图
    ax2.plot(num_days, change_percent, marker='o', linestyle='-', color='blue')
    ax2.set_ylabel('Gain/Loss Ratio')

    # 调整第二个纵轴的范围
    ax2.set_ylim([-1, 1])  # 根据实际情况调整范围

    # 添加图例
    ax2.legend(['Gain/Loss Ratio'])

    # 显示图形
    image_path = 'stock-chart.png'
    plt.savefig(image_path)
    return image_path

import matplotlib.pyplot as plt

def plot_histogram(up_count, down_count, volumes):
    # 计算总交易日数
    num_days = len(up_count)

    # 计算每日涨跌比
    changes = [(up - down) / (up + down) for up, down in zip(up_count, down_count)]

    # 创建一个图形窗口
    fig, ax1 = plt.subplots(figsize=(8, 6))

    # 绘制每日成交量的直方图
    ax1.bar(range(num_days), volumes, color='blue', alpha=0.5)
    ax1.set_xlabel('Day')
    ax1.set_ylabel('Volume')

    # 创建第二个纵轴
    ax2 = ax1.twinx()

    # 绘制每日涨跌比的折线图
    ax2.plot(range(num_days), changes, marker='o', linestyle='-', color='green')
    ax2.set_ylabel('Gain/Loss Ratio')

    # 调整第二个纵轴的范围
    ax2.set_ylim([-1, 1])  # 根据实际情况调整范围

    # 添加图例
    ax2.legend(['Gain/Loss Ratio'])

    # 显示图形
    plt.savefig('stock-chart.png')
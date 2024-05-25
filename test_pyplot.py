import matplotlib.pyplot as plt

# 假设这是每日上涨和下跌的数量数据
daily_rises = [5, 3, 2, 4, 6, 1, 2]
daily_declines = [2, 4, 1, 3, 2, 5, 2]

# 计算每日涨跌比
daily_changes = [(rise - decline) / (rise + decline) for rise, decline in zip(daily_rises, daily_declines)]

# 假设这是每日的成交量数据
daily_volumes = [100000, 150000, 120000, 180000, 200000, 90000, 110000]

# 创建一个图形窗口
fig, ax1 = plt.subplots(figsize=(8, 6))

# 绘制每日成交量的直方图
ax1.bar(range(len(daily_volumes)), daily_volumes, color='blue', alpha=0.5)
ax1.set_xlabel('Day')
ax1.set_ylabel('Volume')

# 创建第二个纵轴
ax2 = ax1.twinx()

# 绘制每日涨跌比的折线图
ax2.plot(range(len(daily_changes)), daily_changes, marker='o', linestyle='-', color='green')
ax2.set_ylabel('Gain/Loss Ratio')

# 调整第二个纵轴的范围
ax2.set_ylim([-1, 1])  # 根据实际情况调整范围

# 添加图例
ax2.legend(['Gain/Loss Ratio'])

# 显示图形
plt.savefig('chart.png')
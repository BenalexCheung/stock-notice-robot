import pandas as pd

# 假设这是每日的股票数据，包含日期、股票代码、开盘价、收盘价、最高价、最低价等列
stock_data = [
    ['2024-05-24', 'AAPL', 131.82, 132.54, 133.16, 131.63],
    ['2024-05-24', 'GOOGL', 2425.0, 2430.78, 2443.0, 2420.0],
    ['2024-05-24', 'MSFT', 251.77, 252.57, 253.25, 251.32]
]

# 创建DataFrame对象
df = pd.DataFrame(stock_data, columns=['Date', 'Symbol', 'Open', 'Close', 'High', 'Low'])

# 将日期列转换为日期类型
df['Date'] = pd.to_datetime(df['Date'])

# 格式化日期
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

# 格式化浮点数列（保留2位小数）
df['Open'] = df['Open'].map('{:.2f}'.format)
df['Close'] = df['Close'].map('{:.2f}'.format)
df['High'] = df['High'].map('{:.2f}'.format)
df['Low'] = df['Low'].map('{:.2f}'.format)

# 生成每日股票情况的格式化字符串
formatted_data = df.to_string(index=False)

# 打印格式化的股票情况
print(formatted_data)
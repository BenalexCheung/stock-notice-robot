import requests

# 定义 Alpha Vantage API 的基本 URL 和您的 API 密钥
BASE_URL = "https://www.alphavantage.co/query"
API_KEY = "WOAIKGXUN16PVGHH"  # 请替换为您自己的 API 密钥

# 定义函数来获取每日涨停信息
def get_daily_limit_up(symbol):
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        print(data)
        if "Time Series (Daily)" in data:
            daily_data = data["Time Series (Daily)"]
            latest_date = max(daily_data.keys())  # 获取最新日期的数据
            latest_data = daily_data[latest_date]
            high_price = float(latest_data["2. high"])  # 获取最高价
            low_price = float(latest_data["3. low"])  # 获取最低价
            close_price = float(latest_data["4. close"])  # 获取收盘价

            if close_price == high_price:
                print(f"{symbol} 今日涨停！")
            else:
                print(f"{symbol} 今日未涨停")
        else:
            print(f"无法获取 {symbol} 的数据")

    except Exception as e:
        print(f"获取 {symbol} 的数据时出现错误：{e}")

# 示例：获取某只股票的每日涨停信息
symbol = "000903.SHZ"  # 苹果公司的股票代码
get_daily_limit_up(symbol)

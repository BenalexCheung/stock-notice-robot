import requests
import json

# 假设你有一个函数来获取实时股票数据


def get_real_time_stock_data():
    # 这里应该是调用API接口的代码
    url = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=1&num=100&sort=changepercent&asc=0&node=hs_a&symbol=&_s_r_a=page"
    stock_data = []
    try:
        response = requests.get(url)
        data = response.text
        if data:
            stock_data = data
        else:
            print("无法获取数据")
    except Exception as e:
        print(f"获取数据时出现错误：{e}")
    return json.loads(stock_data)

# 检查股票是否连板
def is_consecutive_board(stock_data, threshold=10):

    # 这里假设你已经有了昨天的连板股票信息，存储在一个字典中
    # key为股票代码，value为连板天数
    yesterday_consecutive_board = {
        '000001': 2,  # 假设000001昨天已经连板2天
        # ... 其他昨天的连板股票信息
    }

    today_consecutive_board = {}
    for stock in stock_data:
        symbol = stock['symbol']
        name = stock['name']
        change_percent = stock['changepercent']

        # 检查涨幅是否达到涨停阈值（例如10%）
        if change_percent >= threshold:
            # 如果是昨天的连板股票，则连板天数加1
            if symbol in yesterday_consecutive_board:
                yesterday_consecutive_days = yesterday_consecutive_board[symbol]
                today_consecutive_board[symbol] = {
                    'days': yesterday_consecutive_days + 1,
                    'name': name,
                }
            # 如果是新出现的连板股票，则连板天数为1
            else:
                today_consecutive_board[symbol] = {
                    'days': 1,
                    'name': name,
                }

    return today_consecutive_board

# 主函数


def main():
    # 获取实时股票数据
    stock_data = get_real_time_stock_data()

    # 检查连板股票
    today_consecutive_board = is_consecutive_board(stock_data)
    print(today_consecutive_board)

    # 输出连板股票信息
    for symbol, board in today_consecutive_board.items():
        print(f"股票代码：{symbol}, 股票名称：{board['name']}, 连板天数：{board['days']}天")


# 运行主函数
if __name__ == "__main__":
    main()

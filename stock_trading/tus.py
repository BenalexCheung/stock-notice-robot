import tushare as ts  
import pandas as pd  
  
# 初始化tushare  
ts.set_token('eda81f0fbe6d9efefe355f91b11048ebfc7ebe2749b0fe4882393088')  # 设置你的tushare token  
pro = ts.pro_api()  
  
# 定义获取股票历史数据的函数  
def get_stock_history(ts_code, start_date, end_date):  
    df = pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)  
    return df  
  
# 定义判断涨停的函数  
def is_limit_up(pct_chg):  
    # 假设涨停阈值为10%  
    return pct_chg >= 10  
  
# 定义计算连板天数的函数  
def calculate_consecutive_days(df):  
    consecutive_days = []  
    current_consecutive = 0  
    for index, row in df.iterrows():  
        if is_limit_up(row['pct_chg']):  
            current_consecutive += 1  
        else:  
            current_consecutive = 0  
        consecutive_days.append(current_consecutive)  
    return consecutive_days  
  
# 定义识别连板高度突破的函数  
def identify_breakthrough(consecutive_days, previous_max):  
    if max(consecutive_days) > previous_max:  
        return max(consecutive_days)  
    else:  
        return None  
  
# 主函数  
def main(ts_code, start_date, end_date, previous_max_consecutive):  
    df = get_stock_history(ts_code, start_date, end_date)  
    df['pct_chg'] = df['pct_chg'] / 100  # 转换涨跌幅为小数  
    print(df)
    consecutive_days = calculate_consecutive_days(df)  
    breakthrough = identify_breakthrough(consecutive_days, previous_max_consecutive)  
    if breakthrough:  
        print(f"股票{ts_code}的连板高度突破了之前的记录，当前最大连板天数为：{breakthrough}天")  
    else:  
        print(f"股票{ts_code}的连板高度没有突破之前的记录")  
  
# 使用示例  
ts_code = '832023.BJ'  # 示例股票代码  
start_date = '20240322'  # 开始日期  
end_date = '20240322'  # 结束日期  
previous_max_consecutive = 5  # 假设之前的最大连板天数是5天  
  
main(ts_code, start_date, end_date, previous_max_consecutive)
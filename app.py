import schedule
import time
from app.stock_plt import plot_histogram
from app.services import send_message_to_dingtalk
from app.imgbb import upload_image_to_imgbb
from datetime import datetime
import sys
import signal


# 5月24日，市场全天冲高回落，创业板指领跌，沪指失守3100点。截至收盘，沪指跌0.88%，深成指跌1.23%，创业板指跌1.81%。
# 　　板块方面，电力、铜缆高速连接、猪肉、乳业等板块涨幅居前，低空经济、AI手机、房地产、存储芯片等板块跌幅居前。
# 　　总体上个股跌多涨少，全市场超3800只个股下跌。沪深两市今日成交额7639亿，较上个交易日缩量838亿。
# 　　截至今天收盘，此前周线5连阳的沪指也终于收阴，进入弱势调整格局；沪指4月底站上3100点迄今，还不满一个月，今天也首次跌破了。
def job():

    up_count = [2823, 2823, 2755, 1148, 3108, 735, 1313, 3397, 1149]
    down_count = [2342, 1125, 2411, 4093, 2020, 4578, 3851, 1760, 4140]
    limit_up = [63, 96, 61, 34, 55, 39, 58, 45, 34]
    limit_down = [19, 19, 49, 48, 36, 29, 30, 51, 52]
    volumes = [8504, 8901, 9982, 8019., 8343, 8559, 7692, 7748, 7417]
    num_days = ['5.16', '5.17', '5.20', '5.21', '5.22', '5.23', '5.24', '5.27', '5.28']

    image_path = plot_histogram(up_count, down_count, limit_up, limit_down, volumes, num_days)
    time.sleep(1)

    image_url = upload_image_to_imgbb(image_path)
    time.sleep(1)

    now_time = datetime.now().strftime('%Y.%m.%d %H:%M:%S')

    shanghai_drop = 0.88
    shenzhen_drop = 1.23
    chuangye_drop = 1.81
    leading_sectors = "电力、铜缆高速连接、猪肉、乳业等板块"
    declining_sectors = "低空经济、AI手机、房地产、存储芯片等板块"
    total_decliners = 3800
    trading_volume = "7639亿"
    volume_change = "838亿"
    additional_info = "此前周线5连阳的沪指也终于收阴，进入弱势调整格局；沪指4月底站上3100点迄今，还不满一个月，今天也首次跌破了。"

    md_template = '''
![每日走势]({image_url})

沪指失守3100点，市场全天冲高回落。截至收盘，沪指跌{shanghai_drop}%，深成指跌{shenzhen_drop}%，创业板指跌{chuangye_drop}%。

**<font color="#dd0000">板块涨幅居前：{leading_sectors}</font>**

**<font color="#2F4F4F">板块跌幅居前：{declining_sectors}</font>**

全市场超过{total_decliners}只个股下跌，个股跌多涨少。

沪深两市成交额为{trading_volume}，较上个交易日缩量{volume_change}。

**<font color="#FFA500">点评：{additional_info}</font>**

[涨跌停历史数据](https://q.stock.sohu.com/cn/zdt.shtml)

*发送时间: {now_time}* 
'''
    md = md_template.format(now_time=now_time,
                            image_url=image_url,
                            shanghai_drop=shanghai_drop,
                            shenzhen_drop=shenzhen_drop,
                            chuangye_drop=chuangye_drop,
                            leading_sectors=leading_sectors,
                            declining_sectors=declining_sectors,
                            total_decliners=total_decliners,
                            trading_volume=trading_volume,
                            volume_change=volume_change,
                            additional_info=additional_info)

    date = datetime.now().strftime('%Y.%m.%d')
    title = '股票市场日报 - {date}'.format(date=date)
    send_message_to_dingtalk(title, md)
    print("This is a scheduled job.")
    global running
    running = False


# 设置一个标志变量来控制循环
running = True


def exit_gracefully(signum, frame):
    # 改变标志来退出循环
    global running
    running = False
    print("正在优雅退出...")


# 注册信号处理程序，以便在收到 SIGINT（通常是 Ctrl+C）时优雅退出
signal.signal(signal.SIGINT, exit_gracefully)

# 创建一个每分钟执行一次的任务
schedule.every(5).seconds.do(job)

while running:
    try:
        schedule.run_pending()
    except Exception as e:
        # 捕获异常并打印错误信息
        print(e)
    time.sleep(1)  # 这里的 sleep 时间可以根据需要调整

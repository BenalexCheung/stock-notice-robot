from app import app
from app.services import send_message_to_dingtalk
from app.services import send_image_to_dingtalk
from app.imgbb import upload_image_to_imgbb
from app.stock_plt import plot_histogram
import base64


@app.route('/')
def hello():
    app.logger.warning('This is a warning message')
    return 'Hello, World!'


@app.route("/send_message", methods=["GET"])
def send_message():
    title = 'Test message'
    text = f'This is a paragraph with **bold** and *italic* text.'
    image_url = upload_image_to_imgbb('chart.png')
    return send_image_to_dingtalk(image_url)


@app.route("/test", methods=["GET"])
def test():
    up_count = [5, 3, 2, 4, 6, 1, 2]
    down_count = [2, 4, 1, 3, 2, 5, 2]
    volumes = [100000, 150000, 120000, 180000, 200000, 90000, 110000]

    # plot_histogram(up_count, down_count, volumes)
    # 读取图片文件并进行Base64编码
    with open('chart.png', 'rb') as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')

    # 打印Base64编码的字符串
    print(base64_image)
    html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Base64 Image Demo</title>
</head>
<body>
    <img src="data:image/png;base64,{base64_data}"></img>
</body>
</html>
"""
    # 使用字符串格式化将Base64编码数据替换到HTML变量中
    html = html_template.format(base64_data=base64_image)
    return html

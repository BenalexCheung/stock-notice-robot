import requests

from app.config import CLIENT_API_KEY


def upload_image_to_imgbb(image_url):
    url = "https://api.imgbb.com/1/upload"
    params = {"expiration": 60 * 60 * 24 * 7, "key": CLIENT_API_KEY}
    files = {"image": open(image_url, "rb")}

    response = requests.post(url, params=params, files=files)
    data = response.json()

    # 处理响应结果
    if response.status_code == 200:
        image_url = data["data"]["url"]
        # 在这里可以对图像URL进行进一步处理或返回
        return image_url
    else:
        error_message = data["error"]["message"]
        # 在这里可以对错误进行处理或返回
        print(error_message)
        return None

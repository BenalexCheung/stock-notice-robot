from app import app
from app.services import send_message_to_dingtalk


@app.route('/')
def hello():
    app.logger.warning('This is a warning message')
    return 'Hello, World!'


@app.route("/send_message", methods=["GET"])
def send_message():
    title = 'Test message'
    text = f'This is a paragraph with **bold** and *italic* text.'
    markdown_string = '''
# Heading 1

This is a paragraph with **bold** and *italic* text.

## Heading 2

- List item 1
- List item 2
- List item 3

> This is a blockquote.

Here's a [link](https://example.com) to a website.

![Image](image.jpg)
'''
    return send_message_to_dingtalk(title, markdown_string)

from flask import Flask, request, send_from_directory, jsonify
import time
import subprocess
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_markdown():
    content = request.get_data(as_text=True)
    time_name = str(int(time.time()))
    file_name = time_name + ".md"
    html_name = time_name + ".html"
    
    try:
        # 保存 Markdown 文件
        with open(f"data/{file_name}", 'w', encoding='utf-8') as f:
            f.write(content)
        
        # 转换 MD 为 HTML
        result = subprocess.run(
            ['markmap', f'data/{file_name}', '--output', f'data/{html_name}', '--no-open'],
            capture_output=True,
            text=True,
            check=True  # 自动抛出错误
        )
        
        # 返回正确的访问链接（使用容器实际端口 5005）
        # 直接返回纯链接字符串 (text/plain)
        return f"http://{request.host}/html/{html_name}"
    
    except subprocess.CalledProcessError as e:
        # 错误时仍返回JSON结构
        return jsonify({
            "status": "error",
            "message": f"Markmap conversion failed: {e.stderr}"
        }), 500
    except Exception as e:
        # 捕获其他可能的异常
        return jsonify({
            "status": "error",
            "message": f"Server error: {str(e)}"
        }), 500

@app.route('/html/<filename>', methods=['GET'])
def get_html(filename):
    return send_from_directory("data", filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)

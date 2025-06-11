import logging
from flask import Flask, request, send_from_directory
import os
import time
import subprocess

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

# 确保 data 目录存在
os.makedirs('data', exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_markdown():
    # 获取上传的 Markdown 内容
    content = request.get_data(as_text=True)
    
    # 生成唯一文件名
    timestamp = str(int(time.time()))
    md_filename = f"{timestamp}.md"
    pptx_filename = f"{timestamp}.pptx"

    # 保存 Markdown 文件
    md_path = os.path.join('data', md_filename)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(content)

    # 构建 PPTX 文件路径
    pptx_path = os.path.join('data', pptx_filename)

    # 使用 marp 转换 Markdown 为 PPTX
    try:
        app.logger.info(f"Converting {md_path} to PPTX...")
        result = subprocess.run(
            [
                'marp', 
                md_path,
                '--theme', 'default',  # 使用更兼容的默认主题
                '--allow-local-files',  # 允许本地资源
                '--output', pptx_path
            ],
            capture_output=True,
            text=True,
            encoding='utf-8',
            check=True
        )
        app.logger.info(f"Conversion successful: {result.stdout}")
    except subprocess.CalledProcessError as e:
        error_msg = f"转换失败: {e.stderr if e.stderr else '未知错误'}"
        app.logger.error(f"Conversion failed: {error_msg}")
        app.logger.error(f"Command output: {e.output}")
        return error_msg, 500

    # 返回下载链接
    return f'PPT 已生成\n下载地址: http://{request.host}/download/{pptx_filename}'

@app.route('/download/<filename>', methods=['GET'])
def download_ppt(filename):
    # 提供生成的 PPT 文件下载
    return send_from_directory('data', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)

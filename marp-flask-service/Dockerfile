# 使用官方的 Python 镜像作为基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制 requirements.txt 并安装依赖
COPY requirements.txt .
RUN pip install -r requirements.txt

# 更新包列表并安装必要的依赖
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    libnss3 \
    software-properties-common \
    npm \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libxcomposite1 \
    libxrandr2 \
    libxdamage1 \
    libxkbcommon0 \
    libgbm1 \
    libpango-1.0-0 \
    libcairo2 \
    libasound2 \
    libxtst6 \
    libxshmfence1 \
    fonts-liberation \
    fonts-wqy-zenhei \ 
    fonts-noto-cjk \  
    libvulkan1 \
    # 安装Chromium浏览器及驱动
    chromium chromium-driver \
    && rm -rf /var/lib/apt/lists/*

RUN npm install -g n && n stable
RUN npm install npm@latest -g && \
    npm install n -g && \
    n latest
# 安装 marp-cli 和相关工具
RUN npm install -g \
    @marp-team/marp-cli

# 配置环境变量指向Chromium（解决Headless模式路径问题）
ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium
# 设置UTF-8环境
ENV LANG=C.UTF-8

COPY . .

# 设置容器启动时执行的命令
CMD ["python", "main.py"]

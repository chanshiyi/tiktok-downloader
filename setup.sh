#!/bin/bash
echo "正在下载最新版本..."
git clone https://github.com/chanshiyi/tiktok-downloader.git tiktok-downloader
cd tiktok-downloader
pip install -r requirements.txt
playwright install
echo "安装完成！"
echo "运行方式：python app.py"
echo "更新方式：运行 update.sh" 
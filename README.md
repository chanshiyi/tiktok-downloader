# TikTok 视频下载器

一个简单的 TikTok 视频下载工具，支持网页界面操作。

## 功能特点
- 简洁的网页操作界面
- 自动保存到downloads文件夹
- 显示下载进度条
- 支持批量下载
- 自动错误处理和日志记录

## 安装说明

### 前置要求
- Python 3.7 或更高版本
- Git（可选，用于更新）

### 快速开始
1. 下载此仓库（两种方式）：
   - 使用 Git：`git clone [仓库地址]`
   - 或直接下载 ZIP 文件并解压

2. 运行安装脚本：
   - Windows: 双击运行 `setup.bat`
   - Linux/Mac: 运行 `./setup.sh`

3. 启动程序：
   ```bash
   python app.py
   ```

4. 打开浏览器访问：
   ```
   http://127.0.0.1:5000
   ```

### 更新程序
- Windows: 运行 `update.bat`
- Linux/Mac: 运行 `update.sh`

## 使用方法
1. 打开 TikTok，复制视频链接
2. 粘贴到下载器网页中
3. 点击"下载视频"按钮
4. 视频将自动下载到 downloads 文件夹

## 注意事项
- 确保有稳定的网络连接
- 下载的视频将保存在程序目录的 downloads 文件夹中
- 如遇到问题，请查看 downloader.log 文件中的错误日志

## 问题反馈
如果遇到问题，请在 Issues 中提交，并附上 downloader.log 文件的相关内容。 
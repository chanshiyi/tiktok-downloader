@echo off
echo 正在安装依赖...
pip install -r requirements.txt
playwright install
echo.
echo 安装完成！
echo 运行方式：
echo 1. 打开命令提示符 (Win+R，输入cmd)
echo 2. 进入程序所在文件夹
echo 3. 输入：python app.py
echo 4. 打开浏览器访问：http://127.0.0.1:5000
pause 
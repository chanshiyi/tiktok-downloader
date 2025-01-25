@echo off
pip install pywin32
python install_service.py install
python install_service.py start
echo 服务安装完成！
pause 
import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import sys
import os
import logging
from pathlib import Path
from waitress import serve
from app import app

class TikTokDownloaderService(win32serviceutil.ServiceFramework):
    _svc_name_ = "TikTokDownloader"
    _svc_display_name_ = "TikTok Downloader Service"
    _svc_description_ = "TikTok视频下载服务"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)
        self.is_alive = True

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)
        self.is_alive = False

    def SvcDoRun(self):
        try:
            # 设置工作目录
            os.chdir(str(Path(__file__).parent))
            
            # 配置日志
            logging.basicConfig(
                filename='service.log',
                level=logging.INFO,
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            
            # 启动服务器
            serve(app, host='0.0.0.0', port=5000)
            
        except Exception as e:
            logging.error(f"服务启动失败: {str(e)}")
            self.SvcStop()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(TikTokDownloaderService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(TikTokDownloaderService) 
import asyncio
from playwright.async_api import async_playwright
import requests
from tqdm import tqdm
import re
import os
import logging
from datetime import datetime

# 配置日志
logging.basicConfig(
    filename='downloader.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

async def get_video_url(tiktok_url):
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            
            logging.info(f"正在访问: {tiktok_url}")
            await page.goto(tiktok_url)
            await page.wait_for_load_state('networkidle')
            
            video = await page.wait_for_selector('video')
            video_url = await video.get_attribute('src')
            
            await browser.close()
            logging.info("成功获取视频地址")
            return video_url
    except Exception as e:
        logging.error(f"获取视频地址失败: {str(e)}")
        raise

def download_video(video_url, output_path):
    try:
        response = requests.get(video_url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        
        logging.info(f"开始下载视频到: {output_path}")
        with open(output_path, 'wb') as file, tqdm(
            desc='下载进度',
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as pbar:
            for data in response.iter_content(chunk_size=1024):
                size = file.write(data)
                pbar.update(size)
        
        logging.info("视频下载完成")
    except Exception as e:
        logging.error(f"下载视频失败: {str(e)}")
        raise

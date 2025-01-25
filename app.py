from flask import Flask, render_template, request, send_file, jsonify
import asyncio
import os
from downloader import get_video_url, download_video

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
async def download():
    tiktok_url = request.form.get('url')
    
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    
    try:
        # 获取视频URL
        video_url = await get_video_url(tiktok_url)
        
        # 生成输出文件名
        output_path = os.path.join('downloads', f'tiktok_video_{len(os.listdir("downloads")) + 1}.mp4')
        
        # 下载视频
        download_video(video_url, output_path)
        
        # 返回下载文件
        return send_file(output_path, as_attachment=True)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 
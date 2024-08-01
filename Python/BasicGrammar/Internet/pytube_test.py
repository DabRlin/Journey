from pytube import YouTube

#创建Yotube对象
yt = YouTube('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

#获取最高分辨率视频流
stream = yt.streams.get_highest_resolution()

#下载视频
stream.download(output_path="C:/Users/dangh/Downloads",filename="video.mp4")
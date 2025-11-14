import requests

url = 'https://parsinger.ru/video_downloads/videoplayback.mp4'

response = requests.get(url=url, stream=True)
with open('download.mp4', 'wb') as file:
    for i in response.iter_content(chunk_size=10000):
        file.write(i)


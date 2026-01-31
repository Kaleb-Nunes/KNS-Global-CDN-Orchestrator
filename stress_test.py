import requests, time
TARGET = 'http://localhost/video.mp4'
for i in range(5):
    start = time.time()
    r = requests.get(TARGET)
    print(f'Tempo: {time.time()-start:.4f}s')
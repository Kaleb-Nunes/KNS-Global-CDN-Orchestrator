import requests, time
TARGET = 'http://localhost/video.mp4'
print(' Testando Performance do CDN...')
try:
    for i in range(5):
        start = time.time()
        r = requests.get(TARGET)
        print(f'Req {i+1}: {time.time()-start:.4f}s')
except Exception as e: print(f'Erro: {e}')
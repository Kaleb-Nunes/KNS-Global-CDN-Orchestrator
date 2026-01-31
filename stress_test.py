import requests, time, statistics
TARGET = 'http://localhost/video.mp4'
results = []
print(' Validando Estabilidade Operacional...')
for i in range(10):
    start = time.time()
    try:
        r = requests.get(TARGET)
        duration = time.time() - start
        results.append(duration)
        print(f'Amostra {i+1}: {duration:.4f}s')
    except: pass
if results:
    print(f'\n--- MÉTRICAS OPERACIONAIS ---')
    print(f'Média: {statistics.mean(results):.4f}s')
    print(f'Jitter: {statistics.stdev(results):.4f}s') # Validação de consistência

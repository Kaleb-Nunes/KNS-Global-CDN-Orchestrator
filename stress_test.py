import requests, time, statistics

TARGET = 'http://localhost/video.mp4'
data = []

print(' Validando Performance Operacional (Protocolo 09)...')
for i in range(10):
    start = time.time()
    try:
        r = requests.get(TARGET)
        latency = time.time() - start
        data.append(latency)
        print(f'Amostra {i+1}: {latency:.4f}s | Cache: {r.headers.get("X-Cache-Status", "N/A")}')
    except: pass

if len(data) > 1:
    print(f'\n--- DASHBOARD OPERACIONAL ---')
    print(f'Média de Latência: {statistics.mean(data):.4f}s')
    print(f'Jitter (Instabilidade): {statistics.stdev(data):.4f}s') # Prova de estabilidade

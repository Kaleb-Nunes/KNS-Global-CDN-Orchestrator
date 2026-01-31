import requests, time, statistics

TARGET = 'http://localhost/video.mp4'
latencies = []

print(' Executando Stress Test Operacional...')
for i in range(10):
    start = time.time()
    try:
        r = requests.get(TARGET)
        end = time.time() - start
        latencies.append(end)
        print(f'Req {i+1}: {end:.4f}s | Status: {r.status_code}')
    except: pass

if len(latencies) > 1:
    print(f'--- RESULTADOS OPERACIONAIS ---')
    print(f'Média: {statistics.mean(latencies):.4f}s')
    print(f'Jitter: {statistics.stdev(latencies):.4f}s') # Validação de estabilidade

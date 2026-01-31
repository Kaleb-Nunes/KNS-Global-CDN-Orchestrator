import matplotlib.pyplot as plt

labels = ['Sem Protocolo 09', 'Com Protocolo 09']
latencies = [6.9, 0.06]

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(labels, latencies, color=['#ff4444', '#00ff00'])

ax.set_title('Redução de Latência - KNS Global CDN', fontsize=14, color='white')
ax.set_ylabel('Segundos (Tempo de Resposta)', color='white')

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, f'{yval}s', va='bottom', ha='center', color='white', fontweight='bold')

plt.savefig('assets/latency-comparison.png', transparent=True)
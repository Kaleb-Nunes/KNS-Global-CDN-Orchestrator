import matplotlib.pyplot as plt
import numpy as np

# --- DADOS DE ELITE ---
labels = ['Legado (Lento)', 'Protocolo 09 (KNS)']
values = [6.9, 0.06]
colors = ['#FF2A2A', '#00FF7F'] # Vermelho Alerta vs Verde Matrix

# --- ESTILO DARK MODE PREMIUM ---
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6))

# Ajuste de cor de fundo para combinar com GitHub Dark
fig.patch.set_facecolor('#0d1117') 
ax.set_facecolor('#0d1117')

# --- BARRAS ---
x = np.arange(len(labels))
width = 0.5
bars = ax.bar(x, values, width, color=colors, edgecolor='none')

# --- TEXTOS E RÓTULOS ---
# Título que vende
ax.set_title('ROI: Comparativo de Latência Global', fontsize=20, fontweight='bold', color='white', pad=25)

# Remover bordas feias (Clean Design)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#30363d')

# Eixos
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=14, fontweight='bold')
ax.tick_params(axis='y', colors='gray', labelsize=10)
ax.grid(axis='y', color='#30363d', linestyle='--', alpha=0.5)

# --- O DETALHE QUE GANHA O JOGO (VALORES) ---
for bar in bars:
    height = bar.get_height()
    # Se for o valor alto (6.9s)
    if height > 1:
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.1, 
                f'{height}s', ha='center', va='bottom', fontsize=18, fontweight='bold', color='#FF2A2A')
    # Se for o valor baixo (0.06s) - Destacar a vitória
    else:
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.2, 
                f'{height}s\n( 115x Mais Rápido)', ha='center', va='bottom', fontsize=18, fontweight='bold', color='#00FF7F')

plt.tight_layout()

# Salvar sobrescrevendo o arquivo anterior para o README atualizar sozinho
plt.savefig('assets/latency-comparison.png', dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
print(" Gráfico de Elite gerado: assets/latency-comparison.png")
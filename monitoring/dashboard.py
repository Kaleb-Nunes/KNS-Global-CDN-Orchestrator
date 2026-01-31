import json
import os

def generate_html():
    with open('monitoring/nodes_health.json', 'r') as f:
        nodes = json.load(f)
    
    html_content = f"""
    <html>
    <head>
        <title>KNS Global CDN - Real-Time Status</title>
        <style>
            body {{ font-family: sans-serif; background: #121212; color: white; text-align: center; }}
            .container {{ display: flex; justify-content: center; gap: 20px; margin-top: 50px; }}
            .card {{ padding: 20px; border-radius: 10px; border: 2px solid #333; width: 250px; }}
            .online {{ border-color: #00ff00; background: #003300; }}
            .offline {{ border-color: #ff0000; background: #330000; }}
            .latency {{ font-size: 0.8em; color: #aaa; }}
        </style>
    </head>
    <body>
        <h1> KNS Global Dashboard (Protocolo 09)</h1>
        <div class="container">
    """
    
    for name, data in nodes.items():
        status_class = "online" if data['status'] == 'online' else "offline"
        html_content += f"""
            <div class="card {status_class}">
                <h3>{name}</h3>
                <p>Status: {data['status'].upper()}</p>
                <p>IP: {data['ip']}</p>
                <p class="latency">Latência: {data['latency']}s</p>
            </div>
        """
        
    html_content += "</div></body></html>"
    
    with open('monitoring/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(" Dashboard atualizado com sucesso em monitoring/index.html")

if __name__ == "__main__":
    generate_html()
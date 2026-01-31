import json
import os

HEALTH_FILE = 'monitoring/nodes_health.json'

def load_nodes():
    # Fallback caso o arquivo de monitoramento ainda não exista
    if not os.path.exists(HEALTH_FILE):
        return {
            "SA-East-1": {"ip": "191.x.x.1", "status": "online", "latency": 0.06},
            "US-East-1": {"ip": "34.x.x.2", "status": "online", "latency": 0.12}
        }
    with open(HEALTH_FILE, 'r') as f:
        return json.load(f)

def resolve_dns(user_region):
    nodes = load_nodes()
    if nodes.get(user_region) and nodes[user_region]["status"] == "online":
        return nodes[user_region]["ip"]
    else:
        # Failover Automático: Busca o melhor nó online disponível
        available = {k: v for k, v in nodes.items() if v["status"] == "online"}
        if not available: return "127.0.0.1" # Safe mode
        best_node = min(available, key=lambda x: available[x]["latency"])
        return available[best_node]["ip"]

print(f" [DNS DINÂMICO] Resolução para EU-West-1: {resolve_dns('EU-West-1')}")
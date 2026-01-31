import json

nodes = {
    "SA-East-1": {"ip": "191.x.x.1", "status": "online", "latency": 0.06},
    "US-East-1": {"ip": "34.x.x.2", "status": "online", "latency": 0.12},
    "EU-West-1": {"ip": "52.x.x.3", "status": "offline", "latency": 0.99}
}

def resolve_dns(user_region):
    if nodes[user_region]["status"] == "online":
        return nodes[user_region]["ip"]
    else:
        available_nodes = {k: v for k, v in nodes.items() if v["status"] == "online"}
        best_node = min(available_nodes, key=lambda x: available_nodes[x]["latency"])
        return nodes[best_node]["ip"]

print(f" [DNS Global] Direcionando utilizador de EU-West-1 para: {resolve_dns('EU-West-1')}")
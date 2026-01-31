import re
def analyze_cdn_logs(log):
    return 'ALERTA IA' if re.search(r' 500 ', log) else 'Normal'
print(analyze_cdn_logs('192.168.1.1 - 500'))
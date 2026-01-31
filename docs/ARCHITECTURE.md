# Arquitetura Técnica - KNS Global CDN (Protocolo 09)

##  Regras de Negócio
1. **Independência de Cloud:** Operação exclusiva em hardware Bare-Metal para evitar vendor lock-in.
2. **Segurança de Borda:** Implementação obrigatória de Hardening sistêmico antes da entrada em produção.
3. **Eficiência de Performance:** Uso de Direct I/O e Sendfile para maximizar o throughput de rede.

##  Parâmetros Técnicos (Tuning)
| Parâmetro | Valor | Objetivo |
| :--- | :--- | :--- |
| worker_connections | 16384 | Suporte a alto volume de usuários simultâneos |
| sendfile | on | Transferência direta disco-NIC sem overhead de CPU |
| directio | 512 | Otimização para leitura de arquivos grandes |

##  Inteligência de Monitoramento
Utilização do 'log_analyzer_ai.py' para análise preditiva de anomalias e isolamento automático de nós instáveis.

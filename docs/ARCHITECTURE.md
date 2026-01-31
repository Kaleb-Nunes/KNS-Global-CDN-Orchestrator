# Arquitetura Técnica - KNS Global CDN (Protocolo 09)

##  Regras de Negócio
1. **Independência de Cloud:** Operação exclusiva em Bare-Metal para evitar vendor lock-in.
2. **Segurança de Borda:** Hardening obrigatório (Firewall/Kernel) antes da produção.
3. **Eficiência:** Uso de Direct I/O e Sendfile para performance bruta.

##  Parâmetros Técnicos (Tuning)
| Parâmetro | Valor | Objetivo |
| :--- | :--- | :--- |
| worker_connections | 16384 | Alta densidade de utilizadores |
| sendfile | on | Offload de CPU na entrega de ficheiros |
| directio | 512 | Otimização para streaming de média |

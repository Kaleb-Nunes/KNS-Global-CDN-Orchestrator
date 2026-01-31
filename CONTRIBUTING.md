# Guia de Manutenção e Evolução

Para garantir a estabilidade do Protocolo 09, seguimos este fluxo de trabalho:

1. **Desenvolvimento em Branch:** Nunca alteramos a 'main' diretamente.
2. **Validação Operacional:** Todo novo código deve passar pelo 'stress_test.py' e reportar métricas de Jitter aceitáveis.
3. **Documentação de PR:** Cada Pull Request deve explicar o valor de negócio da alteração.
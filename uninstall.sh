#!/bin/bash

echo "⚠️ Isso irá remover o ambiente WEBER-DDoS e todos os logs gerados."
read -p "Deseja continuar? (s/n): " CONFIRM

if [[ "$CONFIRM" != "s" ]]; then
    echo "❌ Cancelado."
    exit 0
fi

rm -rf WEBER-DDoS logs
echo "🧼 Ambiente removido com sucesso."

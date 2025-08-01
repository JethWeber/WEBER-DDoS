#!/bin/bash

# Caminho do ambiente virtual
VENV_DIR="$(dirname "$0")/WEBER-DDoS"

# Verifica se o ambiente existe
if [ ! -d "$VENV_DIR" ]; then
    echo "❌ Ambiente virtual não encontrado. Execute './install.sh' primeiro."
    exit 1
fi

# Ativa o ambiente e executa a ferramenta
source "$VENV_DIR/bin/activate"
weber

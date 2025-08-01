#!/bin/bash

echo "🔧 Iniciando instalação do WEBER-DDoS..."

# Caminho do projeto
PROJECT_DIR="$(dirname "$0")"
PACKAGE_DIR="$PROJECT_DIR/weber-ddos"
VENV_DIR="$PROJECT_DIR/WEBER-DDoS"

# Verifica se o ambiente já existe
if [ -d "$VENV_DIR" ]; then
    echo "⚠️ Ambiente virtual já existe em '$VENV_DIR'. Pulando criação..."
else
    echo "📦 Criando ambiente virtual..."
    python3 -m venv "$VENV_DIR"
fi

# Ativa o ambiente virtual
source "$VENV_DIR/bin/activate"

# Instala o pacote
echo "🚀 Instalando o pacote WEBER-DDoS..."
pip install "$PACKAGE_DIR"

# Mensagem final
echo ""
echo "✅ Instalação concluída com sucesso!"
echo "Para iniciar a ferramenta, execute:"
echo ""
echo "source WEBER-DDoS/bin/activate && weber"
echo ""
echo "📘 Dica: use './run.sh' para facilitar o uso diário."
echo "⚠️ Esta ferramenta é para fins educacionais em ambientes controlados."

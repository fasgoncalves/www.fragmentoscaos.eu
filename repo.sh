#!/bin/bash

# ⚠️ CONFIGURA AQUI O TEU REPOSITÓRIO:
REPO_URL="https://github.com/fasgoncalves/www.fragmentoscaos.eu.git"
BRANCH="main"

echo "⚠️ Isto irá remover TODO o histórico Git local e forçar o push para $REPO_URL na branch $BRANCH"

# Confirmação
read -p "Desejas continuar? (s/n): " CONFIRMA
if [[ "$CONFIRMA" != "s" ]]; then
    echo "Operação cancelada."
    exit 1
fi

# Apagar e reiniciar Git
rm -rf .git
git init
git remote add origin "$REPO_URL"
git checkout -b "$BRANCH"

# Adicionar e commitar todos os ficheiros
git add .
git commit -m "Reset completo do repositório"

# Push forçado para o remoto
git push --force origin "$BRANCH"

echo "✅ Repositório substituído com sucesso!"

#!/bin/bash
# =============================================================================
# IA para Todos — Script de Inicialização do Repositório
# LABRIOT (UTFPR) + Multicortex
# =============================================================================
#
# USO:
#   chmod +x setup-repo.sh
#   ./setup-repo.sh
#
# Este script configura o repositório local para contribuição e cria
# arquivos .gitkeep nas pastas vazias (necessário para o Git rastrear
# diretórios sem arquivos).
# =============================================================================

set -e

echo ""
echo "╔═══════════════════════════════════════════════════════╗"
echo "║           IA para Todos — Setup do Repositório        ║"
echo "║         LABRIOT (UTFPR) + Multicortex                 ║"
echo "╚═══════════════════════════════════════════════════════╝"
echo ""

# Criar .gitkeep em todas as pastas de recursos vazias
echo "📁 Criando marcadores para diretórios vazios..."

DIRS=(
  "anos-iniciais/1-ano/recursos"
  "anos-iniciais/2-ano/recursos"
  "anos-iniciais/3-ano/recursos"
  "anos-iniciais/4-ano/recursos"
  "anos-iniciais/5-ano/recursos"
  "anos-finais/6-ano/recursos"
  "anos-finais/7-ano/recursos"
  "anos-finais/8-ano/recursos"
  "anos-finais/9-ano/recursos"
  "recursos-professores/slides-prontos"
  "recursos-professores/planos-de-aula"
  "temas-transversais/privacidade-e-lgpd"
  "temas-transversais/combate-fake-news"
  "temas-transversais/ia-e-meio-ambiente"
  "temas-transversais/inclusao-digital"
  "ferramentas"
)

for dir in "${DIRS[@]}"; do
  mkdir -p "$dir"
  touch "$dir/.gitkeep"
  echo "  ✓ $dir"
done

echo ""
echo "✅ Setup concluído!"
echo ""
echo "📋 Próximos passos:"
echo "   1. git init (se ainda não inicializado)"
echo "   2. git add ."
echo "   3. git commit -m 'feat: estrutura inicial do repositório IA para Todos'"
echo "   4. git remote add origin https://github.com/ItamarIliuk/ia-para-todos.git"
echo "   5. git push -u origin main"
echo ""
echo "💚 Bom trabalho! O conhecimento é livre."

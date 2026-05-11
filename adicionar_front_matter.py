#!/usr/bin/env python3
"""
Script: adicionar_front_matter.py
Adiciona front matter Jekyll em todos os arquivos .md do repositório
IA para Todos — LABRIOT/UTFPR

Uso: python adicionar_front_matter.py
Execute na raiz do repositorio local do GitHub
"""

import os
import re
import pathlib

# ─── Configurações ────────────────────────────────────────────────────────────

# Caminho raiz do repositório (onde este script está)
REPO_ROOT = pathlib.Path(__file__).parent

# Arquivos a ignorar completamente
IGNORAR = {
    "README.md",        # Já é a página inicial do GitHub
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "CHANGELOG.md",
    "CITATION.cff",
}

# ─── Mapeamentos de navegação ─────────────────────────────────────────────────

# Títulos amigáveis para nomes de pastas/arquivos
TITULOS_ANOS = {
    "1-ano": "1º Ano — O que é IA?",
    "2-ano": "2º Ano — Jogos e Algoritmos",
    "3-ano": "3º Ano — Como a IA Vê",
    "4-ano": "4º Ano — IA que Lê e Escreve",
    "5-ano": "5º Ano — Criando com IA",
    "6-ano": "6º Ano — Dados e Viés",
    "7-ano": "7º Ano — Privacidade Digital",
    "8-ano": "8º Ano — Fake News e Deepfakes",
    "9-ano": "9º Ano — Ética e Futuro",
}

TITULOS_ATIVIDADES = {
    # 1º ano
    "ativ-01-o-assistente-da-turma":      "Ativ. 01 — O Assistente da Turma",
    "ativ-02-maquina-aprende-cores":      "Ativ. 02 — A Máquina que Aprende Cores",
    "ativ-03-quem-ensinou-o-computador":  "Ativ. 03 — Quem Ensinou o Computador?",
    "ativ-04-ia-no-caminho-escola":       "Ativ. 04 — A IA no Caminho para a Escola",
    "ativ-05-quando-maquina-erra":        "Ativ. 05 — Quando a Máquina Erra",
    # 2º ano
    "ativ-01-robo-obediente":             "Ativ. 01 — O Robô Obediente",
    "ativ-02-regras-do-inimigo":          "Ativ. 02 — As Regras do Inimigo",
    "ativ-03-programando-com-setas":      "Ativ. 03 — Programando com Setas",
    "ativ-04-ia-que-aprende-jogar":       "Ativ. 04 — A IA que Aprende a Jogar",
    "ativ-05-criando-regras":             "Ativ. 05 — Criando Nossas Próprias Regras",
    # 3º ano
    "ativ-01-como-computador-ve-foto":    "Ativ. 01 — Como o Computador Vê uma Foto?",
    "ativ-02-treinando-ia-objetos":       "Ativ. 02 — Treinando IA para Reconhecer Objetos",
    "ativ-03-reconhecimento-facial":      "Ativ. 03 — Reconhecimento Facial",
    "ativ-04-ia-ve-errado":              "Ativ. 04 — Quando a IA Vê Errado",
    "ativ-05-arte-com-ia":               "Ativ. 05 — Arte com IA",
    # 4º ano
    "ativ-01-complete-a-frase":           "Ativ. 01 — Complete a Frase",
    "ativ-02-conversando-chatbot":        "Ativ. 02 — Conversando com Chatbots",
    "ativ-03-humano-ou-maquina":          "Ativ. 03 — Humano ou Máquina?",
    "ativ-04-ia-nao-entende-piadas":      "Ativ. 04 — A IA Não Entende Piadas",
    "ativ-05-escrevendo-com-ia":          "Ativ. 05 — Escrevendo com IA",
    # 5º ano
    "ativ-01-historias-com-ia":           "Ativ. 01 — Histórias com IA",
    "ativ-02-arte-gerada-ia":            "Ativ. 02 — Arte Gerada por IA",
    "ativ-03-musica-e-ia":               "Ativ. 03 — Música e IA",
    "ativ-04-direitos-autorais-ia":       "Ativ. 04 — Direitos Autorais na Era da IA",
    "ativ-05-projeto-final":             "Ativ. 05 — Projeto Final",
    # 6º ano
    "ativ-01-o-que-sao-dados":           "Ativ. 01 — O que São Dados?",
    "ativ-02-vies-em-dados":             "Ativ. 02 — Viés em Dados",
    "ativ-03-coletando-dados":           "Ativ. 03 — Coletando Dados com Responsabilidade",
    "ativ-04-mapa-do-vies-brasil":       "Ativ. 04 — Mapa do Viés no Brasil",
    "ativ-05-ia-mais-justa":             "Ativ. 05 — Propondo uma IA Mais Justa",
    # 7º ano
    "ativ-01-quanto-vale-em-dados":      "Ativ. 01 — Quanto Você Vale em Dados?",
    "ativ-02-rastro-digital":            "Ativ. 02 — Rastreando o Rastro Digital",
    "ativ-03-lgpd-seus-direitos":        "Ativ. 03 — A LGPD e Seus Direitos",
    "ativ-04-termos-de-servico":         "Ativ. 04 — Termos de Serviço",
    "ativ-05-guia-privacidade":          "Ativ. 05 — Guia de Privacidade",
    # 8º ano
    "ativ-01-o-que-e-deepfake":          "Ativ. 01 — O que é um Deepfake?",
    "ativ-02-detectives-fake-news":      "Ativ. 02 — Detetives de Fake News",
    "ativ-03-por-que-acreditamos":       "Ativ. 03 — Por que a Gente Acredita em Mentiras?",
    "ativ-04-fact-checking":             "Ativ. 04 — Fact-Checking com Ferramentas",
    "ativ-05-campanha-desinformacao":    "Ativ. 05 — Campanha Contra Desinformação",
    # 9º ano
    "ativ-01-ia-no-tribunal":            "Ativ. 01 — A IA no Tribunal",
    "ativ-02-regulando-a-ia":            "Ativ. 02 — Regulando a IA",
    "ativ-03-ia-e-minha-profissao":      "Ativ. 03 — IA e Minha Profissão",
    "ativ-04-habilidades-humanas":       "Ativ. 04 — Habilidades que a IA Não Tem",
    "ativ-05-projeto-final-comunidade":  "Ativ. 05 — Projeto Final: IA para Minha Comunidade",
}

TITULOS_RECURSOS = {
    "modulo-01-fundamentos-ia":                  "Módulo 1 — Fundamentos de IA",
    "modulo-02-conduzindo-atividades":            "Módulo 2 — Conduzindo Atividades",
    "modulo-03-ia-como-ferramenta-pedagogica":    "Módulo 3 — IA como Ferramenta Pedagógica",
    "modulo-04-implementacao-comunidade":         "Módulo 4 — Implementação e Comunidade",
    "rubrica-geral":                              "Rubrica Geral de Avaliação",
    "rubricas-por-ciclo":                         "Rubricas por Ciclo",
    "planos-bimestrais-1ao9ano":                  "Planos Bimestrais — 1º ao 9º Ano",
    "exercicios-fixacao-1ano":  "Exercícios de Fixação — 1º Ano",
    "exercicios-fixacao-2ano":  "Exercícios de Fixação — 2º Ano",
    "exercicios-fixacao-3ano":  "Exercícios de Fixação — 3º Ano",
    "exercicios-fixacao-4ano":  "Exercícios de Fixação — 4º Ano",
    "exercicios-fixacao-5ano":  "Exercícios de Fixação — 5º Ano",
    "exercicios-fixacao-6ano":  "Exercícios de Fixação — 6º Ano",
    "exercicios-fixacao-7ano":  "Exercícios de Fixação — 7º Ano",
    "exercicios-fixacao-8ano":  "Exercícios de Fixação — 8º Ano",
    "exercicios-fixacao-9ano":  "Exercícios de Fixação — 9º Ano",
}

TITULOS_DOCS = {
    "guia-professores":    "Guia para Professores",
    "guia-pais":           "Guia para Pais e Responsáveis",
    "lgpd-criancas":       "LGPD e Crianças",
    "como-usar-pendrive":  "Como Usar o Pendrive Multicortex",
    "como-contribuir":     "Como Contribuir",
}

TITULOS_TEMAS = {
    "privacidade-e-lgpd":   "Privacidade e LGPD",
    "combate-fake-news":    "Combate à Desinformação",
    "ia-e-meio-ambiente":   "IA e Meio Ambiente",
    "inclusao-digital":     "Inclusão Digital",
}

# ─── Funções principais ───────────────────────────────────────────────────────

def ja_tem_front_matter(conteudo: str) -> bool:
    """Verifica se o arquivo já tem front matter Jekyll."""
    return conteudo.strip().startswith("---")


def extrair_titulo_do_md(conteudo: str) -> str:
    """Extrai o primeiro título H1 do arquivo."""
    for linha in conteudo.splitlines():
        linha = linha.strip()
        if linha.startswith("# "):
            # Remove emojis e limpa o título
            titulo = linha[2:].strip()
            titulo = re.sub(r"[^\w\s\-\—\.º\?!,\(\)áéíóúâêîôûãõàèìòùçÁÉÍÓÚÂÊÎÔÛÃÕÀÈÌÒÙÇ]", "", titulo)
            return titulo.strip()
    return ""


def montar_front_matter(title: str, parent: str = "", grand_parent: str = "",
                         nav_order: int = 1, has_children: bool = False) -> str:
    """Monta o bloco de front matter."""
    linhas = ["---", f'title: "{title}"']
    if has_children:
        linhas.append("has_children: true")
    if grand_parent:
        linhas.append(f'grand_parent: "{grand_parent}"')
    if parent:
        linhas.append(f'parent: "{parent}"')
    linhas.append(f"nav_order: {nav_order}")
    linhas.append("---\n")
    return "\n".join(linhas)


def processar_arquivo(caminho: pathlib.Path, front_matter: str):
    """Adiciona front matter no início do arquivo."""
    conteudo = caminho.read_text(encoding="utf-8")

    if ja_tem_front_matter(conteudo):
        # Substitui front matter existente
        partes = conteudo.split("---", 2)
        if len(partes) >= 3:
            conteudo_novo = front_matter + partes[2].lstrip("\n")
        else:
            conteudo_novo = front_matter + conteudo
    else:
        conteudo_novo = front_matter + conteudo

    caminho.write_text(conteudo_novo, encoding="utf-8")
    return True


# ─── Lógica de decisão por caminho ───────────────────────────────────────────

def determinar_front_matter(caminho: pathlib.Path) -> str | None:
    """
    Determina o front matter correto baseado no caminho do arquivo.
    Retorna None se o arquivo deve ser ignorado.
    """
    partes = caminho.relative_to(REPO_ROOT).parts
    nome = caminho.stem  # nome sem extensão

    # Ignorar arquivos da lista
    if caminho.name in IGNORAR:
        return None

    # ── Raiz do repositório ──────────────────────────────────────────────────
    if len(partes) == 1:
        if nome == "index":
            return None  # já configurado pelo github-pages
        return None  # outros .md na raiz: ignorar

    # ── docs/ ────────────────────────────────────────────────────────────────
    if partes[0] == "docs":
        titulo = TITULOS_DOCS.get(nome, nome.replace("-", " ").title())
        fm = montar_front_matter(
            title=titulo,
            parent="Documentação",
            nav_order=list(TITULOS_DOCS.keys()).index(nome) + 1 if nome in TITULOS_DOCS else 99
        )
        return fm

    # ── temas-transversais/ ──────────────────────────────────────────────────
    if partes[0] == "temas-transversais":
        if len(partes) == 2 and nome == "README":
            return None  # README raiz da pasta: ignorar
        if len(partes) >= 2:
            pasta_tema = partes[1]
            titulo = TITULOS_TEMAS.get(pasta_tema, pasta_tema.replace("-", " ").title())
            fm = montar_front_matter(
                title=titulo,
                parent="Temas Transversais",
                nav_order=list(TITULOS_TEMAS.keys()).index(pasta_tema) + 1 if pasta_tema in TITULOS_TEMAS else 99
            )
            return fm

    # ── recursos-professores/ ───────────────────────────────────────────────
    if partes[0] == "recursos-professores":
        if len(partes) == 2:
            return None  # READMEs das subpastas: ignorar

        if "formacao-continuada" in partes:
            titulo = TITULOS_RECURSOS.get(nome, nome.replace("-", " ").title())
            idx = list(TITULOS_RECURSOS.keys()).index(nome) + 1 if nome in TITULOS_RECURSOS else 99
            return montar_front_matter(
                title=titulo,
                parent="Formação Continuada",
                grand_parent="Recursos para Professores",
                nav_order=idx
            )

        if "rubricas-avaliacao" in partes:
            titulo = TITULOS_RECURSOS.get(nome, nome.replace("-", " ").title())
            return montar_front_matter(
                title=titulo,
                parent="Avaliação",
                grand_parent="Recursos para Professores",
                nav_order=1 if "geral" in nome else 2
            )

        if "planos-de-aula" in partes:
            titulo = TITULOS_RECURSOS.get(nome, "Planos de Aula")
            return montar_front_matter(
                title=titulo,
                parent="Planos de Aula",
                grand_parent="Recursos para Professores",
                nav_order=1
            )

        if "slides-prontos" in partes and nome == "README":
            return None

        return None

    # ── anos-iniciais/ e anos-finais/ ────────────────────────────────────────
    if partes[0] in ("anos-iniciais", "anos-finais"):
        ciclo_label = "Anos Iniciais (1º ao 5º)" if partes[0] == "anos-iniciais" else "Anos Finais (6º ao 9º)"

        # README do ano: ex. anos-iniciais/1-ano/README.md
        if len(partes) == 3 and nome == "README":
            ano_pasta = partes[1]
            titulo = TITULOS_ANOS.get(ano_pasta, ano_pasta)
            nav = int(ano_pasta.split("-")[0])
            return montar_front_matter(
                title=titulo,
                parent=ciclo_label,
                nav_order=nav,
                has_children=True
            )

        # Exercícios: anos-iniciais/1-ano/exercicios/exercicios-fixacao-1ano.md
        if "exercicios" in partes:
            ano_pasta = partes[1]
            ano_label = TITULOS_ANOS.get(ano_pasta, ano_pasta)
            titulo = TITULOS_RECURSOS.get(nome, f"Exercícios — {ano_label}")
            return montar_front_matter(
                title=titulo,
                parent=ano_label,
                grand_parent=ciclo_label,
                nav_order=90
            )

        # Atividades: anos-iniciais/1-ano/atividades/ativ-XX-nome/para-o-professor.md
        if "atividades" in partes and len(partes) >= 5:
            ano_pasta  = partes[1]
            ativ_pasta = partes[3]
            ano_label  = TITULOS_ANOS.get(ano_pasta, ano_pasta)
            ativ_label = TITULOS_ATIVIDADES.get(ativ_pasta, ativ_pasta.replace("-", " ").title())

            if nome == "para-o-professor":
                titulo = f"👩‍🏫 Roteiro do Professor"
                nav = 1
            elif nome == "folha-do-aluno":
                titulo = f"📝 Folha do Aluno"
                nav = 2
            else:
                titulo = nome.replace("-", " ").title()
                nav = 3

            return montar_front_matter(
                title=titulo,
                parent=ativ_label,
                grand_parent=ano_label,
                nav_order=nav
            )

        # README de atividade: anos-iniciais/1-ano/atividades/ativ-XX/README.md
        if "atividades" in partes and len(partes) == 5 and nome == "README":
            ano_pasta  = partes[1]
            ativ_pasta = partes[3]
            ano_label  = TITULOS_ANOS.get(ano_pasta, ano_pasta)
            ativ_label = TITULOS_ATIVIDADES.get(ativ_pasta, ativ_pasta.replace("-", " ").title())
            num = int(ativ_pasta.split("-")[1]) if ativ_pasta.split("-")[1].isdigit() else 99
            return montar_front_matter(
                title=ativ_label,
                parent=ano_label,
                grand_parent=ciclo_label,
                nav_order=num,
                has_children=True
            )

    return None


# ─── Execução principal ───────────────────────────────────────────────────────

def main():
    arquivos_md = sorted(REPO_ROOT.rglob("*.md"))
    processados = 0
    ignorados   = 0
    erros       = 0

    print(f"Repositório: {REPO_ROOT}")
    print(f"Total de arquivos .md encontrados: {len(arquivos_md)}\n")

    for caminho in arquivos_md:
        rel = caminho.relative_to(REPO_ROOT)

        try:
            fm = determinar_front_matter(caminho)
            if fm is None:
                print(f"  IGNORADO  {rel}")
                ignorados += 1
                continue

            processar_arquivo(caminho, fm)
            print(f"  OK        {rel}")
            processados += 1

        except Exception as e:
            print(f"  ERRO      {rel} → {e}")
            erros += 1

    print(f"\n{'='*60}")
    print(f"  Processados : {processados}")
    print(f"  Ignorados   : {ignorados}")
    print(f"  Erros       : {erros}")
    print(f"{'='*60}")
    print("\nPronto! Agora faça: git add . && git commit -m 'fix: front matter Jekyll' && git push")


if __name__ == "__main__":
    main()

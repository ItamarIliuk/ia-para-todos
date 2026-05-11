---
title: "👩‍🏫 Roteiro do Professor"
grand_parent: "3º Ano — Como a IA Vê"
parent: "Ativ. 02 — Treinando IA para Reconhecer Objetos"
nav_order: 1
---
# 👩‍🏫 Para o Professor — Atividade 02: "Treinando uma IA para Reconhecer Objetos"

**Ano:** 3º ano | **Duração:** 50 minutos | **Recursos:** Computador com câmera + internet | **Offline:** ⚠️ Requer internet

---

## 📋 Resumo Rápido

> Com o Teachable Machine (Google), a turma treina sua própria IA para reconhecer objetos usando a câmera. Cada grupo coleta exemplos, treina o modelo e testa — vivenciando o ciclo completo de machine learning em 50 minutos.

---

## 🛒 Pré-requisitos

- Computador com câmera (1 por grupo de 4-5 alunos) ou 1 computador com projetor para demonstração
- Acesso a `teachablemachine.withgoogle.com` (sem conta, sem instalação)
- Internet (carrega em ~1 minuto, depois funciona localmente)

---

## ⏱️ Roteiro

### 🔵 Abertura (8 min)

> *"Hoje vocês vão ser cientistas de IA de verdade. Vão treinar uma IA do zero para reconhecer objetos. O mesmo processo — em escala muito maior — que a Google, a Apple e outras empresas usam."*

Acesse `teachablemachine.withgoogle.com` e mostre a interface. Clique em "Começar" → "Projeto de imagem" → "Modelo de imagem padrão".

---

### 🟡 Desenvolvimento — Treinamento (25 min)

**Configuração do experimento:**

Cada grupo vai treinar a IA para distinguir entre **3 objetos** (exemplos: caneta, borracha e apontador; ou mão aberta, mão fechada e punho).

**Etapas:**

1. **Nomeie as classes** (ex.: "Caneta", "Borracha", "Nada")
2. **Colete exemplos** — segure cada objeto na câmera e grave 30-50 imagens de cada classe
3. **Treine** — clique em "Treinar Modelo" e aguarde (~30 segundos)
4. **Teste** — mostre os objetos e veja a IA classificar em tempo real

**Experimentos extras (se der tempo):**

- "E se eu mostrar um objeto que a IA nunca viu?" (ex.: tesoura)
- "E se eu mostrar o objeto de um ângulo diferente?"
- "E se eu colocar uma fita sobre o objeto?"

---

### 🟢 Análise e Discussão (12 min)

Reunir os grupos e debater:
- "O que aconteceu quando vocês mostraram poucos exemplos?"
- "E quando mostraram o objeto de lado?"
- "O que a IA estava 'aprendendo' na verdade?"

> *"A IA não aprendeu o que é uma caneta — ela aprendeu como canetas apareceram nas fotos que vocês deram. Por isso, pequenas mudanças de ângulo ou iluminação podem confundi-la."*

---

### 🔴 Caixa de Ética (5 min)

> *"Vocês treinaram a IA com objetos da sala. E se alguém treinasse uma IA para reconhecer rostos de crianças sem a permissão dos pais? Quais seriam os riscos?"*

---

## 📝 Avaliação

- ✅ O grupo conseguiu treinar um modelo funcional?
- ✅ Testou os limites da IA (ângulos, luz, objetos novos)?
- ✅ Conseguiu explicar por que a IA acertou ou errou?

---

*LABRIOT — UTFPR | CC BY-NC-SA 4.0*

---
---

# 👩‍🏫 Para o Professor — Atividade 03: "Reconhecimento Facial — Incrível e Perigoso"

**Ano:** 3º ano | **Duração:** 50 minutos | **Recursos:** Nenhum | **Offline:** ✅ Total

---

## 📋 Resumo Rápido

> Uma das aulas mais importantes do 3º ano: reconhecimento facial é uma das aplicações de visão mais poderosas — e mais controversas. A turma analisa benefícios e riscos a partir de casos concretos.

**⚠️ Atenção:** Nunca use fotos reais de alunos nesta aula. Use apenas exemplos genéricos ou imagens de ilustração.

---

## ⏱️ Roteiro

### 🔵 Abertura — "O Celular que Sabe quem você é" (10 min)

> *"Quando você pega o celular de alguém para olhar, às vezes ele pede o código de segurança. Por quê? Porque o rosto da outra pessoa não é igual ao de quem cadastrou. A câmera usou reconhecimento facial com IA para saber que não é você."*

Perguntas de levantamento:
- Quem tem celular em casa que desbloqueia pelo rosto?
- O celular já confundiu alguém da família com outra pessoa?

---

### 🟡 Desenvolvimento — Casos Bons e Casos Preocupantes (25 min)

Apresente os casos em dois grupos — discuta cada um por 2-3 minutos:

**Casos em que o reconhecimento facial AJUDA:**

| Caso | Por que ajuda? |
|------|---------------|
| Desbloquear celular | Segurança pessoal sem precisar de senha |
| Encontrar pessoas desaparecidas | Polícia pode identificar em câmeras |
| Acessibilidade | Pessoas que não podem digitar usam o rosto |
| Rastrear golpistas | Bancos identificam fraudes em tempo real |

**Casos que geram PREOCUPAÇÃO:**

| Caso | Por que preocupa? |
|------|-----------------|
| Câmeras em toda a cidade | Governo pode saber onde você está sempre |
| Reconhecimento em eventos públicos | Manifestações políticas podem ser monitoradas |
| Erro na identificação (falso positivo) | Pessoa inocente pode ser presa |
| Dados de crianças coletados sem consentimento | Viola privacidade e LGPD |

**Caso brasileiro real (adapte para a faixa etária):**

> *"Em 2023, um sistema de reconhecimento facial no Brasil identificou incorretamente um homem negro como suspeito de um crime que ele não cometeu — e ele foi preso por engano. O sistema errou porque foi treinado com poucos exemplos de pessoas negras."*

Pergunte: *"Por que esse sistema errou mais com esse homem do que erraria com outras pessoas?"*

---

### 🟢 Votação — "Você aprovaria?" (10 min)

Para cada situação, a turma vota: **APROVARIA** / **NÃO APROVARIA** / **DEPENDE**

1. Reconhecimento facial para entrar na escola em vez de carteirinha
2. Câmeras com reconhecimento facial em todas as ruas da cidade
3. Reconhecimento facial para liberar acesso à biblioteca escolar
4. IA que identifica emoções dos alunos durante a aula (detecta se estão entediados)

Para cada votação: "Quem votou diferente explica por quê?"

---

### 🔴 Caixa de Ética (5 min)

> *"Vocês têm o direito à privacidade — inclusive o direito de andar na rua sem que uma câmera saiba quem vocês são. Esse direito está na Constituição brasileira e na LGPD. Como cidadãos, vocês podem cobrar que esse direito seja respeitado — inclusive da tecnologia."*

---

*LABRIOT — UTFPR | CC BY-NC-SA 4.0*

---
---

# 👩‍🏫 Para o Professor — Atividade 04: "Quando a IA Vê Errado"

**Ano:** 3º ano | **Duração:** 50 minutos | **Recursos:** Imagens impressas ou projetor | **Offline:** ✅ Total

---

## 📋 Resumo Rápido

> Ilusões de ótica, imagens ambíguas e exemplos de erros reais de visão computacional revelam os limites da IA. Uma aula que desenvolve pensamento crítico sobre confiança em sistemas automatizados.

---

## 🛒 Materiais

Imprima (ou projete) as seguintes categorias de imagens:
1. Ilusões de ótica clássicas (cubo de Necker, vestido azul/dourado, pato-coelho)
2. Exemplos de IA confundindo objetos (banana de plástico vs. real, gato dormindo vs. pãozinho)
3. Casos reais de falha de visão computacional (opcional, se encontrar imagens apropriadas)

---

## ⏱️ Roteiro

### 🔵 Abertura — Ilusões de Ótica (10 min)

Mostre ilusões de ótica e deixe a turma discutir.

> *"O cérebro humano também 'vê errado' às vezes! Mas quando um humano erra, geralmente percebe logo. Quando a IA erra... ela pode nem saber que errou — e continuar confiante."*

---

### 🟡 Galeria de Erros da IA (20 min)

Apresente os casos um a um. Para cada um, pergunte:

1. "O que a IA 'viu'?"
2. "O que era de verdade?"
3. "Por que ela errou?"
4. "Quais consequências esse erro poderia ter?"

**Casos clássicos:**
- IA classificou uma bolsa de pão como um cachorro (pelo pelo da alça)
- IA não reconheceu uma pessoa com óculos escuros
- IA confundiu neve branca com papel em branco
- IA de carro autônomo não reconheceu um caminhão branco contra o céu claro

---

### 🟢 Experimento com Teachable Machine (15 min — se tiver computador)

Retome o modelo treinado na aula anterior e teste propositalmente situações que causam erro:
- Mude a iluminação
- Mostre o objeto de lado
- Cubra metade do objeto

> *"Encontrar os erros da IA é tão importante quanto encontrar os acertos. Engenheiros chamam isso de 'teste adversarial' — testar justamente onde a IA pode falhar."*

---

### 🔴 Caixa de Ética (5 min)

> *"Se um carro autônomo errar e atropelar alguém, quem tem culpa — o carro, o fabricante, ou quem vendeu o carro dizendo que era seguro? Como a gente garante que sistemas de IA sejam suficientemente testados antes de ser usados em situações de risco?"*

---

*LABRIOT — UTFPR | CC BY-NC-SA 4.0*

---
---

# 👩‍🏫 Para o Professor — Atividade 05: "Arte com IA"

**Ano:** 3º ano | **Duração:** 50 minutos | **Recursos:** Computador opcional | **Offline:** ⚠️ Parcial

---

## 📋 Resumo Rápido

> Atividade criativa de encerramento do 3º ano: usando a IA como ferramenta de expressão artística. Os alunos criam obras usando ferramentas de geração de imagem (com supervisão) ou fazem o exercício analógico de "instruções para a IA" no papel.

---

## ⏱️ Roteiro

### 🔵 Abertura — "Isso é arte?" (8 min)

Mostre imagens criadas por IA (sem revelar que são de IA primeiro). Pergunte: "O que vocês acham dessa arte? Quem criou?"

Após a revelação: *"Uma IA gerou essas imagens. Alguém deu uma instrução — como 'pôr do sol sobre a floresta amazônica em estilo aquarela' — e a IA criou. Isso é arte? Quem é o artista — a pessoa ou a máquina?"*

---

### 🟡 Desenvolvimento — "Escrevendo para a IA" (20 min)

**Versão online:** Acesse `labs.google/fx/tools/image-fx` (gratuito, sem conta necessária) e deixe grupos escreverem prompts (instruções) para gerar imagens. **Atenção:** Não use fotos de alunos, não escreva nomes pessoais.

**Versão offline:** Em papel, cada aluno escreve uma "instrução para a IA" extremamente detalhada:
```
"Crie uma imagem de:
- Onde: _______________________
- O que tem: __________________
- Cores: ______________________
- Estilo (como um desenho de livro infantil / como fotografia / como pintura): ________
- Clima/emoção: ________________"
```
Depois, trocam com um colega que desenha a instrução. Comparam o resultado com o que o criador imaginava.

---

### 🟢 Galeria e Debate (12 min)

Expo rápida das obras. Para cada uma: quem é o autor — quem deu a instrução ou a IA?

---

### 🔴 Caixa de Ética + Encerramento do 3º Ano (10 min)

> *"Se uma IA aprende com milhões de obras de artistas humanos — sem pedir permissão — e depois cria arte parecida, isso é justo para os artistas originais? Quem deveria ser pago — quem deu a instrução, quem fez a IA, ou os artistas cujas obras foram usadas para treinar?"*

Fechamento do 3º ano:
> *"Vocês aprenderam como a IA vê o mundo — em pixels e números. Que ela pode ver incrível e errar feio. Que ela pode criar arte. E que há questões de privacidade, justiça e autoria que ainda não têm resposta. Essas perguntas estão esperando por vocês!"*

---

*LABRIOT — UTFPR | Profa. Dra. Itamar Iliuk (Coordenadora) | CC BY-NC-SA 4.0*

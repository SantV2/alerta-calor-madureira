# Alerta Calor Madureira

> Global Solution 2026.2 · CitizenTech · Engenharia de Software 1º ano · FIAP Rio de Janeiro

## Ficha da CitizenTech

| Campo | Resposta da equipe |
|---|---|
| **Nome da CitizenTech** | Alerta Calor Madureira |
| **Cidade e bairro** | Rio de Janeiro, Madureira |
| **Cidadão beneficiado** | Quem passa o dia na rua em Madureira, como trabalhadores ambulantes, pessoas que esperam ônibus e idosos, e convive com o calor extremo sem saber quando ele fica perigoso. |
| **Problema, em uma frase** | Moradores de Madureira não sabem quando o calor fica perigoso e não recebem um aviso simples para se proteger. |
| **Como funciona** | O sensor mede a temperatura, o Python classifica cada leitura em NORMAL, ATENÇÃO ou PERIGO e gera o aviso, e a página mostra ao cidadão o aviso em linguagem simples. |
| **O que cada parte faz** | veja a tabela abaixo |
| **Link do repositório** | [https://github.com/SantV2/alerta-calor-madureira] |
| **Indicador de impacto** | Percentual de leituras em alerta (ATENÇÃO + PERIGO) e número de avisos entregues, para estimar as horas de exposição ao calor que o cidadão consegue evitar. |
| **ODS conectados** | **ODS 3** (Saúde e Bem-Estar): o aviso ajuda a prevenir desidratação e insolação. **ODS 11** (Cidades e Comunidades Sustentáveis): dá ao bairro informação local para a população se proteger. **ODS 13** (Ação Contra a Mudança Global do Clima): ajuda a população a se adaptar ao calor extremo. |

### O que cada parte faz

| Parte | Disciplina | Pasta | O que faz |
|---|---|---|---|
| Lógica | Computational Thinking with Python | `python/` | Classifica as leituras de temperatura em NORMAL, ATENÇÃO (≥ 35 °C) e PERIGO (≥ 40 °C) e gera o aviso e o resumo do dia. |
| Matemática | Differentiated Problem Solving | `[pasta]` | [o cálculo que ajuda a decidir] |
| Sensor | Edge Computing & Computer Systems | `[pasta]` | Circuito que mede a temperatura e reage com as mesmas faixas do Python. |
| Interface | Front-end Design | `[pasta]` | Página que mostra ao cidadão a faixa atual e o aviso, com os mesmos textos do Python. |
| Experiência | Software & Total Experience Design | `[pasta]` | A jornada do cidadão e os requisitos que originaram as opções do menu. |
| Interação | Web Development | `[pasta]` | JavaScript da página, com a regra de decisão reescrita a partir do Python. |
| Pitch | Storytelling & Inspiração Empreendedora | — | [link do vídeo no YouTube] |

## Equipe

| Nome completo | RM |
|---|---|
| Paulo | RM576294 |

# ============================================================
#  GS CitizenTech · Computational Thinking with Python
#  Atividade: O Cérebro da CitizenTech
#
#  Equipe: [Paulo - RM576294], [Nome 2 - RM], [Nome 3 - RM]
#  CitizenTech: Alerta Calor Madureira
#  Problema, em uma frase: moradores de Madureira não sabem quando
#  o calor fica perigoso e não recebem um aviso simples para se proteger.
# ============================================================
#
#  Partes do programa:
#    PARTE 1 - Dados       (lista com 12 registros)
#    PARTE 2 - Faixas      (os mesmos limites do circuito de Edge)
#    PARTE 3 - Menu        (loop que só termina no Sair)
#    PARTE 4 - Opções      (classificar, resumir, consultar)
# ============================================================


# ------------------------------------------------------------
# PARTE 1 - DADOS
# Cada valor simula uma leitura do sensor de temperatura.
# Fonte dos dados: simulados pela equipe (sem dados pessoais).
# ------------------------------------------------------------

nome_local = "Madureira"
grandeza = "Temperatura"
unidade = "°C"

leituras = [31.5, 33.0, 34.8, 36.4, 38.2, 39.5, 41.2, 42.0, 40.6, 38.9, 34.3, 31.2]


# ------------------------------------------------------------
# PARTE 2 - FAIXAS DE DECISÃO
# Mesmos limites do circuito de Edge e mesmos textos da página.
# ------------------------------------------------------------

limite_atencao = 35.0   # a partir daqui: ATENÇÃO
limite_perigo = 40.0    # a partir daqui: PERIGO

aviso_normal = "Tudo certo por enquanto."
aviso_atencao = "Beba água e procure sombra."
aviso_perigo = "Evite sol das 11h às 16h."


# ------------------------------------------------------------
# PARTE 3 - MENU
# O menu repete até o usuário escolher 0.
# Entrada inválida NUNCA derruba o programa.
# ------------------------------------------------------------

print("=" * 44)
print(f"  Alerta Calor Madureira · {nome_local}")
print("=" * 44)

opcao = ""
while opcao != "0":
    print()
    print("1 - Ver todas as leituras classificadas")
    print("2 - Resumo do dia")
    print("3 - Consultar uma leitura")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ").strip()

    # --------------------------------------------------------
    # PARTE 4 - OPÇÕES
    # --------------------------------------------------------

    if opcao == "1":
        # Percorre a lista e classifica cada registro.
        print()
        print(f"{grandeza} em {nome_local}:")
        for posicao in range(len(leituras)):
            valor = leituras[posicao]

            if valor >= limite_perigo:
                faixa = "PERIGO"
            elif valor >= limite_atencao:
                faixa = "ATENÇÃO"
            else:
                faixa = "NORMAL"

            print(f"  Leitura {posicao + 1:02d}: {valor} {unidade} -> {faixa}")

    elif opcao == "2":
        # Resumo: média, maior valor, variação e % de leituras em alerta
        # (alerta = ATENÇÃO + PERIGO).
        soma = 0
        maior = leituras[0]
        menor = leituras[0]
        qtd_atencao = 0
        qtd_perigo = 0
        for valor in leituras:
            soma = soma + valor
            if valor > maior:
                maior = valor
            if valor < menor:
                menor = valor
            if valor >= limite_perigo:
                qtd_perigo = qtd_perigo + 1
            elif valor >= limite_atencao:
                qtd_atencao = qtd_atencao + 1

        media = soma / len(leituras)
        variacao = maior - menor
        qtd_alerta = qtd_atencao + qtd_perigo
        percentual_alerta = qtd_alerta / len(leituras) * 100

        print()
        print(f"Média do dia: {media:.1f} {unidade}")
        print(f"Maior valor: {maior} {unidade}")
        print(f"Variação entre menor e maior: {variacao:.1f} {unidade}")
        print(f"Leituras em ATENÇÃO: {qtd_atencao} de {len(leituras)}")
        print(f"Leituras em PERIGO: {qtd_perigo} de {len(leituras)}")
        print(f"Leituras em alerta: {qtd_alerta} de {len(leituras)} ({percentual_alerta:.0f}%)")

        # O aviso final usa o mesmo texto da página.
        if qtd_perigo > 0:
            print(f"AVISO: {aviso_perigo}")
        elif media >= limite_atencao or qtd_atencao > 0:
            print(f"AVISO: {aviso_atencao}")
        else:
            print(f"AVISO: {aviso_normal}")

    elif opcao == "3":
        # Consulta com validação: insiste até receber um número válido.
        # try/except evita erro com qualquer texto estranho.
        numero = 0
        valido = False
        while not valido:
            texto = input(f"Número da leitura (1 a {len(leituras)}): ").strip()
            try:
                numero = int(texto)
                if numero >= 1 and numero <= len(leituras):
                    valido = True
                else:
                    print("Valor inválido. Digite um número dentro do intervalo.")
            except ValueError:
                print("Valor inválido. Digite apenas o número da leitura.")

        valor = leituras[numero - 1]

        if valor >= limite_perigo:
            faixa = "PERIGO"
            aviso = aviso_perigo
        elif valor >= limite_atencao:
            faixa = "ATENÇÃO"
            aviso = aviso_atencao
        else:
            faixa = "NORMAL"
            aviso = aviso_normal

        print(f"Leitura {numero}: {valor} {unidade} -> {faixa}")
        print(f"AVISO: {aviso}")

    elif opcao == "0":
        print("Até logo! Fique atento ao calor.")

    else:
        print("Opção inválida. Escolha um número do menu.")

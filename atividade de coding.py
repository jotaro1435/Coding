def exibir_menu() -> None:
    print("\n" + "=" * 36)
    print("        CALCULADORA        ")
    print("=" * 36)
    print("  [1] +  Adição")
    print("  [2] -  Subtração")
    print("  [3] ×  Multiplicação")
    print("  [4] ÷  Divisão")
    print("  [0]    Sair")
    print("=" * 36)


def calcular(opcao: str, num1: float, num2: float) -> str:
    if opcao == "1":
        resultado = num1 + num2
        simbolo = "+"
    elif opcao == "2":
        resultado = num1 - num2
        simbolo = "-"
    elif opcao == "3":
        resultado = num1 * num2
        simbolo = "×"
    elif opcao == "4":
        if num2 == 0:
            return "Erro: Não é possível dividir por zero!"
        resultado = num1 / num2
        simbolo = "÷"
    else:
        return "Opção inválida!"

    # Formata para inteiro se não tiver casas decimais relevantes
    n1_fmt = int(num1) if num1.is_integer() else num1
    n2_fmt = int(num2) if num2.is_integer() else num2
    res_fmt = int(resultado) if isinstance(resultado, float) and resultado.is_integer() else round(resultado, 4)

    return f"Resultado: {n1_fmt} {simbolo} {n2_fmt} = {res_fmt}"


def main() -> None:
    while True:
        exibir_menu()
        opcao = input("Escolha uma operação (0-4): ").strip()

        if opcao == "0":
            print("\nEncerrando a calculadora. Até mais!")
            print("=" * 36)
            break

        if opcao not in ("1", "2", "3", "4"):
            print("\n[!] Opção inválida! Tente novamente.")
            continue

        try:
            num1 = float(input("Digite o primeiro número: ").replace(",", "."))
            num2 = float(input("Digite o segundo número:  ").replace(",", "."))
        except ValueError:
            print("\n[!] Erro: Digite apenas números válidos!")
            continue

        print("-" * 36)
        print("  " + calcular(opcao, num1, num2))
        print("-" * 36)


if __name__ == "__main__":
    main()

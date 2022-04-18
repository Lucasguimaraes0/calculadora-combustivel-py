from calculo import Calculo

def main():
    print("Este programa exibe a quantidade combustível necessário e o valor a ser gasto para realizar a viagem.")

    print("Os combustíveis disponíveis são:\nGasolina\nDiesel\nEtanol")

    try: #se as condições de transformação do valor de entrada não forem satisfeitas o print em except será executado
        distancia = float(input("Informe a distância a ser percorrida na viagem (Km)\n"))
        autonomia = float(input("Informe a autonomia do seu veículo (Km/l)\n"))
        calculo = Calculo()
        print(calculo.calcular_autonomia(distancia, autonomia))
    except ValueError as erro:
        print("O valor informado não é válido")

if __name__ == "__main__":
    main()
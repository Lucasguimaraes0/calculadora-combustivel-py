class Calculo:
    def __init__(self):
        self.__valor_gasolina = 6.99
        self.__valor_diesel = 6.49
        self.__valor_etanol = 5.29

    def calcular_autonomia(self, distancia, autonomia):
        if distancia <= 0 or autonomia <= 0:
            raise Exception('O valor informado não pode ser menor ou igual a zero')

        gasto_gasolina = round((distancia/autonomia)*self.__valor_gasolina, 2)
        gasto_diesel = round((distancia/autonomia)*self.__valor_diesel, 2)         
        gasto_etanol = round((distancia/autonomia)*self.__valor_etanol, 2)         

        # return """O valor total gasto na viagem será:\n
        
        # Gasolina: R${}\n
        # Diesel: R${}\n
        # Etanol: R${}
        # """.format(gasto_gasolina, gasto_diesel,gasto_etanol)

        return f"""O valor total gasto na viagem será:
        
        Gasolina: R${gasto_gasolina}
        Diesel: R${gasto_diesel}
        Etanol: R${gasto_etanol}
        """
class Registro:
    
    #constructor
    def __init__(self, temperatura: int, humedad: int, presion: float):
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presion = presion
    #getters
    def get_temperatura(self):
        return self.__temperatura
    def get_humedad(self):
        return self.__humedad
    def get_presion(self):
        return self.__presion
    def mostrar(self):
        print("temperatura: ", self.__temperatura)
        print("humedad: ", self.__humedad)
        print("presion: ", self.__presion)
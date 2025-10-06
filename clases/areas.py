import math

class CalcularAreas:
    def __init__(self):
        self.resultados = {}

    def leer_datos(self, figura):
        print(f"\nCálculo de área de {figura}")
        if figura == "círculo":
            radio = float(input("Ingrese el radio del círculo: "))
            return radio, None
        else:
            base = float(input(f"Ingrese la base del {figura}: "))
            altura = float(input(f"Ingrese la altura del {figura}: "))
            return base, altura

    def calcular_ATriangulo(self, base, altura):
        return (base * altura) / 2

    def calcular_ARectangulo(self, base, altura):
        return base * altura

    def calcular_ACirculo(self, radio):
        if radio < 0:
            raise ValueError("El radio no puede ser negativo.")
        return math.pi * radio ** 2

    def mostrarResultado(self, figura, area):
        print(f"El área del {figura} es: {area:.2f} unidades cuadradas")
        self.resultados[figura] = area

    def calcular(self):
        # Triángulo
        base_t, altura_t = self.leer_datos("triángulo")
        area_t = self.calcular_ATriangulo(base_t, altura_t)
        self.mostrarResultado("triángulo", area_t)

        # Rectángulo
        base_r, altura_r = self.leer_datos("rectángulo")
        area_r = self.calcular_ARectangulo(base_r, altura_r)
        self.mostrarResultado("rectángulo", area_r)

        # Círculo
        radio_c, _ = self.leer_datos("círculo")
        area_c = self.calcular_ACirculo(radio_c)
        self.mostrarResultado("círculo", area_c)
# Componente
class Cafe:
    def costo(self):
        return 5  # Costo base del café

# Decorador abstracto
class DecoradorCafe:
    def __init__(self, cafe):
        self._cafe = cafe

    def costo(self):
        return self._cafe.costo()

# Decoradores concretos
class LecheDecorator(DecoradorCafe):
    def costo(self):
        return self._cafe.costo() + 2

class AzucarDecorator(DecoradorCafe):
    def costo(self):
        return self._cafe.costo() + 1

# Uso del patrón
cafe_simple = Cafe()
print("Café simple costo:", cafe_simple.costo())

cafe_con_leche = LecheDecorator(cafe_simple)
print("Café con leche costo:", cafe_con_leche.costo())

cafe_con_azucar = AzucarDecorator(cafe_simple)
print("Café con azúcar costo:", cafe_con_azucar.costo())

cafe_con_todo = LecheDecorator(AzucarDecorator(cafe_simple))
print("Café con leche y azúcar costo:", cafe_con_todo.costo())

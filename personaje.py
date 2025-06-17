class Personajes:
    def __init__(self, nombre:str) -> None:
        self._nombre = nombre
        self._nivel  = 1
        self._experiencia = 0


nombre = input("""
        Bienvenido al juego Gran Fantasía.
        Antes de comenzar.
      Ingresa el nombre de tu personaje:
""")

print(f"Tu personaje es: {nombre}")

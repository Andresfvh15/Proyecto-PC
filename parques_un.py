# -*- coding: utf-8 -*-
"""Parques_UN.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Xu0ExY4KDzWPkJhK3892YJs-LrRITSlc
"""

import random

class Parques:
    def __init__(self):
        self.jugadores = ["Rojo", "Azul", "Verde", "Amarillo"]
        self.turno_jugador = 0
        self.fichas = self.inicializar_fichas()
        self.dados = [0, 0]
        self.pares_consecutivos = 0
        self.ultima_ficha_movida = None
        self.modo_juego = "real"
        self.salidas = {"Rojo": 5, "Azul": 22, "Verde": 39, "Amarillo": 56}
        self.llegadas = {
            "Rojo": list(range(68, 76)),
            "Azul": list(range(76, 84)),
            "Verde": list(range(84, 92)),
            "Amarillo": list(range(92, 100))
        }
        self.seguros = [5, 12, 19, 26, 33, 40, 47, 54, 61, 68]
        self.bloqueos = {}  # Diccionario para rastrear bloqueos

    def inicializar_fichas(self):
        fichas = {}
        for jugador in self.jugadores:
            fichas[jugador] = {
                f"ficha{i+1}": {"posicion": "carcel"} for i in range(4)
            }
        return fichas

    def lanzar_dados(self):
        if self.modo_juego == "real":
            self.dados = [random.randint(1, 6) for _ in range(2)]
        else:
            self.dados = [int(input(f"Dado {i + 1}: ")) for i in range(2)]
        print(f"Dados: {self.dados}")

        if self.dados[0] == self.dados[1]:
            self.pares_consecutivos += 1
            print("¡Sacaste pares! Tienes otro turno.")
        else:
            self.pares_consecutivos = 0

        if self.pares_consecutivos == 3:
            if self.ultima_ficha_movida:
                jugador, ficha = self.ultima_ficha_movida
                self.fichas[jugador][ficha]["posicion"] = "carcel"
                print("¡Tres pares seguidos! La última ficha movida regresa a la cárcel.")
                self.ultima_ficha_movida = None
            self.pares_consecutivos = 0
            self.turno_siguiente()
            return

        self.determinar_movimientos_posibles()

    def determinar_movimientos_posibles(self):
        jugador_actual = self.jugadores[self.turno_jugador]
        fichas_jugador = self.fichas[jugador_actual]
        dados = self.dados

        if 5 in dados or sum(dados) == 5:
            for ficha, estado in fichas_jugador.items():
                if estado["posicion"] == "carcel" and self.puede_sacar_ficha(jugador_actual):
                    self.sacar_ficha(jugador_actual, ficha)
                    print(f"¡{jugador_actual} sacó {ficha} de la cárcel!")
                    if self.dados[0] != self.dados[1]:  # Si sacas ficha, no hay movimiento extra a menos que saques pares
                        self.turno_siguiente()
                    return

        movimientos_posibles = []
        for ficha, estado in fichas_jugador.items():
            if estado["posicion"] != "carcel" and estado["posicion"] not in self.llegadas[jugador_actual]:
                posicion_actual = estado["posicion"]
                movimientos = self.calcular_movimientos(jugador_actual, ficha, posicion_actual, dados)
                if movimientos:
                    movimientos_posibles.append((ficha, posicion_actual, movimientos))

        if movimientos_posibles:
            self.mostrar_opciones_movimiento(movimientos_posibles)
        else:
            print("No hay movimientos posibles.")
            if self.dados[0] != self.dados[1]:
                self.turno_siguiente()

    def calcular_movimientos(self, jugador, ficha, posicion_actual, dados):
        movimientos = []
        dado1, dado2 = dados

        for dado in [dado1, dado2, dado1 + dado2]:
            nueva_posicion = (posicion_actual + dado) % 68 if posicion_actual <= 67 else posicion_actual
            if self.es_movimiento_valido(jugador, posicion_actual, nueva_posicion, dado):
                movimientos.append((nueva_posicion, dado))

        return movimientos

    def puede_sacar_ficha(self, jugador):
        casilla_salida = self.salidas[jugador]
        fichas_en_salida = sum(1 for j in self.jugadores for f, e in self.fichas[j].items() if e["posicion"] == casilla_salida)
        return fichas_en_salida < 2

    def sacar_ficha(self, jugador, ficha):
        self.fichas[jugador][ficha]["posicion"] = self.salidas[jugador]

    def es_movimiento_valido(self, jugador, posicion_actual, nueva_posicion, dado):
        if nueva_posicion < 0:
            return False

        if nueva_posicion in self.llegadas[jugador]:
            return True

        if self.hay_bloqueo_en_el_camino(posicion_actual, nueva_posicion):
            print("¡No puedes pasar el bloqueo!")
            return False

        if self.hay_bloqueo(nueva_posicion, jugador):
            print("¡No puedes mover directamente a una casilla con bloqueo!")
            return False

        if self.contar_fichas_en_casilla(nueva_posicion) >= 2:
            print("¡Casilla llena! No puedes mover aquí.")
            return False

        return True

    def hay_bloqueo_en_el_camino(self, posicion_inicial, posicion_final):
        distancia = abs(posicion_final - posicion_inicial)
        for i in range(1, distancia +1):
            posicion_en_el_camino = (posicion_inicial + i) % 68
            if posicion_en_el_camino in self.bloqueos:
                return True
        return False

    def contar_fichas_en_casilla(self, posicion):
        count = 0
        for jugador in self.jugadores:
            for ficha, estado in self.fichas[jugador].items():
                if estado["posicion"] == posicion:
                    count += 1
        return count

    def hay_bloqueo(self, posicion, jugador):
        if posicion in self.bloqueos:
            return True
        count = 0
        for ficha, estado in self.fichas[jugador].items():
            if estado["posicion"] == posicion:
                count += 1
        return count >= 2

    def crear_bloqueo(self, posicion):
        print(f"¡Bloqueo creado en la casilla {posicion}!")
        self.bloqueos[posicion] = True

    def romper_bloqueo(self, posicion):
        if posicion in self.bloqueos:
            del self.bloqueos[posicion]
            print(f"¡Bloqueo roto en la casilla {posicion}!")

    def turno_siguiente(self):
        self.turno_jugador = (self.turno_jugador + 1) % len(self.jugadores)

    def mostrar_opciones_movimiento(self, movimientos_posibles):
        print("Movimientos posibles:")
        for i, (ficha, posicion_actual, movimientos) in enumerate(movimientos_posibles):
            print(f"{i + 1}. Ficha {ficha} en posición {posicion_actual}:")
            for j, (nueva_posicion, dado) in enumerate(movimientos):
                print(f"   {j + 1}. Mover a {nueva_posicion} usando {dado}")

        opcion = int(input("Elige una opción: ")) - 1
        ficha, _, movimientos = movimientos_posibles[opcion]
        sub_opcion = int(input("Elige un movimiento: ")) - 1
        nueva_posicion, _ = movimientos[sub_opcion]

        self.mover_ficha(self.jugadores[self.turno_jugador], ficha, nueva_posicion)
        if self.dados[0] != self.dados[1]:  # No cambias el turno si sacas par
            self.turno_siguiente()

    def mover_ficha(self, jugador, ficha, nueva_posicion):
        posicion_anterior = self.fichas[jugador][ficha]["posicion"]
        self.fichas[jugador][ficha]["posicion"] = nueva_posicion
        self.ultima_ficha_movida = (jugador, ficha)
        print(f"{jugador} movió {ficha} a la posición {nueva_posicion}")

        # Check if there's an opponent's piece in the new position
        for oponente in self.jugadores:
            if oponente != jugador:
                for ficha_oponente, estado in self.fichas[oponente].items():
                    if estado["posicion"] == nueva_posicion and nueva_posicion not in self.seguros:
                        # Send the opponent's piece back to jail
                        self.fichas[oponente][ficha_oponente]["posicion"] = "carcel"
                        print(f"¡Ficha comida! {jugador} comió la ficha {ficha_oponente} de {oponente}")

        # Crear bloqueo si dos fichas del mismo jugador están en la misma casilla
        if self.hay_bloqueo(nueva_posicion, jugador):
            self.crear_bloqueo(nueva_posicion)

        # Romper bloqueo si la ficha se movió de una casilla con bloqueo
        if posicion_anterior in self.bloqueos:
            self.romper_bloqueo(posicion_anterior)

    def jugar(self):
        while True:
            jugador_actual = self.jugadores[self.turno_jugador]
            print(f"\nTurno de {jugador_actual}")
            self.lanzar_dados()
            input("Presiona Enter para continuar...")
            if self.pares_consecutivos < 3 and self.dados[0] != self.dados[1]:
                continue  # Si no hay pares consecutivos ni dobles, pasamos al siguiente turno.

    def seleccionar_modo_juego(self):
        print("Seleccione el modo de juego:")
        print("1. Modo Real")
        print("2. Modo Desarrollador")
        opcion = input("Ingrese su opción (1/2): ")

        if opcion == "1":
            self.modo_juego = "real"
        elif opcion == "2":
            self.modo_juego = "desarrollador"
        else:
            print("Opción inválida. Seleccionando modo real por defecto.")
            self.modo_juego = "real"

if __name__ == "__main__":
    juego = Parques()
    juego.seleccionar_modo_juego()
    juego.jugar()
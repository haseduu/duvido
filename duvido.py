import random

# Definição dos valores das cartas e dos naipes
cartas = ["As", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Q", "J", "K"]
naipes = ["Paus", "Espadas", "Copas", "Ouros"]


class Carta:
    def __init__(self, num, naipe):
        self.carta_num = num
        self.carta_naipe = naipe
        
        self.carta = f"{num} de {naipe}"
       
    

class Baralho:
    def __init__(self):
        self.cartas = [Carta(num, naipe) for num in cartas for naipe in naipes]
        self.embaralhar()

    def embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir(self, num_cartas):
        if num_cartas > len(self.cartas):
            raise ValueError("Não há cartas suficientes no baralho.")
        mao = self.cartas[:num_cartas]
        self.cartas = self.cartas[num_cartas:]
        return mao

    def virar_carta(self):
        # Vira a última carta do baralho como a "vira"
        return self.cartas.pop()

class Player:
    def __init__(self, name, team):
        self.team = team
        self.name = name
        self.hand = []
        self.ia = False
        
    def add_card(self, carta):
        self.hand.append(carta)

    def show_hand(self):
        print(f"\nMão de {self.name}:")
        for i, card in enumerate(self.hand):
            print(f"{i+1}. {card}")

class Game:
    def __init__(self, numberofplayers):
        quantidadedecartas = len(cartas) * len(naipes)
        cards_dist = 0
        if quantidadedecartas % numberofplayers // 0:
            self.card_per_player = quantidadedecartas / numberofplayers
        else:
            cards_dist = (int(quantidadedecartas / numberofplayers) - 1) * numberofplayers
            remain = quantidadedecartas - cards_dist
            

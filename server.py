from random import randint


class Card:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom


class Trail:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail


class Hand:
    def __init__(self, cards):
        self.cards = cards


class Deck:
    def __init__(self):
        self.cards = Deck.new_cards()
    @staticmethod
    def new_cards ():
        cards = []
        for i in range(0,7):
            for j in range(i,7):
                card = Card(i,j)
                cards.append(card)
        return cards


class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.points = 0


class Board:
    def __init__(self, deck, trail):
        self.trail = trail
        self.deck = deck
        self.turn = randint(0,2)


class GameRoom ():
    def __init__(self, board, Players):
        self.board = board
        self.players = Players
        self.end_points = 100


def new_game ():
    hand = Hand([])  # Assuming an empty hand for the new players
    players = [Player("Player1", hand), Player("Player2", hand), Player("Player3", hand)]
    deck = Deck()  
    board = Board(deck)
    NewGame = GameRoom(board, players)

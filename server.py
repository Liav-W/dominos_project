from random import randint
import pygame

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
    players = [Player("Player1", hand), Player("Player2", hand)]
    deck = Deck()  
    board = Board(deck)
    NewGame = GameRoom(board, players)


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
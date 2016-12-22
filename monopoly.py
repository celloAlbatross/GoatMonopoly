import arcade
from random import randint

GAME_TITLE = "Goat Monopoly"
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
COIN_POSITION_WIDTH = SCREEN_WIDTH/2
COIN_POSITION_HEIGHT = SCREEN_HEIGHT/1.5

class BetWindow(arcade.Window) :
    count = 0
    toss = None

    def __init__(self, width, height) :
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

        arcade.set_background_color(arcade.color.BABY_BLUE)

        self.headCoin = arcade.Sprite('images/head.png')
        self.headCoin.set_position(COIN_POSITION_WIDTH, COIN_POSITION_HEIGHT)
        self.tailCoin = arcade.Sprite('images/tail.png')
        self.tailCoin.set_position(COIN_POSITION_WIDTH, COIN_POSITION_HEIGHT)
        self.bg = arcade.Sprite('images/background.jpg')
        self.bg.set_position(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

        self.initTwoPlayer()
        # self.playerI = Player(self)
        # self.playerI.playerName = "Player I"
        # self.playerII = Player(self)
        # self.playerII.playerName = "Player II"

    def on_draw(self) :
        arcade.start_render()
        self.bg.draw()
        if self.toss == 0 :
            self.headCoin.draw()
        elif self.toss == 1 :
            self.tailCoin.draw()

    def animate(self, delta) :
        if self.count > 0 and self.count < 11:
            self.coinToss()

            self.chooseToss(self.playerI)
            self.chooseToss(self.playerII)

            self.getMoney(self.playerI)
            self.getMoney(self.playerII)

            print("Current money of PlayerI:",self.playerI.money)
            print("Current money of PlayerII:",self.playerII.money)
            print(self.toss)

        elif self.count != 0 :
            self.whoWin()
            self.reset()
        self.count += 1

    def getMoney(self,player) :
        if self.toss == player.choose :
            print(player.playerName,"get 1000")
            player.money += 2000

    def chooseToss(self,player) :
        while player.choose != "1" and player.choose != "0" :
            print(player.playerName, end = " ")
            player.choose = input("Choose 0 or 1: ")

        player.choose = int(player.choose)
        player.money -= 1000

    def coinToss(self) :
        self.toss = randint(0,1)
        return self.toss

    def whoWin(self) :
        if self.playerI.money > self.playerII.money :
            print("PlayerII Win !!")
            print("----------------------------------")
        elif self.playerII.money > self.playerI.money :
            print("PlayerI Win !!")
            print("----------------------------------")
        else :
            print("Draw!! you two noob")
            print("----------------------------------")

    def reset(self) :
        # self.playerI = Player(self)
        # self.playerII = Player(self)
        self.initTwoPlayer()
        self.count = 0

    def initTwoPlayer(self) :
        self.playerI = Player(self)
        self.playerI.playerName = "Player I"
        self.playerII = Player(self)
        self.playerII.playerName = "Player II"


class Player() :
    def __init__(self,betWindow) :
        self.money = 10000
        self.choose = None
        self.playerName = None


if __name__ == '__main__' :
    window = BetWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

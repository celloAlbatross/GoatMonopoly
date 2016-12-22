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

        self.playerI = Player(self)
        self.playerII = Player(self)

    def on_draw(self) :
        arcade.start_render()
        if self.toss == 1 :
            self.headCoin.draw()

    def animate(self, delta) :
        if self.count > 0 and self.count < 11:
            self.coinToss()
            while self.playerI.choose != "1" and self.playerI.choose != "0" :
                self.playerI.choose = input("PlayerI Choose 0 or 1: ")
            while self.playerII.choose != "1" and self.playerII.choose != "0" :
                self.playerII.choose = input("playerII Choose 0 or 1: ")
            self.playerI.choose = int(self.playerI.choose)
            self.playerII.choose = int(self.playerII.choose)
            self.playerI.money -= 1000;
            self.playerII.money -= 1000;
            if self.toss == self.playerI.choose :
                print("playerI get 1000")
                self.playerI.money += 2000
                # print("Current money of PlayerI:",self.playerI.money)
            if self.toss == self.playerII.choose :
                print("playerII get 1000")
                self.playerII.money += 2000
                # print("Current money of PlayerI:",self.playerII.money)
            print("Current money of PlayerI:",self.playerI.money)
            print("Current money of PlayerII:",self.playerII.money)
            print(self.toss)
        self.count += 1
        # elif self.count != 0 :
        #     self.whoWin()
        #     self.reset()

        # self.toss = self.coinToss()
        # print(self.toss)

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
        self.playerI = Player(self)
        self.playerII = Player(self)
        count = 0

class Player() :
    def __init__(self,betWindow) :
        self.money = 10000
        self.choose = None

if __name__ == '__main__' :
    window = BetWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

import arcade
from random import randint
import arcade.key

GAME_TITLE = "Goat Monopoly"
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
COIN_POSITION_WIDTH = SCREEN_WIDTH/2
COIN_POSITION_HEIGHT = SCREEN_HEIGHT/1.5

class BetWindow(arcade.Window) :
    # self.count = 0
    # self.toss = None
    # self.chooseI = None
    # self.chooseII = None
    # self.stateCoinToss = 1
    # self.stateChooseToss = 0
    # self.statePrintCurrent = 0

    def __init__(self, width, height) :
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

        arcade.set_background_color(arcade.color.BABY_BLUE)

        self.headCoin = arcade.Sprite('images/head.png')
        self.headCoin.set_position(COIN_POSITION_WIDTH, COIN_POSITION_HEIGHT)
        self.tailCoin = arcade.Sprite('images/tail.png')
        self.tailCoin.set_position(COIN_POSITION_WIDTH, COIN_POSITION_HEIGHT)
        self.bg = arcade.Sprite('images/background.jpg')
        self.bg.set_position(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

        self.count = 1
        self.toss = None
        self.chooseI = None
        self.chooseII = None
        self.stateCoinToss = 1
        self.stateChooseToss = 0
        self.statePrintCurrent = 0
        self.prevCoin = None

        self.initTwoPlayer()
        # self.playerI = Player(self)
        # self.playerI.playerName = "Player I"
        # self.playerII = Player(self)
        # self.playerII.playerName = "Player II"

    def on_draw(self) :
        arcade.start_render()
        self.bg.draw()

        if self.prevCoin == 0 :
            self.headCoin.draw()
        elif self.prevCoin == 1:
            self.tailCoin.draw()

    def animate(self, delta) :
        # print(2)
        if self.count > 0 and self.count < 11 :
            # print(self.stateCoinToss)
            if self.stateCoinToss :
                # self.canIDraw = 0
                self.coinToss()
                self.count += 1
                self.stateCoinToss = 0
                self.stateChooseToss = 1
                # print(1)

            # self.chooseToss(self.playerI, self.chooseI)
            # self.chooseToss(self.playerII, self.chooseII)
            if self.stateChooseToss:
                if self.chooseI == 1 and self.chooseII == 1 :
                    self.getMoney(self.playerI)
                    self.getMoney(self.playerII)
                    self.stateChooseToss = 0
                    self.statePrintCurrent = 1
                    self.chooseI = 0
                    self.chooseII = 0
                    self.prevCoin = self.toss

            if self.statePrintCurrent :
                print("Current money of PlayerI:",self.playerI.money)
                print("Current money of PlayerII:",self.playerII.money)
                print(self.toss)
                self.statePrintCurrent = 0
                self.stateCoinToss = 1

        elif self.count != 0 :
            self.whoWin()
            self.reset()
        # self.count += 1

    def getMoney(self,player) :
        if self.toss == player.choose :
            print(player.playerName,"get 1000")
            player.money += 2000

    def chooseToss(self,player,choose) :
        # while player.choose != "1" and player.choose != "0" :
            # print(player.playerName, end = " ")
            # player.choose = input("Choose 0 or 1: ")

        #while choose != 1 :
            #x=1
        # player.choose = int(player.choose)
        # player.choose = None
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
        # self.count = 0
        self.count = 1
        self.toss = None
        self.chooseI = None
        self.chooseII = None
        self.stateCoinToss = 1
        self.stateChooseToss = 0
        self.statePrintCurrent = 0
        self.prevCoin = None

    def initTwoPlayer(self) :
        self.playerI = Player(self)
        self.playerI.playerName = "Player I"
        self.playerII = Player(self)
        self.playerII.playerName = "Player II"

    def on_key_press(self, key, key_modifier) :
        if key == arcade.key.A :
            self.playerI.choose = 0
        if key == arcade.key.D :
            self.playerI.choose = 1
        if key == arcade.key.S :
            self.chooseI = 1
        if key == arcade.key.J :
            self.playerII.choose = 0
        if key == arcade.key.L :
            self.playerII.choose = 1
        if key == arcade.key.K :
            self.chooseII = 1

class Player() :
    def __init__(self,betWindow) :
        self.money = 10000
        self.choose = None
        self.playerName = None



if __name__ == '__main__' :
    window = BetWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

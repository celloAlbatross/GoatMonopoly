import arcade
from random import randint
import arcade.key

GAME_TITLE = "Goat Monopoly"
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
COIN_POSITION_WIDTH = SCREEN_WIDTH/2
COIN_POSITION_HEIGHT = SCREEN_HEIGHT/1.5
P1_W = SCREEN_WIDTH/4
P1_H = SCREEN_HEIGHT/3
P2_W = SCREEN_WIDTH*3/4
P2_H = SCREEN_HEIGHT/3

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
        self.headP1 = arcade.Sprite('images/head.png')
        self.headP1.set_position(P1_W, P1_H)
        self.headP2 = arcade.Sprite('images/head.png')
        self.headP2.set_position(P2_W, P2_H)
        self.tailP1 = arcade.Sprite('images/tail.png')
        self.tailP1.set_position(P1_W, P1_H)
        self.tailP2 = arcade.Sprite('images/tail.png')
        self.tailP2.set_position(P2_W, P2_H)
        self.winP1 = arcade.Sprite('images/player1win.png')
        self.winP1.set_position(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.winP2 = arcade.Sprite('images/player2win.png')
        self.winP2.set_position(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.noob = arcade.Sprite('images/noob.jpg')
        self.noob.set_position(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


        self.count = 1
        self.toss = None
        self.chooseI = None
        self.chooseII = None
        self.stateCoinToss = 1
        self.stateChooseToss = 0
        self.statePrintCurrent = 0
        self.stateWin = 0
        self.prevCoin = None
        self.winShow = None
        self.timer = 0

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
        elif self.prevCoin == 1 :
            self.tailCoin.draw()
        if self.playerI.choose == 0 :
            self.headP1.draw()
        elif self.playerI.choose == 1 :
            self.tailP1.draw()
        if self.playerII.choose == 0 :
            self.headP2.draw()
        elif self.playerII.choose == 1 :
            self.tailP2.draw()
        if self.stateWin :
            if self.whoWin() == 0 :
                self.winP1.draw()
            elif self.whoWin() == 1 :
                self.winP2.draw()
            elif self.whoWin() == 2 :
                self.noob.draw()

    def animate(self, delta) :
        # print(2)

        self.timer += delta
        self.sec = int(self.timer)
        # print(self.sec)

        if self.count > 0 and self.count < 11 :

            if self.stateCoinToss :
                self.coinToss()
                self.count += 1
                self.stateCoinToss = 0
                self.stateChooseToss = 1

            if self.stateChooseToss:
                if self.chooseI == 1 and self.chooseII == 1 :
                    self.playerI.money -= 1000
                    self.playerII.money -= 1000
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
                # self.stateCoinToss = 0
                # self.stateWin = 1
                self.currentTime = self.sec
                print(self.count)
                self.stateCoinToss = 1

        elif self.count > 10 :
            self.whoWin()
            self.stateWin = 1
            if self.stateWin :
                if self.sec - self.currentTime == 3 :
                    self.stateWin = 0
                    self.reset()

    def getMoney(self,player) :
        if self.toss == player.choose :
            print(player.playerName,"get 1000")
            player.money += 2000

    def coinToss(self) :
        self.toss = randint(0,1)
        return self.toss

    def whoWin(self) :
        if self.playerI.money > self.playerII.money :
            print("PlayerII Win !!")
            print("----------------------------------")
            self.winShow = 1
            return 1
        elif self.playerII.money > self.playerI.money :
            print("PlayerI Win !!")
            print("----------------------------------")
            self.winShow = 0
            return 0
        else :
            print("Draw!! you two noob")
            print("----------------------------------")
            return 2

    def reset(self) :
        self.initTwoPlayer()
        self.count = 1
        self.toss = None
        self.chooseI = None
        self.chooseII = None
        self.stateCoinToss = 1
        self.stateChooseToss = 0
        self.statePrintCurrent = 0
        self.prevCoin = None
        self.stateWin = 0

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
        self.choose = 0
        self.playerName = None



if __name__ == '__main__' :
    window = BetWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

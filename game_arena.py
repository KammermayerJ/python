'''

Arena fighter - game
Created by Jan Kammermayer
honza.kammermayer@gmail.com

'''


from random import randint, choice, shuffle
from time import sleep

NAMES = ['Tiawin', 'Aigori', 'Comach', 'Zilalith', 'Ulomali', 'Ediraweth', 'Mirirash', 'Wiathiel', 'Vohajan', 'Kelawen', 'Jerirald', 'Umilandra', 'Ibaugan', 'Eowardored', 'Naolith']
TIME_SLEEP = 0.01

class Dice():
    '''
    Class representing dice for game
    '''
    def __init__(self, sides_number=6):
        self.__sides_number = sides_number

    def throw(self):
        '''
        Return throwed number
        '''
        return randint(1, self.__sides_number)

    def double_same_throw(self):
        return self.throw() == self.throw()

class Fighter():
    '''
    Class create Fighter
    '''
    def __init__(self, name, lives, attack, defence, dice = Dice()):
        self.__name = name
        self.__lives = lives
        self.__attack = attack
        self.__defence = defence
        self.__dice = dice

    def defence(self, hit):
        '''
        Defence agains attack
        '''

        if self.__dice.double_same_throw():
            print('{}({}) cover the hit (double same).'.format(self.__name, self.__lives))
        else:
            injury = hit - self.__defence - self.__dice.throw()
            if injury > 0:
                self.__lives -= injury
                if self.__lives < 0:
                    self.__lives = 0
                    print('{} died !'.format(self.__name))
                else:
                    print('{} lost {} hp.'.format(self.__name, injury))

    def attack(self, opponent):
        '''
        Throw with dice and attack opponent
        '''
        if self.is_alive():
            hit = self.__attack + self.__dice.throw()
            print('{}({}) hit {}({}) with {}'.format(self.__name, self.__lives, opponent.__name, opponent.__lives, hit))
            sleep(TIME_SLEEP)
            opponent.defence(hit)
            sleep(TIME_SLEEP)

    def is_alive(self):
        '''
        Check if player is alive
        '''
        return self.__lives > 0

class Arena():
    '''
    Class creating area with fighters
    '''

    def __init__(self, fighters = 2):
        self.arena = []
        self.create_fighters(fighters)

    def create_fighters(self, fighters):
        '''
        Create all fighters
        '''
        shuffle(NAMES)
        if fighters > len(NAMES) or fighters < 2:   # min 2 players and max by names
            return
        for i in range(fighters):
            fighter = Fighter(NAMES.pop(), 100, 20, 5)
            self.arena.append(fighter)

    def play(self):
        '''
        Start game loop
        '''
        print("Wellcome to Arena!")
        print("Let's the game begin...")
        self.round = 1
        while len([__ for __ in self.arena if __.is_alive()]) > 1:     # check if more than 1 player
            print('#'*40)
            print('Round {}'.format(self.round))
            print('#'*40)
            self.arena = [__ for __ in self.arena if __.is_alive()]
            shuffle(self.arena)
            for fighter in self.arena:
                _temp = [p for p in self.arena if fighter != p]
                fighter.attack(choice(_temp))
            self.round += 1
        else:
            print('#'*40)
            print('Game is over !')
            print('#'*40)

if __name__ == '__main__':
    inpt = int(input('How much players ? (2-15): '))
    arena = Arena(inpt)
    arena.play()

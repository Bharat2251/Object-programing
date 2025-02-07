import random

# Class definition
class Coin:
    def __init__(self):
        self.sideup = 'Heads'

    def toss_the_coin(self):
        outcome = random.randint(0, 4)
        if outcome == 0:
            self.sideup = 'Heads'
            print("The coin landed showing: Heads")
        elif outcome == 1:
            self.sideup = 'Tails'
            print("The coin landed showing: Tails")
        elif outcome == 2:
            print("The coin landed upright on the table.")
        elif outcome == 3:
            print("The coin dropped on the ground and disappeared in a rabbit hole.")
        else:
            print("The coin defied gravity and got lost in a wormhole in space.")

    def get_sideup(self):
        return self.sideup

# Main function definition
def main():
    my_coin = Coin()
    print("This side is up:", my_coin.get_sideup())
    print("Tossing the coin...")
    my_coin.toss_the_coin()
    print("Now this side is up:", my_coin.get_sideup())

main()

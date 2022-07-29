import random
from collections import Counter


class GameLogic:
    def __init__(self):
        pass


    @staticmethod
    def roll_dice(num):
        rolls = []
        while len(rolls) < num:
            rolls.append(random.randint(1, 6))

        return tuple(rolls)

    @staticmethod
    def calculate_score(tup):
        total = 0
        roll = Counter(tup).most_common()

        if len(tup) == 0:
            return total


        print(f"print roll: {roll}")

        if len(roll) == 6:
            total += 1500

        if roll [0][1] == 6:
            if roll[0][0] == 1:
                total += 4000
                return total
            total += int(roll[0][0]) * 400
            return total

        elif roll[0][1] == 5:
            if roll[1][0] == 1:
                total += 3000


            elif len (roll) > 1:
                if roll[1][0] == 5:
                    total += 50

                elif roll[1][0] == 1:
                    total += 100


            else:
                total += int(roll[0][0]) * 300
                return total





import random
form collections import Counter



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
            total +- int




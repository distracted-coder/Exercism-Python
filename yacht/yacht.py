"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"


def score(dice, category):
    numbers = {"ONES": 1, "TWOS": 2, "THREES": 3, "FOURS": 4, "FIVES": 5, "SIXES": 6}
    score = 0
    if category in numbers:
        for i in dice:
            if i == numbers[category]:
                score += i
        return score
    if category == "YACHT":
        score = 50
        for i in range(1, len(dice)):
            if dice[i] != dice[i -1]:
                score = 0
        return score
    if category == "FULL_HOUSE":
        temp_dict = {}
        triple = 0
        double = 0

        for i in dice:
            if i not in temp_dict:
                temp_dict[i] = 1
            else:
                temp_dict[i] += 1
        for i in temp_dict:
            if temp_dict[i] >= 3:
                triple = i
                temp_dict[i] = 0
        for i in temp_dict:
            if temp_dict[i] >= 2:
                double = i
        if triple != 0 and double != 0:
            return 3 * triple + 2 * double
        else:
            return 0
    if category == "CHOICE":
        return sum(dice)
    if category == "FOUR_OF_A_KIND":
        temp_dict = {}
        quadruple = 0

        for i in dice:
            if i not in temp_dict:
                temp_dict[i] = 1
            else:
                temp_dict[i] += 1
        for i in temp_dict:
            if temp_dict[i] >= 4:
                quadruple = i
        if quadruple != 0:
            return 4 * quadruple
        else:
            return 0
    if category == "LITTLE_STRAIGHT":
        if sorted(dice) == [1, 2, 3, 4, 5]:
            return 30
        else:
            return 0
    if category == "BIG_STRAIGHT":
        if sorted(dice) == [2, 3, 4, 5, 6]:
            return 30
        else:
            return 0


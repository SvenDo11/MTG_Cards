from enum import Enum
from util import dictAddOne, dictAddX

class Color(Enum):
    """Enum for mtg color.
    """
    Colorless = 0
    White = 1
    Black = 2
    Green = 3
    Red = 4
    Blue = 5

class ManaCost:
    """Class representing ManaCost
    """
    def __init__(self) -> None:
        self.colors = {}
    
    def fromStr(self, colorStr: str) -> None:
        """Turn a mana cost string in form {3}{B}{B} into a ManaCost list

        :param colorStr: String containing the manacost
        :type colorStr: str
        """
        colorStr = colorStr.replace(' ', '')
        colors = colorStr.split('}')
        for color in colors:
            color = color.replace('{', '')
            if color == 'B':
                dictAddOne(self.colors, Color.Black)
            elif color == 'W':
                dictAddOne(self.colors, Color.White)
            elif color == 'R':
                dictAddOne(self.colors, Color.Red)
            elif color == 'U':
                dictAddOne(self.colors, Color.Blue)
            elif color == 'G':
                dictAddOne(self.colors, Color.Green)
            else:
                try:
                    amount = int(color)
                    dictAddX(self.colors, Color.Colorless, amount)
                except:
                    print("Could not parse '{}' to a color cost!".format(color))

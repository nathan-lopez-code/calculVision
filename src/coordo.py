dico = {
            "1top": (20, 100),
            "1bom": (213, 250),
            "1v": 1,
            "2top": (20, 250),
            "2bom": (213, 400),
            "4v": 4,
            "3top": (20, 400),
            "3bom": (213, 550),
            "7v": 7,
            "4top": (20, 550),
            "4bom": (213, 700),
            "+v": "+",
            "5top": (213, 100),
            "5bom": (406, 250),
            "2v": 2,
            "6top": (213, 250), "6bom": (406, 400), "5v": 5,
            "7top": (213, 400), "7bom": (406, 550), "8v": 8,
            "8top": (213, 550), "8bom": (406, 700), "0v": 0,
            "9top": (406, 100), "9bom": (600, 250), "3v": 3,
            "10top": (406, 250), "10bom": (600, 400), "6v": 6,
            "11top": (406, 400), "11bom": (600, 550), "9v": 9,
            "12top": (406, 550), "12bom": (600, 700),   "=v": "=",

        }


class Calculate:

    def __init__(self, string):

        self.string = string

    def calcule(self, s):
        """
            take on string eg : 45+34*54/566-343*4+34
        """
        string = "34/4*6"
        plus = string.count("+")
        multi = string.count("*")
        sous = string.count('-')
        div = string.count('/')
        if multi:
            m = string.split("*")
            for s in m:
                self.calcule(s)




if __name__ == '__main__' :
    pass

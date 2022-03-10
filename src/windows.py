class Main:
    def __init__(self, d):
        self.run = False
        self.vid = cv2.VideoCapture(0)      # capture video with webcam
        self.hand = HandTracking(nb_hands=1)
        self.c = d
        self.DEFAULT = ((123, 0, 123), 2)

    def winsize(self, width=1000, height=800):
        """change the size of the windows cam"""
        self.vid.set(3, width), self.vid.set(4, height)

    def running(self):
        """change the value of run variable"""
        self.run = True

    @staticmethod
    def show(img, title="my capture video"):
        """this function aloaws to screening image"""
        cv2.imshow(title, img)
        cv2.waitKey(1)

    def draw_number(self, img):
        """ create same text in the rectagle """
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        color = (255, 5, 10)
        cv2.putText(img, str(self.c["1v"]), (64, 220), font, 5, color, 5)
        cv2.putText(img, str(self.c["4v"]), (64, 365), font, 5, color, 5)
        cv2.putText(img, str(self.c["7v"]), (64, 520), font, 5, color, 5)
        cv2.putText(img, str(self.c["+v"]), (64, 680), font, 5, color, 5)
        cv2.putText(img, str(self.c["2v"]), (256, 220), font, 5, color, 5)
        cv2.putText(img, str(self.c["5v"]), (256, 370), font, 5, color, 5)
        cv2.putText(img, str(self.c["8v"]), (256, 520), font, 5, color, 5)
        cv2.putText(img, str(self.c["0v"]), (256, 680), font, 5, color, 5)
        cv2.putText(img, str(self.c["3v"]), (450, 220), font, 5, color, 5)
        cv2.putText(img, str(self.c["6v"]), (450, 370), font, 5, color, 5)
        cv2.putText(img, str(self.c["9v"]), (450, 520), font, 5, color, 5)
        cv2.putText(img, str(self.c["=v"]), (450, 680), font, 5, color, 5)

    @staticmethod
    def draw_calcul(img, tup_top, tup_bot, color, taille):
        # main cadre
        cv2.rectangle(img, tup_top, tup_bot, color, taille)

    @staticmethod
    def finger_detection(x, y, tuple1, tuple2, v):
        point = (x, y)
        is_in = Geometry.is_in(point, tuple1, tuple2)
        if is_in:
            return v
        else:
            return ""

    def values(self, x, y, which):
        color, taille = (123, 60, 120), 20

        if which == 1:
            v = self.finger_detection(x, y, self.c['1top'], self.c['1bom'], self.c['1v'])
            if v:
                return v, (color, taille)
            else:
                return "nan", self.DEFAULT
        if which == 2:
            v = self.finger_detection(x, y, self.c['2top'], self.c['2bom'], self.c['4v'])
            if v:
                return v, (color, taille)
            else:
                return "nan", self.DEFAULT
        if which == 3:
            v = self.finger_detection(x, y, self.c['3top'], self.c['3bom'], self.c['7v'])
            if v:
                return v, (color, taille)
            else:
                return "nan", self.DEFAULT
        if which == 4:
            v = self.finger_detection(x, y, self.c['4top'], self.c['4bom'], self.c['+v'])
            if v:
                return v, (color, taille)
            else:
                return "nan", self.DEFAULT
        if which == 5:
            v = self.finger_detection(x, y, self.c['5top'], self.c['5bom'], self.c['2v'])
            if v:
                return v, (color, taille)
            else:
                return "nan", self.DEFAULT
        if which == 6:
            v = self.finger_detection(x, y, self.c['6top'], self.c['6bom'], self.c['5v'])
            if v:
                return v, (color, taille)
            else:
                return "nan", self.DEFAULT
        if which == 7:
            v = self.finger_detection(x, y, self.c['7top'], self.c['7bom'], self.c['8v'])
            if v:
                return v, (color, taille)
            else:
                return "nan", self.DEFAULT
        if which == 8:
            v = self.finger_detection(x, y, self.c['8top'], self.c['8bom'], self.c['0v'])
            if v == 0:
                return v, (color, taille)
            else:
                return "nan", self.DEFAULT
        if which == 9:
            v = self.finger_detection(x, y, self.c['9top'], self.c['9bom'], self.c['3v'])
            if v:
                return v, (color, taille)
            else:
                return "nan", self.DEFAULT
        if which == 10:
            v = self.finger_detection(x, y, self.c['10top'], self.c['10bom'], self.c['6v'])
            if v:
                return v, (color, taille)
            else:
                return "nan", self.DEFAULT
        if which == 11:
            v = self.finger_detection(x, y, self.c['11top'], self.c['11bom'], self.c['9v'])
            if v:
                return v, (color, taille)
            else:
                return "nan", self.DEFAULT
        if which == 12:
            v = self.finger_detection(x, y, self.c['12top'], self.c['12bom'], self.c['=v'])
            if v:
                return v, (color, taille)
            else:
                return "nan", self.DEFAULT

    def main_loop(self):
        while self.run:
            cool, img = self.vid.read()
            img = self.hand.detectingHand(img, draw=False)
            listcoord = self.hand.positionPoint(img, andPoint=False)
            cv2.rectangle(img, (20, 100), (600, 700), (255, 123, 0), 1)

            color1, taille1 = self.DEFAULT
            color2, taille2 = self.DEFAULT
            color3, taille3 = self.DEFAULT
            color4, taille4 = self.DEFAULT
            color5, taille5 = self.DEFAULT
            color6, taille6 = self.DEFAULT
            color7, taille7 = self.DEFAULT
            color8, taille8 = self.DEFAULT
            color9, taille9 = self.DEFAULT
            color10, taille10 = self.DEFAULT
            color11, taille11 = self.DEFAULT
            color12, taille12 = self.DEFAULT

            if len(listcoord) != 0:
                x = listcoord[8][1]
                y = listcoord[8][2]
                # now = int(round(time.time()))
                # print(f" x  = {x} / y = {y}")
                color1, taille1 = self.values(x, y, 1)[1]
                color2, taille2 = self.values(x, y, 2)[1]
                color3, taille3 = self.values(x, y, 3)[1]
                color4, taille4 = self.values(x, y, 4)[1]
                color5, taille5 = self.values(x, y, 5)[1]
                color6, taille6 = self.values(x, y, 6)[1]
                color7, taille7 = self.values(x, y, 7)[1]
                color8, taille8 = self.values(x, y, 8)[1]
                color9, taille9 = self.values(x, y, 9)[1]
                color10, taille10 = self.values(x, y, 10)[1]
                color11, taille11 = self.values(x, y, 11)[1]
                color12, taille12 = self.values(x, y, 12)[1]

            self.draw_calcul(img, self.c["1top"], self.c["1bom"], color1, taille1)
            self.draw_calcul(img, self.c["2top"], self.c["2bom"], color2, taille2)
            self.draw_calcul(img, self.c["3top"], self.c["3bom"], color3, taille3)
            self.draw_calcul(img, self.c["4top"], self.c["4bom"], color4, taille4)
            # second column
            self.draw_calcul(img, self.c["5top"], self.c["5bom"], color5, taille5)
            self.draw_calcul(img, self.c["6top"], self.c["6bom"], color6, taille6)
            self.draw_calcul(img, self.c["7top"], self.c["7bom"], color7, taille7)
            self.draw_calcul(img, self.c["8top"], self.c["8bom"], color8, taille8)
            # third
            self.draw_calcul(img, self.c["9top"], self.c["9bom"], color9, taille9)
            self.draw_calcul(img, self.c["10top"], self.c["10bom"], color10, taille10)
            self.draw_calcul(img, self.c["11top"], self.c["11bom"], color11, taille11)
            self.draw_calcul(img, self.c["12top"], self.c["12bom"], color12, taille12)
            # drawing number
            self.draw_number(img)
            self.show(img, title="calculatrice")


if __name__ == "__main__":
    import cv2
    from handTracking import HandTracking
    from coordo import *
    from geometry import Geometry
    # import time

    main = Main(dico)
    main.winsize()

    print("voulez vous faire tourner le programme ??")
    c = input("soit [o/n]")
    if c == "o":
        main.running()
        main.main_loop()
    else:
        print(" A plus")

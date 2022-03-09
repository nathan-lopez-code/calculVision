class Main:
    def __init__(self, d):
        self.run = False
        self.vid = cv2.VideoCapture(0)      # capture video with webcam
        self.hand = HandTracking(nb_hands=1)
        self.c = d

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

    def draw_calcul(self, img):
        # main cadre
        cv2.rectangle(img, (20, 100), (600, 700), (255, 123, 0), 1)
        # first column
        cv2.rectangle(img, self.c["1top"], self.c["1bom"], (25, 123, 12), 2)
        cv2.rectangle(img, self.c["2top"], self.c["2bom"], (25, 123, 12), 2)
        cv2.rectangle(img, self.c["3top"], self.c["3bom"], (25, 123, 12), 2)
        cv2.rectangle(img, self.c["4top"], self.c["4bom"], (25, 123, 12), 2)
        # second column
        cv2.rectangle(img, self.c["5top"], self.c["5bom"], (25, 123, 12), 2)
        cv2.rectangle(img, self.c["6top"], self.c["6bom"], (25, 123, 12), 2)
        cv2.rectangle(img, self.c["7top"], self.c["7bom"], (25, 123, 12), 2)
        cv2.rectangle(img, self.c["8top"], self.c["8bom"], (25, 123, 12), 2)
        # third
        cv2.rectangle(img, self.c["9top"], self.c["9bom"], (25, 123, 12), 2)
        cv2.rectangle(img, self.c["10top"], self.c["10bom"], (25, 123, 12), 2)
        cv2.rectangle(img, self.c["11top"], self.c["11bom"], (25, 123, 12), 2)
        cv2.rectangle(img, self.c["12top"], self.c["12bom"], (25, 123, 12), 2)

        self.draw_number(img)

    @staticmethod
    def finger_detection(x, y, tuple1, tuple2, v):
        point = (x, y)
        is_in = Geometry.is_in(point, tuple1, tuple2)
        if is_in:
            return v
        else:
            return ""

    def values(self, x, y, which, now):
        delay = now + 10
        if which == 1:
            return self.finger_detection(x, y, self.c['1top'], self.c['1bom'], self.c['1v'])
        if which == 2:
            return self.finger_detection(x, y, self.c['2top'], self.c['2bom'], self.c['2v'])
        if which == 3:
            return self.finger_detection(x, y, self.c['3top'], self.c['3bom'], self.c['3v'])
        if which == 4:
            return self.finger_detection(x, y, self.c['4top'], self.c['4bom'], self.c['4v'])
        if which == 5:
            return self.finger_detection(x, y, self.c['5top'], self.c['5bom'], self.c['5v'])
        if which == 6:
            return self.finger_detection(x, y, self.c['6top'], self.c['6bom'], self.c['6v'])
        if which == 7:
            return self.finger_detection(x, y, self.c['7top'], self.c['7bom'], self.c['7v'])
        if which == 8:
            return self.finger_detection(x, y, self.c['8top'], self.c['8bom'], self.c['8v'])
        if which == 9:
            return self.finger_detection(x, y, self.c['9top'], self.c['9bom'], self.c['9v'])
        if which == 10:
            return self.finger_detection(x, y, self.c['10top'], self.c['10bom'], self.c['10v'])
        if which == 11:
            return self.finger_detection(x, y, self.c['11top'], self.c['11bom'], self.c['11v'])
        if which == 12:
            return self.finger_detection(x, y, self.c['12top'], self.c['12bom'], self.c['12v'])

    def main_loop(self):
        while self.run:
            cool, img = self.vid.read()
            img = self.hand.detectingHand(img, draw=False)
            listcoord = self.hand.positionPoint(img, andPoint=False)
            if len(listcoord) != 0:
                x = listcoord[8][1]
                y = listcoord[8][2]
                now = int(round(time.time()))
                # print(f" x  = {x} / y = {y}")
                print(self.values(x, y, 1, now))
                print(self.values(x, y, 2, now))
                print(self.values(x, y, 3, now))
                print(self.values(x, y, 4, now))
                print(self.values(x, y, 5, now))
                print(self.values(x, y, 6, now))
                print(self.values(x, y, 7, now))
                print(self.values(x, y, 8, now))
                print(self.values(x, y, 9, now))
                print(self.values(x, y, 10, now))
                print(self.values(x, y, 11, now))
                print(self.values(x, y, 12, now))



            self.draw_calcul(img)
            self.show(img, title="calculatrice")


if __name__ == "__main__":
    import cv2
    from handTracking import HandTracking
    from coordo import *
    from geometry import Geometry
    import time

    main = Main(dico)
    main.winsize()

    print("voulez vous faire tourner le programme ??")
    c = input("soit [o/n]")
    if c == "o":
        main.running()
        main.main_loop()
    else:
        print(" A plus")

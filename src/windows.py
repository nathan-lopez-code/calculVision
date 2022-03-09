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

    @staticmethod
    def draw_number(img):
        """ create same text in the rectagle """
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        color = (255, 5, 10)
        cv2.putText(img, "1", (64, 220), font, 5, color, 5)
        cv2.putText(img, "4", (64, 365), font, 5, color, 5)
        cv2.putText(img, "7", (64, 520), font, 5, color, 5)
        cv2.putText(img, "+", (64, 680), font, 5, color, 5)
        cv2.putText(img, "2", (256, 220), font, 5, color, 5)
        cv2.putText(img, "5", (256, 370), font, 5, color, 5)
        cv2.putText(img, "8", (256, 520), font, 5, color, 5)
        cv2.putText(img, "0", (256, 680), font, 5, color, 5)
        cv2.putText(img, "3", (450, 220), font, 5, color, 5)
        cv2.putText(img, "6", (450, 370), font, 5, color, 5)
        cv2.putText(img, "9", (450, 520), font, 5, color, 5)
        cv2.putText(img, "=", (450, 680), font, 5, color, 5)

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

    def main_lopp(self):
        while self.run:
            cool, img = self.vid.read()
            img = self.hand.detectingHand(img, draw=False)
            listcoord = self.hand.positionPoint(img, andPoint=False)
            if len(listcoord) != 0:






            self.draw_calcul(img)
            self.show(img, title="calculatrice")


if __name__ == "__main__":
    import cv2
    from handTracking import HandTracking
    from coordo import *
    from geometry import Geometry

    main = Main(dico)
    main.winsize()

    print("voulez vous faire tourner le programme ??")
    c = input("soit [o/n]")
    if c == "o":
        main.running()
        main.main_lopp()
    else:
        print(" A plus")

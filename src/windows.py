
class Main:
    def __init__(self):
        self.run = False
        self.vid = cv2.VideoCapture(0)      # capture video with webcam
        self.hand = HandTracking(nb_hands=1)
        self.c = {
            "1top": (20, 100),
            "1bom": (213, 250),
            "2top": (20, 250),
            "2bom": (213, 400),
            "3top": (20, 400),
            "3bom": (213, 550),
            "4top": (20, 550),
            "4bom": (213, 700),
            "5top": (213, 100),
            "5bom": (406, 250),
            "6top": (213, 250), "6bom": (406, 400),
            "7top": (213, 400), "7bom": (406, 550),
            "8top": (213, 550), "8bom": (406, 700),
            "9top": (406, 100), "9bom": (600, 250),
            "10top": (406, 250), "10bom": (600, 400),
            "11top": (406, 400), "11bom": (600, 550),
            "12top": (406, 550), "12bom": (600, 700),

        }

    def winsize(self, width=1000, height=800):
        """change the size of the windows cam"""
        self.vid.set(3, width), self.vid.set(4, height)

    def running(self):
        """change the value of run variable"""
        self.run = True

    def show(self, img, title="my capture video"):
        """this function aloaws to screening image"""
        cv2.imshow(title, img)
        cv2.waitKey(1)


 # def putText(img, text, org, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=None): # real signature unknown; restored from __doc__

    def draw_number(self, img):
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


    def draw_calcl(self, img):

        # main cadre
        cv2.rectangle(img, (20, 100), (600, 700), (255, 123, 0), 1)

        # first column
        cv2.rectangle(img, self.c["1top"], self.c["1bom"], (25, 123, 12), 2)
        cv2.rectangle(img, self.c["2top"], self.c["2bom"], (25, 123, 12), 2)
        cv2.rectangle(img, (20, 400), (213, 550), (25, 123, 12), 2)
        cv2.rectangle(img, (20, 550), (213, 700), (25, 123, 12), 2)
        # second column
        cv2.rectangle(img, (213, 100), (406, 250), (25, 123, 12), 2)
        cv2.rectangle(img, (213, 250), (406, 400), (25, 123, 12), 2)
        cv2.rectangle(img, (213, 400), (406, 550), (25, 123, 12), 2)
        cv2.rectangle(img, (213, 550), (406, 700), (25, 123, 12), 2)
        # third
        cv2.rectangle(img, (406, 100), (600, 250), (25, 123, 12), 2)
        cv2.rectangle(img, (406, 250), (600, 400), (25, 123, 12), 2)
        cv2.rectangle(img, (406, 400), (600, 550), (25, 123, 12), 2)
        cv2.rectangle(img, (406, 550), (600, 700), (25, 123, 12), 2)

        self.draw_number(img)



    def main_lopp(self):
        while self.run:
            cool, img = self.vid.read()
            img = self.hand.detectingHand(img, draw=False)
            listcoord = self.hand.positionPoint(img, andPoint=False)
            if len(listcoord) != 0:
                print(listcoord[4])
                print("**************")

            self.draw_calcl(img)
            self.show(img, title="calculatrice")


if __name__ == "__main__":
    #import mediapipe as mp
    import cv2
    from handTracking import HandTracking
    from cordo import *

    main = Main()
    main.winsize()

    print("voulez vous faire tourner le programme ??")
    c = input("soit [o/n]")
    #if c == "o":
    main.running()
    main.main_lopp()
    #else:
    #    print(" A plus")

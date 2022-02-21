
class Main:
    def __init__(self):
        self.run = False
        self.vid = cv2.VideoCapture(0)      # capture video with webcam
        self.hand = HandTracking(nb_hands=1)

    def winsize(self, width=1000, height=800):
        """change the size of the windows cam"""
        self.vid.set(3, width), self.vid.set(4, height)

    def running(self):
        """change the value of run variable"""
        self.run = True

    def show(self, img, title="my capture video"):
        """this function alone to screening image"""
        cv2.imshow(title, img)
        cv2.waitKey(1)


    def draw_calcl(self, img):

        cv2.rectangle(img, (20, 100), (600, 700), (255, 123, 0), 1)


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

    main = Main()
    main.winsize()

    print("voulez vous faire tourner le programme ??")
    c = input("soit [o/n]")
    if c == "o":
        main.running()
        main.main_lopp()
    else:
        print(" A plus")

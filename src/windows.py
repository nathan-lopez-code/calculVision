class Main:
    def __init__(self, d):
        self.run = False
        self.vid = cv2.VideoCapture(0)      # capture video with webcam
        self.hand = HandTracking(nb_hands=1)
        self.c = d
        self.DEFAULT = ((123, 0, 123), 2)
        self.DEFAULT_VALUE = -1
        self.font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        self.init_value()
        self.speed = 5

    def init_value(self):
        self.value1 = self.DEFAULT_VALUE
        self.value2 = self.DEFAULT_VALUE
        self.value3 = self.DEFAULT_VALUE
        self.value4 = self.DEFAULT_VALUE
        self.value5 = self.DEFAULT_VALUE
        self.value6 = self.DEFAULT_VALUE
        self.value7 = self.DEFAULT_VALUE
        self.value8 = self.DEFAULT_VALUE
        self.value9 = self.DEFAULT_VALUE
        self.value10 = self.DEFAULT_VALUE
        self.value11 = self.DEFAULT_VALUE
        self.value12 = self.DEFAULT_VALUE

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

    def draw_number(self, img, font):
        """ create same text in the rectagle """
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
                return v, (color, taille), True
            else:
                return "nan", self.DEFAULT, False
        if which == 2:
            v = self.finger_detection(x, y, self.c['2top'], self.c['2bom'], self.c['4v'])
            if v:
                return v, (color, taille), True
            else:
                return "nan", self.DEFAULT, False
        if which == 3:
            v = self.finger_detection(x, y, self.c['3top'], self.c['3bom'], self.c['7v'])
            if v:
                return v, (color, taille), True
            else:
                return "nan", self.DEFAULT, False
        if which == 4:
            v = self.finger_detection(x, y, self.c['4top'], self.c['4bom'], self.c['+v'])
            if v:
                return v, (color, taille), True
            else:
                return "nan", self.DEFAULT, False
        if which == 5:
            v = self.finger_detection(x, y, self.c['5top'], self.c['5bom'], self.c['2v'])
            if v:
                return v, (color, taille), True
            else:
                return "nan", self.DEFAULT, False
        if which == 6:
            v = self.finger_detection(x, y, self.c['6top'], self.c['6bom'], self.c['5v'])
            if v:
                return v, (color, taille), True
            else:
                return "nan", self.DEFAULT, False
        if which == 7:
            v = self.finger_detection(x, y, self.c['7top'], self.c['7bom'], self.c['8v'])
            if v:
                return v, (color, taille), True
            else:
                return "nan", self.DEFAULT, False
        if which == 8:
            v = self.finger_detection(x, y, self.c['8top'], self.c['8bom'], self.c['0v'])
            if v == 0:
                return v, (color, taille), True
            else:
                return "nan", self.DEFAULT, False
        if which == 9:
            v = self.finger_detection(x, y, self.c['9top'], self.c['9bom'], self.c['3v'])
            if v:
                return v, (color, taille), True
            else:
                return "nan", self.DEFAULT, False
        if which == 10:
            v = self.finger_detection(x, y, self.c['10top'], self.c['10bom'], self.c['6v'])
            if v:
                return v, (color, taille), True
            else:
                return "nan", self.DEFAULT, False
        if which == 11:
            v = self.finger_detection(x, y, self.c['11top'], self.c['11bom'], self.c['9v'])
            if v:
                return v, (color, taille), True
            else:
                return "nan", self.DEFAULT, False
        if which == 12:
            v = self.finger_detection(x, y, self.c['12top'], self.c['12bom'], self.c['=v'])
            if v:
                return v, (color, taille), True
            else:
                return "nan", self.DEFAULT, False

    @staticmethod
    def do_this(fvalue, t, index):
        temp = t[index-1]
        if fvalue not in temp and len(temp) < main.speed+1:
            temp.append(fvalue)
        t = [[], [], [], [], [], [], [], [], [], [], [], [], []]
        t[index-1] = temp

    @staticmethod
    def take_it(t, index, value):
        if len(t[index-1]) >= main.speed:
            return value


    @staticmethod
    def listing(tt):

        if tt.__contains__('3'):
            index = tt.index('3')
            tt[index] = 0
            return 3


        if tt.__contains__('1'):
            index = tt.index('1')
            tt[index] = 0
            return 1

        if tt.__contains__('2'):
            index = tt.index('2')
            tt[index] = 0
            return 2

        if tt.__contains__('3'):
            index = tt.index('3')
            tt[index] = 0
            return 3
        if tt.__contains__('4'):
            index = tt.index('4')
            tt[index] = 0
            return 4
        if tt.__contains__('5'):
            index = tt.index('5')
            tt[index] = 0
            return 5
        if tt.__contains__('6'):
            index = tt.index('6')
            tt[index] = 0
            return 6

        if tt.__contains__('7'):
            index = tt.index('7')
            tt[index] = 0
            return 7
        if tt.__contains__('8'):
            index = tt.index('8')
            tt[index] = 9
            return 8
        if tt.__contains__('9'):
            index = tt.index('9')
            tt[index] = 0
            return 9

        if tt.__contains__('0'):
            index = tt.index('0')
            tt[index] = 0
            return 0
        if tt.__contains__('+'):
            index = tt.index('+')
            tt[index] = 0
            return 11
        if tt.__contains__('='):
            index = tt.index('=')
            tt[index] = 0
            return 12

    def main_loop(self):
        fvalue = int(time.time())
        value = "result"
        t, tt = [[], [], [], [], [], [], [], [], [], [], [], []], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        my_string = ""
        while self.run:
            cool, img = self.vid.read()
            img = self.hand.detectingHand(img, draw=False)
            listcoord = self.hand.positionPoint(img, andPoint=False, draw=False)
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
                is_it1 = self.values(x, y, 1)[2]
                is_it2 = self.values(x, y, 2)[2]
                is_it3 = self.values(x, y, 3)[2]
                is_it4 = self.values(x, y, 4)[2]
                is_it5 = self.values(x, y, 5)[2]
                is_it6 = self.values(x, y, 6)[2]
                is_it7 = self.values(x, y, 7)[2]
                is_it8 = self.values(x, y, 8)[2]
                is_it9 = self.values(x, y, 9)[2]
                is_it10 = self.values(x, y, 10)[2]
                is_it11 = self.values(x, y, 11)[2]
                is_it12 = self.values(x, y, 12)[2]

                if is_it1:
                    color1, taille1 = self.values(x, y, 1)[1]
                    self.value1 = self.values(x, y, 1)[0]
                    self.do_this(fvalue, t, 1)
                elif is_it2:
                    color2, taille2 = self.values(x, y, 2)[1]
                    self.value2 = self.values(x, y, 2)[0]
                    self.do_this(fvalue, t, 2)
                elif is_it3:
                    color3, taille3 = self.values(x, y, 3)[1]
                    self.value3 = self.values(x, y, 3)[0]
                    self.do_this(fvalue, t, 3)
                elif is_it4:
                    color4, taille4 = self.values(x, y, 4)[1]
                    self.value4 = self.values(x, y, 4)[0]
                    self.do_this(fvalue, t, 4)
                elif is_it5:
                    color5, taille5 = self.values(x, y, 5)[1]
                    self.value5 = self.values(x, y, 5)[0]
                    self.do_this(fvalue, t, 5)

                elif is_it6:
                    color6, taille6 = self.values(x, y, 6)[1]
                    self.value6 = self.values(x, y, 6)[0]
                    self.do_this(fvalue, t, 6)

                elif is_it7:
                    color7, taille7 = self.values(x, y, 7)[1]
                    self.value7 = self.values(x, y, 7)[0]
                    self.do_this(fvalue, t, 7)
                elif is_it8:
                    color8, taille8 = self.values(x, y, 8)[1]
                    self.value8 = self.values(x, y, 8)[0]
                    self.do_this(fvalue, t, 8)
                elif is_it9:
                    color9, taille9 = self.values(x, y, 9)[1]
                    self.value9 = self.values(x, y, 9)[0]
                    self.do_this(fvalue, t, 9)
                elif is_it10:
                    color10, taille10 = self.values(x, y, 10)[1]
                    self.value10 = self.values(x, y, 10)[0]
                    self.do_this(fvalue, t, 10)
                elif is_it11:
                    color11, taille11 = self.values(x, y, 11)[1]
                    self.value11 = self.values(x, y, 11)[0]
                    self.do_this(fvalue, t, 11)
                elif is_it12:
                    color12, taille12 = self.values(x, y, 12)[1]
                    self.value12 = self.values(x, y, 12)[0]
                    self.do_this(fvalue, t, 12)
                else:
                    t = [[], [], [], [], [], [], [], [], [], [], [], [], []]

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
            # show the number
            if self.value1 != self.DEFAULT_VALUE:
               value = str(self.value1)
               tt[0] = self.take_it(t, 1, value)

            if self.value2 != self.DEFAULT_VALUE:
                value = str(self.value2)
                tt[1] = self.take_it(t, 2, value)
            if self.value3 != self.DEFAULT_VALUE:
                value = str(self.value3)
                tt[2] = self.take_it(t, 3, value)

            if self.value4 != self.DEFAULT_VALUE:
                value = str(self.value4)
                tt[3] = self.take_it(t, 4, value)
            if self.value5 != self.DEFAULT_VALUE:
                value = str(self.value5)
                tt[4] = self.take_it(t, 5, value)

            if self.value6 != self.DEFAULT_VALUE:
                value = str(self.value6)
                tt[5] = self.take_it(t, 6, value)

            if self.value7 != self.DEFAULT_VALUE:
                value = str(self.value7)
                tt[6] = self.take_it(t, 7, value)

            if self.value8 != self.DEFAULT_VALUE:
                value = str(self.value8)
                tt[7] = self.take_it(t, 8, value)

            if self.value9 != self.DEFAULT_VALUE:
                value = str(self.value9)
                tt[8] = self.take_it(t, 9, value)

            if self.value10 != self.DEFAULT_VALUE:
                value = str(self.value10)
                tt[9] = self.take_it(t, 10, value)

            if self.value11 != self.DEFAULT_VALUE:
                value = str(self.value11)
                tt[10] = self.take_it(t, 11, value)

            if self.value12 != self.DEFAULT_VALUE:
                value = str(self.value12)
                tt[11] = self.take_it(t, 12, value)

            # write text in windows
            cv2.putText(img, str(fvalue), (950, 120), self.font, 1, (234, 66, 7), 1)
            # cv2.putText(img, str(tt), (950, 200), self.font, 1, (234, 66, 7), 1)
            print(tt)
            print("\n *************** \n")
            self.init_value()
            fvalue = int(time.time())
            if value:
                vals = Main.listing(tt)
                if vals == 11:
                    vals = "+"
                elif vals == 12:
                    vals = "="
                if vals != None:
                    l = len(my_string)

                    if l > 0:
                        if my_string[l-1] == str(vals) or my_string[l-1] == vals:
                            my_string = my_string
                        else:
                            my_string = my_string + str(vals)
                    else:
                        my_string = my_string + str(vals)

            print("\n\n" + my_string)
            if my_string != "":
                cv2.putText(img, my_string, (950, 70), self.font, 1, (234, 66, 7), 1)
            else:
                cv2.putText(img, "resulte", (950, 70), self.font, 1, (234, 66, 7), 1)



            # show windows and draw  number
            self.draw_number(img, self.font)
            self.show(img, title="calculatrice")



if __name__ == "__main__":
    import cv2
    from handTracking import HandTracking
    from coordo import *
    from geometry import Geometry
    import time

    main = Main(dico)
    main.winsize(width=1500, height=1200)

    #print("voulez vous faire tourner le programme ??")
    c = "o"            # input("soit [o/n]")
    if c == "o":
        print("starting streaming")
        main.running()
        main.main_loop()
    else:
        print(" A plus")

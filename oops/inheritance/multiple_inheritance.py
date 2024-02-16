class p1:
    def m1(self):
        print("inside parent 1")

class p2:
    def m1(self):
        print("inside parent 2")

class child(p1,p2):
    def m3(self):
        print("inside child")

ch=child()
ch.m1()
class p1:
    def m1(self):
        print("inside p1")

class p2(p1):
    def m1(self):
        print("inside p2")

class child(p2):
    def m3(self):
        print("inside child")

ch=child()
ch.m1()

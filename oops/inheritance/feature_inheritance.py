# inheritance

class parent:
    def mobile(self):
        print("samsung")

    def bike(self):
        print("passionpro")

class child(parent):
    pass

obj=child()
obj.mobile()
obj.bike()
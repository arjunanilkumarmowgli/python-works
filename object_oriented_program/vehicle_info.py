class GrandParent:
    def m(self):
        print("Grand parent class m method")
class parent():
    def m(self):
        print("parent calss m method")
class Child(GrandParent,parent):
    def m3(self):
        print("child class m3 method")

child_instance=Child()
child_instance.m3()
child_instance.m

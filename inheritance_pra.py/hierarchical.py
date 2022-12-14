class parent:
    def parent_function(self):
        print("this is parent class")
class child1(parent):
    def ch_1function(self):
        print("This is child_1 class")
class child2(parent):
    def ch_2function(self):
        print("This is child_2 class")

ob_ch1 = child1()
ob_ch2 = child2()
ob_ch1.parent_function()
ob_ch2.parent_function()
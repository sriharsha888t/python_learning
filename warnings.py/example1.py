# warning example
import warnings
class warningex:
    def __init__(self):
        self.text = "warning"

    def method1(self):
        warnings.warn("method 1 is deprecated,use new method instead",DeprecationWarning)

        print("method1",len(self.text))
    def method2(self):
        warnings.warn("method 2 is deprecated in version,use new method instead",PendingDeprecationWarning)

        print("method2",len(self.text))
    def new_method(self):
        print("new method",len(self.text))

if __name__ == '__main__':
  e = warningex()
  e.method1()
  e.method2()
  e.new_method()
#print(warnings.simplefilter("default"))
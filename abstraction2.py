from abc import ABC,abstractmethod
class parent(ABC):
    def common_fn(self):
        print("in the common method parent")

    @abstractmethod
    def abs_fn(self):
        pass
class child1(parent):
    def abs_fn(self):
        print("In the abstract method of child1")

class child2(parent):
    def abs_fn(self):
        print("In the abstract method of child2")

c1 = child1()
c1.abs_fn()



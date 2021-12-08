from typing import Any, Callable

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self,value: Any):
        self.value= value
        self.left_child=None
        self.right_child=None

    def __str__(self):
        wynik = str(self.value)
        return wynik

    def is_leaf(self):
        if(self.left_child is None and self.right_child is None):
            return True
        else:
            return False



    def add_left_child(self, value: Any):
        self.left_child=value



    def add_right_child(self,value: Any):
        self.right_child=value


    def traverse_in_order(self, visit: Callable[[Any], None]):

        if (self.left_child):
            self.left_child.traverse_in_order(visit)

        visit(self)

        if self.right_child:
            self.right_child.traverse_in_order(visit)
    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        if (self.left_child):
            self.left_child.traverse_pre_order(visit)

        if(self.right_child):
            self.right_child.traverse_pre_order(visit)

    def traverse_post_order(self,visit: Callable[[Any],None]):
        if(self.left_child):
            self.left_child.traverse_post_order(visit)
        if(self.right_child):
            self.right_child.traverse_post_order(visit)
        visit(self)









class BinaryTree:
    root: BinaryNode

    def __init__(self,root):
        self.root=root

    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)


def fun(x):
    print(x)


ten=BinaryNode(10)

tree=BinaryTree(ten)

nine=BinaryNode(9)
ten.add_left_child(nine)

one=BinaryNode(1)
nine.add_left_child(one)

three=BinaryNode(3)
nine.add_right_child(three)

two=BinaryNode(2)
ten.add_right_child(two)

four=BinaryNode(4)
two.add_left_child(four)

six=BinaryNode(6)
two.add_right_child(six)
print(six)
ten.traverse_post_order(fun)
ten.traverse_pre_order(fun)
ten.traverse_in_order(fun)
print("\n")
tree.traverse_in_order(fun)
assert tree.root.value == 10
assert tree.root.right_child.value == 2
assert tree.root.right_child.is_leaf() is False
assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True
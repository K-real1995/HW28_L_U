# Реализовать класс элемента дерева, который может содержать произвольное число детей - объектов этого же класса
# и некоторый текст. Реализовать метод у класса, позволяющий вывести текст указанный во всех элементах дерева.
lst = []


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        lst.append(self)

    def __repr__(self):
        return f"TreeNode со значением {self.val}"

    @staticmethod
    def print_text():
        for i in range(len(lst)):
            print(lst[i])


# Уровень 0
root = TreeNode('a')

# Уровень 1
root.left = TreeNode('b')
root.right = TreeNode('c')

# Уровень 2
root.left.left = TreeNode('d')
root.left.right = TreeNode('e')

root.right.left = TreeNode('f')
root.right.right = TreeNode('g')


TreeNode.print_text()

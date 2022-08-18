# Нарисовать дерево, используя библиотеку graphviz в питоне
from graphviz import Digraph

tree_branch = Digraph(comment='TreeNode')

tree_branch.node('A', 'TreeNode со значением A')
tree_branch.node('B', 'TreeNode со значением B')
tree_branch.node('C', 'TreeNode со значением C')
tree_branch.node('D', 'TreeNode со значением D')
tree_branch.node('E', 'TreeNode со значением E')
tree_branch.node('F', 'TreeNode со значением F')
tree_branch.node('G', 'TreeNode со значением G')

tree_branch.edges(['AB', 'AC', 'BD', 'BE', 'CF', 'CG'])
tree_branch.view()

print(tree_branch.source)


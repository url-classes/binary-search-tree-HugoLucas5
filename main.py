from binary_search_tree import BinarySearchTree
numeros: BinarySearchTree[int] = BinarySearchTree()
numeros.insert(60)



print(numeros.preorder())
numeros.delete(60)
print(numeros.preorder())
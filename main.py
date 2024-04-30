from binary_search_tree import BinarySearchTree
numeros: BinarySearchTree[int] = BinarySearchTree()
numeros.insert(60)
numeros.insert(12)
numeros.insert(90)
numeros.insert(80)
numeros.insert(100)



print(numeros.preorder())
numeros.delete(12)
numeros.delete(60)
numeros.insert(12)
numeros.insert(95)
numeros.insert(101)
print(numeros.preorder())
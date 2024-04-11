from binary_search_tree import BinarySearchTree
numeros: BinarySearchTree[int] = BinarySearchTree()
numeros.insert(60)
numeros.insert(12)
numeros.insert(90)
numeros.insert(4)
numeros.insert(41)
numeros.insert(71)
numeros.insert(99)
numeros.insert(29)
numeros.insert(84)
numeros.insert(23)
numeros.insert(37)


print(numeros.preorder())
numeros.delete(60)
print(numeros.preorder())
print("Nodo maximo: ")
print(numeros.max())
print("Nodo minimo: ")
print(numeros.min())
print(numeros.search(37))
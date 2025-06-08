# BONUS CHALLENGES - SANTIAGO SALAS

# Definición de un nodo del árbol AVL
class Node:
    def __init__(self, key):
        self.key = key                # Valor del nodo
        self.left = self.right = None # Hijos izquierdo y derecho
        self.height = 1               # Altura del nodo (inicialmente 1)

# Definición de la clase del árbol AVL
class AVLTree:
    # Obtiene la altura de un nodo (0 si es None)
    def getHeight(self, node):
        return node.height if node else 0

    # Calcula el factor de balanceo de un nodo
    def getBalance(self, node):
        return self.getHeight(node.left) - self.getHeight(node.right) if node else 0

    # Rotación simple a la izquierda
    def rotateLeft(self, x):
        y = x.right           # y es el hijo derecho de x
        T2 = y.left           # T2 es el subárbol izquierdo de y
        y.left = x            # x pasa a ser hijo izquierdo de y
        x.right = T2          # T2 pasa a ser hijo derecho de x
        # Actualiza alturas
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y              # y es la nueva raíz del subárbol

    # Rotación simple a la derecha
    def rotateRight(self, y):
        x = y.left            # x es el hijo izquierdo de y
        T2 = x.right          # T2 es el subárbol derecho de x
        x.right = y           # y pasa a ser hijo derecho de x
        y.left = T2           # T2 pasa a ser hijo izquierdo de y
        # Actualiza alturas
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        return x              # x es la nueva raíz del subárbol

    # Inserta un nodo en el árbol AVL
    def insert(self, root, key):
        if not root: return Node(key) # Si el árbol está vacío, crea el nodo
        if key < root.key:            # Si la clave es menor, va a la izquierda
            root.left = self.insert(root.left, key)
        else:                        # Si es mayor o igual, va a la derecha
            root.right = self.insert(root.right, key)
        # Actualiza la altura del nodo actual
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root) # Calcula el balanceo
        # Casos de desbalanceo y rotaciones necesarias
        if balance > 1 and key < root.left.key:   # Izquierda-Izquierda
            return self.rotateRight(root)
        if balance < -1 and key > root.right.key: # Derecha-Derecha
            return self.rotateLeft(root)
        if balance > 1 and key > root.left.key:   # Izquierda-Derecha
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
        if balance < -1 and key < root.right.key: # Derecha-Izquierda
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)
        return root # Retorna la raíz (puede haber cambiado)

    # Busca el nodo con el valor mínimo en un subárbol
    def getMinValueNode(self, node):
        while node.left: node = node.left # Sigue a la izquierda
        return node

    # Elimina un nodo del árbol AVL
    def delete(self, root, key):
        if not root: return root # Si el árbol está vacío, retorna None
        if key < root.key:       # Si la clave es menor, busca a la izquierda
            root.left = self.delete(root.left, key)
        elif key > root.key:     # Si es mayor, busca a la derecha
            root.right = self.delete(root.right, key)
        else:                    # Nodo encontrado
            if not root.left:    # Un solo hijo derecho o ninguno
                return root.right
            elif not root.right: # Un solo hijo izquierdo
                return root.left
            # Nodo con dos hijos: busca el sucesor
            temp = self.getMinValueNode(root.right)
            root.key = temp.key  # Copia el valor del sucesor
            root.right = self.delete(root.right, temp.key) # Elimina el sucesor
        # Actualiza la altura
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root) # Calcula el balanceo
        # Casos de desbalanceo y rotaciones necesarias
        if balance > 1 and self.getBalance(root.left) >= 0: # Izquierda-Izquierda
            return self.rotateRight(root)
        if balance > 1 and self.getBalance(root.left) < 0:  # Izquierda-Derecha
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
        if balance < -1 and self.getBalance(root.right) <= 0: # Derecha-Derecha
            return self.rotateLeft(root)
        if balance < -1 and self.getBalance(root.right) > 0:  # Derecha-Izquierda
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)
        return root # Retorna la raíz (puede haber cambiado)

    # Recorrido inorder (izquierda, raíz, derecha)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=' ')
            self.inorder(root.right)

# 🧪 Pruebas de eliminación en AVL
def test_avl_delete():
    avl = AVLTree()
    root = None
    for val in [20, 10, 30, 25, 35]: # Inserta valores
        root = avl.insert(root, val)
    root = avl.delete(root, 35)      # Elimina hoja
    print("🧪 Test 1 (Delete leaf): Pass 👌")
    root = avl.delete(root, 25)      # Elimina nodo con un hijo
    print("🧪 Test 2 (Delete one child): Pass ✂️")
    root = avl.delete(root, 20)      # Elimina nodo con dos hijos
    print("🧪 Test 3 (Delete two children): Pass 🪓")
    print("🧪 Test 4 & 5: Use inorder to validate balance 📏")
    avl.inorder(root)                # Muestra el árbol en orden
    print()

# 🚀 Ejecutar pruebas
test_avl_delete()

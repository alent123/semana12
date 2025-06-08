# Challenge 1: 🌪️ Auto-Balance After Insert 
# CRISTIAN RUFYNO
# Definición del nodo del árbol AVL
class AVLNode:
    def __init__(self, key):
        self.key = key                  # Valor de la clave del nodo
        self.left = self.right = None   # Hijos izquierdo y derecho
        self.height = 1                 # Altura del nodo

# Definición del árbol AVL
class AVLTree:
    # Inserta un nodo en el árbol y balancea si es necesario
    def insert(self, root, key):
        if not root:                                # Si el árbol está vacío
            return AVLNode(key)                     # Crear un nuevo nodo
        if key < root.key:                          # Si la clave es menor, ir a la izquierda
            root.left = self.insert(root.left, key)
        else:                                       # Si es mayor o igual, ir a la derecha
            root.right = self.insert(root.right, key)

        # Actualizar la altura del nodo actual
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        # Calcular el factor de balanceo
        balance = self.get_balance(root)

        # Si el nodo está desbalanceado, hay 4 casos
        if balance > 1:
            if key < root.left.key:                 # Caso LL
                return self.rotate_right(root)
            else:                                   # Caso LR
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
        if balance < -1:
            if key > root.right.key:                # Caso RR
                return self.rotate_left(root)
            else:                                   # Caso RL
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)
        return root                                 # Retornar el nodo (posiblemente nuevo raíz)

    # Devuelve la altura de un nodo
    def height(self, node):
        return node.height if node else 0

    # Calcula el factor de balanceo de un nodo
    def get_balance(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    # Rotación simple a la izquierda
    def rotate_left(self, z):
        y = z.right
        z.right, y.left = y.left, z
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    # Rotación simple a la derecha
    def rotate_right(self, z):
        y = z.left
        z.left, y.right = y.right, z
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    # Recorrido inorder (izquierda, raíz, derecha)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

# Función para probar la inserción en el árbol AVL
def test_avl_insert():
    avl = AVLTree()

    root = None
    for val in [10, 20, 30]:
        root = avl.insert(root, val)
    print("🧪 Test 1 (RR):", end=" ")
    avl.inorder(root)  # Esperado: 10 20 30
    print()

    avl = AVLTree()
    root = None
    for val in [30, 20, 10]:
        root = avl.insert(root, val)
    print("🧪 Test 2 (LL):", end=" ")
    avl.inorder(root)  # Esperado: 10 20 30
    print()

    avl = AVLTree()
    root = None
    for val in [30, 10, 20]:
        root = avl.insert(root, val)
    print("🧪 Test 3 (LR):", end=" ")
    avl.inorder(root)  # Esperado: 10 20 30
    print()

    avl = AVLTree()
    root = None
    for val in [10, 30, 20]:
        root = avl.insert(root, val)
    print("🧪 Test 4 (RL):", end=" ")
    avl.inorder(root)  # Esperado: 10 20 30
    print()

    avl = AVLTree()
    root = None
    for val in [15, 10, 20, 25, 30]:
        root = avl.insert(root, val)
    print("🧪 Test 5 (Balanced):", end=" ")
    avl.inorder(root)  # Esperado: 10 15 20 25 30
    print()

# 🚀 Ejecutar todas las pruebas
test_avl_insert()
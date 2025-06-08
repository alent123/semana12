#RONY BELLIDO
class AVLNode:
    def __init__(self, key):
        self.key = key              # Valor del nodo
        self.left = None            # Hijo izquierdo
        self.right = None           # Hijo derecho
        self.height = 1             # Altura del nodo (inicialmente 1)

class AVLTree:
    def height(self, node):
        # Devuelve la altura de un nodo, o 0 si es None
        return node.height if node else 0

    def update_height(self, node):
        # Actualiza la altura de un nodo según sus hijos
        if node:
            node.height = 1 + max(self.height(node.left), self.height(node.right))

    def get_balance(self, node):
        # Calcula el factor de balanceo de un nodo
        return self.height(node.left) - self.height(node.right) if node else 0

    def rotate_right(self, z):
        # Rotación simple a la derecha
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        self.update_height(z)
        self.update_height(y)
        return y

    def rotate_left(self, z):
        # Rotación simple a la izquierda
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        self.update_height(z)
        self.update_height(y)
        return y

    def insert(self, root, key):
        # Inserta un nodo y balancea el árbol
        if not root:
            return AVLNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # No permite duplicados

        self.update_height(root)
        balance = self.get_balance(root)

        # Casos de desbalanceo y rotaciones
        if balance > 1 and key < root.left.key:      # Izquierda-Izquierda
            return self.rotate_right(root)
        if balance < -1 and key > root.right.key:    # Derecha-Derecha
            return self.rotate_left(root)
        if balance > 1 and key > root.left.key:      # Izquierda-Derecha
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and key < root.right.key:    # Derecha-Izquierda
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def is_avl_balanced(self, root):
        # Verifica si el árbol está balanceado según AVL
        if not root:
            return True

        lh = self.height(root.left)
        rh = self.height(root.right)
        if abs(lh - rh) > 1:
            return False

        return self.is_avl_balanced(root.left) and self.is_avl_balanced(root.right)

# 🧪 Pruebas
def test_is_avl_balanced():
    avl = AVLTree()
    root = None
    for val in [20, 10, 30]:
        root = avl.insert(root, val)
    print("🧪 Test 1:", avl.is_avl_balanced(root) == True)

    # Simula un árbol desbalanceado
    unbalanced = AVLNode(10)
    unbalanced.right = AVLNode(20)
    unbalanced.right.right = AVLNode(30)
    print("🧪 Test 2:", avl.is_avl_balanced(unbalanced) == False)

    print("🧪 Test 3:", avl.is_avl_balanced(None) == True)

test_is_avl_balanced()

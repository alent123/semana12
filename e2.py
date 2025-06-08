# Challenge 2: 🔄 Left & Right Rotations
# CRISTIAN RUFYNO
# Definición de un nodo para el árbol AVL
class AVLNode:
    def __init__(self, key):
        self.key = key            # Valor del nodo
        self.left = None          # Hijo izquierdo
        self.right = None         # Hijo derecho
        self.height = 1           # Altura del nodo

# Definición de la clase para el árbol AVL
class AVLTree:
    # Obtiene la altura de un nodo
    def get_height(self, node):
        return node.height if node else 0

    # Actualiza la altura de un nodo
    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    # Realiza una rotación a la izquierda sobre el nodo z
    def rotate_left(self, z):
        y = z.right           # y es el hijo derecho de z
        T2 = y.left           # T2 es el subárbol izquierdo de y
        y.left = z            # z se convierte en hijo izquierdo de y
        z.right = T2          # T2 se convierte en hijo derecho de z
        self.update_height(z) # Actualiza la altura de z
        self.update_height(y) # Actualiza la altura de y
        return y              # Retorna el nuevo subárbol raíz

    # Realiza una rotación a la derecha sobre el nodo z
    def rotate_right(self, z):
        y = z.left            # y es el hijo izquierdo de z
        T3 = y.right          # T3 es el subárbol derecho de y
        y.right = z           # z se convierte en hijo derecho de y
        z.left = T3           # T3 se convierte en hijo izquierdo de z
        self.update_height(z) # Actualiza la altura de z
        self.update_height(y) # Actualiza la altura de y
        return y              # Retorna el nuevo subárbol raíz

# 🧪 Pruebas de rotaciones
def test_rotations():
    tree = AVLTree()  # Crea un árbol AVL

    # Test 1: Rotación a la izquierda
    z = AVLNode(10)               # Nodo raíz
    z.right = AVLNode(20)         # Hijo derecho
    z.right.right = AVLNode(30)   # Nieto derecho
    z = tree.rotate_left(z)       # Aplica rotación a la izquierda
    print("🧪 Test 1:", z.key == 20)  # Debe imprimir True

    # Test 2: Rotación a la derecha
    z = AVLNode(30)               # Nodo raíz
    z.left = AVLNode(20)          # Hijo izquierdo
    z.left.left = AVLNode(10)     # Nieto izquierdo
    z = tree.rotate_right(z)      # Aplica rotación a la derecha
    print("🧪 Test 2:", z.key == 20)  # Debe imprimir True

    # Test 3–5: Verificación manual de estructura y alturas
    print("🧪 Test 3–5: Check structure manually 👀")

# 🚀 Ejecuta las pruebas
test_rotations()

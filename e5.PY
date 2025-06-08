
#SANTIAGO SALAS
from collections import deque
# Nodo de un árbol AVL
class AVLNode:
    def __init__(self, key):
        self.key = key          # Valor del nodo
        self.left = None        # Hijo izquierdo
        self.right = None       # Hijo derecho
        self.height = 1         # Altura del nodo

# Clase para el árbol AVL
class AVLTree:
    # Devuelve la altura de un nodo (0 si es None)
    def height(self, node):
        return node.height if node else 0

    # Inserta un valor en el árbol y balancea
    def insert(self, root, key):
        if not root:
            return AVLNode(key)  # Si el árbol está vacío, crea nodo nuevo
        if key < root.key:
            root.left = self.insert(root.left, key)   # Inserta a la izquierda
        elif key > root.key:
            root.right = self.insert(root.right, key) # Inserta a la derecha
        else:
            return root  # No permite duplicados

        # Actualiza la altura del nodo actual
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        # Calcula el factor de balanceo
        balance = self.get_balance(root)

        # Casos de rotación para balancear el árbol
        # Rotación simple a la derecha
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)
        # Rotación simple a la izquierda
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)
        # Rotación doble izquierda-derecha
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        # Rotación doble derecha-izquierda
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root  # Devuelve el nodo raíz actualizado

    # Calcula el factor de balanceo de un nodo
    def get_balance(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    # Rotación simple a la izquierda
    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        # Actualiza alturas
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y  # Nueva raíz del subárbol

    # Rotación simple a la derecha
    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        # Actualiza alturas
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y  # Nueva raíz del subárbol

    # Imprime el árbol por niveles mostrando la altura de cada nodo
    def print_level_order(self, root):
        """Imprime por niveles con alturas"""
        if not root:
            return
        q = deque([(root, 0)])  # Cola para recorrido por niveles
        current_level = 0
        line = []
        while q:
            node, level = q.popleft()
            if level != current_level:
                print(", ".join(line))  # Imprime la línea del nivel anterior
                line = []
                current_level = level
            line.append(f"{node.key}(h{node.height})")  # Agrega nodo a la línea
            if node.left:
                q.append((node.left, level + 1))   # Agrega hijo izquierdo a la cola
            if node.right:
                q.append((node.right, level + 1))  # Agrega hijo derecho a la cola
        if line:
            print(", ".join(line))  # Imprime la última línea

# 🧪 Prueba de inserción y recorrido por niveles
def test_level_order_heights():
    avl = AVLTree()
    root = None
    for val in [10, 5, 15, 2, 7]:
        root = avl.insert(root, val)

    print("🧪 Test 1–5: Expected output:")
    avl.print_level_order(root)

# 🚀 Ejecutar prueba si es el archivo principal
if __name__ == "__main__":
    test_level_order_heights()

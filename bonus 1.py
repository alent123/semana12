# BONUS CHALLENGES - RONY BELLIDO

class Node:  # Node class for both seats and products
    def __init__(self, key, value=1):  # value=1 means reserved or quantity
        self.key = key                # key can be seat ID or SKU
        self.value = value            # value = 1 (seat) or quantity (product)
        self.left = None              # left child
        self.right = None             # right child
        self.height = 1               # height for AVL balancing

class MiniAVL:  # Minimal AVL Tree
    def height(self, n): return n.height if n else 0  # Get node height
    def balance(self, n): return self.height(n.left) - self.height(n.right) if n else 0  # Balance factor

    def rotate_left(self, z):        # Left rotation
        y = z.right                  # Get right child
        z.right = y.left             # Move subtree
        y.left = z                   # Rotate
        z.height = 1 + max(self.height(z.left), self.height(z.right))  # Update height
        y.height = 1 + max(self.height(y.left), self.height(y.right))  # Update height
        return y                     # Return new root

    def rotate_right(self, z):       # Right rotation
        y = z.left                   # Get left child
        z.left = y.right             # Move subtree
        y.right = z                  # Rotate
        z.height = 1 + max(self.height(z.left), self.height(z.right))  # Update height
        y.height = 1 + max(self.height(y.left), self.height(y.right))  # Update height
        return y                     # Return new root

    def insert(self, root, key, value=1):  # Insert key with value
        if not root: return Node(key, value)  # Base case
        if key < root.key: root.left = self.insert(root.left, key, value)  # Insert left
        elif key > root.key: root.right = self.insert(root.right, key, value)  # Insert right
        else:                # If key exists
            root.value += value if value > 0 else 0  # Update value if positive
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))  # Update height
        b = self.balance(root)  # Get balance factor

        if b > 1 and key < root.left.key: return self.rotate_right(root)     # LL
        if b < -1 and key > root.right.key: return self.rotate_left(root)    # RR
        if b > 1 and key > root.left.key:                                     # LR
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if b < -1 and key < root.right.key:                                   # RL
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        return root  # Return unchanged if balanced

    def min_node(self, node):  # Find min in subtree
        while node.left: node = node.left
        return node

    def delete(self, root, key):  # Delete key
        if not root: return root
        if key < root.key: root.left = self.delete(root.left, key)  # Go left
        elif key > root.key: root.right = self.delete(root.right, key)  # Go right
        else:  # Found node
            if not root.left: return root.right  # One child
            elif not root.right: return root.left
            temp = self.min_node(root.right)     # Get successor
            root.key, root.value = temp.key, temp.value  # Copy data
            root.right = self.delete(root.right, temp.key)  # Delete successor

        root.height = 1 + max(self.height(root.left), self.height(root.right))  # Update height
        b = self.balance(root)  # Rebalance

        if b > 1 and self.balance(root.left) >= 0: return self.rotate_right(root)  # LL
        if b > 1:                                 # LR
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if b < -1 and self.balance(root.right) <= 0: return self.rotate_left(root)  # RR
        if b < -1:                                # RL
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        return root

    def inorder(self, root):  # In-order traversal
        if root:
            self.inorder(root.left)
            print(f"{root.key}({root.value})", end=" ")
            self.inorder(root.right)

# === TESTS ===

def test_cineperu():
    print("\n🎬 CinePerú AVL:")
    tree = MiniAVL()
    root = None
    for seat in ["Sala1-A-5", "Sala1-A-6", "Sala1-A-4"]:
        root = tree.insert(root, seat)
    tree.inorder(root)  # Expected sorted seats
    print("\nCancel Sala1-A-5")
    root = tree.delete(root, "Sala1-A-5")
    tree.inorder(root)

def test_supermarket():
    print("\n\n🛒 Supermarket AVL:")
    tree = MiniAVL()
    root = None
    root = tree.insert(root, "SKU100-Rice", 50)
    root = tree.insert(root, "SKU200-Beans", 30)
    root = tree.insert(root, "SKU150-Quinoa", 20)
    root = tree.insert(root, "SKU200-Beans", -30)  # Simulate stock = 0
    root = tree.delete(root, "SKU200-Beans")       # Remove if stock = 0
    tree.inorder(root)  # Expected: SKU100, SKU150

if __name__ == "__main__":
    test_cineperu()
    test_supermarket()

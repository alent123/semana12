# TOURISM AVL TREE - RONY BELLIDO

class Node:  # Node representing a tourist attraction
    def __init__(self, region, name, rating):
        self.key = (region, -rating)       # Sort by region, then highest rating
        self.region = region               # Region name (e.g., Cusco)
        self.name = name                   # Attraction name
        self.rating = rating               # Rating (e.g., 4.9)
        self.left = None                   # Left child
        self.right = None                  # Right child
        self.height = 1                    # Height for AVL balancing

class AVL:  # AVL Tree for attractions
    def height(self, n): return n.height if n else 0  # Return node height
    def balance(self, n): return self.height(n.left) - self.height(n.right) if n else 0  # Balance factor

    def rotate_left(self, z):       # Left rotation
        y = z.right                 # Get right child
        z.right = y.left            # Move subtree
        y.left = z                  # Rotate
        z.height = 1 + max(self.height(z.left), self.height(z.right))  # Update height
        y.height = 1 + max(self.height(y.left), self.height(y.right))  # Update height
        return y                    # Return new root

    def rotate_right(self, z):      # Right rotation
        y = z.left                  # Get left child
        z.left = y.right            # Move subtree
        y.right = z                 # Rotate
        z.height = 1 + max(self.height(z.left), self.height(z.right))  # Update height
        y.height = 1 + max(self.height(y.left), self.height(y.right))  # Update height
        return y                    # Return new root

    def insert(self, root, region, name, rating):  # Insert attraction
        if not root: return Node(region, name, rating)  # Base case
        key = (region, -rating)         # Create sort key
        if key < root.key:              # Go left
            root.left = self.insert(root.left, region, name, rating)
        else:                           # Go right
            root.right = self.insert(root.right, region, name, rating)

        root.height = 1 + max(self.height(root.left), self.height(root.right))  # Update height
        b = self.balance(root)         # Get balance

        if b > 1 and key < root.left.key: return self.rotate_right(root)  # LL case
        if b < -1 and key > root.right.key: return self.rotate_left(root)  # RR case
        if b > 1:  # LR case
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if b < -1:  # RL case
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root  # Return unchanged if balanced

    def inorder(self, root):  # Print attractions in-order
        if root:
            self.inorder(root.left)
            print(f"{root.region} - {root.name} ({root.rating})", end=" | ")
            self.inorder(root.right)

    def range_query(self, root, min_region, max_region):  # Query by region
        if root:
            if root.region >= min_region:
                self.range_query(root.left, min_region, max_region)
            if min_region <= root.region <= max_region:
                print(f"{root.region} - {root.name} ({root.rating})", end=" | ")
            if root.region <= max_region:
                self.range_query(root.right, min_region, max_region)

# === TEST ===

def test_tourism():
    print("\n🌄 AVL Tourism Tree:")
    tree = AVL()
    root = None
    data = [  # Sample attractions
        ("Cusco", "Machu Picchu", 4.9),
        ("Cusco", "Sacsayhuamán", 4.7),
        ("Arequipa", "Colca Canyon", 4.8),
        ("Lima", "Miraflores", 4.5),
        ("Ica", "Huacachina", 4.6),
        ("Puno", "Lake Titicaca", 4.8),
        ("Cusco", "Qorikancha", 4.6),
    ]
    for region, name, rating in data:
        root = tree.insert(root, region, name, rating)

    print("In-order traversal:")
    tree.inorder(root)  # Sorted by region, then rating

    print("\n\nQuery: Cusco to Lima")
    tree.range_query(root, "Cusco", "Lima")  # Show attractions in that range

if __name__ == "__main__":
    test_tourism()

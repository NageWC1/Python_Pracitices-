class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self):
        space = self.get_level() * " " * 3
        prefix = space + "|__" if self.parent else ""
        print(prefix+self.data)
        for child in self.children:
            child.print_tree()

def build_tree():
    root = TreeNode("Electronic")
    laptop = TreeNode("Laptop")
    tv = TreeNode("TV")
    phone = TreeNode("Phone")

    assus = TreeNode("assus")
    xp = TreeNode("xp")
    acer = TreeNode("acer")
    laptop.add_child(assus)
    laptop.add_child(xp)
    laptop.add_child(acer)

    lg = TreeNode("LG")
    galaxy = TreeNode("galaxy")
    lenova = TreeNode("Lenova")
    tv.add_child(lg)
    tv.add_child(galaxy)
    tv.add_child(lenova)

    iphone = TreeNode("Iphone")
    samsung = TreeNode("Samsung")
    pad = TreeNode("Pad")
    phone.add_child(iphone)
    phone.add_child(samsung)
    phone.add_child(pad)

    root.add_child(laptop)
    root.add_child(phone)
    root.add_child(tv)
    return root

if __name__ == "__main__":
    root = build_tree()
    root.print_tree()
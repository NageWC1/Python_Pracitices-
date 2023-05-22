class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children= []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def printTree(self):
        space = self.getLevel() * " " * 3
        prefix = space + "|__" if self.parent else ""
        print(self.data)
        for child in self.children:
            self.printTree()

    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1
        return level


def buildTree():
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

    return root

if __name__ == "__main__":
    pass

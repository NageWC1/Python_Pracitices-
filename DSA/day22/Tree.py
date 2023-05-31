class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent 
            level += 1
        return level

    def print(self):
        space = self.getLevel() * " " * 3
        prefix = space + "|__" if self.parent else ""
        print(prefix + self.data)
        for child in self.children:
            child.print()

def buildTree():
    root = TreeNode("Electronic")

    laptop = TreeNode("Laptop")
    tv = TreeNode("TV")
    phone = TreeNode("Phone")

    hp = TreeNode("HP")
    lenova= TreeNode("Lenova")
    mac = TreeNode("Macbook")

    sony = TreeNode("Sony")
    singer = TreeNode("Singer")
    abanse = TreeNode("Abans")

    apple = TreeNode("Apple")
    oppo = TreeNode("oppo")
    samsung = TreeNode("Sumsung")

    laptop.add_child(hp)        
    laptop.add_child(lenova)        
    laptop.add_child(mac)

    phone.add_child(apple)
    phone.add_child(oppo)
    phone.add_child(samsung)

    tv.add_child(sony)        
    tv.add_child(singer)        
    tv.add_child(abanse)        

    root.add_child(laptop)
    root.add_child(tv)
    root.add_child(phone)

    return root
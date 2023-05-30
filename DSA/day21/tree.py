class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
    
    def getLevel(self):
        level = 0
        p = self.parent 
        while p:
            p = p.parent
            level += 1
        return level
    
    def print(self):
        space  = self.getLevel  * " " * 3
        prefix = space + "|__" if self.parent else ""
        print(prefix + self.data)
        for child in self.children:
            child.print()

def build_tree():
    root = TreeNode("Electronic")
    laptop = TreeNode("Laptop")
    tv = TreeNode("TV")
    phone = TreeNode("Phone")

    iphone = TreeNode('iphone')
    samsun = TreeNode('samsung')
    oppo = TreeNode('oppo')
    phone.add_child(iphone)
    phone.add_child(samsun)
    phone.add_child(oppo)

    sony = TreeNode("Sony")
    abanse = TreeNode("abanse")
    singer = TreeNode("singer")
    tv.add_child(sony)
    tv.add_child(abanse)
    tv.add_child(singer)

    lenova = TreeNode('Lenova')
    apple = TreeNode('apple')
    hp = TreeNode('hp')
    laptop.add_child(lenova)
    laptop.add_child(apple)
    laptop.add_child(hp)

    root.add_child(laptop)
    root.add_child(tv)
    root.add_child(phone)

    return root

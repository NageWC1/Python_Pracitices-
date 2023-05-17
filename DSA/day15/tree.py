class TreeeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def addChild(self, child):
        self.children.append(child)
    
    def printTree(self):
        print(str(self.data))
        if self.children:
            for child in self.children:
                child.printTree()

def buildtree():
    root = TreeeNode("Electronic")
    laptop = TreeeNode("laptop")
    phone = TreeeNode("phone")
    tv = TreeeNode("TV")

    root.addChild(laptop)
    root.addChild(phone)
    root.addChild(tv)

    root.printTree()
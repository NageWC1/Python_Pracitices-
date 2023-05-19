class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.children = []
        self.parent = None
    

    def addChild(self, child):
        child.parent = self
        self.children.append(child)
    
    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1
        return level
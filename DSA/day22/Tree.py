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
        for child in self.children:
            child.print()
        
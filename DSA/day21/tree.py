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

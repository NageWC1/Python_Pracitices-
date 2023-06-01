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
            p = p.parent
            level += 1
        return level
    
    def print(self):
        space = self.get_level() * " " * 3
        prefix = space + "|__" if self.parent else ""
        print(prefix + self.data)
        for child in self.children:
            child.print()

if __name__ == "__main__":
    root = Buildtree()
    root.print()
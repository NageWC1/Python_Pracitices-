class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    
    def print_tree(self):
        space = self.getLevel() * " " * 3
        prefix =  space + "|__"  if self.parent else ""
        print(prefix + str(self.data))
        for child in self.children:
            child.print_tree()

    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1
        return level 

def builtree():
    root = TreeNode("Electronic")
    laptop = TreeNode("laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cellphone")
    cellphone.add_child(TreeNode("iphone"))
    cellphone.add_child(TreeNode("sumsung"))
    cellphone.add_child(TreeNode("vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Galxy"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    return root

if __name__ == "__main__":
    root = builtree()
    root.print_tree()
    

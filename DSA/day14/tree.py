class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        level =  self.get_level()
        spaces =  " " * level * 3
        print(spaces + self.data )
        if len(self.children):
            for child in self.children:
                child.print_tree()

    def get_level(self):
        level = 0 
        p = self.parent
        while p:
            p = p.parent
            level += 1
        return level
    
def build_product_tree():
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
    root = build_product_tree()
    root.print_tree() 

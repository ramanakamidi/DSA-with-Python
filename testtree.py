class Bt:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None

def create_tree_from_list(li):
    root=Bt(li[0])
    queue=[root]
    i=1
    while i<len(li):
        if li is None:
            return 
        current=queue.pop(0)
        if i<len(li):
            current.left=Bt(li[i])
            queue.append(current.left)
            i+=1
        if i<len(li):
            current.right=Bt(li[i])
            queue.append(current.right)
            i+=1
    return root


def print_tree(root):
    while root :
        print(root.data)
        if root.left:
            root=root.left
        else:
            root=root.right

# Call it
root = create_tree_from_list([1,2,3,4,5,6,7,8,9,10])
print_tree(root)



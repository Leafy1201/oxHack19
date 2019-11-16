class Tree:
    def __init__(self):
        self.children = []
        self.data = None
    
    def traverse(self):
        returnList = []
        _traverse(self, returnList)
        return returnList
    
    # Adds None marker when all children have been visited.
    def _traverse(self, node, returnList):
        returnList.append(node.data)
        for child in node.children:
            self._traverse(child, returnList)
        if len(node.children) != 0:
            returnList.append(None)
class Symbol:

    def __init__(self, id, height, width, centre):
        self.id = id #give it an id to find it, since we will remove entries from the list we cannot use the indexes
        self.parent = "" #this is the symbols parent
        self.relationship = "" #relationship to its parent, if its on the same line, above a fraction, suprecripted, subscripted, etc
        self.character = ""
        self.height = height
        self.width = width
        self.centre = centre
    
    def getRatio(self):
        return self.width/self.height
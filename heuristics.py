from fraction import Fraction
from symbol import Symbol
from tree import Tree
foobar = __import__("opencv-recog") #import opencv-recog

def classify(pieceList):
	for piece in pieceList:
		if isFractionBar(piece):
			fracbar = Fraction(piece.width, piece.height, piece.centre)
			above, below = getAboveBelow(fracbar, pieceList)
			fracbar.numerator=classify(above)
			fracbar.denominator=classify(below)
	symlist = []
	for piece in pieceList:
		if not isFractionBar(piece):
			symbol = recognise(piece) #maybe not??????????
			symlist.append(symbol)
	
	tree = Tree()
	superscriptList = []
	subscriptList = []
	parentList = []

	for sym in symlist:
		if isSuperscript(sym, symlist):
			parent = findSuperscriptParent(sym, symlist)
			superscriptList.append((sym, parent))
		elif isSubscript(sym, symlist):
			parent = findSubscriptParent(sym, symlist)
			subscriptList.append((sym, parent))
		else:
			t = Tree(data = sym)
			tree.children.append(t)
			parentList.append(sym)

	# for (sym,parent) in superscriptList:
	# 	tree.findById(parent.id).children.append(sym)
	# for (sym,parent) in subscriptList:
	# 	tree.findById(parent.id).children.append(sym)

	for parent in parentList:
		superscript = []
		for (sym,p) in superscriptList:
			if p==parent:
				superscript.append(sym)
		if len(superscript)>0:
			t = Tree()
			t.data = "superscript" #TODO make good lol
			t.children.append(classify(superscript))
			parent.children.append(t)

		subscript = []
		for (sym,p) in subscriptList:
			if p==parent:
				subscript.append(sym)
		if len(subscript)>0:
			t = Tree()
			t.data = "subscript" #TODO make good lol
			t.children.append(classify(subscript))
			parent.children.append(t)

		tree.children.append(Tree(data=parent))

	return tree


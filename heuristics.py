import fraction
import symbol
import symrecogniser
import tree

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
			symbol = recognise(piece)
			symlist.append(symbol)
	
	tree = Tree()
	superscriptList = []
	subscriptList = []

	for sym in symlist:
		if isSuperscript(sym, symlist):
			parent = findSuperscriptParent(sym, symlist)
			superscriptList.append(sym, parent)
		elif isSubscript(sym, symlist):
			parent = findSubscriptParent(sym, symlist)
			subscriptList.append(sym, parent)
		else:
			t = Tree()
			t.data = sym.id
			t.children.append(sym)
			tree.children.append(t)

	for (sym,parent) in superscriptList:
		t = tree.find(parent.id)
		t.children.append(sym)
	for (sym,parent) in subscriptList:
		t = tree.find(parent.id)
		t.children.append(sym)



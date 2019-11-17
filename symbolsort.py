from symbol import Symbol

def symbolSort(symbolList):
    return sorted(symbolList, key = lambda x: x.centre[0])

if __name__ == "__main__":
    print(symbolSort([Symbol(1, 10, 10, (5, 6)), Symbol(2, 10, 10, (3, 6))]))
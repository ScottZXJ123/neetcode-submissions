class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        nodes = self.root
        for ch in word:
            if ch not in nodes:
                nodes[ch] = {}
            nodes = nodes[ch]
        nodes["$"] = True
 
    def search(self, word: str) -> bool:
        nodes = [self.root]
        for ch in word:
            newnodes = []
            for node in nodes:
                if ch == ".":
                    for key in node:
                        if key != "$":
                            newnodes.append(node[key])
                elif ch in node:
                    newnodes.append(node[ch])
            nodes = newnodes
        
        for node in nodes:
            if "$" in node:
                return True
        return False
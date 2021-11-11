# For startswith, endswith, containing
def handleWildCard(word):
    if '?' in word:
        res = []
        word = list(word)
        index = word.index('?')
        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            word[index] = char
            res.append(''.join(word))
        return res
    else:
        return [word]

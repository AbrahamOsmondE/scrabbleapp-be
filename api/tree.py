# from lexpy.dawg import DAWG
# import os
import dill
import time


class LetterTreeNode:
    def __init__(self, is_word):
        self.is_word = is_word
        self.children = dict()


class LetterTree:
    def __init__(self):
        self.root = LetterTreeNode(False)

    def add_word(self, word):
        current_node = self.root
        for letter in word:
            if letter not in current_node.children.keys():
                current_node.children[letter] = LetterTreeNode(False)
            current_node = current_node.children[letter]
        current_node.is_word = True

    def lookup(self, word):
        current_node = self.root
        for letter in word:
            if letter not in current_node.children.keys():
                return None
            current_node = current_node.children[letter]
        return current_node

    def is_word(self, word):
        word_node = self.lookup(word)
        if word_node is None:
            return False
        return word_node.is_word


# loc = os.path.join(os.path.dirname(
#     os.path.dirname(__file__)), 'api', 'worddef.txt')
# newfile = open(loc)
# csw = {}
# seven_letter_words = []
# CSWTree = LetterTree()
# dawg = DAWG()
# for i in newfile:
#     i = i.replace('\n', '')
#     word, definition = i.split(maxsplit=1)
#     CSWTree.add_word(word)
#     dawg.add(word)
#     csw[word] = definition
#     if len(word) == 7:
#         seven_letter_words.append(word)
# newfile.close()
# with open("csw", "wb") as dill_file:
#     dill.dump(csw, dill_file)

# with open("CSWTree", "wb") as dill_file:
#     dill.dump(CSWTree, dill_file)

# with open("dawg", "wb") as dill_file:
#     dill.dump(dawg, dill_file)

# with open("sevenLetterWords", "wb") as dill_file:
#     dill.dump(seven_letter_words, dill_file)

# with open("csw", "rb") as dill_file:
#     csw = dill.load(dill_file)

# with open("CSWTree", "rb") as dill_file:
#     CSWTree = dill.load(dill_file)

# with open("dawg", "rb") as dill_file:
#     dawg = dill.load(dill_file)

# with open("sevenLetterWords", "rb") as dill_file:
#     seven_letter = dill.load(dill_file)

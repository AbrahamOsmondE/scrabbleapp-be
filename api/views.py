
from django.http.response import HttpResponse, JsonResponse
from .solver import SolveState
from .board import Board
import itertools
from .helper import handleWildCard, countPoints
from django.http import QueryDict
import random
import dill

with open("csw", "rb") as dill_file:
    csw = dill.load(dill_file)

with open("CSWTree", "rb") as dill_file:
    CSWTree = dill.load(dill_file)

# with open("dawg", "rb") as dill_file:
#     dawg = dill.load(dill_file)

with open("sevenLetterWords", "rb") as dill_file:
    seven_letter = dill.load(dill_file)


def getWords(request, word):
    # dictionary = {}
    # word = word.upper()
    # permutations = [''.join(j) for i in range(1, len(word) + 1)
    #                 for j in itertools.permutations(word, i) if CSWTree.is_word(''.join(j))]
    # for combination in permutations:
    #     if len(combination) in dictionary:
    #         dictionary[len(combination)].add(combination)
    #     else:
    #         dictionary[len(combination)] = set([combination])
    # for keys in dictionary:
    #     dictionary[keys] = list(dictionary[keys])
    # del permutations
    # return JsonResponse(dictionary, safe=False)
    # x = CSWTree.is_word(word.upper())
    return


# def getAnagram(request, word):
#     dictionary = {}
#     word = word.upper()
#     word = word.replace('*', '?')
#     if "?" in word:
#         for combination in [''.join(j) for j in itertools.permutations(word, len(word))]:
#             if len(combination) in dictionary:
#                 for res in dawg.search(combination):
#                     dictionary[len(combination)].add(res)
#             else:
#                 dictionary[len(combination)] = set(dawg.search(combination))
#         for keys in dictionary:
#             dictionary[keys] = list(dictionary[keys])
#     else:
#         for combination in [''.join(j) for j in itertools.permutations(word, len(word)) if ''.join(j) in dawg]:
#             if len(combination) in dictionary:
#                 dictionary[len(combination)].add(combination)
#             else:
#                 dictionary[len(combination)] = set([combination])

#         for keys in dictionary:
#             dictionary[keys] = list(dictionary[keys])
#     return JsonResponse(dictionary, safe=False)


# def getStartingWith(request, word):
#     dictionary = {}
#     word = word.upper().replace('*', '?')
#     word = handleWildCard(word)
#     for i in word:
#         i += "*"
#         for res in dawg.search(i):
#             if len(res) in dictionary:
#                 dictionary[len(res)].add(res)
#             else:
#                 dictionary[len(res)] = set([res])
#     for keys in dictionary:
#         dictionary[keys] = list(dictionary[keys])
#     return JsonResponse(dictionary, safe=False)


# def getEndingWith(request, word):
#     dictionary = {}
#     word = word.upper().replace('*', '?')
#     word = handleWildCard(word)
#     for i in word:
#         i = "*" + i
#         for res in dawg.search(i):
#             if len(res) in dictionary:
#                 dictionary[len(res)].add(res)
#             else:
#                 dictionary[len(res)] = set([res])
#     for keys in dictionary:
#         dictionary[keys] = list(dictionary[keys])
#     return JsonResponse(dictionary, safe=False)


# def getContaining(request, word):
#     dictionary = {}
#     word = word.upper().replace('*', '?')
#     word = handleWildCard(word)
#     for i in word:
#         i += "*"
#         for res in dawg.search(i):
#             if len(res) in dictionary:
#                 dictionary[len(res)].add(res)
#             else:
#                 dictionary[len(res)] = set([res])

#     for i in word:
#         i = "*" + i
#         for res in dawg.search(i):
#             if len(res) in dictionary:
#                 dictionary[len(res)].add(res)
#             else:
#                 dictionary[len(res)] = set([res])

#     for i in word:
#         i = '*' + i + '*'
#         for res in dawg.search(i):
#             if len(res) in dictionary:
#                 dictionary[len(res)].add(res)
#             else:
#                 dictionary[len(res)] = set([res])

#     for keys in dictionary:
#         dictionary[keys] = list(dictionary[keys])
#     return JsonResponse(dictionary, safe=False)


# def getDefinition(request, word):
#     dictionary = {}
#     word = word.upper()
#     description = csw[word]
#     if '[' in description:
#         partOfSpeech = description[description.index(
#             '[')+1:description.index(']')].split(" ")[0]
#         definition = description.split('[')[0]

#         dictionary["definition"] = definition
#         dictionary["partOfSpeech"] = partOfSpeech
#         dictionary["points"] = countPoints(word)
#     else:
#         dictionary["definition"] = description
#         dictionary["partOfSpeech"] = "n"
#         dictionary["points"] = countPoints(word)
#     return JsonResponse(dictionary, safe=False)


# def solveBoard(request, rack):
#     rack = rack.upper()
#     rack = [i for i in rack]

#     full_string = request.META['QUERY_STRING']
#     full_string = full_string.strip()
#     if full_string != '':
#         board_entries = QueryDict(full_string)
#         board = Board(15)
#         for i in board_entries:
#             row, col = i.split('-')
#             board.set_tile((int(row), int(col)), board_entries.get(i))

#         solver = SolveState(CSWTree, board, rack)

#         solver.find_all_options()
#         solver.answer.sort(reverse=True, key=lambda i: i['points'])

#         answer = solver.answer[:min(len(solver.answer), 50)]

#         del board
#         del solver

#         return JsonResponse(answer, safe=False)

#     else:
#         words = set()
#         permutations = [''.join(j) for i in range(1, len(rack) + 1)
#                         for j in itertools.permutations(rack, i) if CSWTree.is_word(''.join(j))]
#         for combination in permutations:
#             words.add(combination)
#         words = list(words)

#         board = Board(15)
#         solver = SolveState(CSWTree, board, rack)
#         solver.find_all_options_empty(words)
#         solver.answer.sort(reverse=True, key=lambda i: i['points'])

#         answer = solver.answer[:min(len(solver.answer), 50)]
#         del board
#         del solver
#         del permutations
#         del words
#         return JsonResponse(answer, safe=False)


# def getPuzzle(request):
#     puzzle = {}
#     dictionary = {}
#     letters = "".join(sorted(random.choice(seven_letter)))

#     # letters = ["A"]*9 + ["B"]*2 + ["C"]*2 + ["D"]*4 + ["E"]*12 + ["F"]*2 + ["G"]*3 + ["H"]*2 + ["I"]*9 + ["J"]+["K"] + \
#     #     ["L"]*4 + ["M"]*2+["N"]*6+["O"]*8+["P"]*2+["Q"]+["R"]*6 + \
#     #     ["S"]*4+["T"]*6+["U"]*4+["V"]*2+["W"]*2+["X"]+["Y"]*2+["Z"]
#     seven_letter_word = "".join(random.sample(letters, 7))
#     permutations = [''.join(j) for i in range(1, 8) for j in itertools.permutations(
#         seven_letter_word, i) if CSWTree.is_word(''.join(j))]
#     for combination in permutations:
#         if len(combination) in dictionary:
#             dictionary[len(combination)].add(combination)
#         else:
#             dictionary[len(combination)] = set([combination])
#     del permutations
#     for keys in dictionary:
#         dictionary[keys] = list(dictionary[keys])
#     puzzle["count"] = 0
#     for length in dictionary:
#         dictionary[length].sort()
#         puzzle["count"] += len(dictionary[length])

#     puzzle["word"] = seven_letter_word
#     puzzle["solutions"] = dictionary
#     del dictionary
#     return JsonResponse(puzzle, safe=False)

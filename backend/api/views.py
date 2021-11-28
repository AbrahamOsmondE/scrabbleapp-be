from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from lexpy.dawg import DAWG
import itertools
import os
from .helper import handleWildCard, countPoints

dawg = DAWG()
loc = os.path.join(os.path.dirname(
    os.path.dirname(__file__)), 'api', 'worddef.txt')
newfile = open(loc)
csw = {}

for i in newfile:
    i = i.replace('\n', '')
    x, y = i.split(maxsplit=1)
    csw[x] = y
    dawg.add(x)


def getWords(request, word):
    dictionary = {}
    word = word.upper()
    word = word.replace('*', '?')
    if "?" in word:
        for combination in [''.join(j) for i in range(2, len(word) + 1) for j in itertools.permutations(word, i)]:
            if len(combination) in dictionary:
                for res in dawg.search(combination):
                    dictionary[len(combination)].add(res)
            else:
                dictionary[len(combination)] = set(dawg.search(combination))
        for keys in dictionary:
            dictionary[keys] = list(dictionary[keys])
    else:
        for combination in [''.join(j) for i in range(1, len(word) + 1) for j in itertools.permutations(word, i) if ''.join(j) in dawg]:
            if len(combination) in dictionary:
                dictionary[len(combination)].add(combination)
            else:
                dictionary[len(combination)] = set([combination])

        for keys in dictionary:
            dictionary[keys] = list(dictionary[keys])
    return JsonResponse(dictionary, safe=False)


def getAnagram(request, word):
    dictionary = {}
    word = word.upper()
    word = word.replace('*', '?')
    if "?" in word:
        for combination in [''.join(j) for j in itertools.permutations(word, len(word))]:
            if len(combination) in dictionary:
                for res in dawg.search(combination):
                    dictionary[len(combination)].add(res)
            else:
                dictionary[len(combination)] = set(dawg.search(combination))
        for keys in dictionary:
            dictionary[keys] = list(dictionary[keys])
    else:
        for combination in [''.join(j) for j in itertools.permutations(word, len(word)) if ''.join(j) in dawg]:
            if len(combination) in dictionary:
                dictionary[len(combination)].add(combination)
            else:
                dictionary[len(combination)] = set([combination])

        for keys in dictionary:
            dictionary[keys] = list(dictionary[keys])
    return JsonResponse(dictionary, safe=False)


def getStartingWith(request, word):
    dictionary = {}
    word = word.upper().replace('*', '?')
    word = handleWildCard(word)
    for i in word:
        i += "*"
        for res in dawg.search(i):
            if len(res) in dictionary:
                dictionary[len(res)].add(res)
            else:
                dictionary[len(res)] = set([res])
    for keys in dictionary:
        dictionary[keys] = list(dictionary[keys])
    return JsonResponse(dictionary, safe=False)
    # Create your views here.


def getEndingWith(request, word):
    dictionary = {}
    word = word.upper().replace('*', '?')
    word = handleWildCard(word)
    for i in word:
        i = "*" + i
        for res in dawg.search(i):
            if len(res) in dictionary:
                dictionary[len(res)].add(res)
            else:
                dictionary[len(res)] = set([res])
    for keys in dictionary:
        dictionary[keys] = list(dictionary[keys])
    return JsonResponse(dictionary, safe=False)


def getContaining(request, word):
    dictionary = {}
    word = word.upper().replace('*', '?')
    word = handleWildCard(word)
    for i in word:
        i += "*"
        for res in dawg.search(i):
            if len(res) in dictionary:
                dictionary[len(res)].add(res)
            else:
                dictionary[len(res)] = set([res])

    for i in word:
        i = "*" + i
        for res in dawg.search(i):
            if len(res) in dictionary:
                dictionary[len(res)].add(res)
            else:
                dictionary[len(res)] = set([res])

    for i in word:
        i = '*' + i + '*'
        for res in dawg.search(i):
            if len(res) in dictionary:
                dictionary[len(res)].add(res)
            else:
                dictionary[len(res)] = set([res])

    for keys in dictionary:
        dictionary[keys] = list(dictionary[keys])
    return JsonResponse(dictionary, safe=False)


def getDefinition(request, word):
    dictionary = {}
    word = word.upper()
    description = csw[word]
    if '[' in description:
        partOfSpeech = description[description.index(
            '[')+1:description.index(']')].split(" ")[0]
        definition = description.split('[')[0]
        
        dictionary["definition"] = definition
        dictionary["partOfSpeech"] = partOfSpeech
        dictionary["points"] = countPoints(word)
    else:
        dictionary["definition"] = description
        dictionary["partOfSpeech"] = "n"
        dictionary["points"] = countPoints(word)
    return JsonResponse(dictionary, safe=False)

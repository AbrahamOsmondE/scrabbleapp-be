# scrabbleapp-be
All in one scrabble app, inspired by Lichess.
Utilizes a Double Acyclic Word Graph for fast and efficient lookup and word storage. Supports 1 wild card using asterisk *

Endpoints:
### /api/wordbuilder/<str:word>
Returns every possible words that can be made by the letters given in <str:word>

### /api/anagram/<str:word>
### /api/startingwith/<str:word>
### /api/endingwith/<str:word>
### /api/containing/<str:word>
### /api/definition/<str:word>

# scrabbleapp-be
All in one scrabble app, inspired by Lichess.
Utilizes a Double Acyclic Word Graph for fast and efficient lookup and word storage. Supports 1 wild card using asterisk (\*), word lookup upto 15 letters, but 10 letters onwards start becoming slow.

Endpoints:
### /api/wordbuilder/<str:word>
Returns every possible words that can be made by the letters given in <str:word> <br />
Example: <br />
/api/wordbuilder/rain <br />
{"2": ["NA", "IN", "AR", "AI", "AN"], "3": ["RIA", "ANI", "RAN", "RAI", "AIN", "RIN", "AIR"], "4": ["AIRN", "RANI", "RAIN"]} <br />

### /api/anagram/<str:word>. 
Returns every possible anagram of the word given in <str:word> <br />
Example:<br />
/api/anagram/rain<br />
{"4": ["AIRN", "RANI", "RAIN"]}<br />

### /api/startingwith/<str:word><br />
Returns every possible word that starts with <str:word><br />
Example:<br />
/api/startingwith/rain<br />
{"4": ["RAIN"], "8": ["RAINDATE", "RAINSUIT", "RAINCOAT", "RAINFALL", "RAINBOWS", "RAINDROP", "RAINIEST", "RAINLESS", "RAINWEAR", "RAINWASH", "RAINBIRD", "RAINBAND", "RAINOUTS", "RAINBOWY"], "9": ["RAININESS", "RAINSTORM", "RAINFALLS", "RAINTIGHT", "RAINDROPS", "RAINSWEPT", "RAINMAKER", "RAINSTICK", "RAINWEARS", "RAINDATES", "RAINBOWED", "RAINCOATS", "RAINPROOF", "RAINWATER",...} <br />

### /api/endingwith/<str:word>
Returns every word that ends with <str:word><br />
Example:<br />
/api/endingwith/rain<br />
{"4": ["RAIN"], "9": ["BIRDBRAIN", "HINDBRAIN", "AEROTRAIN", "OUTSTRAIN", "OVERTRAIN", "OVERGRAIN", "WOODGRAIN", "FILIGRAIN", "GROSGRAIN", "FEEDGRAIN", "EYESTRAIN", "LAMEBRAIN", "FOREBRAIN", "CHAMFRAIN", "CONSTRAIN"], "10": ["INTERBRAIN", "SOUTERRAIN", ...}<br />

### /api/containing/<str:word>. 
Returns every word that contains <str:word> (starts with, ends with and in between) <br />
Example: <br />
/api/containing/herit <br />
{"14": ["HERITABILITIES", "DISINHERITANCE", "DIPHTHERITISES", "COINHERITANCES", "INHERITABILITY"], "12": ["DIPHTHERITIS", "COINHERITORS", "INHERITRICES", "DISINHERITED", "INHERITANCES"], "9": ["COHERITOR", "WITHERITE", "HERITAGES", "HERITRESS", "DISHERITS", "INHERITOR", "INHERITED", "HERITABLE", "HERITABLY"], "8": ["INHERITS", "HERITAGE", "DISHERIT", ...} <br />

### /api/definition/<str:word>. 
Returns the definition, part of speech and scrabble points of <str:word> <br />
Example: <br />
/api/definition/rain <br />
{"definition": "to fall in drops of water ", "partOfSpeech": "v", "points": 4} --> R, A, I and N are word 1 point each <br />

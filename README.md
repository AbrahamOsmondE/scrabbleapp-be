# scrabbleapp-be
All in one scrabble app, inspired by Lichess.
Utilizes a Double Acyclic Word Graph for fast and efficient lookup and word storage. Supports 1 wild card using asterisk (\*), word lookup upto 15 letters, but 10 letters onwards start becoming slow.

Endpoints:
### /api/wordbuilder/<str:word>
Returns every possible words that can be made by the letters given in <str:word>
Example:
/api/wordbuilder/rain
{"2": ["NA", "IN", "AR", "AI", "AN"], "3": ["RIA", "ANI", "RAN", "RAI", "AIN", "RIN", "AIR"], "4": ["AIRN", "RANI", "RAIN"]}

### /api/anagram/<str:word>
Returns every possible anagram of the word given in <str:word>
Example:
/api/anagram/rain
{"4": ["AIRN", "RANI", "RAIN"]}

### /api/startingwith/<str:word>
Returns every possible word that starts with <str:word>
Example:
/api/startingwith/rain
{"4": ["RAIN"], "8": ["RAINDATE", "RAINSUIT", "RAINCOAT", "RAINFALL", "RAINBOWS", "RAINDROP", "RAINIEST", "RAINLESS", "RAINWEAR", "RAINWASH", "RAINBIRD", "RAINBAND", "RAINOUTS", "RAINBOWY"], "9": ["RAININESS", "RAINSTORM", "RAINFALLS", "RAINTIGHT", "RAINDROPS", "RAINSWEPT", "RAINMAKER", "RAINSTICK", "RAINWEARS", "RAINDATES", "RAINBOWED", "RAINCOATS", "RAINPROOF", "RAINWATER", "RAINCHECK", "RAINBIRDS", "RAINBANDS", "RAINSUITS", "RAINSPOUT"], "7": ["RAINBOW", "RAINILY", "RAINING", "RAINIER", "RAINOUT"], "10": ["RAINCHECKS", "RAINFOREST", "RAINSPOUTS", "RAINWASHES", "RAINBOWIER", "RAINMAKERS", "RAINPROOFS", "RAINMAKING", "RAINSQUALL", "RAINSTORMS", "RAINWASHED", "RAINSTICKS", "RAINWATERS"], "11": ["RAINPROOFED", "RAINBOWIEST", "RAINSQUALLS", "RAINMAKINGS", "RAINWASHING", "RAININESSES", "RAINBOWLIKE", "RAINFORESTS"], "5": ["RAINS", "RAINE", "RAINY"], "6": ["RAINED", "RAINES"], "12": ["RAINPROOFING"]}

### /api/endingwith/<str:word>
Returns every word that ends with <str:word>
Example:
/api/endingwith/rain
{"4": ["RAIN"], "9": ["BIRDBRAIN", "HINDBRAIN", "AEROTRAIN", "OUTSTRAIN", "OVERTRAIN", "OVERGRAIN", "WOODGRAIN", "FILIGRAIN", "GROSGRAIN", "FEEDGRAIN", "EYESTRAIN", "LAMEBRAIN", "FOREBRAIN", "CHAMFRAIN", "CONSTRAIN"], "10": ["INTERBRAIN", "SOUTERRAIN", "APPLEDRAIN", "OVERSTRAIN", "UNDERDRAIN", "DRIVETRAIN", "WHOLEGRAIN", "DISENTRAIN", "AFTERBRAIN", "WATERBRAIN", "SUPERBRAIN", "CRACKBRAIN", "HOVERTRAIN", "MULTIGRAIN", "POWERTRAIN", "SUBTERRAIN"], "5": ["TRAIN", "GRAIN", "DRAIN", "BRAIN"], "11": ["RATTLEBRAIN", "INTERSTRAIN", "BEETLEBRAIN"], "12": ["BETWEENBRAIN", "SCATTERBRAIN", "FEATHERBRAIN"], "7": ["DARRAIN", "TERRAIN", "INGRAIN", "ENGRAIN", "DETRAIN", "MURRAIN", "REFRAIN", "RETRAIN", "UPTRAIN", "ENTRAIN", "VITRAIN", "CLARAIN"], "8": ["DISTRAIN", "PRETRAIN", "RIVERAIN", "QUATRAIN", "MIDBRAIN", "PEABRAIN", "ENDBRAIN", "SEATRAIN", "SUZERAIN", "MADBRAIN", "RESTRAIN", "MISTRAIN"], "6": ["STRAIN", "SPRAIN"]}

### /api/containing/<str:word>
Returns every word that contains <str:word> (starts with, ends with and in between)
Example:
/api/containing/herit
{"14": ["HERITABILITIES", "DISINHERITANCE", "DIPHTHERITISES", "COINHERITANCES", "INHERITABILITY"], "12": ["DIPHTHERITIS", "COINHERITORS", "INHERITRICES", "DISINHERITED", "INHERITANCES", "DIPHTHERITIC", "BLEACHERITES", "INHERITRIXES", "HERITABILITY"], "9": ["COHERITOR", "WITHERITE", "HERITAGES", "HERITRESS", "DISHERITS", "INHERITOR", "INHERITED", "HERITABLE", "HERITABLY"], "8": ["INHERITS", "HERITAGE", "DISHERIT", "HERITORS", "HERITRIX"], "7": ["HERITOR", "INHERIT"], "11": ["COINHERITOR", "INHERITABLE", "HERITRESSES", "INHERITABLY", "DISHERITING", "INHERITRESS", "MARGHERITAS", "BLEACHERITE", "DISHERITORS", "DISINHERITS", "INHERITANCE"], "10": ["DISHERITED", "DISHERITOR", "DISINHERIT", "INHERITRIX", "INHERITORS", "MARGHERITA", "WITHERITES", "HERITRIXES", "INHERITING", "COHERITORS", "HERITRICES"], "13": ["COINHERITANCE", "INHERITRESSES", "DISINHERITING"], "15": ["INHERITABLENESS", "DISINHERITANCES"]}

### /api/definition/<str:word>
Returns the definition, part of speech and scrabble points of <str:word>
Example:
/api/definition/rain
{"definition": "to fall in drops of water ", "partOfSpeech": "v", "points": 4} --> R, A, I and N are word 1 point each

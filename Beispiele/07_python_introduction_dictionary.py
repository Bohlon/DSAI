######################################################
# Ein weiterer grundlegender Datentyp ist das Dictionary,
# welches Schlüsseln (Keys) eindeutige Werte (Values) zuordnet
# sodas sie mit einem Schlüssel schnell den orrespondierenden Wert ermitteln können


empty_dict = {}                     # in Python üblich
empty_dict2 = dict()                # eher selten verwendet
grades = {'Joel':80, 'Tim':95}      # ausgeschriebenes Dictionary

# Mit einer eckigen Klammer kann der Wert für einen Schlüssel nachgeschlagen werden
joels_grades = grades['Joel']
print(joels_grades)

# Wenn der angefragte Schlüssel nicht im Dictionary enthalten ist, erhält man einen KeyError
try:
    kates_grades = grades['Kate']
except KeyError:
    print('No grade for Kate!')

# Mit dem Operator 'in' kann überprüft werden, ob ein Schlüssel vorhanden ist
joel_has_grades = 'Joel' in grades  # True
kate_has_grades = 'Kate' in grades  # False

"Joel" not in grades                # False

# Dictionaries haben ebenfalls die Methode 'get', die einen Standardwert zurückliefern können
joel_has_grades = grades.get('Joel',0)
kate_has_grades = grades.get('Kate',0)
no_ones_grade = grades.get('No One')    # der Standardwert ist hir None

# Schlüssel/wert-Paare lassen sich über eckige Klammern zuweisen
grades['Tim'] = 99                      # erstetzt den vorigen Wert
grades['Kate'] = 100                    # fügt einen dritten Eintrag hinzu
num_students = len(grades)              # gleich 3

# Dictionaries können eingesetzt werden, um auf einfache Weise struckturierte Daten abzulegen
tweet = {
    'user': 'Miklauc',
    'text': 'Data Science',
    'retweet_count': 100,
    'hashtags': ['#data','#science', '#datascience', '#awesome']
}

# Man kann auch auf alle SChlüssel gleichzeitig zugreifen
tweet_keys = tweet.keys()               # Iterable für die Schlüssel
tweet_values = tweet.values()           # Iterable für die Werte
tweet_items = tweet.items()             # Iterable für die (Schlüssel/Werte-) Tuple

'user' in tweet_keys                    # true
'user' in tweet                         # in Python eher üblich zum Überprüfen von Schlüsseln
'Miklauc' in tweet_values               # langsam, aber einziger Weg, dies zu überprüfen

# Defaultdictionary
from collections import defaultdict
def def_values()->str:
    return 'Not present'

# Defining the dict
d = defaultdict(def_values)
d['a']=1
d['b']=2

print(d['a'])                           # 1
print(d['b'])                           # 2
print(d['c'])                           # not present

dd_int = defaultdict(int)
dd_list = defaultdict(list)


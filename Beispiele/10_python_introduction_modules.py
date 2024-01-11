# Viele Features von Python werden nicht automatisch geladen
# Dazu gehören auch zum Sprachumfang gehörige Features als auch solche die man selbst runterlädt
# Um die Features zu benutzen muss man die entsprechenden Module mit import aktivieren
# Eine Möglichkeit besteht darin, das Modul selbst per import einzubinden

import re
my_regex = re.compile('[0-9]+', re.I) # Hierbei ist re das Modul mit Funktionen
                                      # und Konstanten zur Arbeit mit regulären Ausdrücken
                                      # Nach dieser Art von import müssen Sie den Funktionen
                                      # das Präfix re. voranstellen, um sie zu nutzen

# Wenn ein Bezeichner re bereits in dem Code definiert ist kann man ein Alias verwenden
import re as regex
my_regex = regex.compile('[0-9]+', regex.I)

# Prüft ob eine Übereinstimmung am Anfang des Strings vorliegt
my_regex.match('')
print(my_regex.match(''))
print(my_regex.match('1234'))
print(my_regex.match('1ABCSX'))
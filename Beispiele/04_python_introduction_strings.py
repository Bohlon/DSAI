#########################################################################
# Strings lassen sich durch einfache oder doppelte Anführungszeichen
# begrenzen (es müssen aber vorn und hinten die gleichen sein!!!!)

single_quoted_string = 'data science'
double_quoted_string = "data science"
mixed_qouted_string = "data 'science'"

# Python verwendet Backslashes zum Codieren von Sonderzeichen
tab_string = '\t'   # steht für einen Tabulator
len(tab_string)     # ist 1 falls man den Backslash als solveb verwenden möchte

# Falls man dies als Zeichen verwenden möchte, nimmt man einen raw String
# raw string wird mit r"" erzeugt
not_tab_string = r"\t"  # steht für die Zeichen '\' und 't'
len(not_tab_string)     # ist 2

# Mit dreifachen (doppelten) Anfürungszeichen kann man Strings über mehrere Zeilen definieren
multi_line_string = """
                    Dies ist die erste Zeile.
                    Und dies ist die zweite Zeile.
                    Dies ist die dritte Zeile
                    """

#Ein neues Feature in Python 3.6 ist der f-string
# mit den sich die Werte im String einfach ersetzen lassen
# Beispielsweise Vor- und Nachname in getrennten Variablen enthalten

first_name:str = 'Max'
last_name:str = 'Mustermann'

# Nun wollen wir die Beiden zu einem ganzen Namen zusammenfügen
full_name1 = first_name + " " + last_name   # Strings verketten
full_name2 = "{0} {1}".format(first_name,last_name)     # string.format

# f-String ist es viel übersichtlicher
full_name3 = f"{first_name} {last_name}"
print(full_name3)
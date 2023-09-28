##############################################
#   Programm: 01_python_introductionformat   #
##############################################

for i in [1,2,3,4,5]:
    print(i)    # erste Zeile im Block "for i"
    # python unterscheidet beim Einrücken zwischen Tabs und Leerzeichen
    # der Code wird evt nicht ausgeführt wenn beides vermischt wird
    #Immer Leerzeichen nehmen und niemals Tabs
    for j in [1,2,3,4,5]:
        print(j)    # erste Zeile im Block "for j"
        print(i+j)  # letzte Zeile im Block "for j"
    print(i)        #letzte Zeile im Block "for i"
print('Done looping')

# Leerzeichen zwischen runden und eckigen Klammern werden ignoriert
# was beim Schreiben langer Berechnungsvorschriften hilft

long_winded_computation = (1+2+3+4+5+6
                            +7+8+9+10+11
                            +12+13)
print("long_windedcomputation: "+ str(long_winded_computation))
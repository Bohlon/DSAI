from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Ghandi", "West-Side-Story"]
num_oscars = [5, 11, 3,8,10]

# Plotte die Balken mit den Koordinaten der linken Seite [0,1,2,3,4]
# und der Höhe [num_oscars]
plt.bar(range(len(movies)), num_oscars)

plt.title('My Favorite Movies')

# Beschriftung der Achsen
plt.ylabel('# of Acedamy Awards')
plt.xlabel('Movies')
# Beschrifte die x-Achse mit den Namen der Filme in der Mitte des Balken
plt.xticks(range(len(movies)), movies)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def simulate_class_sizes():
    class1 = np.random.normal(loc = 165, scale = 5, size = 50)
    class2 = np.random.normal(loc = 170, scale = 6, size = 50)
    class3 = np.random.normal(loc = 160, scale = 4, size = 50)
    return class1, class2, class3

def save_data(class1, class2, class3):
    np.savez("class_heights.npz", class1 = class1, class2 = class2, class3 = class3)

def load_data():
    data = np.load("class_heights.npz")
    return data ['class1'], data["class2"], data["class3"]
    
def load_data_4ahif():
    data = pd.read_csv('Koerpergroessen_4AHIF.csv')
    return data

def plot_boxplot(class1, class2, class3, class4a, title):
    plt.style.use('Solarize_Light2')
    plt.figure(figsize=(8, 6))
    plt.boxplot([class1, class2, class3, class4a], labels = ['Class1', 'Class2', 'Class3', '4AHIF'])
    plt.title(title)
    plt.xlabel('Klassen')
    plt.ylabel('Größe in cm')
    plt.show()

# with saving the data
class1, class2, class3 = simulate_class_sizes()
save_data(class1, class2, class3)
class4a = load_data_4ahif()
plot_boxplot(class1, class2, class3, class4a.Koerpergroesse, 'Schülergrößen verschiedener Klassen (mit normal generierten Daten)')

# with loading the saved fdata
class1, class2, class3 = simulate_class_sizes()
class1_saved, class2_saved, class3_saved = load_data()
plot_boxplot(class1, class2, class3, class4a.Koerpergroesse, 'Schülergrößen verschiedener Klassen (mit neu generierten Daten)')
plot_boxplot(class1_saved, class2_saved, class3_saved, class4a.Koerpergroesse, 'Schülergrößen verschiedener Klassen (mit gesicherten Daten vom ersten Mal)')
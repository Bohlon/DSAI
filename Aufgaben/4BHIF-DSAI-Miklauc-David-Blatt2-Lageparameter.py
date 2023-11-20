import math
import numpy as np
import statistics as st

werte = [12.3,13.2,44.4,33.1,25.9,65.3,78.5,53.5,91.7,54.3,34.2,45.8,50.4,37.2,78.1,13.2]
minimum = 1000
maximum = 0

for i in werte:
    if (i < minimum):
        minimum = i
print(f'Minimum without libs: {minimum}')      # expected 12

for i in werte:
    if (i > maximum):
        maximum = i
print(f'Maximum without libs: {maximum}')     # expected 91

class tmp():

    def max(list):
        maxi = 0
        for i in list:
            if (i > maxi):
                maxi= i
        print(f'Max: {maxi}')
        return maxi

    def min(list):
        mini = 1000
        for i in list:
            if (i < mini):
             mini = i
        print(f'Min: {mini}')
        return mini
    
    def floor(list):
        rounded_values = [int(x) for x in list]
        print(f'Floor: {rounded_values}')
        return np.array(rounded_values)
    
    def ceil(list):
        rounded_values = []
        for x in list:
            rounded_values.append(-(-x // 1))
        print(f'Ceil: {rounded_values}')
        return rounded_values

    def mode(list):
        counts = {}
        for num in list:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        
        max_count = max(counts.values())
        modes = [num for num, count in counts.items() if count == max_count]
        print(f'Mode: {modes}')
        return modes[0] if modes else None

    def mean(list):
        y = 0
        erg = 0
        for i in list:
            y+=i
        erg = y/len(list)
        print(f'Mean: {erg}')
        return erg

    def median(list):
        half = len(list) // 2
        list.sort()
        if not len(list) % 2:
            return (list[half - 1] + list[half]) / 2.0
        print(f'Median: {list[half]}')
        return list[half]

    def range(list):
        erg = max(list)-min(list)
        print(f'Range: {erg}')
        return erg

    def standard_derivation(list):
        mean = sum(list) / len(list)
        var = sum((l-mean)**2 for l in list) / len(list)
        st_dev = math.sqrt(var)
        print(f'Standart Derivation: {st_dev}')
        return st_dev

    def variance(list):
        n = len(list)
        mean = sum(list) / n
        deviations = [(x - mean) ** 2 for x in list]
        variance = sum(deviations) / n
        print(f'Variance: {variance}')
        return variance

assert tmp.max(werte) == np.max(werte)
assert tmp.min(werte) == np.min(werte)
assert np.array_equal(tmp.floor(werte), np.floor(werte))
assert np.array_equal(tmp.ceil(werte), np.ceil(werte))
assert np.array_equal(tmp.mode(werte), st.mode(werte))
assert tmp.mean(werte) == np.mean(werte)
assert tmp.median(werte) == np.median(werte)
assert tmp.range(werte) == 79.4
assert np.isclose(tmp.standard_derivation(werte), np.std(werte), rtol=10)
assert np.isclose(tmp.variance(werte), np.var(werte), rtol=10)
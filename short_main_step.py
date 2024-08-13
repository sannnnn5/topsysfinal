def main(data):
    attributes = list(data.keys())[1:]  # Exclude the 'mod' key
    results = []

    for attr in attributes:
        attribute_sum = sum(map(float, data[attr]))
        result = {car: float(value) / (attribute_sum * 2) * 0.5 
                  for car, value in zip(data[list(data.keys())[0]], data[attr])}
        results.append(result)

    return tuple(results)

# Example usage
data = {'mod': ['mod1', 'mod2'], 'prc': ['111', '222'], 'rng': ['111', '222'], 'pow': ['111', '222'], 'acss': ['111', '222'], 'top': ['111', '222']}
data2 = {'1': ['mod1', 'mod2'], '2': ['11', '21'], '3': ['12', '22'], '4': ['13', '23'], '5': ['14', '24'], '6': ['15', '25'], '7': ['16', '26'], '8': ['17', '27'], '9': ['13', '23'], '10': ['14', '24'], '11': ['15', '25'], '12': ['16', '26'], '13': ['17', '27']}

ddt = main(data2)

for i in ddt:
    print(i)
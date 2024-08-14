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
prcnt=[8.333333333333333, 8.333333333333333, 8.333333333333333, 8.333333333333333, 8.333333333333333, 8.333333333333333, 8.333333333333333, 8.333333333333333, 8.333333333333333, 8.333333333333333, 8.333333333333333,8.333333333333333 ]

dddic={}
x=0
for i in ddt:
    x+=1
    dddic[f'dict {x}']=i

c=0
for i in dddic.values():
    c+=1
    for f,e in zip(i.values(),prcnt):
        ssx=(f*e)/100
        print(f'{c} {ssx}')



def calculate_input(cp_p, cr_p, cpp_p, c1_p, t_p, car_price, car_range, car_power, car_100, car_top_spd):
    cp = {k: (v * cp_p) / 100 for k, v in car_price.items()}
    cr = {k: (v * cr_p) / 100 for k, v in car_range.items()}
    cpp = {k: (v * cpp_p) / 100 for k, v in car_power.items()}
    c1 = {k: (v * c1_p) / 100 for k, v in car_100.items()}
    t = {k: (v * t_p) / 100 for k, v in car_top_spd.items()}
    return cp, cr, cpp, c1, t


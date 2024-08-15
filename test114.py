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
def calculate_input(ddt,prcnt):
    dddic={}
    x=0
    for i in ddt:
        x+=1
        dddic[f'dict {x}']=i
    ddol=[]
    for i,e in zip(dddic.values(),prcnt):
        ddo={}
        for f,z in zip(i.values(),i.keys()):
            ssx=(f*e)/100
            ddo[z]=ssx
        ddol.append(ddo)
    return ddol

# ///////

data = {'mod': ['mod1', 'mod2'], 'prc': ['111', '222'], 'rng': ['111', '222'], 'pow': ['111', '222'], 'acss': ['111', '222'], 'top': ['111', '222']}
data2 = {'1': ['mod1', 'mod2'], '2': ['11', '21'], '3': ['12', '22'], '4': ['13', '23'], '5': ['14', '24'], '6': ['15', '25'], '7': ['16', '26'], '8': ['17', '27'], '9': ['13', '23'], '10': ['14', '24'], '11': ['15', '25'], '12': ['16', '26'], '13': ['17', '27']}
ddt = main(data)
prcnt=[40,10,10,15,25]

# //////
ddol=calculate_input(ddt,prcnt)      
d=0
for i in ddol:
    d+=1
    print(d,"-",i)


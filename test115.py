# data = {'mod': ['mod1', 'mod2'], 'prc': ['111', '222'], 'rng': ['111', '222'], 'pow': ['111', '222'], 'acss': ['111', '222'], 'top': ['111', '222']}
# data2 = {'1': ['mod1', 'mod2'], '2': ['11', '21'], '3': ['12', '22'], '4': ['13', '23'], '5': ['14', '24'], '6': ['15', '25'], '7': ['16', '26'], '8': ['17', '27'], '9': ['13', '23'], '10': ['14', '24'], '11': ['15', '25'], '12': ['16', '26'], '13': ['17', '27']}
# data3 = {'mod': ['mod1', 'mod3'], 'prc': ['222', '111'], 'rng': ['222', '111'], 'pow': ['222', '111'], 'acss': ['222', '111'], 'top': ['222', '111']}

# preference = [None,"<","<","<","<","<"]
# prcnt=[20,20,20,20,20]

def all(data, preferences, percentages):
    data1 = main(data)
    calc_o=calculate_input(data1,percentages)
    shed_mi,shed_mx=shed(calc_o,preferences)
    st_b=step4bed(calc_o,shed_mx)
    st_g=step4good(calc_o,shed_mi)
    srt_fi=fin_num(st_g,st_b)
    return srt_fi


def main(data):
    attributes = list(data.keys())[1:]  
    results = []
    for attr in attributes:
        attribute_sum = sum(map(float, data[attr]))
        result = {car: float(value) / (attribute_sum * 2) * 0.5 
                  for car, value in zip(data[list(data.keys())[0]], data[attr])}
        results.append(result)
    return tuple(results)

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

def shed(ddol,preference):
    minsc = []
    maxsc = []
    for i in ddol:
        d = {}
        d["good"] = min(i.values()) 
        minsc.append(d['good'])
        d["bed"] = max(i.values())
        maxsc.append(d['bed'])

    ggdrs = []
    bbdrs = []
    ds = 0
    for i,e in zip(minsc,maxsc):
        ds+=1
        if preference[ds] == "<":
            ggdrs.append(i)
            bbdrs.append(e)
        else:
            ggdrs.append(e)
            bbdrs.append(i)
    return ggdrs, bbdrs

def step4bed(data,bed_results):
    d=0
    qqq = []
    qqs = {}
    for i, b in zip(data, bed_results):
        for z in i:
            n = abs((i[z] - b) * 2)
            if z in qqs:
                qqs[z] += n
            else:
                qqs[z] = n
    qqq.append(qqs)
    snqs=[]
    nqs={}
    for i in qqq:
        for c in i:
            nqs[c]=i[c]*0.5
        snqs.append(nqs)
    return snqs

def step4good(data,good_results):
    qqq = []
    qqs = {}
    for i, b in zip(data, good_results):
        for z in i:
            n = abs((i[z] - b) * 2)
            if z in qqs:
                qqs[z] += n
            else:
                qqs[z] = n
    qqq.append(qqs)
    snqs=[]
    nqs={}
    for i in qqq:
        for c in i:
            nqs[c]=i[c]*0.5
        snqs.append(nqs)
    return snqs

def fin_num(min_num, max_num):
    ddmn=min_num
    ddmx=max_num
    fin={}
    for i,x in zip(ddmn,ddmx):

        for e,v in zip(i,x):
            fin[e]=x[v]/(x[v] + i[e])
    sorted_values_desc = sorted(fin.items(), key=lambda x: x[1], reverse=True)
    return sorted_values_desc

data = {'mod': ['mod1', 'mod2'], 'prc': ['111', '222'], 'rng': ['111', '222'], 'pow': ['111', '222'], 'acss': ['111', '222'], 'top': ['111', '222']}
data2 = {'1': ['mod1', 'mod2'], '2': ['11', '21'], '3': ['12', '22'], '4': ['13', '23'], '5': ['14', '24'], '6': ['15', '25'], '7': ['16', '26'], '8': ['17', '27'], '9': ['13', '23'], '10': ['14', '24'], '11': ['15', '25'], '12': ['16', '26'], '13': ['17', '27']}
data3 = {'mod': ['mod1', 'mod3'], 'prc': ['222', '111'], 'rng': ['222', '111'], 'pow': ['222', '111'], 'acss': ['222', '111'], 'top': ['222', '111']}

preference = [None,"<","<","<","<","<"]
prcnt=[20,20,20,20,20]

print(all(data3,preference,prcnt))


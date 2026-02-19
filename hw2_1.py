def analyze_data(data:list):
    return {
        p[0] : {k[1]:[int(i[-1]) for i in [i.split(',') for i in data] if i[1]==k[1] and i[0]==p[0]] for k in [i.split(',') for i in data] if k[0]==p[0]} for p in [i.split(',') for i in data]
    }

def analyze_data_2(data:list):
    d= {
        p[0] : {k[1]:[int(i[-1]) for i in [i.split(',') for i in data] if i[1]==k[1] and i[0]==p[0]] for k in [i.split(',') for i in data] if k[0]==p[0]} for p in [i.split(',') for i in data]
    }
    b=[[i.split(',')[0],i.split(',')[1], sum((d.get(i.split(',')[0])).get(i.split(',')[1]))/len((d.get(i.split(',')[0])).get(i.split(',')[1]))] for i in data] #data with average
    c=[[i.split(',')[1], sum([int(_[-1]) for _ in [i.split(',') for i in data] if _[1]==i.split(',')[1]])/len([int(_[-1]) for _ in [i.split(',') for i in data] if _[1]==i.split(',')[1]])] for i in data]
    return {
        'av_res': {p[0]:sum([sum((d.get(p[0])).get(k)) for k in set([(i.split(','))[1] for i in data if (i.split(','))[0]==p[0]])])/sum([len((d.get(p[0])).get(k)) for k in set([(i.split(','))[1] for i in data if (i.split(','))[0]==p[0]])]) for p in [i.split(',') for i in data]},
        'best_subj':{p[0]: [i[1] for i in b if i[0]==p[0] and i[-1]==max([_[-1] for _ in b if _[0]==p[0]])]  for p in b},
        'hardest_subj': set([i[0] for i in c if i[-1]==min([_[-1] for _ in c])]),
    }


print(analyze_data_2([
    "Ivan,Math,78",
    "Anna,Math,92",
    "Ivan,Physics,85",
    "Anna,Physics,90",
    "Ivan,Math,81"
]))
import pandas as pd
def solve(capacity,unit,machine,cost):
    o = []
    tot = 0
    while capacity > 0:
        ind = cost.index(min(cost))
        p = capacity//unit[ind]
        if p == 0:
            cost = cost[:ind]
            continue
        m = machine[ind]
        o.append((m,p))
        capacity = capacity % unit[ind]
        tot += p*cost[ind]*unit[ind]
        cost = cost[:ind]
    return o,tot
        
db = pd.read_csv("db.csv")
inputs = list(input("input: ").split(" "))

for i in range(len(inputs)):
    if "Hour" in inputs[i]:
        t = int(inputs[i-1])
    elif inputs[i]=="units":
        c =  int(inputs[i-1])
c *= t
d = {"Output":[]}
col = db.columns

for i in range(2,len(col)):
    di = {}
    m = []
    tot = 0
    x = db[col[i]]/db[col[0]]
    cost = x.to_list()
    unit = db[col[0]].to_list()
    machine = db[col[1]].to_list()
    a,b = solve(c,unit,machine,cost)
    di["region"] = col[i]
    di["totalcost"] = '$'+str(int(b))
    di["machines"] = a
    d["Output"].append(di)
    

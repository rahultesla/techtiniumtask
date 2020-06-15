import pandas as pd

class Solution():
    def __init__(self):
        self.db = pd.read_csv("db.csv")
        
        self.c = 10
        
        self.d = {"Output":[]}
    def promptinput(self):
        inputs = list(input("input: ").split(" "))
        for i in range(len(inputs)):
            if "Hour" in inputs[i]:
                t = int(inputs[i-1])
            elif inputs[i]=="units":
                c =  int(inputs[i-1])
        self.c = c * t
    def solve(self,capacity,unit,machine,cost):
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
    def findanswer(self):
        col = self.db.columns
        for i in range(2,len(col)):
            di = {}
            m = []
            tot = 0
            x = self.db[col[i]]/self.db[col[0]]
            cost = x.to_list()
            unit = self.db[col[0]].to_list()
            machine = self.db[col[1]].to_list()
            a,b = Solution.solve(self,self.c,unit,machine,cost)
            di["region"] = col[i]
            di["totalcost"] = '$'+str(int(b))
            di["machines"] = a
            self.d["Output"].append(di)
    def output(self):
        return self.d
    

s = Solution()
s.promptinput()
s.findanswer()
print(s.output())
    

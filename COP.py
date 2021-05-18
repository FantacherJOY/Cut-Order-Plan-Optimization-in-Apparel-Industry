import random
import math

import pandas as pd

temp=100
for k in range(200):

    demand={'XS':1686,'S':4310,'M':4228,'L':2924,'XL':1946}

    length={'XS':1.01,'S':1.08,'M':1.15,'L':1.21,'XL':1.42}
    #Cutter Minimum Height
    h_min=10
    #Cutter Maximum Height
    h_max=200
    L_max=22
    d=demand
    m=2*len(demand)
    O=[]
    l=list(demand.keys())
    l.append('Plies')
    l.append("Yards")
    l.append("Inchs")
    l.append("Tot Fabric")
    O.append(l)                                                       
    i=1
    while(sum(v for v in demand.values() if v > 0)):
        new=[]
        if i<m:
            for x in demand.keys():
                if 0<demand[x]<h_min:
                    demand[x]=h_min
            h=random.randint(max(h_min,1),min(h_max,max(h_min,max(demand.values()))))
            l=0
            lj=0
            for j in demand.keys():
                if demand[j]>0:
                    Ois=random.randint(0, math.floor(demand[j]/h))
                    lj=Ois*length[j]+lj
                else:
                    Ois=0
                if lj<=L_max:
                    new.append(Ois)
                    l=lj
                elif lj>L_max:
                    Ois=math.floor((L_max-l)/length[j])
                    l=Ois*length[j]+l
                    new.append(Ois)
                else:   
                    new.append(0)
                demand[j]=demand[j]-h*Ois
            if sum(new)==0:
                pass
            else:
                new.append(h)
                new.append(int(l))
                new.append(round((l-int(l))*36))
                new.append(math.ceil(h*l))
                O.append(new)
        else:
            while(max(demand.values())>0):
                new=[]
                h=max(h_min,min(min(demand.values()),h_max))
                l=0
                lj=0
                for j in demand.keys():              
                    if demand[j]>=h_min:
                        if l<=L_max:
                            Ois=math.floor(demand[j]/h)
                            lj=Ois*length[j]+lj
                            if lj<=L_max:
                                new.append(Ois)
                                l=lj
                            else:
                                Ois=math.floor((L_max-l)/length[j])
                                l=Ois*length[j]+l
                                new.append(Ois)
                            demand[j]=demand[j]-h*Ois
                        else:
                            new.append(0)
                    elif 0<demand[j]<h_min:
                        if l<=L_max:
                            Ois=math.ceil(demand[j]/h)
                            lj=Ois*length[j]+lj
                            if lj<=L_max:
                                new.append(Ois)
                                l=lj
                            else:
                                Ois=math.ceil((L_max-l)/length[j])
                                l=Ois*length[j]+l
                                new.append(Ois)
                            demand[j]=demand[j]-h*Ois
                        else:
                            new.append(0)
                    else:
                        new.append(0)
                new.append(h)
                new.append(int(l))
                new.append(round((l-int(l))*36))
                new.append(math.ceil(h*l))
                O.append(new)
        
        # print(i)
        i=i+1
    H5=pd.DataFrame(O)
    new_header = H5.iloc[0] 
    H5= H5[1:]
    H5.columns = new_header
    if len(H5)<temp:
        H=H5
        temp=len(H)
      
H['Plies']=H['Plies'].astype(str).astype(int)
l=[]

for i in H.columns:
    if i in demand.keys():
        l.append((H[i]*H['Plies']).sum())

    else:
        l.append(H[i].sum())
    
H.loc[len(H.index)] = l

H.rename(index={10:'Total'}, inplace=True)





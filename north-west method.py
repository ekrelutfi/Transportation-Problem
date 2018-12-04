    def nwm1(supply, demand, cost):
    s=list(supply)
    d=list(demand)
    k=np.zeros((len(s),len(d)))
    x=0; y=0
    result = np.zeros((len(s),len(d)))
    i=0;j=0
    t=0
    while (x<len(s) and y<len(d)):
        if s[x] < d[y]:
            k[x][y]=s[x]
            d[y] = d[y]-s[x]
            s[x] = 0
            x = x+1
        else:
            k[x][y]= d[y]
            s[x] = s[x]-d[y]
            d[y] = 0
            y = y+1
    for i in range(len(s)):
        for j in range(len(d)):
            result[i][j]=cost[i][j]*k[i][j]
            t = t + result[i][j]
    print ('Solution:')
    print (result)
    print ('Total Cost:', t)
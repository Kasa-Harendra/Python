def LCW(u,v):
    for r in range(len(u)+1):
        LCW[r][len(v)+1]=0
    for c in range(len(v)+1):
        LCW[len(u)+1][c]=0
    maxLCW =0
    for c in range(len(v)+1,-1,-1):
        for r in range(len(u)+1,-1,-1):
            if u[r] == v[c]:
                LCW[r][c] = 1+LCW[r+1][c+1]
            else:
                LCW[r][c] = 0
            if maxLCW < LCW[r][c]:
                maxLCW = LCW[r][c]
    return maxLCW

u = "sector"
v = "bisect"
print(LCW(u,v))

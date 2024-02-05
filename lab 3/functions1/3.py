def solve(numheads, numlegs):
    r_cnt = 0
    c_cnt = 0
    if numlegs % 2 == 0 and numlegs > numheads:
        r_cnt = (numlegs // 2) - numheads
        c_cnt = numheads - r_cnt
    return r_cnt, c_cnt

numheads, numlegs = int(input("Heads:")), int(input("Legs:"))
print("Answer:",solve(numheads, numlegs))
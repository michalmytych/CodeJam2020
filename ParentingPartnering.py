# Code I finally used in ParentingPartnering problem on CodeJam 2020 

def CameronJamie(przedzialy):
    przedzialy = [(przedzialy[i][0], przedzialy[i][1], i) for i in range(len(przedzialy))]
    przedzialy.sort(key=lambda x: x[0])
    literyPlusNumer = []
    kCameron = 0
    kJamie = 0
    for start, koniec, numer in przedzialy:
        if start < kCameron and start < kJamie:
            return "IMPOSSIBLE"
        elif start >= kCameron:
            literyPlusNumer.append(("C", numer))
            kCameron = koniec
        else:
            literyPlusNumer.append(("J", numer))
            kJamie = koniec
    
    literyPlusNumer.sort(key=lambda x: x[1])
    ostateczny_lancuch = ''
    for literka, numer in literyPlusNumer:
        ostateczny_lancuch += literka
    
    return ostateczny_lancuch


T = int(input())
lista_zbierajaca = []
for i in range(1, T+1):
    N = int(input().strip())
    przedzialy = []
    for n in range(N):
        nowe_zajecie = list(map(int, input().strip().split()))
        przedzialy.append(nowe_zajecie)
    literyPlusNumer = CameronJamie(przedzialy)
    lista_zbierajaca.append(literyPlusNumer)
for t in range(len(lista_zbierajaca)):
    print("Case #{}: {}".format(t+1, lista_zbierajaca[t]))
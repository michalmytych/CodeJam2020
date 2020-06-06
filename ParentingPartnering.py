# Code I finally used in ParentingPartnering problem on CodeJam 2020 

def CameronJamie(przedzialy):
    # tworzę za pomocą list comprehension listę skladajaca sie z krotek + numer krotki 
    przedzialy = [(przedzialy[i][0], przedzialy[i][1], i) for i in range(len(przedzialy))]
    # sortuję według czasu rozpoczęcia się zajęcia (lambda zwraca start)
    przedzialy.sort(key=lambda x: x[0])
    literyPlusNumer = []
    kCameron = 0
    kJamie = 0
    # odwołuje się do krotek z listy przedzialy gdzie jest start,
    # zakończenie oraz indeks krotki
    for start, koniec, numer in przedzialy:
        if start < kCameron and start < kJamie:
            return "IMPOSSIBLE"
        elif start >= kCameron:
            literyPlusNumer.append(("C", numer))
            kCameron = koniec
        else:
            literyPlusNumer.append(("J", numer))
            kJamie = koniec
    
    # sortuję po indeksie
    literyPlusNumer.sort(key=lambda x: x[1])
    # łańcuch literek
    ostateczny_lancuch = ''
    for literka, numer in literyPlusNumer:
        ostateczny_lancuch += literka
    
    return ostateczny_lancuch


# Liczba przypadków
T = int(input())
lista_zbierajaca = []
for i in range(1, T+1):
    N = int(input().strip()) # liczba przedzialow czasowych
    # czyszczenie listy z przedzialami czasowymi:
    przedzialy = []
    for n in range(N):
        # mapuję listę funkcją int()
        nowe_zajecie = list(map(int, input().strip().split()))
        przedzialy.append(nowe_zajecie)  # przekazywane do przedzialy  
    literyPlusNumer = CameronJamie(przedzialy)
    lista_zbierajaca.append(literyPlusNumer)
for t in range(len(lista_zbierajaca)):
    print("Case #{}: {}".format(t+1, lista_zbierajaca[t]))
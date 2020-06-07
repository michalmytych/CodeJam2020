# Code I finally used in NestingDepth problem on CodeJam 2020 

def NestingTesting(S):
    Sp = ""

    S = S + "0"

    Sp = Sp + (int(S[0]) * "(")

    for i in range(len(S)-1):
        if int(S[i]) - int(S[i+1]) > 0:
            Sp = Sp + S[i]
            Sp = Sp + ((int(S[i]) - int(S[i+1])) * ")")
        else:
            Sp = Sp + S[i]
            Sp = Sp + ((int(S[i+1]) - int(S[i])) * "(")
    
    return Sp


T = int(input())

for t in range(int(T)):
    S = input()
    Sp = NestingTesting(S)

    print('Case #{}: {}'.format(t+1, Sp))


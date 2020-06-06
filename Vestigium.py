# Code I finally used in Vestigium problem on CodeJam 2020 


T = int(input()) # liczba przypadkow

for t in range(T):
    N = int(input())     # pobranie wymiaru macierzy (N x N)
    rows_wer = 0
    columns_wer = 0
    trace = 0
    matrix = []
    # mechanizm liczenia wierszy które zawierają powtórzenia
    for n in range(N):
        row = input().split()
        if len(row) != len(set(row)):
            rows_wer += 1
        matrix += row
    
    # mechanizm liczenia śladu macierzy
    for x in range(N):
        trace += int(matrix[x * (N+1)])

    # mechanizm liczenia kolumn które zawierają powtórzenia
    for y in range(N):
        column = []
        for z in range(N):      # de facto tworzenie kolumny
            column.append(matrix[(z * N) + y])
        
        if len(column) != len(set(column)):
            columns_wer += 1

    print('Case #{}: {} {} {}'.format(t+1, trace, rows_wer, columns_wer))
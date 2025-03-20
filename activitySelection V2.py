

def activitySelection(n1, start, end):
    risposta = 0
    finish = -1
    """
    La variabile è inizializzata a -1 perché start 
    può anche essere 0.
    """
    for i in range(n1):
        if start[i] > finish:
            finish = end[i]
            risposta += 1
    return risposta

def ordinamentoVettori(n1, start, end):
    for i in range(n1):
        for j in range(n1-i-1):
            if start[j] > start[j+1]:
                start[j], start[j+1] = start[j+1], start[j]
                end[j], end[j+1] = end[j+1], end[j]

N = int(input("Inserisci il numero di richieste: "))
start = []
end = []
for i in range(N):
    start.append(int(input("Inserisci l'orario di inizio: ")))
    end.append(int(input("Inserisci l'orario di fine: ")))

# Ordina le attività in base all'orario di inizio
ordinamentoVettori(N, start, end)
print(activitySelection(N, start, end))

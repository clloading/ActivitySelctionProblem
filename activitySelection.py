
def activitySelection(n1,start, end):

    risposta = 0

    finish = -1 
    """"
    "la variabile è inizializzata a -1 perchè start 
    può anche essere 0. 
    """

    for i in range(n1):
        if start[i] > finish:
            finish = end[i]
            risposta += 1

    return risposta


N= int(input("inserisci il numero di richieste:"))
start = []
end = []
for i in range(N):
    start.append(int(input("inserisci l'orario di inizio:")))
    end.append(int(input("inserisci l'orario di fine:")))

print(activitySelection(N,start, end))

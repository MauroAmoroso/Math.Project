while True: 
    # Inizializzazione della variabile Choice
    Choice = 0 
    # Richiesta di input per scegliere tra avere già un budget (1) o trovarlo (2)
    Choice = int(input("Scrivi 1 se hai già un budget o 2 se vuoi trovarlo: "))
    # Variabile di controllo per uscire dai cicli
    uscita = False
    home=False
    
    if Choice == 1:
        # Input del budget totale e del numero di persone
        Budget = float(input("Budget totale: "))
        Persone = int(input("Numero di persone: "))

        # Ciclo per continuare a chiedere le percentuali finché la somma non è 100
        while True:
            print("Adesso scegli le percentuali in modo che la somma sia 100%")
            Aperitivo = float(input("Budget in aperitivo: "))
            Cena = float(input("Budget in cena: "))
            Main = float(input("Budget in evento principale: "))

            # Calcolo della somma delle percentuali
            somma_percentuali = Aperitivo + Cena + Main

            if somma_percentuali == 100:
                # Conferma che la distribuzione del budget è corretta
                print("Hai distribuito correttamente il budget.")
                
                # Ripeti la cassa fino a quando l'utente decide di fermarsi
                while True:
                    # Richiesta di input per scegliere gli eventi a cui partecipare
                    Choice2 = input("Ora scegli gli eventi a cui parteciperai: 1=Aperitivo, 2=Cena, 3=Main Event. (Scrivi 'esci' per uscire o 'home per riiniziare': ")
                    # Controllo per vedere se l'utente vuole uscire, il.".lower()" serve per poter usare anche maiuscole
                    if Choice2.lower() == 'esci':
                        uscita = True
                        break
                    if Choice2.lower() == 'home':
                        home=True
                        break

                    # Inizializzazione dei costi per evento
                    CostoAperitivo = 0
                    CostoCena = 0
                    CostoMain = 0

                    # Controllo degli eventi scelti e calcolo dei costi
                    if '1' in Choice2:
                        CostoAperitivo = Aperitivo / 100 * Budget / Persone
                    if '2' in Choice2:
                        CostoCena = Cena / 100 * Budget / Persone
                    if '3' in Choice2:
                        CostoMain = Main / 100 * Budget / Persone

                    # Calcolo del costo totale per cliente
                    CostoTotaleCliente = CostoAperitivo + CostoCena + CostoMain
                    
                    # Stampa dei costi
                    print(f"Costo Aperitivo: {CostoAperitivo:.2f}")
                    print(f"Costo Cena: {CostoCena:.2f}")
                    print(f"Costo Main Event: {CostoMain:.2f}")
                    print(f"Costo totale per cliente: {CostoTotaleCliente:.2f}")

                # Esci dal ciclo esterno se l'utente ha scelto di uscire
                if uscita:
                    break
                if home:
                    break
            elif somma_percentuali > 100:
                # Messaggio di errore se la somma delle percentuali è maggiore di 100
                print(f"Devi togliere {abs(100 - somma_percentuali)}%")
            elif somma_percentuali < 100:
                # Messaggio di errore se la somma delle percentuali è minore di 100
                print(f"Devi aggiungere {100 - somma_percentuali}%")
    if uscita:
        break
    elif Choice == 2:
        # Richiesta di input per il costo massimo per persona e il numero di persone
        CostoMaxPersona = round(float(input("Scrivi i soldi che si pagherebbero per partecipare a tutti gli eventi: ")), 2)
        Persone = int(input("Quante persone verranno?: "))
        # Calcolo del budget totale
        Budget = CostoMaxPersona * Persone
        print(f"Budget totale: {Budget:.2f}")

        # Ciclo per continuare a chiedere le percentuali finché la somma non è 100
        while True:
            print("Adesso scegli le percentuali in modo che la somma sia 100%")
            Aperitivo = float(input("Budget in aperitivo: "))
            Cena = float(input("Budget in cena: "))
            Main = float(input("Budget in evento principale: "))

            # Calcolo della somma delle percentuali
            somma_percentuali = Aperitivo + Cena + Main

            if somma_percentuali == 100:
                # Conferma che la distribuzione del budget è corretta
                print("Hai distribuito correttamente il budget.")
                
                # Ripeti la cassa fino a quando l'utente decide di fermarsi
                while True:
                    # Richiesta di input per scegliere gli eventi a cui partecipare
                    Choice2 = input("Ora scegli gli eventi a cui parteciperai separati da uno spazio: 1=Aperitivo, 2=Cena, 3=Main Event. (Scrivi 'esci' per uscire o 'home per riiniziare'): ")
                    # Controllo per vedere se l'utente vuole uscire
                    if Choice2.lower() == 'esci':
                        uscita = True
                        break
                    if Choice2.lower() == 'home':
                        home=True
                        break

                    # Inizializzazione dei costi per evento
                    CostoAperitivo = 0
                    CostoCena = 0
                    CostoMain = 0

                    # Controllo degli eventi scelti e calcolo dei costi
                    if '1' in Choice2:
                        CostoAperitivo = Aperitivo / 100 * CostoMaxPersona
                    elif '2' in Choice2:
                        CostoCena = Cena / 100 * CostoMaxPersona
                    elif '3' in Choice2:
                        CostoMain = Main / 100 * CostoMaxPersona
                    else:
                        print("Scrivi valori accettabili")

                    # Calcolo del costo totale per cliente
                    CostoTotaleCliente = CostoAperitivo + CostoCena + CostoMain
                    
                    # Stampa dei costi
                    print(f"Costo Aperitivo: {CostoAperitivo:.2f}")
                    print(f"Costo Cena: {CostoCena:.2f}")
                    print(f"Costo Main Event: {CostoMain:.2f}")
                    print(f"Costo totale per cliente: {CostoTotaleCliente:.2f}")

                # Esci dal ciclo esterno se l'utente ha scelto di uscire
                if uscita:
                    break
                if home:
                    break
            elif somma_percentuali > 100:
                # Messaggio di errore se la somma delle percentuali è maggiore di 100
                print(f"Devi togliere {abs(100 - somma_percentuali)}%")
            elif somma_percentuali < 100:
                # Messaggio di errore se la somma delle percentuali è minore di 100
                print(f"Devi aggiungere {100 - somma_percentuali}%")
    
    # Esci dal ciclo principale se l'utente ha scelto di uscire
    if uscita:
        break
    else:
        print("Inserisci un numero: 1 o 2")

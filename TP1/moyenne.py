import sys
somme = 0
moyenne = 0
if len(sys.argv) >1:
    for i in range(1,len(sys.argv)):
        try:
            num = float(sys.argv[i])
            if 0 > num or num > 20:
                print("Notes non valides")
                moyenne = -1
                break
            else:
                somme += num
        except ValueError:
            moyenne=-1
            print("Note(s) non valide(s)")
            break
    if moyenne != -1:
        moyenne = somme/(len(sys.argv)-1)
        print(round(moyenne,2))
else:
    print("Aucune moyenne à calculer")
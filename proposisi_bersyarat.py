def implikasi(p,q):
    return not p or q

def konvers (p,q):
    return implikasi(q,p)

def invers(p,q):
    return implikasi(not p, not q)

def kontraposisi(p,q):
    return implikasi (not p, not q)

def tabel_kebenaran():
    print("\n") 
    print("TABEL KEBENARAN PROPOSISI BERSYARAT")
    print("-"* 180)
    print("| p\t alt p-> q\t q> p (Konvers) (t-p-> -q (Invers)\t-q-p (Kontraposisi)|")
    print("-"* 180)

    for p in [True, False]:
        for q in [True, False]:
            print(f"|{p}\t|{q}\t|{implikasi(p, q)}\t\t {konvers (p,q)}\t\t |{invers(p,q)}\t\t\t|{kontraposisi (p,q)}\t\t\t|")
    print("-"* 180)

tabel_kebenaran()

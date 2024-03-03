from datetime import datetime
import numpy as np


def dioDana():
    trenutno_vrijeme = datetime.now().time()

    if trenutno_vrijeme < datetime.strptime("12:00:00", "%H:%M:%S").time():
        return "jutro"
    if trenutno_vrijeme < datetime.strptime("17:00:00", "%H:%M:%S").time():
        return "prijepodne"
    if trenutno_vrijeme < datetime.strptime("20:00:00", "%H:%M:%S").time():
        return "poslijepodne"
    return "večer"


def zadatak_5():
    x = [["kruh", "maslac", "pršut"], "kefir", "sir"]
    y = x[:]
    y[2] = "paprika"
    y[0][2] = "mortadela"
    print("x", x)
    print("y", y)


def numpy_niz():
    niz = np.array([10, 2, 30, 4, 50, 6])

    srednja_vrijednost = np.mean(niz)
    zbroj = np.sum(niz)

    print("NumPy niz:", niz)
    print("Srednja vrijednost:", srednja_vrijednost)
    print("Zbroj elemenata:", zbroj)

    return niz


def sortiraj_niz(niz):
    sortirani_niz = np.sort(niz)
    print("Sortirani niz:", sortirani_niz)


def stvori_niz_cijelih_brojeva(sjeme=None):
    np.random.seed(sjeme)
    cijeli_niz = np.random.choice(np.arange(1, 101), size=10, replace=False)
    return cijeli_niz


if __name__ == '__main__':
    # print("Trenutni dio dana:", dioDana())
    # zadatak_5()
    # niz = numpy_niz()
    # sortiraj_niz(niz)

    sjeme = 42
    niz_cijelih_brojeva = stvori_niz_cijelih_brojeva(sjeme)
    print(f"Niz cijelih brojeva sa sjemenom {sjeme}:", niz_cijelih_brojeva)

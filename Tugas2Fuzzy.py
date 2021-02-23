import csv
import numpy
import matplotlib.pyplot as plt

def getData():
    readerCSV = csv.reader(open("Data2.csv"), delimiter=",")
    x = list(readerCSV)
    return numpy.array(x)

def functionturun (x, a, b):
    return ((b-x)/(b-a))

def functionnaik (x, a, b):
    return ((x-a)/(b-a))

def StatistikGaji():
    plt.title('Gaji')
    plt.plot([0, 0.5, 1], [1, 1, 0], label="rendah")
    plt.plot([0.5, 1, 1.25], [0, 1, 0], label="sedang")
    plt.plot([ 1, 1.25, 2], [0, 1, 1], label="tinggi")
    plt.show()

def StatistikHutang():
    plt.title('Hutang')
    plt.plot([0, 20, 40], [1, 1, 0], label="rendah")
    plt.plot([20, 40, 50, 70], [0, 1, 1, 0], label="sedang")
    plt.plot([50, 70, 100], [0, 1, 1], label="tinggi")
    plt.show()


def KeepData(Array):
    with open('Kelayakan.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        x = 0
        spamwriter.writerows([Array])

def Gaji(x):


    if (x <= 0.50):
        GajiRendah = 1
        GajiSedang = 0
        GajiTinggi = 0
        return GajiRendah, GajiSedang, GajiTinggi

    elif (x > 0.5 and x < 1.25):
        GajiRendah = functionturun(x, 0.5, 1.25)
        GajiSedang = functionnaik(x, 0.5, 1.25)
        GajiTinggi = 0
        return GajiRendah, GajiSedang, GajiTinggi

    if (x == 1):
        GajiRendah = 0
        GajiSedang = 0
        GajiTinggi = 1
        return GajiRendah, GajiSedang, GajiTinggi

    elif (x >= 1 and x < 1.25):
        GajiRendah = 0
        GajiSedang = functionturun(x, 1, 1.25)
        GajiTinggi = functionnaik(x, 1, 1.25)
        return GajiRendah, GajiSedang, GajiTinggi

    elif (x >= 1.25):
        GajiTinggi = 1
        GajiRendah = 0
        GajiSedang = 0
        return GajiRendah, GajiSedang, GajiTinggi



def Hasil(Layak,TidakLayak):
    return ((Layak*70) - (TidakLayak*30) / (Layak+TidakLayak))

def Tagihan(x):

    if (x <= 25):
        TagihanHutangRendah = 1
        TagihanHutangSedang = 0
        TagihanHutangTinggi = 0
        return TagihanHutangRendah, TagihanHutangSedang, TagihanHutangTinggi

    elif (x > 25 and x < 50):
        TagihanHutangRendah = functionturun (x,20,40)
        TagihanHutangSedang = functionnaik (x,20,40)
        TagihanHutangTinggi = 0
        return TagihanHutangRendah, TagihanHutangSedang, TagihanHutangTinggi

    elif (x == 50):
        TagihanHutangRendah = 0
        TagihanHutangSedang = 1
        TagihanHutangTinggi = 0
        return TagihanHutangRendah, TagihanHutangSedang, TagihanHutangTinggi

    elif (x >= 50 and x < 75):
        TagihanHutangRendah = 0
        TagihanHutangSedang = functionturun (x,50,70)
        TagihanHutangTinggi = functionnaik (x,50,70)
        return TagihanHutangRendah, TagihanHutangSedang, TagihanHutangTinggi

    elif (x >= 75):
        TagihanHutangRendah = 0
        TagihanHutangSedang = 0
        TagihanHutangTinggi = 1
        return TagihanHutangRendah, TagihanHutangSedang, TagihanHutangTinggi

    return TagihanHutangRendah, TagihanHutangSedang, TagihanHutangTinggi

def Layak(Gaji, TagihanHutang, NilaiLayak):
    if (Gaji<=TagihanHutang):
        if (Gaji>=NilaiLayak):
            return Gaji
        else:
            return NilaiLayak
    elif (TagihanHutang<Gaji):
        if (TagihanHutang>=NilaiLayak):
            return TagihanHutang
        else:
            return NilaiLayak


#gr = gajirendah#
#gs = gajisedang#
#gt = gajitinggi#
#tr = tagihanrendah#
#ts = tagihansedang#
#tt = tagihantinggi#

def HitungKelayakan(gr, gs, gt, tr, ts, tt):
    l = 0
    tl = 0
    if (gr > 0 and tr > 0):
        l = Layak(gr, tr, l)
    if (gr > 0 and ts > 0):
        l = Layak(gr, ts, l)
    if (gr > 0 and tt > 0):
        l = Layak(gr, tt, l)
    if (gs > 0 and tr > 0):
        tl = Layak(gs, tr, tl)
    if (gs > 0 and ts > 0):
        tl = Layak(gs, ts, l)
    if (gs > 0 and tt > 0):
        l = Layak(gs, tt, l)
    if (gt > 0 and tt > 0):
        l = Layak(gt, tt, l)
    if (gt > 0 and tr > 0):
        tl = Layak(gt, tr, tl)
    if (gt > 0 and ts > 0):
        tl = Layak(gt, ts, tl)
    return l, tl


List = getData()
y = []
z = []
for i in range (1,101):
    h = Tagihan(float(List[i][2]))
    p = Gaji(float(List[i][1]))
    per = HitungKelayakan(p[0], p[1], p[2], h[0], h[1], h[2])
    y.append([Hasil(per[0], per[1]), str(i)])
y.sort()
x = 100
while (x != 80):
    z.append(y[x - 1][1])
    x -= 1
print(z)
KeepData(z)
StatistikHutang()
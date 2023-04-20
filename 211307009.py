#Yunus Emre Gül
import sys


def dosyadan_oku(txtdosyasi):
    sayilar_matrisi = []
    with open(txtdosyasi, 'r') as file:
        for line in file:
            row = []
            for c in line.strip():
                if c.isdigit():
                    row.append(int(c))
            if row:
                sayilar_matrisi.append(row)
    return sayilar_matrisi


def dosyaya_yazdir(txtdosyasi, sayilar_matrisi):
    with open(txtdosyasi, 'w') as f:
        for satir in sayilar_matrisi:
            f.write(''.join(map(str, satir)) + '\n')


def tahta_yazdir(sayilar_matrix):
    print("------------Sayi Tahtasi------------")
    sayi_satir = len(sayilar_matrix)
    sayi_sutun = len(sayilar_matrix[0])
    for i in range(sayi_satir):
        for j in range(sayi_sutun):
            print(sayilar_matrix[i][j], end="\t")  # bosluk birakarak yazdir
        print()


def puan_hesapla(sayi_degeri, bosalan_hucre):
    puan = sayi_degeri * fibonacci(bosalan_hucre)
    return puan

def fibonacci(a):
    if a <= 1:
        return a
    else:
        return fibonacci(a - 1) + fibonacci(a - 2)

#herhangi bir hucrenin komsusu o hucre ile ayni mi
def oyun_devam(sayilar_matrisi):
    for i in range(len(sayilar_matrisi)):
        for j in range(len(sayilar_matrisi[0])):
            value = sayilar_matrisi[i][j]
            if value == "":
                continue
            komsular = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for komsu in komsular:
                k_satir, k_sutun = komsu
                if 0 <= k_satir < len(sayilar_matrisi) and 0 <= k_sutun < len(sayilar_matrisi[0]) and \
                        sayilar_matrisi[k_satir][k_sutun] == value:
                    return True
    return False

#komsu buldukca komsu degerine "" ata ve nerede komsu varsa o hucreye gecip kendini yineleyen fonksiyon
def komsulari_kaldir(sayilar_matrisi, satir, sutun):
    value = sayilar_matrisi[satir][sutun]
    if value=="":
        return sayilar_matrisi
    sayilar_matrisi[satir][sutun] = ""
    # burada hucre direkt '' olmamlıdır
    if sutun > 0 and sayilar_matrisi[satir][sutun - 1] == value:
        komsulari_kaldir(sayilar_matrisi, satir, sutun - 1)
    if sutun < len(sayilar_matrisi[0]) - 1 and sayilar_matrisi[satir][sutun + 1] == value:
        komsulari_kaldir(sayilar_matrisi, satir, sutun + 1)
    if satir > 0 and sayilar_matrisi[satir - 1][sutun] == value:
        komsulari_kaldir(sayilar_matrisi, satir - 1, sutun)
    if satir < len(sayilar_matrisi) - 1 and sayilar_matrisi[satir + 1][sutun] == value:
        komsulari_kaldir(sayilar_matrisi, satir + 1, sutun)
    return sayilar_matrisi


#satirda "" degeri olursa ustteki elemani alta tasima islemini yaptik
def sayilari_tasi_satir(sayilar_matrisi):
    bos_sayisi = 0
    bos_satirlar = []
   # puan hesaplama isleminde kullanacagimiz bos sayisi
    for sutun in range(len(sayilar_matrisi[0])):
        for satir in range(len(sayilar_matrisi)):
            if sayilar_matrisi[satir][sutun] == "":
                bos_sayisi += 1
                bos_satirlar.insert(0, satir)  # ekleme yaparken ilk bulunan elemani listenin başına ekliyoruz ki sutunlar duzgunce asagiya kayabilsin
        if bos_sayisi > 0:
            for i in range(bos_sayisi):
                for j in range(len(bos_satirlar)):
                    if bos_satirlar[j] > 0 and sayilar_matrisi[bos_satirlar[j] - 1][sutun] != "":
                        sayilar_matrisi[bos_satirlar[j]][sutun], sayilar_matrisi[bos_satirlar[j] - 1][sutun] = sayilar_matrisi[bos_satirlar[j] - 1][sutun], sayilar_matrisi[bos_satirlar[j]][sutun]

    return bos_sayisi

#sutun bossa sola kaydirma islemini gerceklestir
def sutun_bos_mu(sayilar_matrisi):
    bos_sutunlar = []
    for i in range(len(sayilar_matrisi[0])):
        sutun = [sayilar_matrisi[j][i] for j in range(len(sayilar_matrisi))]
        if all(val == "" for val in sutun):
            bos_sutunlar.append(i)  # burada satirlardaki gibi insert islemi yapilmadi cunku burda ilk giren elemanin ilk eklenmesini istiyoruz

    for i in range(len(sayilar_matrisi)):
        for j in bos_sutunlar:
            for k in range(j + 1, len(sayilar_matrisi[0])):
                temp = sayilar_matrisi[i][k]
                sayilar_matrisi[i][k] = sayilar_matrisi[i][k - 1]
                sayilar_matrisi[i][k - 1] = temp
    return sayilar_matrisi

#kullanicinin girdigi degerleri azaltmak gerekli bir islem
def deger_azalt(satir, sutun):
    satir = satir - 1
    sutun = sutun - 1
    return satir, sutun



def oyun_oynat(sayilar_matrisi,output_adi):
    new_matrix=sayilar_matrisi
    new_puan=0
    puan=0
    while oyun_devam(new_matrix):
        tahta_yazdir(new_matrix)
        print("Puan: " + str(new_puan))
        girdi = input("Seçmek istediğiniz elemanın satır ve sütun indekslerini giriniz (örnek: 2 3): ")
        satir, sutun = map(int, girdi.split())
        satir, sutun = deger_azalt(satir, sutun)
        if 0 <= satir < len(new_matrix) and 0 <= sutun < len(new_matrix[0]):
            value=new_matrix[satir][sutun]
            if ((satir > 0 and sayilar_matrisi[satir - 1][sutun] == value) or #burda secilen elemanin herhangi bir komsusu var mi ve eleman bos mu kontrol ediyorum
                        (satir < len(sayilar_matrisi)-1 and sayilar_matrisi[satir + 1][sutun] == value) or
                        (sutun > 0 and sayilar_matrisi[satir][sutun - 1] == value) or
                        (sutun < len(sayilar_matrisi[0])-1 and sayilar_matrisi[satir][sutun + 1] == value))and value != "" :
                bos_sayisi_once=sum(satir.count("") for satir in new_matrix)
                new_matrix = komsulari_kaldir(new_matrix, satir, sutun)
                bos_sayisi = sayilari_tasi_satir(new_matrix)
                bos_sayisi_sonra=sum(satir.count("") for satir in new_matrix)
                new_matrix=sutun_bos_mu(new_matrix)
                try:
                    new_puan += puan_hesapla(value, bos_sayisi_sonra-bos_sayisi_once)
                except TypeError:
                    pass
            else:
                continue
        else:
            print("Girdiginiz satir/sutun tablo boyutundan buyuktur veya negatiftir!")
   #secilen son elemandan sonra oyun biterse while loop biter dolayisiyla tahtanin son durumu ve puan yazdirilmaz
    sayilar_matrisi=sutun_bos_mu(new_matrix)
    sayilari_tasi_satir(sayilar_matrisi)
    tahta_yazdir(sayilar_matrisi)
    print("Puan: " + str(new_puan))
    dosyaya_yazdir(output_adi, sayilar_matrisi)
    print("Oyun bitti!")

#kullanicidan girdi al
if len(sys.argv) > 2:
    input_adi = sys.argv[1]
    output_adi=sys.argv[2]
    print("Dosya adı:", input_adi)
    sayilar_matrisi = dosyadan_oku(input_adi)
    oyun_oynat(sayilar_matrisi,output_adi)
else:
    print("Dosya adı belirtilmedi. Konsola gidip varsayilan matrix girdisi input.txt argumani veriniz.")

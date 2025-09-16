"""Görev

Verilen bir tam sayı olan n için aşağıdaki koşullu eylemleri gerçekleştirin:

Eğer n tek ise, Weird yazdır

n çift ise ve 2 ile 5 arasındaki kapsayıcı aralıktaysa, Not Weird yazdırın

n çift ise ve 6 ile 20 arasındaki kapsayıcı aralıktaysa, Weird yazdır

Eğer n çift ve 20'den büyükse, Not Weird yazdır

Giriş Formatı

Pozitif bir tam sayı olan n'yi içeren tek bir satır.

Kısıtlamalar

1 ≤ n ≤ 100

Çıkış Formatı

Sayı tuhafsa Weird yaz. Aksi takdirde Not Weird yaz."""


if __name__ == '__main__':
    n = int(input().strip())
    if n > 0 and 1 <= n and n <= 100:
        if n % 2 == 1:
            print("Weird")
        if n % 2 == 0:
            if 2 < n and n < 5:
                print("Not Weird")
            elif 6 < n and n <= 20:
                print("Weird")
            elif 20 < n:
                print("Not Weird")
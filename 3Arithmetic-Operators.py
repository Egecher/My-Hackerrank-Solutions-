"""Görev

Sağlanan kod parçası STDIN'den a ve b olmak üzere iki tam sayı okur. Aşağıdaki üç satırı yazdıran kodu ekleyin:

1. İlk satırda iki sayının toplamı yer alır.

2. İkinci satırda iki sayının (birinci - ikinci) farkı yer alır.

3. Üçüncü satırda iki sayının çarpımı yer alır.

Örnek

a=3

b=5

Aşağıdakileri yazdırın:

8

-2

15

Giriş Formatı

İlk satırda ilk tam sayı olan a yer alıyor.

İkinci satırda ikinci tam sayı olan b yer alıyor.

Kısıtlamalar

1 ≤ a ≤ 10¹⁰

1 ≤ b ≤ 10¹⁰

Çıkış Formatı

Yukarıda anlatıldığı gibi üç satırı yazdırın.

Örnek Giriş O

3

2

Örnek Çıkışı O

5

1

6

Açıklama O

3+2 ==> 5

3-2 ==> 1

3*2 ==> 6"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if 1 <= a <= 10**10 and 1 <= b <= 10**10:
        print(a+b)
        print(a-b)
        print(a*b)
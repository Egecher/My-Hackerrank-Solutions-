"""Görev

Sağlanan kod parçası STDIN'den a ve b olmak üzere iki tam sayıyı okur.

İki satır yazdırmak için mantık ekleyin. İlk satır, tamsayı bölme işleminin sonucunu, yani // ifadesini içermelidir.

b. İkinci satırda float bölümünün sonucu olan a / b bulunmalıdır.

Yuvarlama veya biçimlendirme yapılmasına gerek yoktur.

Örnek

3

b=5

Tam sayı bölümünün sonucu 3//5 = 0'dır.

Float bölümünün sonucu 3/5 = 0,6'dır.

Yazdır:

0

0,6

Giriş Formatı

İlk satırda ilk tam sayı olan a yer alıyor.

İkinci satırda ikinci tam sayı olan b yer alıyor.

Çıkış Formatı

Yukarıda anlatıldığı gibi iki satırı yazdırın.

Sample Input 0

4
3
Sample Output 0

1
1.33333333333
"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())
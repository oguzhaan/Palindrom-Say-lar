def PalindromeNumber():
    # Girilen sayı string şeklinde alındı ki bunun tersine ulaşabilelim
    num = input("Sayıyı giriniz: ")
    # Dizinin tersi alındı
    rev_num = num[::-1]
    if num == rev_num:
        return "Bu sayı bir palindrom sayıdır"
    else:
        return "Bu sayı palindrom bir sayı degildir"

print(PalindromeNumber())
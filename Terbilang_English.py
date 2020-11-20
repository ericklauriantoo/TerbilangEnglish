kata_satuan = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
kata_belasan = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
kata_puluhan = ["", "", "twenty", "thirty", "fourty", "fifty" , "sixty" , "seventy", "eighty", "ninety",]

def terbilang(n):
    if n < 10 :
        return kata_satuan[n]
    elif 10 <= n <= 19 :
        return kata_belasan[n-10]
    elif n >= 1000000000:
        return terbilang(n // 1000000000) + " billion " + terbilang(n % 1000000000)
    elif n >= 1000000 :
        return terbilang(n // 1000000) + " million " + terbilang(n % 1000000)
    elif n >= 1000 :
        return terbilang(n // 1000) + " thousand " + terbilang(n % 1000)
    elif n >= 100 :
        return terbilang(n // 100) + " hundred " + terbilang(n % 100)
    elif n >= 20 :
        return kata_puluhan[n // 10] + " " + terbilang(n % 10)


    else :
        if n == 10 :
            return "ten"
        elif n == 11 :
            return "eleven"
        else :
            return


# test
import os
while True:
    os.system('cls')
    try:
        n = int(input('angka ? '))
        print(f'{n:,} = {terbilang(n)}')
    except:
        print('data input anda tidak benar ...')
    os.system('pause')            

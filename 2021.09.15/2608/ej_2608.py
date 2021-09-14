import math


def arb_to_rom(arb):
    rom = ""
    for i in range(len(str(arb)), 0, -1):
        place = int(math.pow(10, i - 1))     # 자리수
        num = int(arb % place)               # 나머지
        temp = arb - num
        arb = num
        if arb_dict.get(temp):
            rom += arb_dict.get(temp)
        else:
            quot = int(temp / place)          # 몫
            if quot == 2 or quot == 3:
                rom += arb_dict.get(place) * quot
            elif quot == 6 or quot == 7 or quot == 8:
                rom += arb_dict.get((quot - 5) * place) \
                    + arb_dict.get(place) * (quot - 5)
    return rom


def rom_to_arb(text):
    num = rom_dict.get(text[0])
    for i in range(1, len(text)):
        num += rom_dict.get(text[i])
        if rom_dict.get(text[i - 1]) < rom_dict.get(text[i]):
            num -= (rom_dict.get(text[i - 1])) * 2
    return num


rom_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
            "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
arb_dict = {v: k for k, v in rom_dict.items()}
m, n = list(input()), list(input())
arb_mul = rom_to_arb(m) + rom_to_arb(n)
print(arb_mul)
print(arb_to_rom(arb_mul))

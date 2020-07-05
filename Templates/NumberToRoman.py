class RNum:
    def num__rom(self, num):
        value = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        symbol = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_number = ""
        i = 0
        while num > 0:
            for i1 in range(num // value[i]):
                num -= value[i]
                roman_number += symbol[i]
            i += 1
        return(roman_number)

number = input("Please input the number: ")

print(RNum().num__rom(int(number)))



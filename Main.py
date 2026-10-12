class RomanConverter:
    def __init__(self, num: int):
        self.num = num

    def to_roman(self) -> str:
        values = [ 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = [ "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        roman = ""
        temp = self.num
        
        for i in range(len(values)):
            while temp >= values[i]:
                roman += symbols[i]
                temp -= values[i]
                
        return roman
converter = RomanConverter(14)
print(converter.to_roman())  

class IntegerToRoman:
    def __init__(self,num):
        self.num=num
    def roman(self):
        romanvalue=["I","II","III","IV","V"]
        if not 1 <= self.num <= len(romanvalue):
            raise ValueError("num must be between 1 and 5")
        return romanvalue[self.num-1]

obj=IntegerToRoman(2)
print(obj.roman())
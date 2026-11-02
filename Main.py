class IntegerToRoman:
    def __init__(self,num):
        self.num=num
    def roman(self):
        romanvalue=["I","II","III","IV","V"]
        return romanvalue[self.num-1]

obj=IntegerToRoman(int(input("Enter a number:")))
print(obj.roman())
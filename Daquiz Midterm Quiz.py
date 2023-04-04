class TempConversion():
    def __init__(self, temp):
        self.__temp = temp
# F to C
    def fc(self):
        return (self.__temp - 32) * 5/9
# K to C
    def kc(self):
        return self.__temp - 273.15
# C to F
    def cf(self):
        return (self.__temp * 9/5) + 32
# K to F
    def kf(self):
        return (self.__temp * 1.8) - 459.67
# C to K
    def ck(self):
        return self.__temp + 273.15
# F to K
    def fk(self):
        return (self.__temp + 459.67) / 1.8
# input
temp = float(input("Enter Your Temperature: "))
# tempconversion
temp_obj = TempConversion(temp)
# outputs
print("Fah to Cel:", temp_obj.fc())
print("Kel to Cel:", temp_obj.kc())
print("Cel to Fah:", temp_obj.cf())
print("Kel to Fah:", temp_obj.kf())
print("Cel to Kel:", temp_obj.ck())
print("Fah to Kel:", temp_obj.fk())
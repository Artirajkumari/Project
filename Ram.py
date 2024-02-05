#Ploymorphism overriding = same method is in the both class but when
#child class  call the method than call own method.
    class Phone:
    def __init__(self,price,brand,camera):
        print('inside phone constructor')
        self.price= price
        self.brand= brand
        self.camera= camera
    def buy(self):
        print('Buying phone')
    def return_phone(self):
        print("Returning a phone")
class SmartPhone(Phone):
    def buy(self):
        print("Buying a SmartPhone")


s=SmartPhone(14000, "Redmii",16)
s.buy()





##################################################################CLASS PARRENT####################################################################################
class Parrent:
    def __init__(self.num):
        self.num=num

    def get_num(self):
        return self.__num
class Child(Parrent):
    def Show(self):
        print("this is in child class")

son=Child(100)
print(son.get_num())
son.show()


##############################################################Example 2#######################################################################################


lass Parrent:
    def __init__(self.num):
        self.num=num

    def get_num(self):
        return self.__num
    
class Child(Parrent):
    def __init__(self,val,num):
        self__val= val

    def get_val(self):
        return self.__val

son=Child(100,10)
print("Parrent Num",  son.get_() )
print(Child:Val", son.get_val())


##########################################################  Example 3 ###############################################################################################



class A:
    def__init__(self):
        self.var1=100

    def display1(self,var1):
        print("class A:", self.var)

class B:
    def display2(self,var1)

obj=B ()
obj.display(200)


############################################################### Example of super #####################################################################################

class Phone:
    def __init__(self,price,brand,camera):
        print('inside phone constructor')
        self.price= price
        self.brand= brand
        self.camera= camera
    def buy(self):
        print('Buying phone')
    def return_phone(self):
        print("Returning a phone")

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    def buy(self):
        print("Buying a SmartPhone")
        super()buy()

s=SmartPhone(20000,"one++",16)
s.buy()


s=SmartPhone(14000, "Redmii",16)
s.buy()

############################################################
        

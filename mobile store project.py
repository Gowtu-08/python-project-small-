

class Mobile:
    def __init__(self, brand, model, price, offer=None):
        self.brand=brand
        self.model=model
        self.price=price
        self.offer=offer
    
    def __start__(self):
        print(f"{self.brand} - {self.model} - {self.price} and offer is {self.offer}")


M1= Mobile("Apple", "i phone 14 pro max", "RS 1,50,000", "10% off")
M2= Mobile("Samsung", "Galaxy s24 ultra", "RS 1,20,000", "5% off")
M3= Mobile("Oneplus", "11R", "RS 50,000", "15% off")
M4= Mobile("Nokia", "G60", "RS 30,000", "20% off")
M5= Mobile("Redmi", "Note 12 pro", "RS 20,000", "30% off")
M6= Mobile("Nothing", "phone 1", "RS 30,000", "25% off")


Q= input("Enter the key of the mobile you want to buy: ".lower())
if Q == "apple":
    M1.__start__()
elif Q == "samsung":
    M2.__start__()
elif Q == "oneplus":
    M3.__start__()
elif Q == "nokia":
    M4.__start__()
elif Q == "redmi":
    M5.__start__()
elif Q == "nothing":
    M6.__start__()
else:
    print("Invalid key. Please enter a valid mobile brand.")

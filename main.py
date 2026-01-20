import json as js
import pandas as pd
class User:
    def __init__(self,name="",age=-1,pn=-1,cnic=-1,):
        self.name=name
        self.age=age
        self.phone_number=pn
        self.cnic=cnic
    def input(self):
        self.name=input("Enter your name = ")
        self.age=input("Enter your age = ")
        self.phone_number=input("Enter your phone number = ")
        self.cnic=input("Enter your CNIC = ")
    def show(self):
        print("Your Name = ",self.name)
        print("Your Age = ",self.age)
        print("Your Phone Number = ",self.phone_number)
        print("Your CNIC = ",self.cnic)

# Passenger Class

class Authentication(User):
    def __init__(self, name="", age=-1, pn=-1, cnic=-1,email="",password=""):
        super().__init__(name, age, pn, cnic)
        self.email=email
        self.password=password
    def sign_up(self):
        super().input()
        self.email=input("Enter your Email = ")
        self.password=input("Enter your password = ")
        try:
            with open(r"TMS\passengers.json","r") as file:
                data=js.load(file)
        except js.JSONDecodeError:
            with open(r"TMS\passengers.json","w") as file:
                js.dump([self.to_dict()],file,indent=4)
                print("\n")
                print("Account Created Successfully😊")
        except FileNotFoundError:
            with open(r"TMS\passengers.json","w") as file:
                js.dump([self.to_dict()],file,indent=4)
                print("\n")
                print("Account Created Successfully😊")
        else:
            data.append(self.to_dict())
            with open(r"TMS\passengers.json","w") as file:
                js.dump(data,file,indent=4)
                print("\n")
                print("Account Created Successfully😊")
            print("Account Created Successfully😊")

    @staticmethod
    def login():
        temp_email=input("Enter Your Email = ")
        temp_password=input("Enter Your Password = ")
        try:
            with open(r"TMS\passengers.json","r") as file:
                record=js.load(file)
        except js.JSONDecodeError:
            print("\n")
            print("Invalid User Credentials!")
        except FileNotFoundError:
            print("\n")
            print("Invalid User Credentials!")
        else:
            check=False
            for passenger in record:
                if passenger["Email"]==temp_email and passenger["Password"]==temp_password:
                    print("\n")
                    print("Login Successfull")
                    check=True
                    break
            if not check:
                print("\n")
                print("Invalid User Credentials!")

    def to_dict(self):
        return {
            "Name":self.name,
            "Age":self.age,
            "Phone Number":self.phone_number,
            "Cnic":self.cnic,
            "Email":self.email,
            "Password":self.password
        }



def main():
    u1=Authentication()
    choice=int(input("1.Login\n2.Sign Up\n"))
    if choice==1:
        Authentication.login()
    else:
        u1.sign_up()

if __name__=="__main__":
    main()
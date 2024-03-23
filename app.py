import csv

def get_user_info():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
   # if age <=20:
      #  age1=print(age)
   # else:
   #     print("no")
   # if age>20 and age<=35 :
    #    age2=print(age)
    #else:
     #3   print("no")
    #if age>35 and age<=60 :
      #  age3=print(age)
    #else:
       # print("no")
    #if age>60:
        #age4=print(age)
   # else :
      #  print("no")
    Senior = input("Are Senior Sitizion :")
    if Senior == 'yes':
        print("yes")
        age2=print("no")
        age3=print("no")
    else:
        age2= input("are you Early Ager:")
        if age == 'yes':
            print("yes")
            age3=print("no")
        else:
            age3 = input ("are you Teenager:")
            print("yes")
    dep=input("are you Disable:" )
    gen = input("Enter your Gender (Male/Femal):")

    internet = input("Is there Internet is available or not : ")

    a=input("Are you Happy With Owr services : ")

    b=input("you want to Coninue With us or not : ")

    c=input("How much ratting you give us out of 5 : ")

    d=input("Tenure of Your recharg : ")
    
    e = input("Enter monthly Charges : ")

    f = input("Yearly Charges : ")

    g = input("Any Churn : ")

    return name , age ,Senior ,age2 ,age3 ,dep ,gen, internet , a , b ,c , d, e ,g

def write_to_csv(filename, user_info):
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(user_info)
    print("User information has been saved successfully.")

def main():
    filename = "user_information.csv"
    try:
        with open(filename, 'r') as f:
            pass
    except FileNotFoundError:
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'age','Senior','Early Teanager', 'TeenAge' , 'Disability' , 'Gender' , 'Internet' , 'Are you Happy with our services :', 'you want to Coninue With us','How much ratting you give us out of 5','Tenure of Your recharg','Enter monthly Charges','Yearly Charges','Any Churn' ])
    
    while True:
        choice = input("Do you want to add user information? (yes/no): ").lower()
        if choice == 'yes':
            user_info = get_user_info()
            write_to_csv(filename, user_info)
        elif choice == 'no':
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()

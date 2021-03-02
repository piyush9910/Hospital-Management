import random
import csv
import datetime
import pandas as pd
list1 = []
list2 = []
name = input("Enter Visitor's name: ")
phone = int(input("Enter phone number: "))


def patientinfo():
    with open('Patient.csv', 'a+') as patient:
        data1 = csv.writer(patient)
        cust_no = int(input("Enter customer ID: "))
        mob = int(input("Enter mobile number: "))
        addrs = input("Enter address: ")
        email = input("Enter email address: ")
        patient = [name, phone, cust_no, mob, addrs, email]
        data1.writerow(patient)


def patientadm():
    print("*************************")
    print("| 1. Admit Patient       |")
    print("| 2. Discharge Patient   |")
    print("| 3. EXIT                |")
    print("*************************")
    choicee=int(input("Enter Your Choice : "))
    if choicee==1:
        list2 = []
        pname = input("Enter Patient's Name : ")
        page = int(input("Age : "))
        pprob = input("Problem/ Disease : ")
        print(" Enter Admission Data  ")
        d = int(input("Date : "))
        m = int(input("Month: "))
        y = int(input("Year : "))
        admdate = datetime.date(y, m, d)
        ndays = int(input("No of Days : "))
        with open('Rooms.csv', 'r')as file:
            data = csv.reader(file)
            print("Avaialble Rooms\n")
            for i in data:
                print(i[0], i[1], i[2])
            ch = int(input("Enter Your Option: "))
            if ch == 1:
                p = 500 * ndays
                list2.append(p)
            elif ch == 2:
                p = 1500 * ndays
                list2.append(p)
            elif ch == 3:
                p = 2000 * ndays
                list2.append(p)
            else:
                print("INVALID !!!")

        with open('doctors.csv', 'r') as csv_file:
            read = csv.reader(csv_file)
            print("Avaiable Doctors\n")
            print('S.no\tName \t\tSpeciality\t\tFees')
            for i in read:
                print(i[0], i[1], i[2], i[3])
            nn = int(input("Enter Your Choice: "))
            ch = input("Do you want to continue : (y/n)")
            if ch == 'y' or ch == 'Y':
                if nn == 1:
                    price = 1000 * ndays
                    list2.append(price)

                elif nn == 2:
                    price = 1500 * ndays
                    list2.append(price)

                elif nn == 3:
                    price = 500 * ndays
                    list2.append(price)

                elif nn == 4:
                    price = 500 * ndays
                    list2.append(price)

                elif nn == 5:
                    price = 1000 * ndays
                    list2.append(price)

                else:
                    print("INVALID ENTRY")
        services = int(input("Service Charge: "))
        list2.append(services)
        surgery = int(input("Surgery Fee (If Available else input 0): "))
        list2.append(surgery)
        vaccine = int(input("Vaccine Fee (If Availalble else input 0): "))
        list2.append(vaccine)
        amount = sum(list2)
        print(amount)
        print("\t" * 10 + "Total Bill\n")
        print("*" * 80)
        print()
        e = datetime.datetime.now()
        print("Date :                       ", e.strftime("%Y-%m-%d %H:%M:%S"))
        print()
        print("Patient Name :               ", pname)
        print("PhoneNo :                    ", phone)
        print("Age     :                    ", page)
        print("Disease  :                    ", pprob)
        tax=0.18*amount
        total=tax+amount
        pati = [pname, page, pprob, d, m, y, admdate, ndays, p, price, services, surgery, vaccine, amount, tax, total]
        with open("Patientadm.csv", "a") as pat:
            d = csv.writer(pat)
            d.writerow(pati)
            print("Record successfully added to database")
            menu()
    elif choicee==2:
        bill2()
    else:
        exit()

def patientdis():
    lines = list()
    members = input("Please enter a Patient's name to be deleted: ")
    with open('Patientadm.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == members:
                    lines.remove(row)
    with open('Patientadm.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
        print("Patient Succesfully Deleted...")
    a=("Main Menu : (y/n): ")
    if a=='y' or a=='Y':
        menu()

def showpatiens():
    df = pd.read_csv('Patientadm.csv')
    print(df)

def bill2():
    lines = list()
    members = input("Please enter a Patient's name View Bill: ")
    print()
    print("*******************************")
    print("| 1. Want to See Only Bill:    |")
    print("| 2. Bill + Discahrge          |")
    print("*******************************")
    print()
    a=int(input("Enter your Choice : "))
    if a==1:
        with open('Patientadm.csv', 'r')as fileZ:
            read = csv.reader(fileZ)
            for i in read:
                if i:
                    if i[0] == members:
                        print("\n\t\t\t\tBill of Patient ")
                        print(
                            "\nName, Agr, Problem, Date, Month, Year, AdmDate,     No of Days, Room Fee, Doctor Fee, Services , Surgery, Vaccine, Amount , Tax,    Tot")
                        print("\n", i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12],
                              i[13], i[14], i[15])
                        print("\t" * 10 + "Total Bill\n")
                        print("*" * 80)
                        print()
                        e = datetime.datetime.now()
                        print("Date :                       ", e.strftime("%Y-%m-%d %H:%M:%S"))
                        print()
                        print("Patient Name :                   ", i[0])
                        print("Age     :                    ", i[1])
                        print("Disease  :                    ", i[2])

                        print("*" * 80)
                        print("Doctor Fee :                               ", i[9], 'for', i[7], "days", "=",
                              int(i[9]) * int(i[7]))
                        print("Room Fee :                             ", i[8], 'for', i[7], "days", "=",
                              int(i[8]) * int(i[7]))
                        print("Service Fee :                            ", i[10])
                        print("Surgery Fee :                             ", i[11])
                        print("Vaccine Fee :                                ", i[12])
                        tax = 0.018 * int(i[13])
                        total = int(i[13])
                        print("Amount Before Tax :                        ", i[13])
                        print("Add Taxes as per Government Regulations 18%     ", tax)
                        print("Total Billing Amount :                          ", total + tax)
                        print("*" * 80)
                        print("1. Main Menu")
                        print("2. Discharge Patient")
                        b=int(input("Choice : "))
                        if a==1:
                            menu()
                        elif a==2:
                            patientdis()
    elif a==2:
        patientdis()
    menu()


def regular():
    with open('doctors.csv', 'r') as csv_file:
        read = csv.reader(csv_file)
        print('S.no\tName \t\tSpeciality\t\tFees')
        for i in read:
            print(i[0], i[1], i[2], i[3])
        nn = int(input("Enter Your Choice"))
        ch = input("Do you want to make an appointment : (y/n)")
        if ch == 'y' or ch == 'Y':
            if nn == 1:
                price = 1000
                list1.append(price)

            elif nn == 2:
                price = 1500
                list1.append(price)

            elif nn == 3:
                price = 500
                list1.append(price)

            elif nn == 4:
                price = 500
                list1.append(price)

            elif nn == 5:
                price = 1000
                list1.append(price)

            else:
                print("INVALID ENTRY")
        c = input("Do you want to continue for more info or any other Problem : (Y/N)")
        if c == 'y' or ch == 'Y':
            menu()
        else:
            bill1(name, phone)
            menu()


def bill1(name, phone):
    print("\t" * 10 + "Total Bill\n")
    print("*" * 80)
    print()
    e = datetime.datetime.now()
    print("Date :                       ", e.strftime("%Y-%m-%d %H:%M:%S"))
    print()
    print("Customer Name :              ", name)
    print("PhoneNo :                    ", phone)
    print("*" * 80)
    s = sum(list1)
    print("Basic Amount :                               ", s)
    tax = (18 / 100) * s
    print("Add Taxes as per Government Regulations 18% ", tax)
    print("Total Billing Amount :                       ", s.__round__() + tax)
    print("*" * 80)


def menu():
    print("*"*84)
    print("|\t\t\tWelcome to the Rijul Super Speciality Hospital                        |")
    print("|\t\t\t\t Majlis Park, Adarsh Nagar                                          |")
    print("|\t\t\t\t\t\t\t\t\t\t    Phone No: 9874859674/ 7485967485                    |")
    print("*" * 84)
    print("1. Regular Appointment ")
    print("2. Admit Patient/Discharge patient")
    print("3. Show All Patients")
    n = int(input("Choice : "))
    if n == 1:
        patientinfo()
        regular()
    elif n == 2:
        patientadm()
    elif n==3:
        showpatiens()

menu()
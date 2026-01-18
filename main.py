#MAIN MODULE

import Doctor
import Patient
import lab_admin
import mysql.connector as mysq

con = mysq.connect(host='localhost', user='root', password='user123', database='blood_trial')

if con.is_connected():
    print('Connected successfully')
    cur = con.cursor()
    
    while True:
        ch = int(input('''Enter your status:
        1. Doctor
        2. Patient
        3. Lab Administration/ Lab Assistant
        :'''))

        if ch == 1:
            Doctor.DOCTOR()
        elif ch == 2:
            Patient.Patient()
        elif ch == 3:
            lab_admin.LabAdmin()
        else:
            yn = input("Invalid choice. Do you wish to continue? (Y/N): ")
            if yn in 'Yy':
                pass
            else:
                break

    print("The entire program has been terminated")


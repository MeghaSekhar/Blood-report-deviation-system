#LAB ADMINISTRATION MODULE

def lab_admin():
    import mysql.connector as mysq

    con = mysq.connect(host='localhost', user='root', password='user123', database='blood_trial')
    if con.is_connected():
        print('Connected succesfully')

    cur = con.cursor()

    p = input('Enter server password: ')
    if p == "rose87er":
        while True:
            choice = int(input('''Enter your choice:
1. View patient details
2. View patient report
3. Update patient details
4. Update patient report
5. Enter new report
Enter any other number to exit
.'''))

            if choice == 1:
                q1 = int(input('''Enter your choice;
1. View details of all patients
2. View details of selected patients'''))

                if q1 == 1:
                    cur.execute('select * from la;')
                    de = cur.fetchall()
                    for i in de:
                        print("Slno:", i[0], "Patient id:", i[1], "Birth date:", i[2], "Name:", i[3], "Age:", i[4],
                              "Gender:", i[5], "Blood type:", i[6], "Doctor id:", i[7], "Phone number:", i[8],
                              "Address:", i[9], "Test:", i[10], "Test fee:", i[11], sep="\n")

                elif q1 == 2:
                    y = int(input("Enter patient id:"))
                    cur.execute('select * from la where Patient_id=%s' % (y))
                    vu = cur.fetchall()
                    for i in vu:
                        print("Slno:", i[0], "Patient id:", i[1], "Birth date:", i[2], "Name:", i[3], "Age:", i[4],
                              "Gender:", i[5], "Blood type:", i[6], "Doctor id:", i[7], "Phone number:", i[8],
                              "Address:", i[9], "Test:", i[10], "Test fee:", i[11], sep="\n")

            elif choice == 2:
                q2 = int(input('''Enter your choice;
1. View reports of all patients
2. View reports of selected patients'''))

                if q2 == 1:
                    cur.execute('select * from bl;')
                    fe = cur.fetchall()
                    for i in fe:
                        print(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11])

                elif q2 == 2:
                    z = int(input("Enter patient id:"))
                    cur.execute('select * from bl where pid=%s' % (z))
                    fe = cur.fetchall()
                    for i in fe:
                        print(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11])

            elif choice == 3:
                pid = int(input("Enter patient id:"))
                up = int(input('''Choose parameter to be changed:
1. Patient id
2. Birth date
3. Name
4. Age
5. Gender
6. Blood type
7. Doctor id
8. Phone number
9. Address
10. Test Fee
'''))

                if up == 1:
                    l = int(input("Enter new patient id:"))
                    cur.execute('update la set patient_id=%s where patient_id=%s' % (l, pid))

                elif up == 2:
                    l = input("Enter new birth date:")
                    cur.execute('update la set bdate=%s where patient_id=%s' % (l, pid))

                elif up == 3:
                    l = input("Enter new name:")
                    cur.execute('update la set name=%s where patient_id=%s' % (l, pid))

                elif up == 4:
                    l = int(input("Enter new age:"))
                    cur.execute('update la set age=%s where patient_id=%s' % (l, pid))

                elif up == 5:
                    l = input("Enter new gender:")
                    cur.execute('update la set gender=%s where patient_id=%s' % (l, pid))

                elif up == 6:
                    l = input("Enter new blood type:")
                    cur.execute('update la set blood_type=%s where patient_id=%s' % (l, pid))

                elif up == 7:
                    l = int(input("Enter new Doctor id:"))
                    cur.execute('update la set doctor_id=%s where patient_id=%s' % (l, pid))

                elif up == 8:
                    l = int(input("Enter new phone number:"))
                    cur.execute('update la set phone_no=%s where patient_id=%s' % (l, pid))

                elif up == 9:
                    l = input("Enter new address:")
                    cur.execute('update la set address=%s where patient_id=%s' % (l, pid))

                elif up == 10:
                    l = input("Enter new test fee:")
                    cur.execute('update la set test_fee=%s where patient_id=%s' % (l, pid))

            elif choice == 4:
                pd = int(input("Enter patient id"))
                a = int(input('''Enter the parameter to be changed:
1. Haemoglobin
2. WBC
3. RBC
4. Glucose
5. Urea
6. Creatinin
7. Iron
8. Protein
9. Albumin
10. Triglyceride
11. Platelet
'''))

                if a == 1:
                    s = int(input("New value for haemoglobin: "))
                    cur.execute('update bl set haemoglobin=%s where pid=%s' % (s, pd))
                    print("The record has been updated! Thankyou!")

                elif a == 2:
                    s = int(input("New value for WBC: "))
                    cur.execute('update bl set WBC=%s where pid=%s' % (s, pd))
                    print("The record has been updated! Thankyou!")

                elif a == 3:
                    s = int(input("New value for RBC: "))
                    cur.execute('update bl set RBC=%s where pid=%s' % (s, pd))
                    print("The record has been updated! Thankyou!")

                elif a == 4:
                    s = int(input("New value for Glucose: "))
                    cur.execute('update bl set Glucose=%s where pid=%s' % (s, pd))
                    print("The record has been updated! Thankyou!")

                elif a == 5:
                    s = int(input("New value for Urea: "))
                    cur.execute('update bl set urea=%s where pid=%s' % (s, pd))
                    print("The record has been updated! Thankyou!")

                elif a == 6:
                    s = int(input("New value for Creatinin: "))
                    cur.execute('update bl set creatinin=%s where pid=%s' % (s, pd))
                    print("The record has been updated! Thankyou!")

                elif a == 7:
                    s = int(input("New value for Iron: "))
                    cur.execute('update bl set iron=%s where pid=%s' % (s, pd))
                    print("The record has been updated! Thankyou!")

                elif a == 8:
                    s = int(input("New value for Protein: "))
                    cur.execute('update bl set Protein=%s where pid=%s' % (s, pd))
                    print("The record has been updated! Thankyou!")

                elif a == 9:
                    s = int(input("New value for Albumin: "))
                    cur.execute('update bl set albumin=%s where pid=%s' % (s, pd))
                    print("The record has been added! Thankyou!")

                elif a == 10:
                    s = int(input("New value for Triglyceride: "))
                    cur.execute('update bl set triglyceride=%s where pid=%s' % (s, pd))
                    print("The record has been updated! Thankyou!")

                elif a == 11:
                    s = int(input("New value for Platelet: "))
                    cur.execute('update bl set Platelet=%s where pid=%s' % (s, pd))
                    print("The record has been updated! Thankyou!")

            elif choice == 5:
                while True:
                    ch1 = int(input('''Enter your choice
1. Enter details of patient
2. Enter blood report
'''))

                    if ch1 == 1:
                        pid = int(input("Enter new patient id"))
                        bd = eval(input("Enter date of birth:"))
                        name = input("Enter the name:")
                        age = int(input("Enter the age"))
                        gn = input("Enter the gender(M/F):")
                        blt = input("Enter blood type:")
                        did = int(input("Enter doctor id:"))
                        phn = int(input("Enter phone number:"))
                        add = input("Enter the address")
                        tstf = int(input("Enter the test fee"))

                        cur.execute(
                            'insert into la values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                            % (pid, bd, name, age, gn, blt, did, phn, add, tstf)
                        )
                        print('The records have been added! Thankyou!')

                    elif ch1 == 2:
                        pid = int(input("Enter new patient id:"))
                        hb = int(input("Enter new haemoglobin value:"))
                        wbc = int(input("Enter new wbc value:"))
                        rbc = int(input("Enter new rbc value:"))
                        gl = int(input("Enter new glucose value:"))
                        ur = int(input("Enter new urea value:"))
                        cr = int(input("Enter new creatinin value:"))
                        ir = int(input("Enter new iron value:"))
                        pr = int(input("Enter new protein value:"))
                        al = int(input("Enter new albumin value:"))
                        tr = int(input("Enter new triglyceride value:"))
                        pl = int(input("Enter new platelet value:"))

                        cur.execute(
                            'insert into la values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                            % (pid, hb, wbc, rbc, gl, ur, cr, ir, pr, al, tr, pl)
                        )
                        print("The records have been added! Thankyou!")

                    else:
                        break
            else:
                break

        print("Lab Admin's Program has been terminated. Redirecting to main program")
        con.close()

    
        
        
        

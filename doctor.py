#DOCTOR MODULE

def Doctor():
    import mysql.connector as mysq

    con = mysq.connect(
        host='localhost',
        user='root',
        password='user123',
        database='blood_trial'
    )

    if con.is_connected():
        print('Connected successfully')
        cur = con.cursor()

        dic = {67: 201, 112: 202, 114: 203, 166: 204, 167: 205, 187: 206, 201: 207}
        f = 0

        while True:
            if f == 1:
                break

            p = input('Enter server password: ')
            if p != "lavn34er":
                print('You have entered the wrong password')
                chh = input("Do you wish to try again? Y/N: ")
                if chh in ['N', 'n']:
                    break
            else:
                did = int(input("Enter Doctor ID: "))
                pas = int(input("Enter your password: "))

                if pas == dic.get(did, None):
                    cur.execute("SELECT Patient_ID FROM la WHERE Doctor_ID=%s", (did,))
                    a = cur.fetchall()

                    print('Your patients are:')
                    for i in a:
                        print(i[0])

                    while True:
                        ch = int(input('''Enter your choice:
                        1. View reports of all patients
                        2. View reports of selected patients
                        3. Exit program
                        :'''))

                        if ch == 3:
                            break

                        if ch == 1:
                            while True:
                                ch1 = int(input('''Choose the parameter you wish to view:
                                0. All parameters
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
                                (Enter any other number to exit)
                                :'''))

                                if ch1 == 0:
                                    cur.execute('''SELECT Patient_ID, Haemoglobin, WBC, RBC, Glucose, Urea, Creatinin, Iron, Protein, Albumin, Triglyceride, Platelet 
                                        FROM bl b, la a 
                                        WHERE Doctor_ID=%s AND b.pid=a.patient_id''', (did,))
                                    f = cur.fetchall()
                                    
                                    for i in f:
                                        if i[1] > 20:
                                            hb = 'Extremely High'
                                        elif i[1] > 15:
                                            hb = 'High'
                                        elif i[1] < 8:
                                            hb = 'Low'
                                        else:
                                            hb = 'Normal'

                                        print(f'{i[0]}\nHaemoglobin: {i[1]} - {hb}')
                                        # Similar checks for other parameters

                                elif ch1 == 1:
                                    cur.execute('''SELECT Patient_ID, Haemoglobin FROM bl b, la a 
                                                WHERE Doctor_ID=%s AND a.patient_id=b.pid''', (did,))
                                    f = cur.fetchall()
                                    for i in f:
                                        pass  # Similar logic for Haemoglobin

                                elif ch1 == 2:
                                    # Similar structure for WBC
                                    pass

                                # And so on for other parameters...

                                else:
                                    f = 1
                                    break

                        elif ch == 2:
                            pid = int(input("Enter patient ID: "))
                            while True:
                                ch2 = int(input('Choose the parameter you wish to view:
                                    0. All parameters
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
                                    (Enter any other number to exit)
                                    :'))

                                if ch2 == 0:
                                    cur.execute('''SELECT Patient_ID, Haemoglobin, WBC, RBC, Glucose, Urea, Creatinin, Iron, Protein, Albumin, Triglyceride, Platelet 
                                        FROM bl b, la a 
                                        WHERE Doctor_ID=%s AND a.patient_id=b.pid''', (did, pid))
                                    f = cur.fetchall()

                                    for i in f:
                                        # For each parameter, determine the status
                                        # For example, Haemoglobin
                                        if i[1] > 20:
                                            hb = 'Extremely High'
                                        elif i[1] > 15:
                                            hb = 'High'
                                        elif i[1] < 8:
                                            hb = 'Low'
                                        else:
                                            hb = 'Normal'

                                        # Print the patient ID and Haemoglobin status
                                        print(f'Patient ID: {i[0]}\nHaemoglobin: {i[1]} - {hb}')
                                        # Repeat similar logic for other parameters like WBC, RBC, etc.

                                elif ch2 == 1:
                                    cur.execute('''SELECT Patient_ID, Haemoglobin FROM bl b, la a 
                                                WHERE Doctor_ID=%s AND a.patient_id=b.pid''', (did, pid))
                                    f = cur.fetchall()
                                    for i in f:
                                        pass  # Similar logic for Haemoglobin

                                elif ch2 == 2:
                                    # Similar structure for WBC
                                    pass

                                # And so on for other parameters...

                                else:
                                    f = 1
                                    break

                            print('Doctor Program terminated. Moving on to the main program.')


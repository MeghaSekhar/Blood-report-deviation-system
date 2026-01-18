#PATIENT MODULE

def Patient():
    import mysql.connector as mysq

    con = mysq.connect(
        host='localhost',
        user='root',
        password='user123',
        database='Blood_Trial'
    )

    if con.is_connected():
        print('Connected successfully')
        cur = con.cursor()

        dic = {
            10001: 301, 10002: 302, 10003: 303, 10004: 304, 10005: 305, 10006: 306, 10007: 307, 10008: 308, 10009: 309, 10010: 310
        }

        pid = int(input("Enter your patient id: "))
        pasw = int(input("Enter your password: "))

        if pasw == dic.get(pid):
            while True:
                ch = int(input('''Enter your choice:
                1. View your blood report
                2. View abnormal quantities
                3. Exit program
                :'''))

                if ch == 3:
                    break

                elif ch == 1:
                    while True:
                        cur.execute('SELECT * FROM bl WHERE pid=%s', (pid,))
                        f = cur.fetchall()

                        for i in f:
                            hb = 'Normal'
                            if i[1] > 20:
                                hb = 'Extremely High'
                            elif i[1] > 15:
                                hb = 'High'
                            elif i[1] < 8:
                                hb = 'Low'

                            wbc = 'Normal'
                            if i[2] > 18:
                                wbc = 'Extremely High! In need of immediate attention!!'
                            elif i[2] > 12:
                                wbc = 'High'
                            elif i[2] < 4:
                                wbc = 'Low'

                            rbc = 'Normal'
                            if i[3] > 14:
                                rbc = 'Extremely High'
                            elif i[3] > 10:
                                rbc = 'High'
                            elif i[3] < 5:
                                rbc = 'Low'

                            gl = 'Normal'
                            if i[4] > 5:
                                gl = 'Extremely High'
                            elif i[4] > 3.6:
                                gl = 'High'
                            elif i[4] < 2.8:
                                gl = 'Low'

                            ure = 'Normal'
                            if i[5] > 10:
                                ure = 'Extremely High'
                            elif i[5] > 7.3:
                                ure = 'High'
                            elif i[5] < 3.4:
                                ure = 'Low'

                            cr = 'Normal'
                            if i[6] > 200:
                                cr = 'Extremely High'
                            elif i[6] > 165:
                                cr = 'High'
                            elif i[6] < 44:
                                cr = 'Low'

                            ir = 'Normal'
                            if i[7] > 60:
                                ir = 'Extremely High'
                            elif i[7] > 41:
                                ir = 'High'
                            elif i[7] < 21:
                                ir = 'Low'

                            pro = 'Normal'
                            if i[8] > 95:
                                pro = 'Extremely High'
                            elif i[8] > 81:
                                pro = 'High'
                            elif i[8] < 61:
                                pro = 'Low'

                            alb = 'Normal'
                            if i[9] > 50:
                                alb = 'Extremely High'
                            elif i[9] > 39:
                                alb = 'High'
                            elif i[9] < 27:
                                alb = 'Low'

                            tri = 'Normal'
                            if i[10] > 40:
                                tri = 'Extremely High! Needs immediate attention!!'
                            elif i[10] > 20:
                                tri = 'High'
                            elif i[10] < 0:
                                tri = 'Low'

                            plat = 'Normal'
                            if i[11] > 1000:
                                plat = 'Extremely High'
                            elif i[11] > 800:
                                plat = 'High'
                            elif i[11] < 100:
                                plat = 'Low'

            # Print the patient report
            print(f"Patient ID: {i[0]}")
            print(f"Haemoglobin: {i[1]} || {hb}")
            print(f"WBC: {i[2]} || {wbc}")
            print(f"RBC: {i[3]} || {rbc}")
            print(f"Glucose: {i[4]} || {gl}")
            print(f"Urea: {i[5]} || {ure}")
            print(f"Creatinin: {i[6]} || {cr}")
            print(f"Iron: {i[7]} || {ir}")
            print(f"Protein: {i[8]} || {pro}")
            print(f"Albumin: {i[9]} || {alb}")
            print(f"Triglyceride: {i[10]} || {tri}")
            print(f"Platelet: {i[11]} || {plat}")

        elif ch==2:
            for i in f:
                if i[1] > 20:
                    print(f"Haemoglobin: Extremely High ({i[1]}) - Normal range: 8-15 g/dl")
                elif i[1] > 15:
                    print(f"Haemoglobin: High ({i[1]}) - Normal range: 8-15 g/dl")
                elif i[1] < 8:
                    print(f"Haemoglobin: Low ({i[1]}) - Normal range: 8-15 g/dl")
        
                if i[2] > 18:
                    print(f"WBC: Extremely High ({i[2]}) - Normal range: 4-12 10^9/l")
                elif i[2] > 12:
                    print(f"WBC: High ({i[2]}) - Normal range: 4-12 10^9/l")
                elif i[2] < 4:
                    print(f"WBC: Low ({i[2]}) - Normal range: 4-12 10^9/l")
        
                if i[3] > 14:
                    print(f"RBC: Extremely High ({i[3]}) - Normal range: 4-12 10^9/l")
                elif i[3] > 10:
                    print(f"RBC: High ({i[3]}) - Normal range: 4-12 10^9/l")
                elif i[3] < 5:
                    print(f"RBC: Low ({i[3]}) - Normal range: 4-12 10^9/l")
        
                if i[4] > 5:
                    print(f"Glucose: Extremely High ({i[4]}) - Normal range: 2.8-3.6 mmol/l")
                elif i[4] > 3.6:
                    print(f"Glucose: High ({i[4]}) - Normal range: 2.8-3.6 mmol/l")
                elif i[4] < 2.8:
                    print(f"Glucose: Low ({i[4]}) - Normal range: 2.8-3.6 mmol/l")
        
                if i[5] > 10:
                    print(f"Urea: Extremely High ({i[5]}) - Normal range: 3.4-7.3 mmol/l")
                elif i[5] > 7.3:
                    print(f"Urea: High ({i[5]}) - Normal range: 3.4-7.3 mmol/l")
                elif i[5] < 3.4:
                    print(f"Urea: Low ({i[5]}) - Normal range: 3.4-7.3 mmol/l")
        
                if i[6] > 200:
                    print(f"Creatinin: Extremely High ({i[6]}) - Normal range: 44-165 umol/l")
                elif i[6] > 165:
                    print(f"Creatinin: High ({i[6]}) - Normal range: 44-165 umol/l")
                elif i[6] < 44:
                    print(f"Creatinin: Low ({i[6]}) - Normal range: 44-165 umol/l")
        
                if i[7] > 60:
                    print(f"Iron: Extremely High ({i[7]}) - Normal range: 21-41 umol/l")
                elif i[7] > 41:
                    print(f"Iron: High ({i[7]}) - Normal range: 21-41 umol/l")
                elif i[7] < 21:
                    print(f"Iron: Low ({i[7]}) - Normal range: 21-41 umol/l")
        
                if i[8] > 95:
                    print(f"Protein: Extremely High ({i[8]}) - Normal range: 61-81 g/l")
                elif i[8] > 81:
                    print(f"Protein: High ({i[8]}) - Normal range: 61-81 g/l")
                elif i[8] < 61:
                    print(f"Protein: Low ({i[8]}) - Normal range: 61-81 g/l")
        
                if i[9] > 50:
                    print(f"Albumin: Extremely High ({i[9]}) - Normal range: 27-39 g/l")
                elif i[9] > 39:
                    print(f"Albumin: High ({i[9]}) - Normal range: 27-39 g/l")
                elif i[9] < 27:
                    print(f"Albumin: Low ({i[9]}) - Normal range: 27-39 g/l")
        
                tri = 'Normal'
                if i[10] > 40:
                    print(f"Triglyceride: Extremely High ({i[10]}) - Normal range: 0-20 mmol/l")
                elif i[10] > 20:
                    print(f"Triglyceride: High ({i[10]}) - Normal range: 0-20 mmol/l")
                elif i[10] < 0:
                    print(f"Triglyceride: Low ({i[10]}) - Normal range: 0-20 mmol/l")
        
                plat = 'Normal'
                if i[11] > 1000:
                    print(f"Platelet: Extremely High ({i[11]}) - Normal range: 100-800 10^9/l")
                elif i[11] > 800:
                    print(f"Platelet: High ({i[11]}) - Normal range: 100-800 10^9/l")
                elif i[11] < 100:
                    print(f"Platelet: Low ({i[11]}) - Normal range: 100-800 10^9/l")
        
        
        else:
            print("Invalid Choice")
        
        print("Patient program has been terminated. Moving on to the main program.")
    
    else:
      print("Wrong password entered. Program is being terminated! Moving on to the main program.")
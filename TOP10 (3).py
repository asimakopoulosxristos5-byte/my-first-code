# -*- coding: utf-8 -*-
import random
import time
import os
import tkinter as tk  
from tkinter import messagebox
import webbrowser


def show_learning_resources():
    # Στην Python 3 η print θέλει παρενθέσεις
    print("\n=== Εκπαιδευτικοί Σύνδεσμοι ===")
    print("1. Python Tutorial (W3Schools)")
    print("2. HTML Tutorial (W3Schools)")
    print("3. Python Documentation (Επίσημο)")
    print("4. Ελληνικό Βοήθημα Προγραμματισμού (ΑΕΠΠ)")
    print("5. Python Tutor")
    print("6. Codecademy")
    print("7. Ψηφιακά Βιβλία ΕΠΑΛ")
    
    # Στην Python 3 η raw_input έγινε σκέτο input
    choice = input("Επίλεξε πηγή (ή 0 για επιστροφή): ")
    
    links = {
        "1": "https://www.w3schools.com/python/",
        "2": "https://www.w3schools.com/html/",
        "3": "https://docs.python.org/3/", # Άλλαξα το link στην Python 3
        "4": "https://alkisg.mysch.gr/",
        "5": "https://pythontutor.com/",
        "6": "https://www.codecademy.com/catalog/language/html/",
        "7": "https://e-books.ebooks.edu.gr/"
    }
    
    if choice in links:
        webbrowser.open(links[choice])
        print(">> Η σελίδα ανοίγει...")
    elif choice == "0":
        return
    else:
        print("Μη έγκυρη επιλογή.")

# ==============================
# GUI Παράθυρο Καλωσορίσματος
# ==============================

def launch_gui():
    root = tk.Tk()
    root.title("Efarmogi Mathiton EPAL")
    root.geometry("400x250") 

    root.configure(bg="#f0f0f0")
    
    label = tk.Label(root, text="Diaxeirisi Mathiton & Exetaseon", 
                     font=("Helvetica", 14, "bold"), bg="#f0f0f0", pady=20)
    label.pack()

    info = tk.Label(root, text="Patiste to koumpi gia na ksekinisete\nto programma stin konsola.", 
                    bg="#f0f0f0")
    info.pack(pady=10)

    def start_now():
        messagebox.showinfo("Etoimoi!", "To programma tha ksekinisei stin konsola.")
        root.destroy()
    # Κουμπί εκκίνησης
    btn = tk.Button(root, text="Ekkinnisi Programmatos", command=start_now, 
                    bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"), 
                    padx=20, pady=10)
    btn.pack(pady=20)

    root.mainloop()

# ==============================
# Ερωτήσεις ανά ενότητα
# ==============================
# Λίστα ερωτήσεων Python
python_questions = [
    ["Ti ektypwnei i entolh print('Hello World');", "Hello World", "H print() emfanizei keimeno stin othoni."],
    ["Poio einai to symbolo sxoliou stin Python;", "#", "To # xrisimopoieitai gia sxolia."],
    ["Poia entolh xrhsimopoieitai gia dhmiourgia listas;", "[]", "Oi agkyles [] einai ο typos gia tis listes."],
    ["Pos dilwnoume sunarthsh;", "def", "H lexi 'def' proerxetai apo to 'define'."],
    ["Poia entolh xrhsimopoieitai gia ektypwsh;", "print()", "H print() einai i vasiki entoli eksodou."],
    ["Ti epistrefei i len([1,2,3]);", "3", "H synartisi len() metraei τα stoixeia."],
    ["Poio einai to apotelesma: 2 + 3 * 2;", "8", "Proigeitai o pollaplaciasmos."],
    ["Pos dhmiourgoume keno le3iko;", "{}", "Ta agkistra {} xrisimopoiountai gia lexika."],
    ["Pos ksekinai ena if statement;", "if", "To 'if' elegxei mia synthiki."],
    ["Pos dilwnoume while loop;", "while", "To 'while' epanalambanei ton kwdika."], # <-- Προστέθηκε κόμμα εδώ
    ["Ti kanei h methodos append();", "Prosthetei stoixeio", "H append() bazei stoixeio sto telos."],
    ["Poia einai h domh dedomenwn LIFO;", "Stoiva", "H Stoiva (Stack) akolouthei tin arxi Last-In-First-Out."],
    ["Poia einai h domh dedomenwn FIFO;", "Oura", "H Oura (Queue) akolouthei tin arxi First-In-First-Out."],
    ["Ti epistrefei h float('10.5');", "10.5", "Metatrepei string se dekadiko arithmo."],
    ["Me poia entolh eisagoume vivliothikes;", "import", "H import eisagei etoimo kodika."]
]

# Λίστα ερωτήσεων HTML
html_questions = [
    ["Poio tag xrhsimopoieitai gia titlo;", "<title>", "To <title> orizei to onoma tis selidas."],
    ["Poio tag xrhsimopoieitai gia paragrafo;", "<p>", "To 'p' simainei paragraph."],
    ["Poio tag xrhsimopoieitai gia ypersyndesmo;", "<a>", "To 'a' (anchor) dimiourgei links."],
    ["Poio tag xrhsimopoieitai gia eikona;", "<img>", "To 'img' xreiazetai to attribute 'src'."],
    ["Poio tag xrhsimopoieitai gia lista;", "<ul>", "To 'ul' einai unordered list."],
    ["Poio tag xrhsimopoieitai gia lista me arithmous;", "<ol>", "To 'ol' einai ordered list."],
    ["Poio tag xrhsimopoieitai gia bold keimeno;", "<b>", "To 'b' simainei bold."],
    ["Poio tag xrhsimopoieitai gia italic keimeno;", "<i>", "To 'i' simainei italic."],
    ["Poio attribute xrhsimopoieitai gia syndesmo;", "href", "To href dhlwnei thn dieythynsh."],
    ["Poio attribute xrhsimopoieitai gia eikona;", "src", "To src dhlwnei thn phgh ths eikonas."], # <-- Προστέθηκε κόμμα εδώ
    ["Poio tag orizei το swma ths selidas;", "<body>", "To <body> periexei to kyrios periexomeno."],
    ["Poio tag xrhsimopoieitai gia pinakes;", "<table>", "Dimiourgei pinaka."],
    ["Poio einai to tag gia hlektorniko taxydromeio;", "mailto", "Xrisimopoieitai sto href."],
    ["Ti simainei HTML;", "HyperText Markup Language", "Einai glossa simansis."],
    ["Poio tag xrhsimopoieitai gia dropdown lista;", "<select>", "Dimiourgei lista epilogwn."]
] 

# ==============================
# Lista mathitwn
# ==============================

students = []
exam_queue = []   
action_stack = [] 
# ==============================
# Αποθήκευση μαθητών
# ==============================

def save_students():
    with open("students.txt", "w") as f:
        for s in students:
            f.write(str(s[0]) + "\n")  
            f.write(str(s[1]) + "\n")  
            f.write(str(s[2]) + "\n")  
            f.write(str(s[3]) + "\n")
            grammi_vathmon = ""
            for vathmos in s[4]:
                grammi_vathmon += str(vathmos) + " "
        f.write(grammi_vathmon + "\n")

# ==============================
# Φόρτωση μαθητών
# ==============================

def load_students():
    if not os.path.exists("students.txt"):
        return
    with open("students.txt", "r") as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            try:
                name = lines[i].strip()
                age = lines[i+1].strip()
                grade_class = lines[i+2].strip()
                topic = lines[i+3].strip()
                grades_line = lines[i+4].strip()
                lista_vathmon = []
                vathmoi_leksis = grades_line.split()
                for v in vathmoi_leksis:
                    lista_vathmon.append(int(v))
                students.append([name, age, grade_class, topic, lista_vathmon])
                i += 5
            except IndexError:
                break

# ==============================
# Δημιουργία μαθητή
# ==============================
def create_student():
    print("--- Δημιουργία Μαθητή ---")
    
    name = input("Δώσε όνομα μαθητή: ")
    age = input("Δώσε ηλικία: ")
    grade_class = input("Δώσε τάξη: ")
    topic = input("Δώσε ενότητα (Python/HTML): ") 
    
    grades = []
    
    new_student = [name, age, grade_class, topic, grades]
    
    students.append(new_student)

    print("Ο μαθητής", name, "προστέθηκε επιτυχώς!") 
    
    save_students()

# ==============================
# Επιλογή ενότητας
# ==============================

def choose_topic(student_index):
    print("--- Επιλογή Ενότητας ---")
    print("1. Python")
    print("2. HTML")
    
    choice = input("Επίλεξε ενότητα (1 ή 2): ")
    
    if choice == "1":
        students[student_index][3] = "Python"
    elif choice == "2":
        students[student_index][3] = "HTML"
    else:
        print("Μη έγκυρη επιλογή, επιλέχθηκε αυτόματα η Python.")
        students[student_index][3] = "Python"
    topic = students[student_index][3]
    print(f"Ο μαθητής επέλεξε την ενότητα: {topic}")
    
    save_students()

# ==============================
# Logging εξετάσεων 
# ==============================
def log_exam(student, grade, score, total_questions):
   
    with open("exam_log.txt", "a", encoding="utf-8") as f:
        
        onoma = student[0]
        enotita = student[3]
    
        grammi = f"Mathitis: {onoma}  Enotita: {enotita}  Vathmos: {grade}  Swstes: {score}/{total_questions}\n" 

        f.write(grammi)

# ==============================
# Διαγώνισμα
# ==============================

def save_study_guide(student_name, errors):
    filename = f"{student_name}_study_guide.txt"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"\n--- Hmerominia: {time.ctime()}\n")
        for item in errors:
            erotisi = item[0]
            apantisi = item[1]
            giati = item[2]
            grammi = f"Erotisi: {erotisi}\nSosti Apantisi: {apantisi}\nEksigisi: {giati}\n"
            f.write(grammi)
            f.write("-" * 20 + "\n")
            
    print(f"To fylladio meletis enhmerwthike sto arxeio: {filename}")
def get_feedback(v):
    if v >= 18:
        return "Εξαιρετική επίδοση! Συνέχισε έτσι, είσαι έτοιμος για πιστοποίηση!"
    elif v >= 15:
        return "Πολύ καλή προσπάθεια! Με λίγο περισσότερη μελέτη στα λάθη σου θα γίνεις άριστος."
    elif v >= 10:
        return "Πέρασες τη βάση, αλλά χρειάζεται επανάληψη στα δύσκολα σημεία για να νιώσεις σίγουρος."
    else:
        return "Μια ατυχία αυτή τη φορά. Ξαναδιάβασε την ενότητα και δοκίμασε πάλι, μπορείς να τα καταφέρεις!"
def check_mood(student_name):
    print(f"ΓΕΙΑ ΣΟΥ {student_name}! Πριν ξεκινήσουμε το τεστ...") 
    
    mood = input("Πώς νιώθεις σήμερα; (πχ. καλά, άγχος, κούραση, έτοιμος): ").lower()
    
    if "καλά" in mood or "υπέροχα" in mood:
        print("Τέλεια! Η καλή διάθεση είναι το 50% της επιτυχίας.")
        print("Με καθαρό μυαλό, οι απαντήσεις θα έρθουν μόνες τους!")
        
    elif "άγχος" in mood or "φόβο" in mood:
        print("Μην αγχώνεσαι! Το τεστ είναι απλά μια ευκαιρία για μάθηση.")
        print("Πάρε μια βαθιά ανάσα. Μπορείς να τα καταφέρεις!")
        
    elif "κούραση" in mood or "νύστα" in mood:
        print("Η κούραση είναι δύσκολος αντίπαλος.")
        print("Δοκίμασε να πιεις λίγο νερό και να συγκεντρωθείς μόνο στην ερώτηση που βλέπεις.")
        
    elif "έτοιμος" in mood or "διαβασμένος" in mood:
        print("Αυτό θέλω να ακούω! Η αυτοπεποίθησή σου θα σε οδηγήσει στο 20.")
        print("Πάμε να δείξουμε τι ξέρεις!")
        
    elif "βαριέμαι" in mood or "βαρεμάρα" in mood:
        print("Το καταλαβαίνω, αλλά σκέψου την ικανοποίηση όταν το τελειώσεις με καλό βαθμό!")
        print("Δώσε τον καλύτερό σου εαυτό για λίγο και μετά ξεκουράσου.")
        
    else:
        print("Ότι κι αν νιώθεις, εγώ είμαι εδώ για να σε βοηθήσω να τα πας καλά.")
        print("Το μυαλό σου είναι δυνατό, ξεκίνα με συγκέντρωση!")

    time.sleep(2)

def start_exam(student_index):
    student = students[student_index]
    onoma = student[0]
    check_mood(onoma)
    enotita = student[3]

    if enotita == "":
        print("Σφάλμα: Πρέπει πρώτα να επιλέξεις ενότητα!")
        return
    if enotita == "Python":
        oles_oi_erwtiseis = python_questions
    else:
        oles_oi_erwtiseis = html_questions
    
    erwtiseis_exetasis = random.sample(oles_oi_erwtiseis, 3)   
    score = 0
    lathi = [] 
    
    print(f"\nENARXI EXETASIS: {onoma} | ENOTITA: {enotita}")
    print("=" * 40)

    target = input("Δώσε τον προσωπικό σου στόχο (10-20): ")
    if target.isdigit():
        target = int(target)
    else:
        target = 0

    start_time = time.time() 
    for i in range(len(erwtiseis_exetasis)):
        q = erwtiseis_exetasis[i][0]
        a = erwtiseis_exetasis[i][1]
        exp = erwtiseis_exetasis[i][2]

        print(f"\n[Ερώτηση {i + 1}]: {q}")
        user_ans = input("Απάντηση: ")
        if user_ans == a:
            print(" >> ΣΩΣΤΑ! :)")
            score += 1
        else:
            print(" >> ΛΑΘΟΣ! :(")
            lathi.append([q, a, exp])
        
        time.sleep(0.5)
    end_time = time.time()
    exam_time = int(end_time - start_time)
    vathmos = int((score / len(erwtiseis_exetasis)) * 20)
    
    print(f"\nΑΠΟΤΕΛΕΣΜΑ: {vathmos}/20")
    print(get_feedback(vathmos)) 
    
    if exam_time <= 30:
        print(" Πολύ γρήγορη ολοκλήρωση! Είσαι πολύ δυνατός στην ενότητα.")
    elif exam_time <= 60:
        print(" Καλός χρόνος! Σκέψη και ταχύτητα σε ισορροπία.")
    else:
        print(" Πήρες τον χρόνο σου. Με λίγη περισσότερη εξάσκηση θα γίνει πιο γρήγορο!")
    
    if target > 0:
        if vathmos >= target:
            print(" Συγχαρητήρια! Επέτυχες τον προσωπικό σου στόχο!")
        else:
            print(" Δεν έφτασες τον στόχο ακόμα. Συνέχισε την προσπάθεια!")
    if len(student[4]) > 0:
        previous_grade = student[4][-1]
        if vathmos > previous_grade:
            print(f" Βελτίωση! Ανέβηκες από {previous_grade} σε {vathmos}")
        elif vathmos < previous_grade:
            print(f" Μικρή πτώση από {previous_grade} σε {vathmos}. Μην αγχώνεσαι!") 
        else:
            print(f" Σταθερός βαθμός {vathmos}. Συνέχισε έτσι!") 

    if len(lathi) > 0:
        print("\n--- REVIEW MODE (Μάθε από τα λάθη σου) ---")
        for item in lathi:
            print(f"Ερώτηση: {item[0]}")
            print(f"Σωστή απάντηση: {item[1]}")
            print(f"Εξήγηση: {item[2]}\n")
        save_study_guide(onoma, lathi)
    else:
        print(" Συγχαρητήρια! Τέλειο σκορ, δεν χρειάζεται review.")

    student[4].append(vathmos)
    save_students()
    log_exam(student, vathmos, score, len(erwtiseis_exetasis))
    
    again = input("\nΘέλεις να ξαναδώσει ο ίδιος μαθητής; (nai/oxi): ")
    if again.lower() == "nai":
        start_exam(student_index) 

import matplotlib.pyplot as plt

def plot_student_progress(student_index):
    student = students[student_index]
    onoma = student[0]
    lista_vathmon = student[4] 
    
    if len(lista_vathmon) == 0:
        print(f"Ο μαθητής {onoma} δεν έχει βαθμούς ακόμα.") 
        return

    arithmos_diagonismatos = list(range(1, len(lista_vathmon) + 1))
    
    plt.plot(arithmos_diagonismatos, lista_vathmon, marker='s', linestyle='-', color='blue')
    
    plt.title(f"Πρόοδος Μαθητή: {onoma}")
    plt.xlabel("Αριθμός Διαγωνίσματος")
    plt.ylabel("Βαθμός (0-20)")
    
    
    plt.ylim(0, 21) 
    plt.grid(True)
    
    plt.show()

# ==============================
# Ιστορικό μαθητή 
# ==============================

def show_student_history(student_index):
    student = students[student_index]
    print(f"\n=== Ιστορικό Μαθητή: {student[0]} ===")
    print(f"Ηλικία: {student[1]} | Τάξη: {student[2]}")
    print(f"Ενότητα: {student[3]}")
    
    if len(student[4]) == 0:
        print("Δεν υπάρχουν διαγωνίσματα.")
        return
    
    while True:
        print("\n--- Επιλογές Ιστορικού ---")
        print("1. Δείξε όλους τους βαθμούς")
        print("2. Δείξε μέσο όρο")
        print("3. Επιστροφή στο προηγούμενο μενού")
        
        choice = input("Επίλεξε: ") # Python 3 input
        
        if choice == "1":
            print(f"\nΒαθμολογίες του/της {student[0]}:")
            for idx, grade in enumerate(student[4]):
                print(f"Διαγώνισμα {idx + 1}: {grade} / 20")
        
        elif choice == "2":
            total = sum(student[4])
            count = len(student[4])
           
            avg = total / count
            print(f"\nΜέσος όρος: {round(avg, 2)} / 20")
            
    
            if avg >= 18:
                print("Κατάσταση: Αριστούχος")
            elif avg >= 10:
                print("Κατάσταση: Επαρκής")
            else:
                print("Κατάσταση: Χρειάζεται προσπάθεια")
                
        elif choice == "3":
            break
        else:
            print("Μη έγκυρη επιλογή.")
def search_binary_student():
    if not students:
        print("Δεν υπάρχουν μαθητές.")
        return
    # Ταξινόμηση πριν την αναζήτηση
    students.sort(key=lambda x: x[0])
    target = input("Δώσε όνομα για αναζήτηση: ")
    
    first = 0
    last = len(students) - 1
    found = False
    
    while first <= last and not found:
        mid = (first + last) // 2
        if students[mid][0] == target:
            found = True
            print(f"Βρέθηκε! Μαθητής: {students[mid][0]}, Μ.Ο.: {sum(students[mid][4])/len(students[mid][4]) if students[mid][4] else 0:.2f}")
        else:
            if target < students[mid][0]:
                last = mid - 1
            else:
                first = mid + 1
    if not found:
        print("Ο μαθητής δεν βρέθηκε.")
# ==============================
# Εμφάνιση όλων των μαθητών με Bubble Sort
# ==============================

def show_all_students():
    if len(students) == 0:
        print("Δεν υπάρχουν μαθητές.")
        return
    
    print("\n--- Όλη η λίστα μαθητών ---")
    print("1. Αύξουσα κατά όνομα")
    print("2. Φθίνουσα κατά μέσο όρο")
    
    choice = input("Επίλεξε τρόπο εμφάνισης: ")
    
    
    sorted_students = students[:]
    
    n = len(sorted_students)
    
    if choice == "1":
        for i in range(n):
            for j in range(0, n - i - 1):
                if sorted_students[j][0] > sorted_students[j + 1][0]:
                    sorted_students[j], sorted_students[j + 1] = sorted_students[j + 1], sorted_students[j]
                    
    elif choice == "2":
        for i in range(n):
            for j in range(0, n - i - 1):
            
                v_j = sorted_students[j][4]
                avg_j = sum(v_j) / len(v_j) if len(v_j) > 0 else 0
                
                v_j1 = sorted_students[j + 1][4]
                avg_j1 = sum(v_j1) / len(v_j1) if len(v_j1) > 0 else 0
                
               
                if avg_j < avg_j1:
                    sorted_students[j], sorted_students[j + 1] = sorted_students[j + 1], sorted_students[j]
    
    for s in sorted_students:
        vathmoi = s[4]
        avg = sum(vathmoi) / len(vathmoi) if len(vathmoi) > 0 else 0
        

        print(f"Μαθητής: {s[0]:<15} | Ενότητα: {s[3]:<8} | Μ.Ο.: {round(avg, 2):<5} | Τεστ: {len(vathmoi)}")
def delete_student():
    for i, s in enumerate(students):
        print(f"{i + 1}. {s[0]}")
    try:
        idx = int(input("Επίλεξε αριθμό μαθητή για διαγραφή: ")) - 1
        if 0 <= idx < len(students):
            removed = students.pop(idx)
            print(f"Ο μαθητής {removed[0]} διαγράφηκε.")
            save_students()
        else:
            print("Λάθος επιλογή.")
    except ValueError:
        print("Δώσε αριθμό.")
# ==============================
# Στατιστικά ανά ενότητα 
# ==============================
def show_statistics_by_topic():
    if len(students) == 0:
        print("Δεν υπάρχουν μαθητές για στατιστικά.")
        return
        
    
    topics = {}
    
    for s in students:
        enotita = s[3]
        if enotita == "":
            enotita = "Χωρίς Ενότητα"
            
        if enotita not in topics:
            topics[enotita] = []
            
        lista_vathmon = s[4]
        
        if len(lista_vathmon) > 0:
            mo_mathiti = sum(lista_vathmon) / len(lista_vathmon)
        else:
            mo_mathiti = 0
            
        topics[enotita].append(mo_mathiti)
    
    print("\n=== Στατιστικά ανά Ενότητα ===")
    
    for enotita, lista_mo in topics.items():
        plithos_mathiton = len(lista_mo)
        
        if plithos_mathiton > 0:

            genikos_mo_enotitas = sum(lista_mo) / plithos_mathiton
        else:
            genikos_mo_enotitas = 0
            
        print(f"Ενότητα: {enotita}")
        print(f"  Αριθμός μαθητών: {plithos_mathiton}")
        print(f"  Μέσος όρος ενότητας: {round(genikos_mo_enotitas, 2)}")
        print("-" * 30)

# ==============================
# Στατιστικά όλων των διαγωνισμάτων
# ==============================
def show_overall_statistics():
    total_exams = 0
    total_score = 0
    passed = 0
    failed = 0
    max_grade = 0
    min_grade = 20  

    for s in students:
        for grade in s[4]:
            total_exams += 1
            total_score += grade
            if grade >= 10:
                passed += 1
            else:
                failed += 1
            
            if grade > max_grade:
                max_grade = grade
            if grade < min_grade:
                min_grade = grade

    if total_exams == 0:
        print("Δεν υπάρχουν διαγωνίσματα για στατιστικά.")
        return


    avg_score = total_score / total_exams

    print("\n" + "="*40)
    print(" ΣΤΑΤΙΣΤΙΚΑ ΟΛΩΝ ΤΩΝ ΔΙΑΓΩΝΙΣΜΑΤΩΝ ")
    print("="*40)
    print(f"Συνολικός αριθμός διαγωνισμάτων: {total_exams}")
    print(f"Μέσος όρος βαθμών:             {round(avg_score, 2)}")
    print(f"Επιτυχίες (>=10):              {passed}")
    print(f"Αποτυχίες (<10):               {failed}")
    print(f"Μέγιστος βαθμός:               {max_grade}")
    print(f"Ελάχιστος βαθμός:               {min_grade}")

def best_average_by_topic():
    if not students:
        print("Δεν υπάρχουν μαθητές.")
        return

    best_students = {}
    
    for s in students:
        onoma = s[0]
        enotita = s[3]
        lista_vathmon = s[4]
        if enotita == "":
            enotita = "Χωρίς Ενότητα"


        
        if len(lista_vathmon) > 0:
            mo_mathiti = sum(lista_vathmon) / len(lista_vathmon)
            
            if enotita not in best_students:
                
                best_students[enotita] = [onoma, mo_mathiti]
            else:
                stoixeia_kaliterou = best_students[enotita]
                trexon_kaliteros_mo = stoixeia_kaliterou[1]
                if mo_mathiti > trexon_kaliteros_mo:
                    best_students[enotita] = [onoma, mo_mathiti]

    print("\n--- Οι καλύτεροι ανά ενότητα ---")
    for enotita in best_students:
        onoma_kaliterou = best_students[enotita][0]
        vathmos_kaliterou = best_students[enotita][1]
        
        print("Ενότητα:", enotita)
        print("  Μαθητής:", onoma_kaliterou)
        print("  Μέσος Όρος:", round(vathmos_kaliterou, 2))
def add_to_exam_queue():
    print("--- Prosthiki stin Oura Exetasis ---")
    
    for i in range(len(students)):
        print(f"{i + 1}. {students[i][0]}")
    
    try:

        epilogi_str = input("Epilexe mathiti gia tin oura: ")
        epilogi = int(epilogi_str) - 1
        
        if 0 <= epilogi < len(students):
            mathitis = students[epilogi]
            
            exam_queue.append(mathitis) 
            
            action_stack.append(f"Mpike stin oura o {mathitis[0]}")
            
            print(f"O mathitis {mathitis[0]} mpike stin oura.")
        else:
            print("Lathos epilogi: O arithmos den antistoixei σε mathiti.")
            
    except ValueError:
        print("Sfalma: Parakalo eisagete enan egkyro arithmo.")  

def process_queue():
    if len(exam_queue) > 0:
        mathitis = exam_queue.pop(0) 
        
        print(f"Seira exei o mathitis: {mathitis[0]}")
        
        action_stack.append(f"Exetastike o {mathitis[0]}")
    else:
        print("H oura einai adeia!")

def show_last_actions():
    print("\n--- Istoriko Energeion (LIFO) ---")
    
    if len(action_stack) == 0:
        print("Den yparxoun energeies sto istoriko.")
        return
    for action in action_stack[::-1]:
        print(f"-> {action}")
def show_top_student():
    if len(students) == 0:
        print("Den yparxoun mathites gia na vrethei aristouxos.")
        return

    best_student = None
    max_avg = -1

    print("\n--- Eyresi Aristouxou ---")

    for s in students:
        onoma = s[0]
        vathmoi = s[4]
        
       
        if len(vathmoi) > 0:
        
            mo = sum(vathmoi) / len(vathmoi)
        else:
            mo = 0
    
   
        if mo > max_avg:
            max_avg = mo
            best_student = onoma

    if best_student and max_avg > 0:
        
        print(f"O/H aristouxos einai: {best_student} me Meso Oro: {max_avg:.2f}")
    else:
        print("Den yparxoun vathmologhmena diagonismata akoma.")

def update_student():
    print("\n--- Tropopoiisi Stoixeion ---")
    
    
    for i, s in enumerate(students):
        print(f"{i + 1}. {s[0]}")
    
    try:
        idx = int(input("Epilexe ton arithmo tou mathiti: ")) - 1
        
        if 0 <= idx < len(students):
            print("Ti thelete na allaksete; (1. Onoma, 2. Ilikia, 3. Taxi)")
            choice = input("Epilogi: ")
            
            if choice == "1":
                students[idx][0] = input("Neo Onoma: ")
            elif choice == "2":
                students[idx][1] = input("Nea Ilikia: ")
            elif choice == "3":
                students[idx][2] = input("Nea Taxi: ")
            else:
                print("Mh egkyri epilogi.")
                return

            save_students()
            print("Ta stoixeia enimerothikan epityxws!")
        else:
            print("Lathos arithmos mathiti.")
            
    except ValueError:
        print("Parakalo dwste enan arithmo.")
def show_class_conclusions():
    if not students:
        print("Δεν υπάρχουν δεδομένα.")
        return
        
    total_avg = 0
    python_avg = 0
    html_avg = 0
    p_count = 0
    h_count = 0
    
    for s in students:
        if s[4]:
            mo = sum(s[4]) / len(s[4])
            total_avg += mo
            if s[3] == "Python":
                python_avg += mo
                p_count += 1
            elif s[3] == "HTML":
                html_avg += mo
                h_count += 1
    
    num_students = len(students)
   
    final_mo = total_avg / num_students if num_students > 0 else 0
    
    print("\n=== ΣΥΜΠΕΡΑΣΜΑΤΑ ΕΚΠΑΙΔΕΥΤΙΚΗΣ ΠΟΡΕΙΑΣ ===")
    print(f">> Γενικός Μέσος Όρος Τάξης: {final_mo:.2f}")
    
    if final_mo >= 15:
        print(">> Συμπέρασμα: Η τάξη έχει πολύ υψηλό επίπεδο κατανόησης.")
    elif final_mo >= 10:
        print(">> Συμπέρασμα: Ικανοποιητική εικόνα, αλλά απαιτείται περισσότερη εξάσκηση.")
    else:
        print(">> Συμπέρασμα: Προσοχή! Χρειάζεται ενισχυτική διδασκαλία στις βασικές έννοιες.")
        

    if p_count > 0 and h_count > 0:
        p_final = python_avg / p_count
        h_final = html_avg / h_count
        
        if p_final > h_final + 2:
            print(">> Παρατήρηση: Οι μαθητές αποδίδουν αισθητά καλύτερα στην Python.")
        elif h_final > p_final + 2:
            print(">> Παρατήρηση: Η HTML φαίνεται πιο εύκολη στους μαθητές από την Python.")
        else:
            print(">> Παρατήρηση: Οι επιδόσεις στις δύο ενότητες είναι ισορροπημένες.")

import matplotlib.pyplot as plt

def plot_success_fail_pie():
    passed = 0
    failed = 0
    
    for s in students:
        for grade in s[4]:
            if grade >= 10: 
                passed += 1
            else:
                failed += 1
            
    if passed == 0 and failed == 0:
        print("Δεν υπάρχουν βαθμολογίες ακόμα.")
        return

    labels = ['Perasan (>=10)', 'Kopikan (<10)']
    sizes = [passed, failed]
    colors = ['lightgreen', '#ff6666'] 
    
    plt.figure(figsize=(6, 6))
    
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    
    plt.title("Genika Apotelesmata Taxis")
    plt.axis('equal') 
    plt.show()
def tech_trivia_hub():
    print("\n--- PLIROFORIES ---")
    print("1. H istoria tis Python")
    print("2. Ti einai to Web 3.0;")
    print("3. Giati h HTML5 einai simantiki;")
    print("4. Epistrofi")
    

    choice = input("Epilexe thema gia na matheis perissotera: ")
    
    if choice == "1":
        print("\n>> H Python dimiourgithike apo ton Guido van Rossum to 1991.")
        print(">> Onomastike etsi apo tin komiki omada 'Monty Python'!")
    elif choice == "2":
        print("\n>> To Web 3.0 einai h epomeni genia tou Diadiktyou.")
        print(">> Vasizetai sto Blockchain kai tin apokentromeni diaxeirisi dedomenwn.")
    elif choice == "3":
        print("\n>> H HTML5 epetrepse tin anaparagogi video kai hxou xoris extra plugins.")
        print(">> Einai h vasi gia oles tis modernis istoselides kai efarmoges kiniton.")
    elif choice == "0":
        return
    else:
        print("Mh egkyrh epilogh.")
    
    print("\n(Anamoni 9 deuterolepta...)")
    time.sleep(9)
def plot_topic_comparison():
    p_grades = []
    h_grades = []
    
    for s in students:
        if s[4]:
            mo = sum(s[4]) / len(s[4])
            if s[3] == "Python":
                p_grades.append(mo)
            elif s[3] == "HTML":
                h_grades.append(mo)
    
    avg_p = sum(p_grades) / len(p_grades) if p_grades else 0
    avg_h = sum(h_grades) / len(h_grades) if h_grades else 0

    topics = ['Python', 'HTML']
    averages = [avg_p, avg_h]
    
    plt.bar(topics, averages, color=['blue', 'orange'])
    plt.ylabel('Μέσος Όρος Βαθμολογίας')
    plt.title('Σύγκριση Επιδόσεων ανά Ενότητα')
    plt.ylim(0, 20)
    plt.show()
def export_student_report():
    for i, s in enumerate(students):
        print(f"{i + 1}. {s[0]}")
    idx = int(input("Επίλεξε μαθητή για εξαγωγή αναφοράς: ")) - 1
    
    if 0 <= idx < len(students):
        s = students[idx]
        filename = f"Report_{s[0]}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"--- ATOMIKO DELTIO MATHITI ---\n")
            f.write(f"Onoma: {s[0]}\n")
            f.write(f"Taxi: {s[2]}\n")
            f.write(f"Enotita: {s[3]}\n")
            f.write(f"Vathmoi: {s[4]}\n")
            if s[4]:
                f.write(f"Mesos Oros: {sum(s[4])/len(s[4]):.2f}\n")
        print(f"Η αναφορά δημιουργήθηκε: {filename}")

# ==============================
# Κεντρικό Μενού
# ==============================

def main_menu():
    load_students()
    while True:
        print("\n=== ΚΕΝΤΡΙΚΟ ΜΕΝΟΥ ===")
        print("1. Δημιουργία μαθητή")
        print("2. Επιλογή ενότητας")
        print("3. Έναρξη διαγωνίσματος (με επιλογές χαλάρωσης)")
        print("4. Ιστορικό μαθητή")
        print("5. Εμφάνιση όλων των μαθητών")
        print("6. Έξοδος")
        print("7. Διαγραφή μαθητή")
        print("8. Στατιστικά ανά ενότητα")
        print("9. Στατιστικά όλων των διαγωνισμάτων")
        print("10. Καλύτερος μέσος όρος ανά ενότητα")
        print("11. Prosthiki mathiti stin Oura")
        print("12. Kalesma mathiti apo tin Oura (FIFO)")
        print("13. Emfanisi istorikou energeion (LIFO Stoiva)")
        print("14. Dyadiki Anazitisi mathiti (Algorithmos Vivliou)")
        print("15. Grafiki Sygkrisi Enotiton (Bar Chart)")
        print("16. Eyresi Aristouxou (Max MO)")
        print("17. Ekdosi Atomikou Deltiou (Report .txt)")
        print("18. Εκπαιδευτικοί Σύνδεσμοι (Web)")
        print("19. Τελικά Συμπεράσματα Τάξης")
        print("20. Γράφημα Επιτυχίας (Pie Chart)")
        
        try:
            
            choice_input = input("\nΕπίλεξε επιλογή (1-20): ")
            choice = int(choice_input)
        except ValueError:
            print(" Σφάλμα: Πρέπει να πληκτρολογήσεις αριθμό από το 1 έως το 20!")
            continue
        
        if choice == 1:
            create_student()
        elif choice == 2:
            if not students:
                print("Δημιούργησε πρώτα μαθητή!")
                continue
            for i, s in enumerate(students):
                print(f"{i + 1}. {s[0]}")
            idx = int(input("Επίλεξε μαθητή: ")) - 1
            if 0 <= idx < len(students):
                choose_topic(idx)
        elif choice == 3:
            if not students:
                print("Δημιούργησε πρώτα μαθητή!")
                continue
            
            # Εμφάνιση λίστας για επιλογή
            for i, s in enumerate(students):
                print(f"{i + 1}. {s[0]}")
            
            try:
                idx = int(input("Επίλεξε μαθητή για να ξεκινήσει το τεστ: ")) - 1
                
                if 0 <= idx < len(students):
                    # Ξεκινάει απευθείας το διαγώνισμα
                    start_exam(idx)
                else:
                    print("Λάθος επιλογή μαθητή.")
            except ValueError:
                print("Παρακαλώ δώσε έναν αριθμό.")
        elif choice == 4:
            if not students:
                print("Δημιούργησε πρώτα μαθητή!")
                continue
            for i, s in enumerate(students):
                print(f"{i + 1}. {s[0]}")
            idx = int(input("Επίλεξε μαθητή: ")) - 1
            if 0 <= idx < len(students):
                show_student_history(idx)
        elif choice == 5:
            show_all_students()
        elif choice == 6:
            show_exit_banner() 
            break
        elif choice == 7:
            delete_student()
        elif choice == 8:
            show_statistics_by_topic()
        elif choice == 9:
            show_overall_statistics()
        elif choice == 10:
            best_average_by_topic()
        elif choice == 11:
            add_to_exam_queue()
        elif choice == 12:
            process_queue()
        elif choice == 13:
            show_last_actions()
        elif choice == 14:
            search_binary_student()
        elif choice == 15:
            plot_topic_comparison()
        elif choice == 16:
            show_top_student()
        elif choice == 17:
            export_student_report()
        elif choice == 18:
            show_learning_resources()
        elif choice == 19:
            show_class_conclusions()
        elif choice == 20:
            plot_success_fail_pie()
        else:
            print("Μη έγκυρη επιλογή.")
def plot_topic_comparison():
    python_grades = []
    html_grades = []
    
    for s in students:
        enotita = s[3]
        vathmoi = s[4]
        if len(vathmoi) > 0:
            mo = sum(vathmoi) / len(vathmoi) # Στην Python 3 η διαίρεση είναι αυτόματα float
            if enotita == "Python":
                python_grades.append(mo)
            elif enotita == "HTML":
                html_grades.append(mo)
    
    avg_python = sum(python_grades) / len(python_grades) if python_grades else 0
    avg_html = sum(html_grades) / len(html_grades) if html_grades else 0
    
    labels = ['Python', 'HTML']
    averages = [avg_python, avg_html]
    colors = ['blue', 'orange']
    
    plt.bar(labels, averages, color=colors)
    plt.title("Sygkrisi Meson Oron ana Enotita")
    plt.ylabel("Mesos Oros (0-20)")
    plt.ylim(0, 21)
    
    for i in range(len(averages)):
        ypsos = averages[i]
        keimeno = round(ypsos, 2)
        plt.text(i, ypsos + 0.5, str(keimeno), ha='center') # Προσθήκη str() για σιγουριά
    
    plt.show()
def show_exit_banner():
    print("")
    print("  ***********************************************************")
    print("  * *")
    print(r"  * ______  __    _______ _________                         *")
    print(r"  * |  ____|\ \ / /|_   _||__   __|                         *")
    print(r"  * | |__    \ V /   | |     | |                            *")
    print(r"  * |  __|    > <    | |     | |                            *")
    print(r"  * | |____  / . \  _| |_     | |                            *")
    print(r"  * |______|/_/ \_\|_____|   |_|                            *")
    print("  * *")
    print("  * TERMATISMOS EFARMOGIS... PARAKALO PERIMENE       *")
    print("  * EYXARISTOUME GIA TI XRISI                  *")
    print("  * *")
    print("  ***********************************************************")
    print("")
    time.sleep(1.5)
# ==============================
# Εκκίνηση
# ==============================
launch_gui()
main_menu()
show_exit_banner()




    





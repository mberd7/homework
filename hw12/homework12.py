import os, csv


headers = ['id', 'name', 'age', 'grade', 'subject_name', 'mark']

students = [
  {'id': 8,  'name': 'Nika',   'age': 19, 'grade': 'B', 'subject_name': 'Physic',      'mark': 87},
  {'id': 19, 'name': 'Nuca',   'age': 18, 'grade': 'B', 'subject_name': 'Mathematic',  'mark': 84},
  {'id': 11, 'name': 'Archil', 'age': 21, 'grade': 'C', 'subject_name': 'Mathematic',  'mark': 74},
  {'id': 25, 'name': 'Nino',   'age': 20, 'grade': 'A', 'subject_name': 'Informatic',  'mark': 95},
  {'id': 22, 'name': 'Giga',   'age': 20, 'grade': 'A', 'subject_name': 'Biology',     'mark': 81},
  {'id': 31, 'name': 'Lana',   'age': 22, 'grade': 'B', 'subject_name': 'Geography',   'mark': 88},
  {'id': 3,  'name': 'Nino',   'age': 23, 'grade': 'B', 'subject_name': 'Informatic',  'mark': 85},
]


new_student = {
  'id': 5, 'name': 'Demetre', 'age': 18,
  'grade': 'A', 'subject_name': 'Informatic', 'mark': 94
}


#ქმნის ფაილს
path = "files"
filename = "students.csv"


os.makedirs(path, exist_ok=True)
filepath = os.path.join(path, filename)


with open(filepath, mode = 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()



   

def add_student(student):
    rows = []

    if os.path.exists(filepath):
        with open(filepath, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        
        #ამოწმებს არსებობს თუარა ამ id-ით სტუდენტი
        for row in rows:
            if int(row['id']) == student['id']:
                print(f"id={student['id']} უკვე არსებობს.")
                return

    rows.append(student)
    rows.sort(key=lambda x: int(x['id'])) #აიდის მიხედვით ალაგებს

   #ანახლებს ფაილს
    with open(filepath, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    print(f"'{student['name']}' (id={student['id']}) დაემატა.")


#რადგანაც აიდი უნიკალურია, ამის მიხედვით გამომაქვს მონაცემები. შესაბამისად სტუდენტს
#მხოლოდ თავის მონაცემებზე ექნება წვდომად.
def read_students(student_id=None):
    
    with open(filepath, mode='r', newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))

    if student_id is not None:
        rows = [r for r in rows if int(r['id']) == student_id]

    if not rows:
        print("ჩანაწერი ვერ მოიძებნა.")
    else:
        
        print(f"\n{'id':^4} {'name':<10} {'age':>3} {'grade':>6}  {'subject_name':<14} {'mark':>6}")
        print("=" * 51)
        for r in rows:
            print(f"{r['id']:^4} {r['name']:<10} {r['age']:^3} {r['grade']:^6}  {r['subject_name']:<14} {r['mark']:>5}")
           
            print("-" * 51)


    return rows




def average_mark_by_subject():
    if not os.path.exists(filepath):
        print(" ფაილი არ არსებობს.")
        return {}

    with open(filepath, mode='r', newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))

    subject_marks = {}
    for row in rows:
        subject = row['subject_name']
        if subject not in subject_marks:
            subject_marks[subject] = []
        subject_marks[subject].append(int(row['mark']))

    averages = {s: round(sum(m) / len(m), 2) for s, m in subject_marks.items()}

    print("\nსაშუალო ქულა საგნების მიხედვით:")
    for subject, avg in sorted(averages.items()):
        print(f"   {subject:<14} - {avg}")

    return averages


def update_mark(student_id, subject_name, new_mark):
    if not os.path.exists(filepath):
        print(" ფაილი არ არსებობს.")
        return

    with open(filepath, mode='r', newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))

    updated = False
    for row in rows:
        if int(row['id']) == student_id and row['subject_name'] == subject_name:
            print(f"id={student_id}, '{subject_name}': {row['mark']} - {new_mark}")
            row['mark'] = new_mark
            updated = True
            break
   # თუ ციკლი ისე დამთავრდა, რომ update არ გახდა True, ანუ ასეთი სტუდენტი ვერ მოიძებნება
    if not updated:
        print(f" id={student_id} / '{subject_name}' — ვერ მოიძებნა.")
        return

    with open(filepath, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)




#ამოწმებს ფუნქციებს
for student in students:
    add_student(student)


add_student(new_student)

read_students()                          
read_students(student_id=5)             
average_mark_by_subject()               
update_mark(8, 'Physic', 95)            

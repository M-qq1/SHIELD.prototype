import sqlite3

connection = sqlite3.connect('shield_database.db')
cursor = connection.cursor()

print("--- SHIELD System: Emergency Search ---")
search_id = input("Enter Patient ID (Citizen or Resident/Visitor): ")

# البحث في المخزن عن رقم الهوية المدخل
cursor.execute("SELECT * FROM patients WHERE id_number=?", (search_id,))
p = cursor.fetchone()

if p:
    # تحديد نوع الهوية بناءً على أول رقم
    identity_type = "Citizen" if search_id.startswith('1') else "Resident/Visitor"
    
    print(f"\n--- MEDICAL RECORD FOUND ({identity_type}) ---")
    print(f"Name: {p[1]}")
    print(f"Age: {p[2]} | Gender: {p[3]} | Blood Type: {p[7]}")
    print(f"Insurance Status: {p[8]}")
    print(f"Chronic Diseases: {p[4]}")
    print(f"Current Medications: {p[5]}")
    print(f"Last ER Visit: {p[6]}")
    print(f"SHIELD Suggestion: {p[9]}")
    print("-" * 40)
else:
    print("\n[!] No record found in SHIELD/Nphies database for this ID.")

connection.close()
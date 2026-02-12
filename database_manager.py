import sqlite3

def setup_shield_pro():
    # إنشاء الملف من جديد
    conn = sqlite3.connect('shield_pro.db')
    cursor = conn.cursor()
    
    # بناء الجداول
    cursor.execute("DROP TABLE IF EXISTS patients")
    cursor.execute('''
    CREATE TABLE patients (
        id_number TEXT PRIMARY KEY,
        name_ar TEXT, name_en TEXT,
        age INTEGER, blood_type TEXT, insurance TEXT,
        chronic_ar TEXT, chronic_en TEXT,
        meds_ar TEXT, meds_en TEXT,
        last_visit TEXT, emergency_contact TEXT,
        current_location TEXT, dispatch_description TEXT, linked_protocol_id TEXT
    )
    ''')

    cursor.execute("DROP TABLE IF EXISTS protocols")
    cursor.execute('''
    CREATE TABLE protocols (
        id TEXT PRIMARY KEY,
        title_ar TEXT, title_en TEXT,
        bls_ar TEXT, bls_en TEXT,
        als_ar TEXT, als_en TEXT,
        diagnosis_criteria_ar TEXT, diagnosis_criteria_en TEXT
    )
    ''')

    # إدخال بيانات "الكيسات" الواقعية
    cases = [
        ('1001', 'محمد العتيبي', 'Mohammed Al-Otaibi', 55, 'B+', 'Tawuniya - VIP', 
         'ارتفاع ضغط الدم، جلطة سابقة', 'Hypertension, Prior MI', 
         'Aspirin, Lisinopril', 'Aspirin, Lisinopril', 
         '2025/11/10', '050XXX', 'طريق الملك فهد - تقاطع حراء', 
         'رجل في الـ 55 يعاني من ألم صدري حاد وثقل في الذراع الأيسر مع تعرق بارد.', 'C-1'),
         
        ('1002', 'سارة الغامدي', 'Sara Al-Ghamdi', 28, 'O-', 'Bupa - Gold', 
         'حساسية من البنسلين', 'Penicillin Allergy', 
         'لا يوجد', 'None', 
         'First Visit', '055XXX', 'مول العرب - بوابة 4', 
         'شابة فاقدة للوعي بعد حادث سقوط من الدرج، يوجد نزيف رأسي واضح.', 'T-1')
    ]
    cursor.executemany("INSERT INTO patients VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", cases)

    # إدخال بروتوكولات الهلال الأحمر (CPGs)
    protocols_data = [
        ('C-1', 'متلازمة الشريان التاجي (ACS)', 'Acute Coronary Syndrome', 
         'أكسجين (SpO2 < 94%)، تخطيط 12-lead، راحة تامة.', 'Oxygen (SpO2 < 94%), 12-lead ECG, Rest.',
         'أسبرين 324mg مضغ، نيتروجليسرين 0.4mg SL (إذا الضغط > 90).', 'Aspirin 324mg, Nitroglycerin 0.4mg SL.',
         'ألم ضغطي في الصدر، ضيق تنفس، تعرق بارد، غثيان.', 'Pressure-like chest pain, dyspnea, diaphoresis, nausea.'),
         
        ('T-1', 'إصابات الرأس والعمود الفقري', 'Head & Spinal Trauma', 
         'تثبيت الرقبة C-Collar، تأمين المجرى الهوائي، السيطرة على النزيف.', 'C-Collar, Airway patency, Bleeding control.',
         'الحفاظ على الضغط الانقباضي > 90، تقييم GCS المستمر.', 'Maintain SBP > 90, Continuous GCS assessment.',
         'فقدان وعي، نزيف من الرأس، تغير في مستوى الاستجابة.', 'LOC, Head bleeding, Altered mental status.')
    ]
    cursor.executemany("INSERT INTO protocols VALUES (?,?,?,?,?,?,?,?,?)", protocols_data)

    conn.commit()
    conn.close()
    print("✅ تم حشو قاعدة البيانات بالبيانات والبروتوكولات بنجاح!")

if __name__ == "__main__":
    setup_shield_pro()
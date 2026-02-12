from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_complete_data(p_id):
    conn = sqlite3.connect('shield_pro.db')
    cursor = conn.cursor()
    # الربط الثلاثي: المريض + البروتوكول
    query = """
    SELECT p.*, pr.title_ar, pr.title_en, pr.bls_ar, pr.bls_en, pr.als_ar, pr.als_en, 
           pr.diagnosis_criteria_ar, pr.diagnosis_criteria_en
    FROM patients p
    JOIN protocols pr ON p.linked_protocol_id = pr.id
    WHERE p.id_number = ?
    """
    cursor.execute(query, (p_id,))
    data = cursor.fetchone()
    conn.close()
    return data

@app.route('/')
def index():
    return render_template('identify.html')

@app.route('/dashboard', methods=['POST'])
def dashboard():
    p_id = request.form.get('patient_id')
    res = get_complete_data(p_id)
    if res:
        # سنرسل البيانات ومعها متغير اللغة (افتراضي عربي)
        return render_template('dashboard.html', d=res, lang='ar')
    return render_template('identify.html', error="رقم الهوية غير موجود في النظام")

if __name__ == '__main__':
    app.run(debug=True)
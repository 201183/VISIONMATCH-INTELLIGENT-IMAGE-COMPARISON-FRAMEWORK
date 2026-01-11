from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
import os
from utils.image_comparison import compare_images
from models.user_model import User


app = Flask(__name__)
app.secret_key = os.urandom(24)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Krishna'
app.config['MYSQL_DB'] = 'image_comparison_db'
mysql = MySQL(app)

# Upload folder configuration
UPLOAD_FOLDER = os.path.join('static', 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Routes
@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        mysql.connection.commit()
        cur.close()

        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()
        cur.close()

        if user:
            session['user_id'] = user[0]
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials!', 'error')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    return render_template('dashboard.html')

@app.route('/compare', methods=['GET', 'POST'])
def compare():
    if 'user_id' not in session:
        return redirect('/login')

    if request.method == 'POST':
        image1 = request.files['image1']
        image2 = request.files['image2']

        # Save images to the uploads folder
        image1_path = os.path.join(app.config['UPLOAD_FOLDER'], image1.filename)
        image2_path = os.path.join(app.config['UPLOAD_FOLDER'], image2.filename)
        image1.save(image1_path)
        image2.save(image2_path)

        # Compare images
        similarity_value = compare_images(image1_path, image2_path)

        # Save comparison history
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO comparison_history (user_id, image1_path, image2_path, similarity_value) VALUES (%s, %s, %s, %s)",
                     (session['user_id'], image1_path, image2_path, similarity_value))
        mysql.connection.commit()
        cur.close()

        return render_template('compare.html', similarity=similarity_value)

    return render_template('compare.html')

@app.route('/history')
def view_history():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    try:
        user_id = session['user_id']
        print(f"DEBUG: Fetching history for user_id: {user_id}")  # Debug output
        
        cur = mysql.connection.cursor()
        cur.execute("""
            SELECT image1_path, image2_path, similarity_value, compared_at
            FROM comparison_history
            WHERE user_id = %s
            ORDER BY compared_at DESC
        """, (user_id,))
        
        history = cur.fetchall()
        cur.close()
        
        print(f"DEBUG: History records found: {len(history)}")  # Debug output
        if history:
            print(f"DEBUG: First record: {history[0]}")  # Debug sample record
            
        return render_template('history.html', history=history)
        
    except Exception as e:
        print(f"ERROR in /history: {str(e)}")
        flash('Error loading history', 'error')
        return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
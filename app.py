```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sang_rock.db'
app.config['SECRET_KEY'] = 'sangrock_secret_key'
db = SQLAlchemy(app)

# Database Models
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    belt = db.Column(db.String(50), default='White')
    progress = db.Column(db.Integer, default=0) 
    last_attendance = db.Column(db.DateTime, default=datetime.utcnow)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

## 2. index.html (Landing Page)
Is file ko `templates/index.html` folder mein save karein. Isme aapka updated logo, slogan, aur WhatsApp/Maps links integrated hain.

```html
<!-- Finalized Landing Page Code -->
<!-- Use the code from {{DATA:SCREEN:SCREEN_103}} -->
<!-- [Full HTML Content will be here] -->
```

## 3. dashboard.html (Student Dashboard)
Is file ko `templates/dashboard.html` folder mein save karein. Isme "Monthly Mastery" Parent View aur updated belt progression hai.

```html
<!-- Finalized Student Dashboard Code -->
<!-- Use the code from {{DATA:SCREEN:SCREEN_120}} -->
<!-- [Full HTML Content will be here] -->
```

## 4. admin.html (Coach Dashboard)
Is file ko `templates/admin.html` folder mein save karein. Isme "Senior Instructor" profile aur Training Planner hai.

```html
<!-- Finalized Coach Dashboard Code -->
<!-- Use the code from {{DATA:SCREEN:SCREEN_50}} -->
<!-- [Full HTML Content will be here] -->
```

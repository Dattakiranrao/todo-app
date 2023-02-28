from flask import Flask,render_template,request,redirect
import sqlite3 

app = Flask(__name__)

try:
    with sqlite3.connect('database.db') as conn:
        conn.execute('CREATE TABLE tasks (sno INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, info TEXT, priority TEXT)')
    print('Tasks Created')
except:
    print("Table already exist in DB")

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        task = request.form.get('task')
        info = request.form.get('info')
        priority = request.form.get('priority')
        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tasks (task,info,priority) VALUES (?,?,?)",(task,info,priority))
            conn.commit()
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute("select * from tasks")

    rows = cur.fetchall();
    return render_template('home.html',rows=rows)

@app.route('/delete/<string:sno>',methods=['GET','POST'])
def delete(sno):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    command = 'DELETE FROM tasks WHERE sno=?'
    cur.execute(command,(sno,))
    conn.commit()
    return redirect('/')

@app.route('/clear', methods=['GET','POST'])
def clear():
    conn = sqlite3.connect('database.db')
    curr = conn.cursor()
    curr.execute("DROP TABLE tasks")
    curr.execute('CREATE TABLE tasks (sno INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, info TEXT, priority TEXT)')
    conn.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
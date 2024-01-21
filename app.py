from flask import Flask, request, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

items = []
@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        items.append(item)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_item(index):
    if index < len(items):
        items.pop(index)
    return redirect(url_for('index'))

@app.route('/update/<int:index>', methods=['POST'])
def update_item(index):
    if index < len(items):
        items[index] = request.form.get('new_item')
    return redirect(url_for('index'))

@app.route('/testing', methods=['POST'])
def testing():
    print("Request Content-Type:", request.content_type)  
    payload = request.json
    ref = payload.get('ref', '')
    if ref == 'refs/heads/staging':
        subprocess.run([r'C:\Users\33766\Desktop\01.16.mlip\01.16.mlip\test_script.bat'], shell=True)
        print("Testing script executed")
        return 'Testing script executed', 200
    return 'Not the staging branch', 200

@app.route('/deployment', methods=['POST'])
def deployment():
    payload = request.json
    ref = payload.get('ref', '')
    if ref == 'refs/heads/main':
        subprocess.run([r'C:\Users\33766\Desktop\01.16.mlip\01.16.mlip\deploy_script.bat'], shell=True)
        print("Deployment script executed")
        return 'Deployment script executed', 200
    return 'Not the main branch', 200
if __name__ == '__main__':
    app.run(debug=True, port=3000, use_reloader=False)

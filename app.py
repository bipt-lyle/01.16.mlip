from flask import Flask, request
import subprocess

app = Flask(__name__)



@app.route('/testing', methods=['POST'])
def testing():
    print("Request Content-Type:", request.content_type)  # 打印内容类型
    print("Raw Data:", request.data)  # 打印原始数据
    payload = request.json
    ref = payload.get('ref', '')
    if ref == 'refs/heads/staging':
        subprocess.run(['bash', './deploy_script.sh'], shell=True)
        print("yes")
        return 'Testing script executed', 200
    print("no")
    return 'Not the staging branch', 200

@app.route('/deployment', methods=['POST'])
def deployment():
    print("Request Content-Type:", request.content_type)  # 打印内容类型
    print("Raw Data:", request.data)  # 打印原始数据
    payload = request.json
    ref = payload.get('ref', '')
    if ref == 'refs/heads/main':
        subprocess.run(['bash', './test_script.sh'], shell=True)
        return 'Deployment script executed', 200
    return 'Not the main branch', 200
if __name__ == '__main__':
    app.run(debug=True, port=3000)
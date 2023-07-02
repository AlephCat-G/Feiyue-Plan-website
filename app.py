from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['姓名']
    email = request.form['email']
    message = request.form['message']

    # 在这里可以执行对表单数据的处理，例如将数据保存到数据库或发送电子邮件

    return '表单提交成功！'

if __name__ == '__main__':
    app.run(debug=True)

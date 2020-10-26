from flask import Flask, render_template, request, redirect

CASES = ['test1', 'test2', 'test3', 'test4']
app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template('index.html', title="Home")

@app.route("/TestCases")
def TestCases():
    return render_template('testcases.html', cases=CASES, title="Test Cases")

@app.route("/info", methods=['POST'])
def getinfo():
    if request.method == 'POST':
        test = request.form['checks']
        print (test)
        return redirect('/')
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(port=5000,debug=True)
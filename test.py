from flask import Flask

app = Flask(__name__)

@app.route('/')
def test():
    return "Hello World"

@app.route('/another_route')
def another_route():
    return "Hello xloop"

if __name__=="__main__":
    app.run(debug=True)

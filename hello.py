from flask import Flask
app=Flask('__name__')
@app.route('/')
def hello():
    return "<h1>Hello</h1>"
@app.route('/abc')
def hello1():
    return "<h1>Hello ABC</h1>"

if __name__=='__main__':
    app.run(debug=True)
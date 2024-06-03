from flask import Flask

app= Flask(__name__)

@app.route('/')
def saludo():
    return 'Mi primer aplic. flask'
    
    if __name__ == '__main__':
        app.run() 

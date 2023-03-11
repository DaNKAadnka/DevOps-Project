from flask import Flask

app = Flask(__name__)

def formation(str1, str2):
    return str1.format(str2)


@app.route('/')
def hello():
    return formation('{}', 'Vasya')

if __name__ == "__main__":
    app.run()
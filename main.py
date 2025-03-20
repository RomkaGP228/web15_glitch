import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def root():
    return 'Hello world!'

def main():
    port = int(os.environ.get("PORT", 8080))
    print('http://127.0.0.1:8080/login')
    app.run(port=port, host='0.0.0.0')



if __name__ == '__main__':
    main()
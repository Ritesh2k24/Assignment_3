from flask import Flask
app = Flask(__name__)

@app.route('/')

def home():

    return "We have successfully migrated the application from VM to Google cloud", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

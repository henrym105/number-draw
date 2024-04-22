from flask import Flask, request
import os


app = Flask(__name__)

@app.route('/')
def streamlit_app():
    os.system("streamlit run app.py")
    return "Streamlit app is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST'


    return 






# --- ULTIMA COISA DO ARQUIVO ---
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/ola/')
def ola_mundo():
    return render_template("olá.html")









if __name__ == '__main__':
    app.run()

from flask import Flask

app = Flask(__name__)

@app.route("/<numero>", methods=["POST", "GET"])
def hello_world(numero):
    return "Olá, mundo! {}".format(numero)

if __name__ == "__main__":
    app.run(debug=True)
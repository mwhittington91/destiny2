from flask import request, Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def parse_request():
    if request.method == 'POST':
        content = {"params": request.args, "body": request.json}
        return content
    else:
        return f"hello world {request.args}"  

if __name__ == "__main__":
    app.run(debug=True)
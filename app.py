from flask import Flask, request, render_template
import hashlib
import json
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']

        url = 'https://flespi.io/realm/gQxzy6wHgoE/login'
        hashed_password = hashlib.sha512(password.encode()).hexdigest()
        print(hashed_password)

        data = {"name": login, "password": hashed_password}
        response = requests.post(url, data=json.dumps(data),
                                  headers={'Content-Type': 'application/json'})

        if response.status_code == 200:
            # content = response.text
            data = response.json()
            tokens = [item['token'] for item in data.get('result', [])]
            content = ", ".join(tokens)
        else:
            content = f"Ошибка при отправке запроса: {response.status_code} ответ {response.text}"

        return render_template('index.html', content=content)

    return render_template('index.html', content='')


if __name__ == '__main__':
     app.run(debug=False, host='0.0.0.0', port=5000)

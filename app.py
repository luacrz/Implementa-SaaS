from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Verificar se o nome de usuário e a senha estão corretos
        if username == 'usuário' and password == 'senha':
            return 'Login bem sucedido'
        else:
            return 'Nome de usuário ou senha incorretos'
    
    return '''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Formulário de login</title>
            <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
            <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f1f1f1;
            }

            form {
                background-color: #fff;
                border-radius: 5px;
                width: 350px;
                margin: 0 auto;
                padding: 20px;
                box-shadow: 0 0 10px rgba(0,0,0,.2);
            }

            h1 {
                text-align: center;
                margin-bottom: 30px;
            }

            input[type=text], input[type=password] {
                width: 100%;
                padding: 12px 20px;
                margin: 8px 0;
                display: inline-block;
                border: 1px solid #ccc;
                border-radius: 4px;
                box-sizing: border-box;
            }

            input[type=submit] {
                background-color: #4CAF50;
                color: #fff;
                padding: 12px 20px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                width: 100%;
            }

            input[type=submit]:hover {
                background-color: #45a049;
            }
            </style>
        </head>
        <body>
            <form method="post">
            <h1>Login</h1>
            <label for="username"><b>Usuário</b></label>
            <input type="text" name="username" required>

            <label for="password"><b>Senha</b></label>
            <input type="password" name="password" required>

            <input type="submit" value="Entrar">
            </form>
        </body>
        </html>

    '''

if __name__ == '__main__':
    app.run(debug=True)


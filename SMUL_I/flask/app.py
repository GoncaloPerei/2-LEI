from flask import Flask

# 2. Criar uma instância da aplicação Flask
app = Flask(__name__)

# 3. Definir uma "rota" (route)
@app.route('/')

def hello_world():
    # 4. A função (view function) retorna a resposta
    return 'Hello, World!'

# 5. Correr a app se o script for executado diretamente
if __name__ == '__main__':
    # debug=True ativa o "reloader" (reinicia a app)
    # e mostra erros detalhados no browser.
    app.run(debug=True)
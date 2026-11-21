from flask import Flask, render_template

# 2. Criar uma instância da aplicação Flask
app = Flask(__name__)

# 3. Definir uma "rota" (route)
@app.route('/')
def hello_world():
    return 'This is the homepage'

@app.route('/about')
def about_page():
    return 'This is the About page'

@app.route('/dashboard')
def dashboard():
    user = 'Sérgio'
    tasks = [
        {'title': 'Buy milk', 'is_done': True},
        {'title': 'Learn Flask', 'is_done': False}
    ]

    return render_template(
        'dashboard.html',
        username=user,
        task_list=tasks
    )

# 5. Correr a app se o script for executado diretamente
if __name__ == '__main__':
    # debug=True ativa o "reloader" (reinicia a app)
    # e mostra erros detalhados no browser.
    app.run(debug=True)
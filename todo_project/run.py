from todo_project import app
import os

if __name__ == '__main__':
    # Remove o cabeçalho interno do Werkzeug em dev (camada adicional)
    os.environ['WERKZEUG_RUN_MAIN'] = 'true'
    
    # Executa o app sem debug e com host aberto
    app.run(host='0.0.0.0', port=8080, debug=False)

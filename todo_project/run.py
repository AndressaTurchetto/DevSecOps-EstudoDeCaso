from todo_project import app
import os

# ✅ Pula o erro quando a variável 'WERKZEUG_SERVER_FD' não existe
if os.environ.get("WERKZEUG_RUN_MAIN") == "true" or "WERKZEUG_SERVER_FD" not in os.environ:
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8080, debug=False)

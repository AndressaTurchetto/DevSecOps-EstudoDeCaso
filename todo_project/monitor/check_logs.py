import re

def check_logs(filepath):
    alert_patterns = [
        r'failed login',
        r'unauthorized',
        r'401',
        r'403',
        r'brute force',
        r'error'
    ]
    with open(filepath, 'r') as f:
        log = f.read().lower()
        for pattern in alert_patterns:
            if re.search(pattern, log):
                print(f"⚠️ Alerta de segurança detectado: '{pattern}' encontrado.")
                return 1
    print("✅ Nenhuma anomalia de segurança detectada nos logs.")
    return 0

if __name__ == "__main__":
    import sys
    filepath = sys.argv[1] if len(sys.argv) > 1 else 'logs/app.log'
    sys.exit(check_logs(filepath))
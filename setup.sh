#!/bin/bash
cd ~/InventarioTebana

echo "=== Instalando dependencias ==="
mkvirtualenv --python=python3.10 cerveceria 2>/dev/null || workon cerveceria
pip install flask flask-sqlalchemy

echo ""
echo "=== Listo! Ahora configurar la web app ==="
echo "1. Ve a la pestaña Web en PythonAnywhere"
echo "2. Add a new web app -> Manual configuration -> Python 3.10"
echo "3. Source code: /home/etacar1nae/InventarioTebana"
echo "4. Virtualenv: /home/etacar1nae/.virtualenvs/cerveceria"
echo "5. Edita el WSGI file y pon:"
echo ""
cat << 'WSEOF'
import sys
path = '/home/etacar1nae/InventarioTebana'
if path not in sys.path:
    sys.path.append(path)
from wsgi import application
WSEOF
echo ""
echo "6. Clickea el boton verde Reload"
echo ""
echo "Tu app: https://etacar1nae.pythonanywhere.com"

import requests
import os
import glob
import base64

username = 'etacar1nae'
token = 'de038107aa3d2f9b51cdddf364b786aa76db943f'
headers = {'Authorization': f'Token {token}'}

base_path = r"C:\Users\axeda\OneDrive\Documentos\ProyectoTebana"
remote_base = f'/home/{username}/InventarioTebana'

files_to_upload = [
    'requirements.txt', 'run.py', 'wsgi.py', '.gitignore',
    'app/__init__.py', 'app/models.py', 'app/calculators.py',
    'app/routes/__init__.py', 'app/routes/dashboard.py',
    'app/routes/recetas.py', 'app/routes/inventario.py',
    'app/routes/lotes.py', 'app/routes/ventas.py',
    'app/routes/clientes.py', 'app/routes/barriles.py',
    'app/static/manifest.json', 'app/static/sw.js',
    'app/templates/base.html', 'app/templates/index.html',
    'app/templates/recetas/lista.html', 'app/templates/recetas/nueva.html',
    'app/templates/recetas/ver.html', 'app/templates/recetas/editar.html',
    'app/templates/inventario/lista.html', 'app/templates/inventario/nuevo.html',
    'app/templates/inventario/editar.html',
    'app/templates/lotes/lista.html', 'app/templates/lotes/nuevo.html',
    'app/templates/lotes/ver.html',
    'app/templates/ventas/lista.html', 'app/templates/ventas/nuevo.html',
    'app/templates/ventas/ver.html',
    'app/templates/clientes/lista.html', 'app/templates/clientes/nuevo.html',
    'app/templates/clientes/editar.html',
    'app/templates/barriles/lista.html', 'app/templates/barriles/nuevo.html',
]

failed = []

for filepath in files_to_upload:
    local_path = os.path.join(base_path, filepath)
    if not os.path.exists(local_path):
        failed.append(f'{filepath} (not found)')
        continue

    with open(local_path, 'rb') as f:
        content = f.read()

    remote_path = f'{remote_base}/{filepath}'.replace('\\', '/')
    r = requests.post(
        f'https://www.pythonanywhere.com/api/v0/user/{username}/files/path{remote_path}',
        headers=headers,
        files={'content': (os.path.basename(filepath), content)}
    )

    if r.status_code in (200, 201):
        print(f'  OK  {filepath}')
    else:
        failed.append(f'{filepath} ({r.status_code}: {r.text[:80]})')
        print(f'  FAIL {filepath}: {r.status_code}')

print(f'\nDone. {len(files_to_upload) - len(failed)}/{len(files_to_upload)} uploaded.')
if failed:
    print(f'Failed: {len(failed)}')
    for f in failed[:5]:
        print(f'  {f}')

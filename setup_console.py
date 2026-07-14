import requests
import re
import json
import time

username = 'etacar1nae'
token = 'de038107aa3d2f9b51cdddf364b786aa76db943f'
headers = {'Authorization': f'Token {token}'}

s = requests.Session()
s.headers.update(headers)

# Get CSRF token and create console via the web form
r = s.get(f'https://www.pythonanywhere.com/user/{username}/consoles/')
csrf = re.search(r'csrfmiddlewaretoken.*?value="([^"]+)"', r.text)
print('Login page status:', r.status_code)
print('CSRF found:', bool(csrf))

if csrf:
    csrf_token = csrf.group(1)
    r2 = s.post(
        f'https://www.pythonanywhere.com/user/{username}/consoles/',
        data={'executable': 'bash', 'csrfmiddlewaretoken': csrf_token},
        allow_redirects=True
    )
    print('Create console status:', r2.status_code)
    print('URL:', r2.url[:100])
    
    # Extract console ID from response
    console_id_match = re.search(r'/consoles/(\d+)/', r2.text)
    print('Console ID:', console_id_match.group(1) if console_id_match else 'not found')
    if console_id_match:
        console_id = console_id_match.group(1)
        
        # Now send commands via API
        time.sleep(2)
        commands = (
            'cd ~/InventarioTebana\n'
            'mkvirtualenv --python=python3.10 cerveceria\n'
        )
        api_headers = {'Authorization': f'Token {token}', 'Content-Type': 'application/json'}
        r3 = requests.post(
            f'https://www.pythonanywhere.com/api/v0/user/{username}/consoles/{console_id}/send_input/',
            headers=api_headers,
            json={'input': commands}
        )
        print('Send cmd status:', r3.status_code, r3.text[:200])
else:
    print("Couldn't find CSRF token")

# Check if page requires login
if 'login' in r.url.lower() or r.status_code == 302:
    print('Need to be logged in. Got redirected to login.')

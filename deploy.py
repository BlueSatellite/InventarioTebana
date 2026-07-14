import requests
username = 'etacar1nae'
token = 'de038107aa3d2f9b51cdddf364b786aa76db943f'
headers = {'Authorization': f'Token {token}'}

# Test upload - upload a simple file
files = {'content': ('test.txt', b'hello world')}
r = requests.post(
    f'https://www.pythonanywhere.com/api/v0/user/{username}/files/path/home/{username}/test.txt',
    headers=headers,
    files=files
)
print('Status:', r.status_code, r.text[:200])

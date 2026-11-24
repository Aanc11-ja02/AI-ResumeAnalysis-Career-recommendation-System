import os
from app import create_app

app = create_app('development')
with app.test_client() as client:
    resp = client.get('/')
    print('Status code:', resp.status_code)
    print('Response data (first 200 chars):', resp.data[:200])

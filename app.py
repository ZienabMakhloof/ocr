from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    print('Hello from main app')
    app.run(host='0.0.0.0', port=8000)
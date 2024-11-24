from flask import Flask
from app.config import Config
import os

def create_app():
    app = Flask(__name__)
    print('Hello from create app')
    app.config.from_object(Config)

    # إنشاء مجلد للملفات المرفوعة
    os.makedirs(os.path.join(app.instance_path, 'uploads'), exist_ok=True)

    from app.routes import main
    app.register_blueprint(main)

    return app
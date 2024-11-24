from flask import Blueprint, jsonify, request, current_app
import os
from werkzeug.utils import secure_filename
from app.utils import OCRModel

main = Blueprint('main', __name__)
ocr_model = OCRModel()

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/')
def index():
    return jsonify({"message": "Welcome to Allergen Detection API!"})

@main.route('/test')
def test():
    return jsonify({'status': 'OK', 'message': 'Test successful'})

@main.route('/api/analyze', methods=['POST'])
def process_image():
    print('Hello from process_image')
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    if 'allergies' not in request.form:
        return jsonify({"error": "No allergies provided"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # تحويل قائمة الحساسية إلى list
    user_allergies = request.form['allergies'].split(',')

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            result = ocr_model.process_image(filepath, user_allergies)
            # حذف الملف بعد المعالجة
            os.remove(filepath)
            return jsonify(result)
        except Exception as e:
            if os.path.exists(filepath):
                os.remove(filepath)
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "Invalid file type"}), 400
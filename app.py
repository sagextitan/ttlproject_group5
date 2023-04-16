from flask import Flask, jsonify, request
import os
import check_camera
import Capture_Image
import Train_Image
from Recognize import recognize_attendance

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Face Recognition Attendance System'

@app.route('/check_camera', methods=['GET'])
def check_camera_api():
    check_camera.check_camera()
    return 'Camera checked successfully'

@app.route('/capture_faces', methods=['POST'])
def capture_faces_api():
    student_id = request.form['student_id']
    Capture_Image.take_images(student_id)
    return 'Faces captured successfully for student ID: {}'.format(student_id)

@app.route('/train_images', methods=['GET'])
def train_images_api():
    Train_Image.train_images()
    return 'Images trained successfully'

@app.route('/recognize_attendance', methods=['POST'])
def recognize_attendance_api():
    student_id = request.form['student_id']
    recognize_attendance(student_id)
    return 'Attendance recognized successfully for student ID: {}'.format(student_id)

@app.route('/options', methods=['GET'])
def options_api():
    options = [
        {
            'id': 1,
            'name': 'Check Camera',
            'url': '/check_camera'
        },
        {
            'id': 2,
            'name': 'Capture Faces',
            'url': '/capture_faces'
        },
        {
            'id': 3,
            'name': 'Train Images',
            'url': '/train_images'
        },
        {
            'id': 4,
            'name': 'Recognize Attendance',
            'url': '/recognize_attendance'
        }
    ]
    return jsonify(options)

if __name__ == '__main__':
    app.run(debug=True, port=7000)

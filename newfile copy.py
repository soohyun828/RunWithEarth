from flask import Flask, request, jsonify
from yolov7_detect import YoloV7, count_lines
from similarity import judge_similarity
import base64
import os
import shutil

# Flask 애플리케이션 생성
app = Flask(__name__)

@app.route('/')
def index():
    return 'home. nothing.'


@app.route('/upload', methods=['POST'])
def upload_images():
    try:
        if 'image1' not in request.files or 'image2' not in request.files:
            return 'No images uploaded', 400

        image_file1 = request.files['image1']
        image_file2 = request.files['image2']

        if image_file1.filename == '' or image_file2.filename == '':
            print('there is no file')
            return 'No selected files', 400

        # 이미지 저장 경로
        save_path = 'uploaded_images'
        os.makedirs(save_path, exist_ok=True)

        # 파일 저장
        image_path1 = os.path.join(save_path, image_file1.filename)
        image_file1.save(image_path1)

        image_path2 = os.path.join(save_path, image_file2.filename)
        image_file2.save(image_path2)
        current_directory = os.getcwd()
        shutil.move(image_path1, current_directory)
        shutil.move(image_path2, current_directory)

        # YOLO 모델 수행
        encoded_image = YoloV7(image_path1)

        # 여기서부터는 필요한 작업을 수행하면 됩니다.
        txt_path = 'result/result/labels/' + image_file1.filename[:-4] + '.txt'
        line_count = count_lines(txt_path)
        similarity = judge_similarity(image_file1, image_file2)
        response_data = {
            'encoded_image': encoded_image,
            'line_number': line_count,
            'similarity': similarity
        }

        return jsonify(response_data), 200

    except Exception as e:
        print("error")
        return str(e), 500


if __name__ == '__main__':
    app.run("0.0.0.0",debug=True)


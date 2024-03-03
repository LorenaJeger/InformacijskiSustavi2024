from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

temp_storage = []

@app.route('/obaveza', methods=['POST'])
def add_todo():
    data = request.json
    temp_storage.append(data)
    return jsonify({'message': 'Obaveza dodana'}), 201

@app.route('/obaveza', methods=['GET'])
def get_todos():
    return jsonify(temp_storage)

@app.route('/obaveza/<rok>', methods=['GET'])
def get_obaveze_by_deadline(rok):
    obaveze_rok = [obaveza for obaveza in temp_storage if obaveza.get('rok') == rok]
    return jsonify(obaveze_rok)

@app.route('/obaveza/isteklo', methods=['GET'])
def get_istekle_obaveze():
    danas = datetime.now().strftime('%d-%m-%Y')
    istekle_obaveze = [obaveza for obaveza in temp_storage if obaveza.get('rok') and datetime.strptime(obaveza['rok'], '%d-%m-%Y') < datetime.strptime(danas, '%d-%m-%Y')]
    return jsonify(istekle_obaveze)

@app.route('/obaveza/nerijesene', methods=['GET'])
def get_nerijesene_obaveze():
    nerijesene_obaveze = [obaveza for obaveza in temp_storage if obaveza.get('gotovo', False) is False]
    return jsonify(nerijesene_obaveze)

if __name__ == '__main__':
    app.run(port=8080)

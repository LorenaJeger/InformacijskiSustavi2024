from flask import Flask, request, jsonify
from flask import abort
from datetime import datetime, timedelta

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

@app.route('/obaveza/<int:obaveza_id>', methods=['PUT'])
def zamijeni_obavezu(obaveza_id):
    novi_podaci = request.json
    for i, obaveza in enumerate(temp_storage):
        if obaveza.get('id') == obaveza_id:
            temp_storage[i] = novi_podaci
            return jsonify({'message': 'Obaveza zamijenjena'}), 200
    abort(404, description="Obaveza nije pronađena")

@app.route('/obaveza/<int:obaveza_id>', methods=['DELETE'])
def obrisi_obavezu(obaveza_id):
    for i, obaveza in enumerate(temp_storage):
        if obaveza.get('id') == obaveza_id:
            del temp_storage[i]
            return jsonify({'message': 'Obaveza obrisana'}), 200
    abort(404, description="Obaveza nije pronađena")

@app.route('/obaveza/<int:obaveza_id>', methods=['PATCH'])
def djelomicno_azuriraj_obavezu(obaveza_id):
    novi_podaci = request.json
    for i, obaveza in enumerate(temp_storage):
        if obaveza.get('id') == obaveza_id:
            obaveza.update(novi_podaci)
            return jsonify({'message': 'Obaveza djelomično ažurirana'}), 200
    abort(404, description="Obaveza nije pronađena")

#########
    
@app.route('/obaveza/azuriraj-rok/<int:obaveza_id>', methods=['PATCH'])
def djelomicno_azuriraj_rok_obaveze(obaveza_id):
    for i, obaveza in enumerate(temp_storage):
        if obaveza.get('id') == obaveza_id:
            stari_rok = datetime.strptime(obaveza['rok'], '%d-%m-%Y')
            novi_rok = stari_rok + timedelta(days=1)
            obaveza['rok'] = novi_rok.strftime('%d-%m-%Y')
            return jsonify({'message': 'Rok obaveze ažuriran'}), 200
    abort(404, description="Obaveza nije pronađena")

@app.route('/obaveza/obrisi-zavrsene', methods=['DELETE'])
def obrisi_zavrsene_obaveze():
    global temp_storage
    temp_storage = [obaveza for obaveza in temp_storage if not obaveza.get('zavrseno', False)]
    return jsonify({'message': 'Završene obaveze obrisane'}), 200

@app.route('/obaveza/obrisi-po-roku/<rok>', methods=['DELETE'])
def obrisi_obaveze_po_roku(rok):
    global temp_storage
    try:
        rok_datum = datetime.strptime(rok, '%d-%m-%Y')
    except ValueError:
        abort(400, description="Neispravan format datuma")

    temp_storage = [obaveza for obaveza in temp_storage if obaveza.get('rok') != rok_datum.strftime('%d-%m-%Y')]
    return jsonify({'message': f'Obaveze s rokom {rok} obrisane'}), 200


@app.route('/obaveza/azuriraj-status/<int:obaveza_id>', methods=['PATCH'])
def azuriraj_status_obaveze(obaveza_id):
    novi_podaci = request.json
    for i, obaveza in enumerate(temp_storage):
        if obaveza.get('id') == obaveza_id:
            if 'novi_status' in novi_podaci:
                obaveza['zavrseno'] = novi_podaci['novi_status']
                return jsonify({'message': 'Status obaveze ažuriran'}), 200
    abort(404, description="Obaveza nije pronađena")


@app.route('/obaveza/obrisi-prosli-mjesec', methods=['DELETE'])
def obrisi_obaveze_prosli_mjesec():
    global temp_storage
    danas = datetime.now()
    prvi_dan_proslog_mjeseca = (danas.replace(day=1) - timedelta(days=1)).replace(day=1)
    temp_storage = [obaveza for obaveza in temp_storage if obaveza.get('rok') and datetime.strptime(obaveza['rok'], '%d-%m-%Y') < prvi_dan_proslog_mjeseca]
    return jsonify({'message': 'Obrisane obaveze za prošli mjesec'}), 200

    

if __name__ == '__main__':
    app.run(port=8080)

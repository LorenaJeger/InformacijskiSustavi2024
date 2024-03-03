from flask import Flask,request,make_response,jsonify, render_template
from pony import orm
from datetime import datetime
from collections import defaultdict
from datetime import datetime
from itertools import groupby
import random


DB = orm.Database()

app = Flask(__name__)

class Obaveza(DB.Entity):
    id = orm.PrimaryKey(int, auto=True)
    naziv = orm.Required(str)
    kategorija = orm.Required(str)
    rok = orm.Required(datetime)
    detalji = orm.Required(str)

DB.bind(provider="sqlite", filename="database.sqlite", create_db=True)
DB.generate_mapping(create_tables=True)

def formatiraj_datum(datum):
    return datum.strftime('%d-%m-%Y') if datum else None

def add_obaveza(json_request):
    try:
        naziv = json_request["naziv"]
        kategorija = json_request["kategorija"]
        detalji = json_request["detalji"]

        try:
            rok = datetime.fromisoformat(json_request['rok'])
        except (ValueError, TypeError):
            rok = None

        with orm.db_session:
            Obaveza(naziv=naziv, kategorija=kategorija, detalji=detalji, rok=rok)
            response = {"response": "Success"}
            return response
    except Exception as e:
        return {"response": "Fail", "error": str(e)}

def get_obaveze():
    try:
        with orm.db_session:
            db_querry = orm.select(x for x in Obaveza)[:]
            results_list = []
            for r in db_querry:
                results_list.append(r.to_dict())
            response = {"response": "Success", "data": results_list}
            return response
    except Exception as e:
        return {"response": "Fail", "error": str(e)}

def get_obaveze_by_month():
    try:
        with orm.db_session:
            db_query = orm.select(x for x in Obaveza)[:]
            results_dict = defaultdict(int)

            for obaveza in db_query:
                if obaveza.rok:  
                    month = obaveza.rok.month
                    results_dict[month] += 1

            response = {"response": "Success", "data": dict(results_dict)}
            return response
    except Exception as e:
        return {"response": "Fail", "error": str(e)}

@orm.db_session
def get_obaveze_by_category():
    try:
        obaveze = orm.select(o for o in Obaveza).order_by(Obaveza.kategorija)

        grouped_by_category = groupby(obaveze, lambda o: o.kategorija)

        result = [{"kategorija": kategorija, "broj_obaveza": len(list(obaveze))} for kategorija, obaveze in grouped_by_category]

        response = {"response": "Success", "data": {"kategorije": result}}

        return response
    except Exception as e:
        error_response = {"response": "Error", "error_message": str(e)}
        return error_response
    

def get_obaveza_by_id(obaveza_id):
    try:
        with orm.db_session:
            result = Obaveza[obaveza_id].to_dict()
            result['rok'] = formatiraj_datum(result['rok'])
            response = {"response": "Success", "data": result}
            return response
    except Exception as e:
        return {"response": "Fail", "error": str(e)}
    
def patch_obaveza(obaveza_id, json_request):
    try:
        with orm.db_session:
            to_update = Obaveza[obaveza_id]
            if 'naziv' in json_request:
                to_update.naziv = json_request['naziv']
            if 'kategorija' in json_request:
                to_update.kategorija = json_request['kategorija']
            if 'rok' in json_request:
                rok = datetime.strptime(json_request['rok'], '%d-%m-%Y')
                to_update.rok = rok
            if 'detalji' in json_request:
                to_update.detalji = json_request['detalji']

            response = {"response": "Success"}
            return response
    except Exception as e:
        return {"response": "Fail", "error": str(e)}

def delete_obavezu(obaveza_id):
    try:
        with orm.db_session:
            to_delete = Obaveza[obaveza_id]
            to_delete.delete()
            response = {"response": "Success"}
            return response
    except Exception as e:
        return {"response": "Fail", "error": str(e)}

@app.route("/dodaj/obavezu", methods=["POST","GET"])
def dodaj_obavezu():
    if request.method == "POST":
            try:
                json_request = {}
                for key,value in request.form.items():
                    if value == "":
                        json_request[key] = None
                    else:
                        json_request[key] = value
            except Exception as e:
                response = {"response":str(e)}
                return make_response(jsonify(response),400)

            response = add_obaveza(json_request)

            if response["response"] == "Success":
                return make_response(render_template("dodaj.html"),200)
            return make_response(jsonify(response),400)
    else:
        return make_response(render_template("dodaj.html"),200)



@app.route("/vrati/obaveze", methods=["GET"])
def vrati_obaveze():
    if request.args and 'id' in request.args:
        obaveza_id = int(request.args.get("id"))
        response = get_obaveza_by_id(obaveza_id)
        if response["response"] == "Success":
            return make_response(render_template("vrati.html", data=response["data"]), 200)
        return make_response(jsonify(response), 400)
    response = get_obaveze()
    if response["response"] == "Success":
        return make_response(render_template("vrati.html", data=response["data"]), 200)
    return make_response(jsonify(response), 400)
    
@app.route("/vrati/obaveze/vizualizacija", methods=["GET"])
def vizualizacija():
    try:
        chart_data = get_obaveze_by_month()

        y_axis = list(chart_data.get("data", {}).values())
        x_axis = list(chart_data.get("data", {}).keys())

        response = {"response": "Success"}

        if response["response"] == "Success":
            return make_response(render_template("vizualizacija.html", y_axis=y_axis, x_axis=x_axis), 200)
        return make_response(jsonify(response), 400)

    except Exception as e:
        error_response = {"response": "Error", "error_message": str(e)}
        return make_response(jsonify(error_response), 500)

@app.route("/vrati/obaveze/kategorije", methods=["GET"])
def obaveze_po_kategorijama():
    try:
        chart_data_kategorije = get_obaveze_by_category()
        print(chr, chart_data_kategorije)

        kategorije = list(chart_data_kategorije.get("data", {}).values())
        print("kat",kategorije)
        return render_template("vizualizacija_kategorije.html", kategorije=kategorije)

    except Exception as e:
        error_response = {"response": "Error", "error_message": str(e)}
        return make_response(jsonify(error_response), 500)
    
@app.route("/obaveza/<int:obaveza_id>", methods=["DELETE"])
def obrisi_obavezu(obaveza_id):
    response = delete_obavezu(obaveza_id)
    if response["response"] == "Success":
            return make_response(jsonify(response), 200)
    return make_response(jsonify(response), 400)

@app.route("/obaveza/<int:obaveza_id>", methods=["PATCH"])
def izmjeni_obavezu():
    try:
        json_request = request.json
    except Exception as e:
        return make_response(jsonify(response), 400)
    if request.args:
        obaveza_id = int(request.args.get("id"))
        response = patch_obaveza(obaveza_id, json_request)
        if response["response"] == "Success":
            return make_response(jsonify(response), 200)
        return make_response(jsonify(response), 400)
    response = {"response": "Query string missing"}
    return make_response(jsonify(response), 400)

@app.route("/", methods=["GET"])
def home():
    return make_response(render_template("index.html"),200)
    
  
if __name__ == "__main__":
    app.run(port=8080)

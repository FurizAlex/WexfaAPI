from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route("/get-user/<user_id>")

def get_app(app_id):
	app_data = {"app_id": app_id,"name:": "example"}

	extra = request.args.get("extra")
	if extra: app_data["extra"] = extra; return jsonify(user_data), 200
	

def get_user(user_id):
	user_data = {"user_id": user_id,
	"name": "John Doe",
	"email": "john.doe@example.com"
	}

	extra = request.args.get("extra")
	if extra: user_data["extra"] = extra; return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])

def create_user(): data = request.get_json(); return jsonify(data), 201

if _name_ == "_main_":
	app.run(debug=True)

from flask import Blueprint, request, jsonify
from firestore_db import db
from datetime import datetime

services_bp = Blueprint("services", __name__)

# Create a new service
@services_bp.route("/services", methods=["POST"])
def create_service():
    data = request.json

    service = {
        "name": data["name"],
        "description": data.get("description", ""),
        "created_at": datetime.utcnow()
    }

    doc_ref = db.collection("services").add(service)

    return jsonify({
        "message": "Service created",
        "service_id": doc_ref[1].id
    }), 201


# Get all services
@services_bp.route("/services", methods=["GET"])
def get_services():
    services = []
    docs = db.collection("services").stream()

    for doc in docs:
        service = doc.to_dict()
        service["id"] = doc.id
        services.append(service)

    return jsonify(services), 200
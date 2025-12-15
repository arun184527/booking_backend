from flask import Blueprint, request, jsonify
from firestore_db import db
from datetime import datetime

bookings_bp = Blueprint("bookings", __name__)

@bookings_bp.route("/book", methods=["POST"])
def book_slot():
    data = request.json

    service_id = data.get("service_id")
    slot = data.get("slot")
    user_name = data.get("user_name")

    if not service_id or not slot or not user_name:
        return jsonify({
            "error": "service_id, slot, and user_name are required"
        }), 400

    # Check if slot already booked
    existing_booking = (
        db.collection("bookings")
        .where("service_id", "==", service_id)
        .where("slot", "==", slot)
        .limit(1)
        .stream()
    )

    if any(existing_booking):
        return jsonify({
            "error": "This slot is already booked"
        }), 409

    # Create booking
    db.collection("bookings").add({
        "service_id": service_id,
        "slot": slot,
        "user_name": user_name,
        "timestamp": datetime.utcnow()
    })

    return jsonify({
        "message": "Slot booked successfully"
    }), 201
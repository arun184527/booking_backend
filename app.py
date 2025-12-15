from flask import Flask
from routes.services import services_bp
from routes.bookings import bookings_bp

app = Flask(__name__)

@app.route("/")
def health():
    return {"message": "Booking Backend is running"}

app.register_blueprint(services_bp)
app.register_blueprint(bookings_bp)

if __name__ == "__main__":
    app.run(debug=True)
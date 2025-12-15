I built a backend service booking system using Flask as the server framework and Google Firestore as the database.
The goal was to manage services with time slots and allow users to book a slot while preventing duplicate bookings.

The backend exposes REST APIs. A GET endpoint retrieves available services and their slots from Firestore. A POST booking endpoint accepts a service ID and slot, validates the input, and then checks the bookings collection in Firestore to ensure that the selected slot is not already booked.

If the slot already exists in the bookings collection, the request is rejected. Otherwise, the booking is stored with structured data including service ID, slot, user name, and timestamp. This guarantees data consistency without relying on a frontend.

I designed the system with clean route separation, backend-first validation, and Firestore reads and writes optimized for simplicity. The project focuses on business logic and database integrity rather than UI, which aligns with real-world backend system design

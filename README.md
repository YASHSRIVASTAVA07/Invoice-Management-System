# Invoice Management System

A simple web application built with **Flask**, **SQLite**, **HTML**, and **CSS** for managing clients and invoices.

## Features

- Add new clients (name, company, email)
- Create invoices linked to clients with item descriptions and total amount
- View clients and invoice details
- Clean and minimal user interface

## Technologies Used

- Python 3.x
- Flask (web framework)
- Flask-SQLAlchemy (ORM for SQLite database)
- SQLite (database)
- HTML & CSS (frontend templates and styling)

## Project Structure

invoice_app/
├── app.py # Main Flask application
├── templates/
│ ├── base.html # Base HTML template layout
│ ├── clients.html # List clients page
│ ├── client_form.html # Add client form
│ ├── invoice_form.html # Create invoice form
│ └── invoice.html # View invoice details
└── static/
└── style.css # CSS stylesheet

 

## Installation & Setup

1. Clone this repository:
git clone https://github.com/your-username/invoice-management-system.git
cd invoice-management-system

 

2. (Optional) Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate # On Windows use: venv\Scripts\activate

 

3. Install required Python packages:
pip install Flask Flask-SQLAlchemy

 

4. Run the Flask app:
python app.py

 

5. Open your browser at:
http://127.0.0.1:5000/

 

## Usage

- Go to **Clients** to view and add new clients.
- Create invoices for clients with descriptions and total amounts.
- View invoice details per client.

## Future Enhancements

- Edit and delete clients and invoices functionality
- Export invoices as PDF
- Email invoices to clients
- Payment integration (e.g., Stripe)
- Improved UI and responsive design

## License

This project is licensed under the MIT License.

---

Feel free to open issues or submit pull requests!

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///invoice.db'

db = SQLAlchemy(app)

# Models
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    company = db.Column(db.String(120))
    email = db.Column(db.String(120))


class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    items = db.Column(db.String(500))
    total = db.Column(db.Float)


# Routes
@app.route('/')
def index():
    return redirect(url_for('clients'))

@app.route('/clients')
def clients():
    clients = Client.query.all()
    return render_template('clients.html', clients=clients)

@app.route('/add_client', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        name = request.form['name']
        company = request.form['company']
        email = request.form['email']
        client = Client(name=name, company=company, email=email)
        db.session.add(client)
        db.session.commit()
        return redirect(url_for('clients'))
    return render_template('client_form.html')

@app.route('/add_invoice/<int:client_id>', methods=['GET', 'POST'])
def add_invoice(client_id):
    client = Client.query.get_or_404(client_id)
    if request.method == 'POST':
        items = request.form['items']
        total = float(request.form['total'])
        invoice = Invoice(client_id=client_id, items=items, total=total)
        db.session.add(invoice)
        db.session.commit()
        return redirect(url_for('invoice', invoice_id=invoice.id))
    return render_template('invoice_form.html', client=client)

@app.route('/invoice/<int:invoice_id>')
def invoice(invoice_id):
    invoice = Invoice.query.get_or_404(invoice_id)
    client = Client.query.get_or_404(invoice.client_id)
    return render_template('invoice.html', invoice=invoice, client=client)

# Init
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

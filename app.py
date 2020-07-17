from flask import Flask, render_template, request, jsonify, make_response
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/customers', methods=['GET'])
def show_customer():
    customers = [{
        'id': 100,
        'fname': 'Max',
        'lname': 'lind',
        'street': '123 Fake Street',
        'city': 'San Antonio',
        'state': 'Texas',
        'zip': '78259',
        'email': 'maxlind@yahoo.com',
        'phone': '(432) 786-9087'
        },
        {
        'id': 101,
        'fname': 'Max',
        'lname': 'lind',
        'street': '123 Fake Street',
        'city': 'San Antonio',
        'state': 'Texas',
        'zip': '78259',
        'email': 'maxlind@yahoo.com',
        'phone': '(432) 786-9087'
        },
        {
        'id': 102,
        'fname': 'Max',
        'lname': 'lind',
        'street': '123 Fake Street',
        'city': 'San Antonio',
        'state': 'Texas',
        'zip': '78259',
        'email': 'maxlind@yahoo.com',
        'phone': '(432) 786-9087'
        }
    ]

    return render_template('customers.html', customers=customers, title='Customers')
    

@app.route('/customers/add-customer')
def add_customer():
    return render_template('addcustomer.html', title='Add Customer')


@app.route('/distributors')
def show_distributor():

    distributors = [{
        'id': 200,
        'name': 'Record Warehouse',
        'street': '456 Dist Street',
        'city': 'Los Angeles',
        'state': 'California',
        'zip': '78259',
        'phone': '(888) 703-6517'
        },
        {
        'id': 201,
        'name': 'Record Warehouse',
        'street': '456 Dist Street',
        'city': 'Los Angeles',
        'state': 'California',
        'zip': '78259',
        'phone': '(888) 703-6517'
        },
        {
        'id': 202,
        'name': 'Record Warehouse',
        'street': '456 Dist Street',
        'city': 'Los Angeles',
        'state': 'California',
        'zip': '78259',
        'phone': '(888) 703-6517'
        },
    ]
    return render_template('distributors.html', distributors=distributors, title='Distributors')

@app.route('/distributors/add-distributor')
def add_distributor():

    return render_template('addistributor.html', title='Add Distributor')


<<<<<<< HEAD
=======

>>>>>>> c4c471b7bfa45722968eef62a4e8d6c6479c33d2

@app.route('/records')
def show_records():
    records = [{
        'id': 200,
        'price': '20',
        'quantity': '12',
        'year': '1985',
        'artist': 'John Smith',
        'name': "John's Best"
        },
        {
        'id': 201,
        'price': '40',
        'quantity': '8',
        'year': '1958',
        'artist': 'George JSON',
        'name': 'String Theory'
        },
        {
        'id': 201,
        'price': '28',
        'quantity': '26',
        'year': '2001',
        'artist': 'Foo',
        'name': 'Bar'
        },
    ]
    return render_template('records.html', records = records, title='Records')

@app.route('/records/add-record')
def add_record():

    return render_template('addrecord.html')

from flask import Flask, render_template, request, send_file
import datetime 
import database


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('login.html')


@app.route('/check_login', methods=["post"])
def check_login():
    username = request.form['username']
    password = request.form['password']

    if username == "root" and password == "":
        return render_template('home.html')

    return render_template('login.html', error="Retype correct login credentials")



@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/add_product')
def add_product():
    return render_template('add_product.html')


@app.route('/add_product_data', methods=["post"])
def add_product_data():
    p_name = request.form['product_name']
    p_quantity = request.form['quantity']
    p_inventory = request.form['inventory']
    p_cat = request.form['p_cat']
    p_sub_cat = request.form['p_sub_cat']
    entry_datetime = datetime.datetime.now()

    database.insert_new_product(p_name.lower(),p_quantity.lower(),int(p_inventory),p_cat.lower(),p_sub_cat.lower(),entry_datetime)
    return render_template('home.html', message="New Product is added in the system!")
    

@app.route('/view_data')
def view_data():
    data = database.show_all_data() 
    return render_template('view_data.html', data=data)


@app.route('/delete/<int:id>')
def delete(id):
    database.delete_product(id)
    return render_template("view_data.html")



@app.route('/edit/<int:id>')
def edit(id):
    return render_template("edit.html", id=id)


@app.route('/edit_data', methods=["post"])
def edit_data():
    new_inventory = request.form['new_inventory']
    operation = request.form['rd_btn_opr']
    id = request.form["id"]

    database.update_inventory(id, new_inventory, operation)
    return render_template('home.html', message="Record was updated!")

@app.route('/view_filtered')
def view_filtered():
    data = database.list_all_cat()
    data1 = database.list_all_sub_cat()
    return render_template('view_f.html',data=data, data1=data1)

@app.route('/view_filtered_data', methods=["post"])
def view_filtered_data():
    cat = request.form['category']
    sub_cat = request.form['sub_category']
    data = database.view_filtered_data(cat, sub_cat)
    return render_template('view_data.html', data=data)



if __name__ == "__main__":
    app.run()
import sqlite3 




def create_data_table():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        create table data (ID INTEGER PRIMARY KEY AUTOINCREMENT, product_name varchar2, quantity varchar, inventory number,product_cat varchar2, product_sub_cat varchar2, entry_dt varchar2);       
        """
    )
    conn.commit()
    cursor.close()
    conn.close()



def insert_new_product(product_name, quantity, inventory, product_cat, product_sub_cat, entry_dt):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""
        insert into data (product_name,quantity,inventory,product_cat,product_sub_cat,entry_dt) values ('{product_name.capitalize()}','{quantity.capitalize()}',{inventory},'{product_cat.capitalize()}','{product_sub_cat.capitalize()}','{entry_dt}');    
        """
    )
    conn.commit()
    cursor.close()
    conn.close()




def show_all_data():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        f"""
         select * from data
        """

    )
    data = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return data


def update_inventory(id, new_inventory, opr):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    if opr == 'add':
        cursor.execute(
            f"""
                update data set inventory=inventory+{new_inventory} where ID={id}
            """

        )
    else:
        cursor.execute(
            f"""
                update data set inventory=inventory-{new_inventory} where ID={id}
            """

        )

    conn.commit()
    cursor.close()
    conn.close()


def delete_product(id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""
             delete from data where ID={id}  
        """

    )
    conn.commit()
    cursor.close()
    conn.close()


def list_all_cat():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        f"""
         select DISTINCT product_cat from data 
        """

    )
    data = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return data


def list_all_sub_cat():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        f"""
         select DISTINCT product_sub_cat from data 
        """

    )
    data = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return data

def view_filtered_data(cat, sub_cat):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    if sub_cat == 'all':
        cursor.execute(
            f"""
            select * from data where product_cat='{cat}'
            """

        )
    else:
        cursor.execute(
            f"""
            select * from data where product_cat='{cat}' and product_sub_cat='{sub_cat}';
            """

        )
    data = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return data

    


import sqlite3


from config import DATABASE_FILE

def connect_db():
    conn = sqlite3.connect(DATABASE_FILE)
    return conn


# مدیریت کاربران
# اقزودن کاربر جدیبد
def add_user(username, password, user_type, first_name, last_name, email, phone):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Users (username, password, user_type, first_name, last_name, email, phone)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (username, password, user_type, first_name, last_name, email, phone))
    conn.commit()
    conn.close()


# دریافت تمام کاربران
def get_all_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    conn.close()
    return users


# دریافت اطلاعات یک کاربر
def get_user_by_username(username):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    return user


# مدیریت یفر ها
# افزودن سفر
def add_trip(departure, destination, departure_date, price, status, bus_id, driver_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Trips (departure, destination, departure_date, price, status, bus_id, driver_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (departure, destination, departure_date, price, status, bus_id, driver_id))
    conn.commit()
    conn.close()


# دریافت تمام سفر ها
def get_all_trips():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Trips')
    trips = cursor.fetchall()
    conn.close()
    return trips


# درسافت سفرخاص براساس ایدی کاربر
def get_trip_by_id(trip_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Trips WHERE trip_id = ?', (trip_id,))
    trip = cursor.fetchone()
    conn.close()
    return trip


# مدیدیت اتوبوس ها
# اقزودن اتوبوس
def add_bus(bus_number, seat_count, model, manufacturer, year, license_plate):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Buses (bus_number, seat_count, model, manufacturer, year, license_plate)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (bus_number, seat_count, model, manufacturer, year, license_plate))
    conn.commit()
    conn.close()


# دریافت تمام اتوبوس ها
def get_all_buses():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Buses')
    buses = cursor.fetchall()
    conn.close()
    return buses


# مدیریت رانندگان
# اقزودن راننده
def add_driver(name, license_number, birth_date, address, hiring_date, experience_years):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Drivers (name, license_number, birth_date, address, hiring_date, experience_years)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, license_number, birth_date, address, hiring_date, experience_years))
    conn.commit()
    conn.close()


# درطافت تمام رانندگان
def get_all_drivers():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Drivers')
    drivers = cursor.fetchall()
    conn.close()
    return drivers


# مدیریت رزرو بلیط اقزودن بلیط جدید
def add_reservation(user_id, trip_id, seat_number, payment_method, reservation_code, notes, modified_by=None):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Reservations (user_id, trip_id, seat_number, payment_method, reservation_code, notes, modified_by)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (user_id, trip_id, seat_number, payment_method, reservation_code, notes, modified_by))
    conn.commit()
    conn.close()


def get_all_reservations():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Reservations')
    reservations = cursor.fetchall()
    conn.close()
    return reservations


# دریافت رزرو خاص بر اساس ticket_id

def get_reservation_by_ticket(ticket_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Reservations WHERE ticket_id = ?', (ticket_id,))
    reservation = cursor.fetchone()
    conn.close()
    return reservation


# ویرایش رزرو بلیط

def update_reservation(ticket_id, seat_number, payment_method, notes, modified_by):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Reservations
        SET seat_number = ?, payment_method = ?, notes = ?, modified_by = ?, status = 'edited'
        WHERE ticket_id = ?
    ''', (seat_number, payment_method, notes, modified_by, ticket_id))
    conn.commit()
    conn.close()


# حذف رزرو بلیط

def delete_reservation(ticket_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Reservations WHERE ticket_id = ?', (ticket_id,))
    conn.commit()
    conn.close()


7.  # مدیریت# تراکنش‌ها (Transactions)


# افزودن #تراکنش

def add_transaction(ticket_id, amount, payment_method, transaction_code, status, payment_gateway, remarks):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Transactions (ticket_id, amount, payment_method, transaction_code, status, payment_gateway, remarks)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (ticket_id, amount, payment_method, transaction_code, status, payment_gateway, remarks))
    conn.commit()
    conn.close()


# دریافت تراکنش خاص بر اساس transaction_id

def get_transaction_by_id(transaction_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Transactions WHERE transaction_id = ?', (transaction_id,))
    transaction = cursor.fetchone()
    conn.close()
    return transaction


8.  # گزارش‌ها و آمار


# تعداد کل سفرها

def get_total_trips():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Trips')
    total_trips = cursor.fetchone()[0]
    conn.close()
    return total_trips


# تعداد #سفرهای# لغو شده

def get_cancelled_trips():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Trips WHERE status = "cancelled"')
    cancelled_trips = cursor.fetchone()[0]
    conn.close()
    return cancelled_trips


# میزان# درآمد (جمع مبلغ سفرها)#

def get_total_income():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT SUM(price) FROM Trips WHERE status = "active"')
    total_income = cursor.fetchone()[0]
    conn.close()
    return total_income


def login(username, password):
    conn = connect_db()
    cursor = conn.cursor()

    # جستجو در پایگاه داده برای یافتن کاربر با نام کاربری وارد شده
    cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    #print(user)

    # اگر کاربر وجود داشته باشد و پسورد صحیح باشد
    if user and user[2] == password:  # user[2] مربوط به پسورد است
        return user  # کاربر را بر می‌گرداند
    else:
        return None  # اگر نام کاربری یا پسورد اشتباه باشد

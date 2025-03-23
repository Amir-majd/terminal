import sqlite3


# اتصال به پایگاه داده
def connect_db():
    conn = sqlite3.connect('your_database.db')
    return conn


# ورود به سیستم
def login(username, password):
    conn = connect_db()
    cursor = conn.cursor()

    # جستجو در پایگاه داده برای یافتن کاربر با نام کاربری وارد شده
    cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    # اگر کاربر وجود داشته باشد و پسورد صحیح باشد
    if user and user[2] == password:  # user[2] مربوط به پسورد است
        return user  # کاربر را بر می‌گرداند
    else:
        return None  # اگر نام کاربری یا پسورد اشتباه باشد


# ثبت کاربر جدید
def register_user(username, password, user_type, first_name, last_name):
    conn = connect_db()
    cursor = conn.cursor()

    # بررسی وجود کاربر با همان نام کاربری
    cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        print("نام کاربری قبلاً ثبت شده است.")
        conn.close()
        return False
    else:
        # اضافه کردن کاربر جدید به پایگاه داده
        cursor.execute("""
            INSERT INTO Users (username, password, user_type, first_name, last_name)
            VALUES (?, ?, ?, ?, ?)
        """, (username, password, user_type, first_name, last_name))

        conn.commit()
        conn.close()
        print("کاربر جدید با موفقیت ثبت شد!")
        return True


# منوی اصلی و انتخاب نوع کاربر
def user_menu():
    print("به سیستم خوش آمدید!")
    print("1. ورود به عنوان مدیر")
    print("2. ورود به عنوان کاربر عادی")
    print("3. ثبت نام کاربر جدید")
    choice = input("لطفاً یکی از گزینه‌ها را انتخاب کنید: ")

    if choice == '1':
        username = input("نام کاربری مدیر را وارد کنید: ")
        password = input("رمز عبور مدیر را وارد کنید: ")
        user = login(username, password)
        if user:
            print("ورود موفقیت‌آمیز! خوش آمدید, مدیر.")
        else:
            print("نام کاربری یا رمز عبور اشتباه است.")

    elif choice == '2':
        username = input("نام کاربری خود را وارد کنید: ")
        password = input("رمز عبور خود را وارد کنید: ")
        user = login(username, password)
        if user:
            print(f"ورود موفقیت‌آمیز! خوش آمدید, {user[4]} {user[5]}.")
        else:
            print("نام کاربری یا رمز عبور اشتباه است.")

    elif choice == '3':
        print("فرم ثبت نام کاربر جدید:")
        username = input("نام کاربری جدید را وارد کنید: ")
        password = input("رمز عبور جدید را وارد کنید: ")
        user_type = input("نوع کاربر (admin/user): ")
        first_name = input("نام: ")
        last_name = input("نام خانوادگی: ")
        if register_user(username, password, user_type, first_name, last_name):
            print("ثبت نام با موفقیت انجام شد.")
        else:
            print("ثبت نام ناموفق بود.")

    else:
        print("انتخاب نامعتبر است. لطفاً دوباره تلاش کنید.")


#if __name__ == "__main__":
 #   user_menu()
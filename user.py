from database import login

from database import connect_db,add_user


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
            user_dashboard()
        else:
            print("نام کاربری یا رمز عبور اشتباه است.")

    elif choice == '3':
        print("فرم ثبت نام کاربر جدید:")
        username = input("نام کاربری جدید را وارد کنید: ")
        password = input("رمز عبور جدید را وارد کنید: ")
        user_type = input("نوع کاربر (admin/user): ")
        first_name = input("نام: ")
        last_name = input("نام خانوادگی: ")
        email=input("ایمیل: ")
        phone=input("شماره تلفن: ")
        if add_user(username, password, user_type, first_name, last_name,email,phone):
            print("ثبت نام با موفقیت انجام شد.")
        else:
            print("ثبت نام ناموفق بود.")

    else:
        print("انتخاب نامعتبر است. لطفاً دوباره تلاش کنید.")







        #user dashborrd


#from reservation import add_reservation, get_all_trips, add_reservation, update_reservation, delete_reservation



# منوی جدید کاربر عادی بعد از ورود موفق
def user_dashboard():
    while True:
        print("\nمنوی کاربر عادی:")
        print("1. عملیات رزرو جدید")
        print("2. ویرایش بلیط")
        print("3. حذف بلیط")
        print("4. نمایش همه سفرهای امروز")
        print("5. خروج")
        choice = input("لطفاً یکی از گزینه‌ها را انتخاب کنید: ")

        # if choice == '1':
        #     input=add_reservation()
        # elif choice == '2':
        #     update_reservation()
        # elif choice == '3':
        #     delete_ticket()
        # elif choice == '4':
        #     trips = get_all_trips()
        #     print("\nسفرهای امروز:")
        #     for trip in trips:
        #         print(f"مبدا: {trip['origin']}, مقصد: {trip['destination']}, تاریخ: {trip['date']}")
        # elif choice == '5':
        #     print("خروج از سیستم...")
        #     break
        # else:
        #     print("انتخاب نامعتبر است. لطفاً دوباره تلاش کنید.")


#if __name__ == "__main__":
 #   user_menu()
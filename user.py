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
            admin_menu()
        else:
            print("نام کاربری یا رمز عبور اشتباه است.")

    elif choice == '2':
        username = input("نام کاربری خود را وارد کنید: ")
        password = input("رمز عبور خود را وارد کنید: ")
        user = login(username, password)
        if user:
            print(f"ورود موفقیت‌آمیز! خوش آمدید, {user[4]} {user[5]}.")
            user_dashboard(user)
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


from reservation import add_reservation, add_reservation, new_reservation,delete_ticket
from reservation import edit_reservation

#from reservation import update get all trips and delete trips


# منوی جدید کاربر عادی بعد از ورود موفق
def user_dashboard(user):
    while True:
        print("\nمنوی کاربر عادی:")
        print("1. عملیات رزرو جدید")
        print("2. ویرایش بلیط")
        print("3. حذف بلیط")
        print("4. نمایش همه سفرهای امروز")
        print("5. خروج")
        choice = input("لطفاً یکی از گزینه‌ها را انتخاب کنید: ")


        if choice == '1':
             new_reservation(user)
        elif choice == '2':
             edit_reservation(user)
        elif choice == '3':
            delete_ticket(user)

        elif choice == '5':
            print("خروج از منوی رزرو کاربر")
            break

        else:
            print("گزینه نامعتبر است")

from database import login
# from transaction import get_income  # فرض می‌کنیم این تابع میزان درآمد رو می‌گیره
# from travel import get_trips_today, get_all_trips, add_trip  # فرضی برای گرفتن سفرهای امروز و افزودن سفر
# from driver_bus import get_drivers, get_buses, add_driver  # فرضی برای گرفتن اطلاعات رانندگان و اتوبوس‌ها
# from report import generate_reports  # فرضی برای گزارش‌گیری


def admin_menu():
    while True:
        print("\nمنوی مدیریت:")
        print("1. تراکنش‌ها")
        print("2. اطلاعات سفرها")
        print("3. اطلاعات رانندگان و اتوبوس‌ها")
        print("4. گزارش‌گیری")
        print("5. خروج")

        choice = input("لطفاً یکی از گزینه‌ها را انتخاب کنید: ")

        if choice == '1':
            transaction_menu()

        elif choice == '2':
            travel_menu()

        elif choice == '3':
            driver_bus_menu()

        elif choice == '4':
            pass
            #generate_reports()

        elif choice == '5':
            print("خروج از منوی مدیریت")
            break

        else:
            print("گزینه نامعتبر است. لطفاً دوباره تلاش کنید.")

from reservation import show_revenue_by_date
# منوی تراکنش‌ها
def transaction_menu():
    print("\nمنوی تراکنش‌ها:")
    print("1. میزان درآمد")
    print("2. بازگشت به منوی اصلی")
    choice = input("لطفاً یکی از گزینه‌ها را انتخاب کنید: ")

    if choice == '1':
        show_revenue_by_date()
        #income = get_income()
        #print(f"میزان درآمد: {income} تومان")
    elif choice == '2':
        pass

    else:
        print("گزینه نامعتبر است.")
from reservation import show_completed_trips
from reservation import add_trip
from reservation import show_trips_by_date
# منوی اطلاعات سفرها
def travel_menu():
    while True:
        print("\nمنوی اطلاعات سفرها:")
        print("1. سفرهای انجام شده")
        print("2. لیست کامل سفرهای امروز")
        print("3. افزودن سفر")
        print("4. بازگشت به منوی اصلی")

        choice = input("لطفاً یکی از گزینه‌ها را انتخاب کنید: ")

        if choice == '1':
            show_completed_trips()
            #trips = get_all_trips()

            #for trip in trips:
                #print(trip)

        elif choice == '2':
            #show_trips_by_date()
            trips_today = show_trips_by_date()
            for trip in trips_today:
                print(trip)

        elif choice == '3':
            add_trip()
            #add_trip()

        elif choice == '4':
            break
        else:
            print("گزینه نامعتبر است.")
from reservation import show_all_buses
from reservation import get_all_drivers
from  reservation import add_new_driver
# منوی اطلاعات رانندگان و اتوبوس‌ها
def driver_bus_menu():
    while True:
        print("\nمنوی اطلاعات رانندگان و اتوبوس‌ها:")
        print("1. اطلاعات رانندگان")
        print("2. اطلاعات اتوبوس‌ها")
        print("3. افزودن راننده جدید")
        print("4. بازگشت به منوی اصلی")

        choice = input("لطفاً یکی از گزینه‌ها را انتخاب کنید: ")

        if choice == '1':
            #get_all_drivers()
             drivers = get_all_drivers()
             for driver in drivers:
                 print(driver)

        elif choice == '2':
            show_all_buses()
            # buses = get_buses()
            # for bus in buses:
            #     print(bus)

        elif choice == '3':
            add_new_driver()
            #add_driver()

        elif choice == '4':
            break
        else:
            print("گزینه نامعتبر است.")



#if __name__ == "__main__":
 #   user_menu()
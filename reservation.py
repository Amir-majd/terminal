from database import add_reservation, add_driver
from database import get_trips_by_destination_and_date

#def new_reservation(user):

from database import add_reservation, get_reserved_seats, get_trip_by_date
from datetime import datetime


def display_seat_plan(bus_type, reserved_seats=None):
    if bus_type == "normal":
        seats = 30
    else:  # VIP bus
        seats = 35

    print("\nچیدمان صندلی‌ها:")
    for i in range(0, seats, 5):
        row = ""
        for j in range(5):
            seat_number = i + j + 1
            if seat_number <= seats:
                row += f"[{seat_number if seat_number not in reserved_seats else 'X'}] "
        print(row)


def new_reservation(user):
    print("\nانتخاب مقصد:")
    destination = input("مقصد سفر را وارد کنید: ")  # مقصد را از کاربر دریافت می‌کنیم
    trip_date = input("تاریخ سفر را وارد کنید (فرمت: YYYY-MM-DD): ")

    try:
        trip_date = datetime.strptime(trip_date, "%Y-%m-%d").date()
        print(trip_date)
    except ValueError:
        print("تاریخ وارد شده صحیح نیست.")
        return

    trip=show_trips(destination, trip_date)
    if trip:
        bus_type=trip[-1]
        #----------------------------------------
        # print("نوع اتوبوس را انتخاب کنید:")
        # print("1. عادی (30 صندلی)")
        # print("2. VIP (35 صندلی)")
        # bus_choice = input("انتخاب شما (1/2): ")
        #
        # bus_type = "normal" if bus_choice == '1' else "VIP"
        #bus_type=reservation.py
        # دریافت صندلی‌های رزرو شده از پایگاه داده
        reserved_seats = get_reserved_seats(trip[0])
        
        display_seat_plan(bus_type,reserved_seats)

        seat_number = int(input("شماره صندلی مورد نظر خود را وارد کنید: "))
        if seat_number in reserved_seats:
            print("این صندلی قبلاً رزرو شده است. لطفاً شماره دیگری وارد کنید.")
            return

        payment_method = input("نحوه پرداخت (آنلاین/نقدی): ").lower()

        confirm = input(
            f"آیا می‌خواهید بلیط برای سفر به {destination} در تاریخ {trip_date} با شماره صندلی {seat_number} رزرو کنید؟ (بله/خیر): ").lower()

        if confirm == 'بله':
            try:
                add_reservation(user[0], trip[0], seat_number, payment_method, "")
                print("رزرو شما با موفقیت انجام شد.")
            except Exception as e:
                print("خطا در ثبت رزرو.",str(e))
        else:
            print("رزرو لغو شد.")
    else :
        print("هیچ سفری وجود ندارد برای این تاریخ")

def show_trips(destination, trip_date):
        # گرفتن سفرها از پایگاه داده با توجه به مقصد و تاریخ
        trips = get_trips_by_destination_and_date(destination, trip_date)

        if not trips:
            print("سفری برای این مقصد و تاریخ پیدا نشد.")
            return

        print("\nلیست سفرهای موجود:")
        for trip in trips:
            print(f"آیدی سفر: {trip[0]} - مقصد: {trip[2]} - تاریخ سفر: {trip[3]} - نوع اتوبوس : {trip[-1]}")

        # درخواست از کاربر برای انتخاب آیدی سفر
        trip_id = int(input("\nآیدی سفر مورد نظر خود را وارد کنید: "))

        # بررسی اینکه آیا آیدی وارد شده معتبر است یا خیر
        if any(trip[0] == trip_id for trip in trips):
            print(f"شما سفر با آیدی {trip_id} را انتخاب کردید.")
            return trip
        else:
            print("آیدی سفر وارد شده صحیح نیست.")
            return None


from database import  get_user_reservations
from database import delete_reservation1


def delete_ticket(user):
    # گرفتن تمام رزروهای کاربر از پایگاه داده
    reservations = get_user_reservations(user[0])  # فرض بر این است که user[0] شناسه کاربر است

    if not reservations:
        print("شما هیچ بلیطی رزرو نکرده‌اید.")
        return

    print("\nلیست بلیط‌های شما:")
    for reservation in reservations:
        print(
            f"آیدی رزرو: {reservation[0]} - مقصد: {reservation[1]} - تاریخ سفر: {reservation[2]} - نوع اتوبوس: {reservation[3]} - شماره صندلی: {reservation[4]}")

    # انتخاب بلیط برای حذف
    reservation_id = input("\nآیدی بلیطی که می‌خواهید حذف کنید را وارد کنید: ")

    # بررسی اینکه آیا آیدی وارد شده معتبر است یا خیر
    if any(reservation[0] == int(reservation_id) for reservation in reservations):
        # حذف بلیط از پایگاه داده
        try:
            delete_reservation1(reservation_id)
            print("بلیط با موفقیت حذف شد.")
        except Exception as e:
            print("خطا در حذف بلیط.", str(e))
    else:
        print("آیدی بلیط وارد شده معتبر نیست.")

#edit ticket*************

from database import get_reservation_by_trip_id, update_seat_in_reservation, get_reserved_seats, get_trip_by_id  #display_seat_plan


def edit_reservation(user):
    # دریافت آیدی سفر از کاربر
    trip_id = int(input("آیدی سفر خود را وارد کنید: "))

    # دریافت سفر از پایگاه داده با آیدی سفر
    trip = get_trip_by_id(trip_id)

    if not trip:
        print("سفری با این آیدی پیدا نشد.")
        return

    # نمایش اطلاعات سفر به کاربر
    print(f"شما سفر به {trip[2]}، تاریخ سفر: {trip[3]} را انتخاب کرده‌اید.")

    # گرفتن رزروهای مربوط به این سفر از پایگاه داده
    reservations = get_reservation_by_trip_id(trip_id)

    if not reservations:
        print("هیچ رزروی برای این سفر وجود ندارد.")
        return

    # نمایش لیست رزروهای کاربر
    print("\nرزروهای شما برای این سفر:")
    for reservation in reservations:
        if reservation[1] == user[0]:  # فقط رزروهای متعلق به کاربر فعلی را نمایش می‌دهیم
            print(f"آیدی رزرو: {reservation[0]} - شماره صندلی: {reservation[6]}")

    # دریافت آیدی رزرو از کاربر
    reservation_id = int(input("آیدی رزرو خود را وارد کنید: "))

    # پیدا کردن رزرو مربوطه
    reservation = next((r for r in reservations if r[0] == reservation_id), None)

    if not reservation:
        print("رزوری با این آیدی برای شما یافت نشد.")
        return

    if reservation[5] == 'cancelled':  # بررسی وضعیت رزرو
        print("این رزرو قبلاً لغو شده است.")
        return

    print(f"رزرو فعلی شما: شماره صندلی {reservation[6]}")

    # دریافت صندلی‌های رزرو شده از پایگاه داده
    reserved_seats = get_reserved_seats(trip_id)

    # نمایش چیدمان صندلی‌ها
    bus_type = trip[-1]  # نوع اتوبوس از اطلاعات سفر
    display_seat_plan(bus_type, reserved_seats)

    # دریافت شماره صندلی جدید از کاربر
    new_seat_number = int(input("شماره صندلی جدید خود را وارد کنید: "))

    if new_seat_number in reserved_seats:
        print("این صندلی قبلاً رزرو شده است. لطفاً شماره دیگری وارد کنید.")
        return

    # تایید نهایی از کاربر
    confirm = input(
        f"آیا می‌خواهید شماره صندلی خود را از {reservation[6]} به {new_seat_number} تغییر دهید؟ (بله/خیر): ").lower()

    if confirm == 'بله':
        try:
            # بروزرسانی شماره صندلی در پایگاه داده
            update_seat_in_reservation(reservation[0], new_seat_number)
            print("تغییرات با موفقیت اعمال شد.")
        except Exception as e:
            print(f"خطا در ویرایش رزرو: {str(e)}")
    else:
        print("ویرایش رزرو لغو شد.")


#--------new functions for admin menu------

from database import get_trips_by_date
#تایع لیست سفر های امروز
def show_trips_by_date():
    while True:  # حلقه برای انجام عملیات مکرر
        date = input("تاریخ مورد نظر را وارد کنید (yyyy-mm-dd): ")

        trips = get_trips_by_date(date)

        if not trips:
            print("هیچ سفری در این تاریخ ثبت نشده است.")
            continue

        print(f"\nلیست سفرهای ثبت شده در تاریخ {date}:\n")
        for trip in trips:
            trip_id, bus_id, driver_id, origin, destination, departure_date, departure_time, is_canceled = trip
            status = "لغو شده" if is_canceled else "فعال"
            print(f"شماره سفر: {trip_id} | از: {origin} به: {destination} | تاریخ: {departure_date} | ساعت: {departure_time} | وضعیت: {status}")

        user_choice = input("\nبرای بازگشت به منو مدیریت عدد 0 را وارد کنید یا هر عدد دیگری را برای مشاهده دوباره سفرها وارد کنید: ")

        if user_choice == '0':
            break  # برگرداندن به منو مدیریت

from database import add_new_trip
def add_trip():
    print("لطفاً اطلاعات سفر جدید را وارد کنید:")

    # گرفتن تاریخ سفر از کاربر
    departure_date = input("تاریخ سفر (فرمت YYYY-MM-DD): ")

    # گرفتن مقصد از کاربر
    destination = input("مقصد سفر: ")

    # گرفتن نوع اتوبوس از کاربر
    bus_type = input("نوع اتوبوس (عادی/وی‌آی‌پی): ")

    # فراخوانی تابع افزودن سفر جدید
    add_new_trip(departure_date, destination, bus_type)


#----سفر هایی که انجام شدن---
from database import get_completed_trips  # فراخوانی تابع دریافت سفرهای انجام شده از database.py


def show_completed_trips():
    print("سفرهای انجام شده:")

    # دریافت سفرهای انجام شده
    trips = get_completed_trips()

    # اگر سفرهای انجام شده وجود داشته باشد
    if trips:
        for trip in trips:
            print(f"ID سفر: {trip[0]}, تاریخ: {trip[1]}, مقصد: {trip[2]}, نوع اتوبوس: {trip[3]}")
    else:
        print("هیچ سفری انجام نشده است.")


#دریافت اطلاعات راننده
from database import get_all_drivers

def show_all_drivers():
    drivers = get_all_drivers()
    if not drivers:
        print("هیچ راننده‌ای در سیستم ثبت نشده است.")
        return

    print("\nلیست رانندگان:")
    print("-" * 40)
    for driver in drivers:
        driver_id, name, phone, license_number = driver  # فرض بر اینکه این فیلدها وجود دارند
        print(f"شناسه: {driver_id}")
        print(f"نام: {name}")
        print(f"شماره تماس: {phone}")
        print(f"شماره گواهینامه: {license_number}")
        print("-" * 40)

    input("برای بازگشت به منو، یک کلید فشار دهید...")

#نمایش اتوبوس ها
from database import get_all_buses

def show_all_buses():
    buses = get_all_buses()
    if not buses:
        print("هیچ اتوبوسی ثبت نشده است.")
    else:
        print("\nلیست اتوبوس‌ها:\n")
        for bus in buses:
            print(f"ID: {bus[0]}, شماره پلاک: {bus[1]}, ظرفیت: {bus[2]}, نوع: {bus[3]}")
    print()


def add_new_driver():
    print("لطفاً اطلاعات راننده جدید را وارد کنید:")

    # گرفتن اطلاعات از کاربر
    name = input("نام راننده: ")
    license_number = input("شماره گواهینامه: ")
    birth_date = input("تاریخ تولد (yyyy-mm-dd): ")
    address = input("آدرس: ")
    hiring_date = input("تاریخ استخدام (yyyy-mm-dd): ")
    experience_years = input("تعداد سال‌های تجربه: ")

    # فراخوانی تابع برای اضافه کردن راننده
    add_driver(name, license_number, birth_date, address, hiring_date, experience_years)
    print("راننده جدید با موفقیت اضافه شد.")


from database import get_income_by_date


def show_revenue_by_date():
    date = input("لطفا تاریخ مورد نظر را وارد کنید (فرمت: YYYY-MM-DD): ")
    revenue = get_income_by_date(date)

    if revenue is not None:
        print(f"میزان درآمد در تاریخ {date}: {revenue} تومان")
    else:
        print(f"هیچ تراکنشی در تاریخ {date} یافت نشد.")

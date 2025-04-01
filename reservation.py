from database import add_reservation
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

#new code for deleting ticket sobi from here ______________________________
from database import  get_user_reservations
from database import delete_reservation1


def delete_ticket(user):
    # گرفتن تمام رزروهای کاربر از پایگاه داده
    reservations = get_user_reservations(user[-1])  # فرض بر این است که user[0] شناسه کاربر است

    if not reservations:
        print("شما هیچ بلیطی رزرو نکرده‌اید.")
        return

    print("\nلیست بلیط‌های شما:")
    for reservation in reservations:
        print(
            f"آیدی رزرو: {reservation[4]} - مقصد: {reservation[2]} - تاریخ سفر: {reservation[3]} - نوع اتوبوس: {reservation[3]} - شماره صندلی: {reservation[3]}")

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








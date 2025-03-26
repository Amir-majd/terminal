from database import add_reservation

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
        trip_date = datetime.strptime(trip_date, "%Y-%m-%d")
    except ValueError:
        print("تاریخ وارد شده صحیح نیست.")
        return

    print("نوع اتوبوس را انتخاب کنید:")
    print("1. عادی (30 صندلی)")
    print("2. VIP (35 صندلی)")
    bus_choice = input("انتخاب شما (1/2): ")

    bus_type = "normal" if bus_choice == '1' else "VIP"

    # دریافت صندلی‌های رزرو شده از پایگاه داده
    reserved_seats = get_reserved_seats(destination, trip_date, bus_type)

    display_seat_plan(bus_type)

    seat_number = int(input("شماره صندلی مورد نظر خود را وارد کنید: "))
    if seat_number in reserved_seats:
        print("این صندلی قبلاً رزرو شده است. لطفاً شماره دیگری وارد کنید.")
        return

    payment_method = input("نحوه پرداخت (آنلاین/نقدی): ").lower()

    confirm = input(
        f"آیا می‌خواهید بلیط برای سفر به {destination} در تاریخ {trip_date} با شماره صندلی {seat_number} رزرو کنید؟ (بله/خیر): ").lower()

    if confirm == 'بله':
        if add_reservation(user['username'], destination, trip_date, bus_type, seat_number, payment_method):
            print("رزرو شما با موفقیت انجام شد.")
        else:
            print("خطا در ثبت رزرو.")
    else:
        print("رزرو لغو شد.")


# فرض می‌کنیم این تابع در پایگاه داده پیاده‌سازی شده است
def get_reserved_seats(destination, trip_date, bus_type):
    # این تابع باید اطلاعات صندلی‌های رزرو شده را از پایگاه داده برگرداند.
    # اینجا یک نمونه است که باید با کوئری‌های واقعی جایگزین شود.
    return [1, 2, 3, 5, 6]  # مثال از صندلی‌های رزرو شده


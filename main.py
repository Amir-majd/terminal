

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from sys import argv

import user
from user import user_menu


def print_hi(name):

  #  print(f'Hi, {name} how are you')  # Press Ctrl+F8 to toggle the breakpoint.
   # print("amir", argv)



#------------------------------



    import user


if __name__ == "__main__":
    user_menu()


from user import user_dashboard()

# بعد از ورود موفقیت‌آمیز کاربر عادی
if user:
    print(f"ورود موفقیت‌آمیز! خوش آمدید, {user[4]} {user[5]}.")
    user_dashboard()




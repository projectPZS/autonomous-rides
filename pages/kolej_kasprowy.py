from tkinter import *
import pages.dashboard as dashboard
import pages.previous_view as previous_view
import pages.touristic_routes as tr
from datetime import datetime
import pages.mocks.users as users
import pages.ride_booking as booking

def book_from_chrancowki():
    global ride_price
    global kolej_kasprowy_section
    booking_info = {
        'user_id': users.current_user['id'],
        'type': 'touristic',
        'departure_address': 'Chrańcówki 35',
        'destination_address': 'Kasprowy Wierch',
        'travel_distance': 14,
        'departure_date': dashboard.today,
        'departure_time': '10:00',
        'price': 28,
        'payment_date': dashboard.today,
        'rate': 5.0,
        'is_favourite': False,
        'is_deleted': False,
        'car': 'Tesla',
        'is_route_of_the_day': False
    }
    booking_info['price'] = 5 if is_ride_of_the_day else 28
    previous_view.destroy()
    booking.finalize_ride_booking(booking_info)

def book_from_maja():
    global kolej_kasprowy_section
    kolej_kasprowy_section = kolej_kasprowy_section
    booking_info = {
        'user_id': users.current_user['id'],
        'type': 'touristic',
        'departure_address': '3 Maja',
        'destination_address': 'Kasprowy Wierch',
        'travel_distance': 13,
        'departure_date': dashboard.today,
        'departure_time': '17:00',
        'price': 26,
        'payment_date': dashboard.today,
        'rate': 5.0,
        'is_favourite': False,
        'is_deleted': False,
        'car': 'Tesla',
        'is_route_of_the_day': False
    }
    booking_info['price'] = 5 if is_ride_of_the_day else 26
    previous_view.destroy()
    booking.finalize_ride_booking(booking_info)

def load_kolej_kasprowy():
    global kolej_kasprowy_section
    global is_ride_of_the_day
    is_ride_of_the_day = False
    dashboard.dashboard_cards_container.destroy()
    if (previous_view.previous_view != ''):
        previous_view.previous_view.destroy()

    kolej_kasprowy_section = Canvas(dashboard.dashboard, width=1100, height=600, borderwidth=0, highlightthickness=0,
                                      background="#ffffff")
    kolej_kasprowy_section.create_text(275, 0, anchor=NW, text="Kolej Kasprowy Wierch Kuźnice", fill='#101828',
                                         font=('Inter 20 bold'))
    if (datetime.now().weekday() == 4):
        kolej_kasprowy_section.create_text(60, 0, anchor=NW, text="This is the ride of the day! Get it for 5zł", fill='#2596be',
                                       font=('Inter 12 bold'))
        is_ride_of_the_day = True
    dashboard.dashboard.create_window(0, 125, anchor=NW, window=kolej_kasprowy_section)
    previous_view.previous_view = kolej_kasprowy_section
    kolej_kasprowy_section.create_text(75, 50, anchor=NW, text="Chrancówki 35 Station", fill='#36454F',
                                       font=('Inter 16 bold'))
    kolej_kasprowy_section.create_text(75, 100, anchor=NW, text="Distance of the course: 14 km", fill='#36454F',
                                       font=('Inter 10 normal'))

    kolej_kasprowy_section.create_text(75, 170, anchor=NW, text="Departue at: 10:00", fill='#36454F',
                                       font=('Inter 12 normal'))
    kolej_kasprowy_section.create_text(275, 170, anchor=NW, text="Casual price: 28 zł", fill='#36454F',
                                       font=('Inter 12 normal'))

    kolej_kasprowy_section.book_img = PhotoImage(file='assets/icons/basket.png')
    book_button1 = Button(kolej_kasprowy_section, image = kolej_kasprowy_section.book_img, relief=FLAT, activebackground='#ffffff', bd=0, background='#ffffff', cursor='hand2', command=book_from_chrancowki)
    book_button1.place(x=220, y=155)

    kolej_kasprowy_section.create_text(650, 50, anchor=NW, text="Al. 3 Maja Dolne Station",
                                       fill='#36454F',
                                       font=('Inter 16 bold'))
    kolej_kasprowy_section.create_text(650, 100, anchor=NW, text="Distance of the course: 13km", fill='#36454F',
                                       font=('Inter 10 normal'))
    kolej_kasprowy_section.create_text(650, 170, anchor=NW, text="Departue at: 17:00", fill='#36454F',
                                       font=('Inter 12 normal'))
    kolej_kasprowy_section.create_text(850, 170, anchor=NW, text="Casual price: 13zł", fill='#36454F',
                                       font=('Inter 12 normal'))
    book_button2 = Button(kolej_kasprowy_section, image=kolej_kasprowy_section.book_img, relief=FLAT,
                          activebackground='#ffffff', bd=0, background='#ffffff', cursor='hand2', command=book_from_maja)
    book_button2.place(x=795, y=155)
    kolej_kasprowy_section.narrow = PhotoImage(file='assets/icons/narrow.png')
    back_button = Button(kolej_kasprowy_section, image=kolej_kasprowy_section.narrow, font=('Inter 12 bold'), relief=FLAT, activebackground='#ffffff', bd=0,
                         background='#ffffff', cursor='hand2', command=back)
    back_button.place(x=20, y=0)

def back():
    previous_view.previous_view.destroy()
    tr.load_touristic_routes()


if __name__ == '__main__':
    load_kolej_kasprowy()
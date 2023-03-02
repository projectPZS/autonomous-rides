from tkinter import *
import pages.dashboard as dashboard
import pages.previous_view as previous_view
import pages.touristic_routes as tr
from datetime import datetime
import pages.mocks.users as users
import pages.ride_booking as booking

def book_from_chrancowki():
    global ride_price
    booking_info = {
        'user_id': users.current_user['id'],
        'type': 'touristic',
        'departure_address': 'Chrańcówki 35',
        'destination_address': 'Gubalowka',
        'travel_distance': 4,
        'departure_date': dashboard.today,
        'departure_time': '10:00',
        'price': 8,
        'payment_date': dashboard.today,
        'rate': 5.0,
        'is_favourite': False,
        'is_deleted': False,
        'car': 'Tesla',
        'is_route_of_the_day': False
    }
    booking_info['price'] = 5 if is_ride_of_the_day else 8
    gubalowka_section.destroy()
    booking.finalize_ride_booking(booking_info)

def book_from_maja():
    booking_info = {
        'user_id': users.current_user['id'],
        'type': 'touristic',
        'departure_address': '3 Maja',
        'destination_address': 'Gubalowka',
        'travel_distance': 9,
        'departure_date': dashboard.today,
        'departure_time': '17:00',
        'price': 18,
        'payment_date': dashboard.today,
        'rate': 5.0,
        'is_favourite': False,
        'is_deleted': False,
        'car': 'Tesla',
        'is_route_of_the_day': False
    }
    booking_info['price'] = 5 if is_ride_of_the_day else 18
    gubalowka_section.destroy()
    booking.finalize_ride_booking(booking_info)


def load_gubalowka():
    global gubalowka_section
    dashboard.dashboard_cards_container.destroy()
    if (previous_view.previous_view != ''):
        previous_view.previous_view.destroy()
    global is_ride_of_the_day
    is_ride_of_the_day = False
    gubalowka_section = Canvas(dashboard.dashboard, width=1100, height=600, borderwidth=0, highlightthickness=0,
                                      background="#ffffff")
    gubalowka_section.create_text(400, 0, anchor=NW, text="Gubałówka", fill='#101828',
                                         font=('Inter 20 bold'))
    if (datetime.now().weekday() == 2):
        gubalowka_section.create_text(80, 0, anchor=NW, text="This is the ride of the day! Get it for 5zł", fill='#2596be',
                                       font=('Inter 12 bold'))
        is_ride_of_the_day = True
    dashboard.dashboard.create_window(0, 125, anchor=NW, window=gubalowka_section)
    previous_view.previous_view = gubalowka_section
    gubalowka_section.create_text(75, 50, anchor=NW, text="Chrancówki 35 Station", fill='#36454F',
                                       font=('Inter 16 bold'))
    gubalowka_section.create_text(75, 100, anchor=NW, text="Distance of the course: 4 km", fill='#36454F',
                                       font=('Inter 10 normal'))
    gubalowka_section.create_text(75, 170, anchor=NW, text="Departue at: 10:00", fill='#36454F',
                                       font=('Inter 12 normal'))
    gubalowka_section.create_text(275, 170, anchor=NW, text="Casual price: 8zł", fill='#36454F',
                                       font=('Inter 12 normal'))

    gubalowka_section.book_img = PhotoImage(file='assets/icons/basket.png')
    book_button1 = Button(gubalowka_section, image = gubalowka_section.book_img, relief=FLAT, activebackground='#ffffff', bd=0, background='#ffffff', cursor='hand2', command=book_from_chrancowki)
    book_button1.place(x=220, y=155)

    gubalowka_section.create_text(650, 50, anchor=NW, text="Al. 3 Maja Dolne Station",
                                       fill='#36454F',
                                       font=('Inter 16 bold'))
    gubalowka_section.create_text(650, 100, anchor=NW, text="Distance of the course: 9zł", fill='#36454F',
                                       font=('Inter 10 normal'))
    gubalowka_section.create_text(650, 170, anchor=NW, text="Departue at: 17:00", fill='#36454F',
                                       font=('Inter 12 normal'))
    gubalowka_section.create_text(850, 170, anchor=NW, text="Casual price: 18zł", fill='#36454F',
                                       font=('Inter 12 normal'))
    book_button2 = Button(gubalowka_section, image=gubalowka_section.book_img, relief=FLAT,
                          activebackground='#ffffff', bd=0, background='#ffffff', cursor='hand2', command=book_from_maja)
    book_button2.place(x=795, y=155)
    gubalowka_section.narrow = PhotoImage(file='assets/icons/narrow.png')
    back_button = Button(gubalowka_section, image=gubalowka_section.narrow, font=('Inter 12 bold'), relief=FLAT, activebackground='#ffffff', bd=0,
                         background='#ffffff', cursor='hand2', command=back)
    back_button.place(x=20, y=0)

def back():
    previous_view.previous_view.destroy()
    tr.load_touristic_routes()


if __name__ == '__main__':
    load_gubalowka()
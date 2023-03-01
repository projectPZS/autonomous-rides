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
        'type': 'custom',
        'departure_address': 'Chrańcówki 35',
        'destination_address': 'Kasprowy Wierch',
        'travel_distance': 25,
        'departure_date': dashboard.today,
        'departure_time': '10:00',
        'price': 50,
        'payment_date': dashboard.today,
        'rate': 5.0,
        'is_favourite': False,
        'is_deleted': False,
        'car': 'Tesla',
        'is_route_of_the_day': False
    }
    booking_info['price'] = 5 if is_ride_of_the_day else 50
    kolej_kasprowy_section.destroy()
    booking.finalize_ride_booking(booking_info)

def book_from_maja():
    booking_info = {
        'user_id': users.current_user['id'],
        'type': 'custom',
        'departure_address': '3 Maja',
        'destination_address': 'Kasprowy Wierch',
        'travel_distance': 30,
        'departure_date': dashboard.today,
        'departure_time': '17:00',
        'price': 60,
        'payment_date': dashboard.today,
        'rate': 5.0,
        'is_favourite': False,
        'is_deleted': False,
        'car': 'Tesla',
        'is_route_of_the_day': False
    }
    booking_info['price'] = 5 if is_ride_of_the_day else 60
    morskie_oko_section.destroy()
    booking.finalize_ride_booking(booking_info)

def load_morskie_oko():
    global morskie_oko_section
    global is_ride_of_the_day
    is_ride_of_the_day = False
    dashboard.dashboard_cards_container.destroy()
    if (previous_view.previous_view != ''):
        previous_view.previous_view.destroy()

    morskie_oko_section = Canvas(dashboard.dashboard, width=1100, height=600, borderwidth=0, highlightthickness=0,
                                      background="#ffffff")
    morskie_oko_section.create_text(400, 0, anchor=NW, text="Morskie Oko", fill='#101828',
                                         font=('Inter 20 bold'))
    if (datetime.now().weekday() == 6):
        morskie_oko_section.create_text(80, 0, anchor=NW, text="This is the ride of the day! Get it for 5zł", fill='#2596be',
                                       font=('Inter 12 bold'))
    dashboard.dashboard.create_window(0, 125, anchor=NW, window=morskie_oko_section)
    previous_view.previous_view = morskie_oko_section
    morskie_oko_section.create_text(75, 50, anchor=NW, text="Chrancówki 35 Station", fill='#36454F',
                                       font=('Inter 16 bold'))

    morskie_oko_section.create_text(75, 100, anchor=NW, text="Distance of the course: 25km", fill='#36454F',
                                       font=('Inter 10 normal'))

    morskie_oko_section.create_text(75, 170, anchor=NW, text="Departue at: 10:00", fill='#36454F',
                                       font=('Inter 12 normal'))
    morskie_oko_section.create_text(275, 170, anchor=NW, text="Casual price: 50zł", fill='#36454F',
                                       font=('Inter 12 normal'))

    morskie_oko_section.book_img = PhotoImage(file='assets/icons/basket.png')
    book_button1 = Button(morskie_oko_section, image = morskie_oko_section.book_img, relief=FLAT, activebackground='#ffffff', bd=0, background='#ffffff', cursor='hand2', command=book_from_chrancowki)
    book_button1.place(x=220, y=155)

    morskie_oko_section.create_text(650, 50, anchor=NW, text="Al. 3 Maja Dolne Station",
                                       fill='#36454F',
                                       font=('Inter 16 bold'))
    morskie_oko_section.create_text(650, 100, anchor=NW, text="Distance of the course: 30km", fill='#36454F',
                                       font=('Inter 10 normal'))
    morskie_oko_section.create_text(650, 170, anchor=NW, text="Departue at: 17:00", fill='#36454F',
                                       font=('Inter 12 normal'))
    morskie_oko_section.create_text(850, 170, anchor=NW, text="Casual price: 60zł", fill='#36454F',
                                       font=('Inter 12 normal'))
    book_button2 = Button(morskie_oko_section, image=morskie_oko_section.book_img, relief=FLAT,
                          activebackground='#ffffff', bd=0, background='#ffffff', cursor='hand2', command=book_from_maja)
    book_button2.place(x=795, y=155)
    morskie_oko_section.narrow = PhotoImage(file='assets/icons/narrow.png')
    back_button = Button(morskie_oko_section, image=morskie_oko_section.narrow, font=('Inter 12 bold'), relief=FLAT, activebackground='#ffffff', bd=0,
                         background='#ffffff', cursor='hand2', command=back)
    back_button.place(x=20, y=0)

def back():
    previous_view.previous_view.destroy()
    tr.load_touristic_routes()


if __name__ == '__main__':
    load_morskie_oko()
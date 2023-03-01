from tkinter import *
import pages.dashboard as dashboard
import pages.previous_view as previous_view
from datetime import datetime
import pages.dolina_filipka as dolina_f
import pages.dolina_koscieliska as dolina_k
import pages.gubalowka as gubalowka
import pages.polana_szymoszkowa as ps
import pages.kolej_kasprowy as kk
import pages.wielka_krokiew as wk
import pages.morskie_oko as mo
import pages.mocks.rides as rides

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

def book_a_touristic_route(bookedRoute):
    bookedRoute = {
        'user_id': 0,
        'type': 'touristic',
        'departure_address': 'Chramcówki 35',
        'destination_address': 'Dolina Filipka',
        'travel_distance': 13,
        'departure_date': '',
        'departure_time': '',
        'price': 26,
        'payment_date': '',
        'rate': 5.0,
        'is_favourite': False,
        'is_deleted': False,
        'car': '',
        'is_route_of_the_day': False
    },
    rides.booked_rides.append(bookedRoute)


def load_touristic_routes():
    global touristic_routes_section
    dashboard.dashboard_cards_container.destroy()
    if (previous_view.previous_view != ''):
        previous_view.previous_view.destroy()
    touristic_routes_section = Canvas(dashboard.dashboard, width=900, height=600, borderwidth=0, highlightthickness=0,
                                      background="#ffffff")
    touristic_routes_section.create_text(200, 0, anchor=NW, text="Touristic routes", fill='#101828',
                                         font=('Inter 20 bold'))
    touristic_routes_section.create_text(205, 33, anchor=NW, text="Click at the image for more details", fill='#101828',
                                         font=('Inter 10 normal'))
    dashboard.dashboard.create_window(0, 125, anchor=NW, window=touristic_routes_section)
    previous_view.previous_view = touristic_routes_section
    # current time
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    # create attractions buttons and info about atraction
    touristic_routes_section.img1 = PhotoImage(file='assets/images/dolina.png')
    atr_button1 = Button(touristic_routes_section, image=touristic_routes_section.img1, bd=0, relief=FLAT, activebackground='#ffffff', background='black', cursor='hand2', command=dolina_f.load_dolina_filipka)
    atr_button1.place(x=200,y=55)
    touristic_routes_section.create_text(115, 95, text="Dolina Filipka", font=('Inter 13 bold'), fill='#101828')
    touristic_routes_section.img2 = PhotoImage(file='assets/images/dolina2.png')
    atr_button2 = Button(touristic_routes_section, image=touristic_routes_section.img2, bd=0, relief=FLAT,
                         activebackground='#ffffff', background='black', cursor='hand2', command=dolina_k.load_dolina_koscieliska)
    atr_button2.place(x=200, y=130)
    touristic_routes_section.create_text(115, 170, text="Dolina Kościelska", font=('Inter 13 bold'), fill='#101828')

    touristic_routes_section.img3 = PhotoImage(file='assets/images/kolej.png')
    atr_button3 = Button(touristic_routes_section, image=touristic_routes_section.img3, bd=0, relief=FLAT,
                         activebackground='#ffffff', background='black', cursor='hand2', command=gubalowka.load_gubalowka)
    atr_button3.place(x=200, y=205)
    touristic_routes_section.create_text(115, 245, text="Gubałowka", font=('Inter 13 bold'), fill='#101828')

    touristic_routes_section.img4 = PhotoImage(file='assets/images/polana.png')
    atr_button4 = Button(touristic_routes_section, image=touristic_routes_section.img4, bd=0, relief=FLAT,
                         activebackground='#ffffff', background='black', cursor='hand2', command=ps.load_polana_szymoszkowa)
    atr_button4.place(x=200, y=280)
    touristic_routes_section.create_text(105, 320, text="Polana Szymoszkowa", font=('Inter 13 bold'), fill='#101828')

    touristic_routes_section.img5 = PhotoImage(file='assets/images/gubalowka.png')
    atr_button5 = Button(touristic_routes_section, image=touristic_routes_section.img5, bd=0, relief=FLAT,
                         activebackground='#ffffff', background='black', cursor='hand2', command=kk.load_kolej_kasprowy)
    atr_button5.place(x=200, y=355)
    touristic_routes_section.create_text(115, 395, text="Kasprowy Wierch", font=('Inter 13 bold'), fill='#101828')

    touristic_routes_section.img6 = PhotoImage(file='assets/images/krokiew.png')
    atr_button6 = Button(touristic_routes_section, image=touristic_routes_section.img6, bd=0, relief=FLAT,
                         activebackground='#ffffff', background='black', cursor='hand2', command=wk.load_wielka_krokiew)
    atr_button6.place(x=200, y=430)
    touristic_routes_section.create_text(115, 470, text="Wielka Krokiew", font=('Inter 13 bold'),fill='#101828')

    touristic_routes_section.img7 = PhotoImage(file='assets/images/morskie_oko.png')
    atr_button7 = Button(touristic_routes_section, image=touristic_routes_section.img7, bd=0, relief=FLAT,
                         activebackground='#ffffff', background='black', cursor='hand2', command=mo.load_morskie_oko)
    atr_button7.place(x=200, y=505)
    touristic_routes_section.create_text(115, 545, text="Morskie Oko", font=('Inter 13 bold'), fill='#101828')



if __name__ == '__main__':
    load_touristic_routes()
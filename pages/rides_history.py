from tkinter import *
import pages.dashboard as dashboard
import pages.previous_view as previous_view
import pages.mocks.rides as booked_rides_list
from PIL import ImageTk, Image
import numpy as np

def load_rides_history():
    global rides_history_section
    dashboard.dashboard_cards_container.destroy()
    if (previous_view.previous_view != ''):
        previous_view.previous_view.destroy()
    rides_history_section = Canvas(dashboard.dashboard, width=1000, height = 660, borderwidth=0, highlightthickness=0, background="#ffffff")
    rides_history_section.create_text(0, 10, anchor = NW, text = "Rides explorer", fill='#101828', font=('Inter 20 bold'))
    hourglass_icon_ref = Image.open('assets/icons/icon_hourglass.png')
    hourglass_icon = ImageTk.PhotoImage(hourglass_icon_ref)
    rides_history_section.create_image(180, 0, anchor = NW, image=hourglass_icon)
    rides_history_section.image_names = [hourglass_icon]
    dashboard.dashboard.create_window(30, 165, anchor = NW, window = rides_history_section)
    record_margin_bottom= 30
    record_margin_bottom +=40
    rides_history_section.create_text(0, record_margin_bottom, anchor = NW, text = 'Type', fill='blue', font=('Inter 16 bold'))
    rides_history_section.create_text(100, record_margin_bottom, anchor = NW, text = 'Departure', fill='blue', font=('Inter 16 bold'))
    rides_history_section.create_text(325, record_margin_bottom, anchor = NW, text = 'Destination', fill='blue', font=('Inter 16 bold'))
    rides_history_section.create_text(550, record_margin_bottom, anchor = NW, text = 'Price [zł]', fill='blue', font=('Inter 16 bold'))
    rides_history_section.create_text(650, record_margin_bottom, anchor = NW, text = 'Departure at', fill='blue', font=('Inter 16 bold'))
    rides_history_section.create_text(800, record_margin_bottom, anchor = NW, text = 'Payment date', fill='blue', font=('Inter 16 bold'))
    for ride in np.flip(np.array(booked_rides_list.booked_rides)):
        record_margin_bottom +=40
        rides_history_section.create_text(0, record_margin_bottom, anchor = NW, text = ride['type'], fill='#101828', font=('Inter 14'))
        rides_history_section.create_text(100, record_margin_bottom, anchor = NW, text = ride['departure_address'], fill='#101828', font=('Inter 14'))
        rides_history_section.create_text(325, record_margin_bottom, anchor = NW, text = ride['destination_address'], fill='#101828', font=('Inter 14'))
        rides_history_section.create_text(550, record_margin_bottom, anchor = NW, text = ride['price'], fill='#101828', font=('Inter 14'))
        rides_history_section.create_text(650, record_margin_bottom, anchor = NW, text = ride['departure_time'], fill='#101828', font=('Inter 14'))
        rides_history_section.create_text(800, record_margin_bottom, anchor = NW, text = ride['payment_date'], fill='#101828', font=('Inter 14'))



    previous_view.previous_view = rides_history_section

if __name__ == '__main__':
    load_rides_history()
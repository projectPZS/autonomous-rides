from tkinter import *
from PIL import ImageTk, Image
import pages.custom_ride as custom_ride
import pages.mocks.rides as rides
import pages.dashboard as dashboard
import pages.previous_view as previous
import pages.custom_ride as custom_ride
import pages.mocks.users as users

def slice_string_to_first_n_words(s, n):
    return " ".join(s.split()[:n])[:-1]

def finalize_ride_booking(booked_ride):
    booked_ride['departure_address'] = slice_string_to_first_n_words(booked_ride['departure_address'], 2)
    booked_ride['destination_address']= slice_string_to_first_n_words(booked_ride['destination_address'], 2)
    rides.booked_rides.append(booked_ride)
    users.current_user['discount_points'] += booked_ride['price']
    for user in users.users:
        if(user['email'] == users.current_user['email']):
            user['discount_points'] += booked_ride['price']
            break
    load_success_page()

def load_success_page():
    previous.previous_view.destroy()
    success_page = Canvas(dashboard.dashboard, width=1140, height = 620, bg = '#f2f7f4', borderwidth=0, highlightthickness=0)
    success_page.create_text(300, 250, anchor = NW, text='Your ride was successfully booked', fill='#6c736e', font=('Inter 15 bold'))
    global success_icon

    success_icon_ref = Image.open('assets/icons/success_tick.png')
    success_icon = ImageTk.PhotoImage(success_icon_ref)
    # Create the logout icon button
    success_page.image_names = [success_icon]
    success_page.create_image(635, 230, anchor = NW, image=success_icon)
    dashboard.dashboard.create_window(0, 100, anchor = NW, window=success_page)
    previous.previous_view =success_page

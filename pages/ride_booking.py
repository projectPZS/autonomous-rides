from tkinter import *
from PIL import ImageTk, Image
import pages.custom_ride as custom_ride
import pages.mocks.rides as rides
import pages.dashboard as dashboard
import pages.previous_view as previous
import pages.custom_ride as custom_ride
import pages.mocks.users as users

def slice_string_to_first_n_words(s, n):
    return " ".join(s.split()[:n])

def finalize_booking():
    departure_input_value = slice_string_to_first_n_words(custom_ride.departure_field_value, 2)
    destination_input_value = slice_string_to_first_n_words(custom_ride.destination_field_value, 2)
    booked_ride = {
        'user_id': users.current_user['id'],
        'type': 'custom',
        'departure_address': departure_input_value,
        'destination_address': destination_input_value,
        'travel_distance': custom_ride.travel_distance,
        'departure_date': dashboard.today,
        'departure_time': f"{custom_ride.hour_input}:{custom_ride.minutes_input}",
        'price': custom_ride.travel_cost,
        'payment_date': dashboard.today,
        'rate': 5.0,
        'is_favourite': False,
        'is_deleted': False,
        'car': 'Tesla',
        'is_route_of_the_day': False
    }
    print(booked_ride)
    rides.booked_rides.append(booked_ride)
    load_success_page()

def load_success_page():
    custom_ride.custom_rides_section.destroy()
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
if __name__ == '__main__':
    finalize_booking()
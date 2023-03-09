from tkinter import *
import pages.dashboard as dashboard
import pages.previous_view as previous_view
import pages.ride_booking as ride_booking
from PIL import ImageTk, Image
import tkintermapview
import openrouteservice
import numpy as np
import pages.mocks.users as users

def create_departure_field():
    global departure_input
    custom_rides_section.create_text(700, 118, anchor = NW, text = 'Departure address/place', font = ('Inter 14 normal'), fill='#344054')
    # Create the departure place input field
    departure_input = Entry(custom_rides_section, fg = '#667085', font = ('Inter 16 normal'), border=0, highlightthickness=2,\
                        highlightcolor='#d0d5dd', highlightbackground='#d0d5dd')
    # Put the field inside the custom ride section container
    custom_rides_section.create_window(700, 145, anchor=NW, window=departure_input, width=300)

def create_destination_field():
    global destination_input
    custom_rides_section.create_text(700, 198, anchor = NW, text = 'Destination address/place', font = ('Inter 14 normal'), fill='#344054')
    # Create the destination place input field
    destination_input = Entry(custom_rides_section, fg = '#667085', font = ('Inter 16 normal'), border=0, highlightthickness=2,\
                        highlightcolor='#d0d5dd', highlightbackground='#d0d5dd')
    custom_rides_section.create_window(700, 225, anchor=NW, width=300, window=destination_input)

def create_time_picker():
    global hour_input
    global minutes_input
    custom_rides_section.create_text(700, 508, anchor = NW, text = 'Choose departure time:', font = ('Inter 14 normal'), fill='#344054')
    hour_input = Entry(custom_rides_section, fg = '#667085', font = ('Inter 11 normal'), border=0, highlightthickness=2,\
                        highlightcolor='#d0d5dd', highlightbackground='#d0d5dd')
    custom_rides_section.create_window(905, 509, anchor=NW, width=30, window=hour_input)
    custom_rides_section.create_text(940, 520, text = ':', font = ('Inter 20 bold'), )
    minutes_input = Entry(custom_rides_section, fg = '#667085', font = ('Inter 11 normal'), border=0, highlightthickness=2,\
                        highlightcolor='#d0d5dd', highlightbackground='#d0d5dd')
    custom_rides_section.create_window(945, 509, anchor=NW, width=30, window=minutes_input)

def load_custom_rides_section():
    global custom_rides_section
    global departure_point
    global travel_cost
    global destination_point
    global travel_distance
    travel_cost = 0
    travel_distance=0
    departure_point = ''
    destination_point = ''
    # Destroy previous views
    dashboard.dashboard_cards_container.destroy()
    if (previous_view.previous_view != ''):
        previous_view.previous_view.destroy()
    # Create the custom rides section with its main texts
    custom_rides_section = Canvas(dashboard.dashboard, width=1030, height = 680, borderwidth=0, highlightthickness=0, background="#ffffff")
    custom_rides_section.create_text(30, 6, anchor = NW, text = "Custom ride", fill='#101828', font=('Inter 20 bold'))
    custom_rides_section.create_text(30, 40, anchor = NW, text = "Select 2 points by clicking on the map.", fill='#101828', font=('Inter 10'))
    dashboard.dashboard.create_window(0, 100, anchor = NW, window = custom_rides_section)
    previous_view.previous_view = custom_rides_section
    # Place a google maps map in the section
    place_a_map()
    create_destination_field()
    create_departure_field()
    create_donation_toggle()
    book_ride_button = Button(padx= 10, text = "Book a ride", cursor='hand2', font = ('Inter 14 bold'), background='#032aab', fg='#ffffff', command = validate_custom_ride_form)
    reset_route_choice_button = Button(padx= 10, text = "Reset route choice", cursor='hand2', font = ('Inter 14 bold'), background='grey', fg='#ffffff', command = delete_markers)

    create_time_picker()
    custom_rides_section.create_window(550, 50, window=reset_route_choice_button, anchor=NW)
    custom_rides_section.create_window(750, 550, window=book_ride_button, anchor=NW)

departure_field_value = ''

def validate_custom_ride_form():
    global departure_point
    global destination_point
    global departure_field_value
    global destination_field_value
    global departure_time
    global booking_info 
    departure_field_value = departure_input.get()
    destination_field_value = destination_input.get()
    if (departure_point == '' or destination_point == '' or departure_field_value == '' or destination_field_value == '' or hour_input.get() == '' or minutes_input.get() == ''):
        custom_rides_section.create_text(30, 70, anchor = NW, text = "Please fill all the fields and select 2 points on the map.", fill='red', font=('Inter 14'), tag="custom_ride_warning")
        return
    departure_time = f"{hour_input.get()}:{minutes_input.get()}"
    custom_rides_section.delete('custom_ride_warning')
    previous_view.was_custom_ride_booked = True
    booking_info =  {
        'user_id': users.current_user['id'],
        'type': 'custom',
        'departure_address': departure_field_value,
        'destination_address': destination_field_value,
        'travel_distance': travel_distance,
        'departure_date': dashboard.today,
        'departure_time': departure_time,
        'price': travel_cost,
        'payment_date': dashboard.today,
        'rate': 5.0,
        'is_favourite': False,
        'is_deleted': False,
        'car': 'Tesla',
        'is_route_of_the_day': False
    }
    
    ride_booking.finalize_ride_booking(booking_info)

def finalize_booking():
    ride_booking.finalize_ride_booking(booking_info)

def create_donation_toggle():
    global donation_toggle_icon
    global toggle_on 
    global donation_toggle_button
    toggle_on = False
    donation_toggle_icon_path = 'assets/icons/toggle-off.png'
    donation_toggle_icon_ref = Image.open(donation_toggle_icon_path)
    donation_toggle_icon = ImageTk.PhotoImage(donation_toggle_icon_ref)
    custom_rides_section.create_text(700, 390, anchor = NW, text='Support autonomous rides:', fill='#101828', font=('Inter 12 bold'))
    custom_rides_section.create_text(700, 410, anchor = NW, text='Donate 50zł:', fill='#101828', font=('Inter 12 bold'))
    donation_toggle_button = Button(image=donation_toggle_icon, background='#ffffff', borderwidth=0, highlightthickness=0, command=toggle_donation_payment_option)
    custom_rides_section.image_names = [donation_toggle_icon]
    custom_rides_section.create_window(820, 410, anchor = NW, window = donation_toggle_button, tags = 'donation_toggle_window')
    

def toggle_donation_payment_option():
    global toggle_on
    global travel_cost
    global donation_toggle_button
    global travel_distance
    toggle_on = not toggle_on
    donation_toggle_icon_path = 'assets/icons/toggle-off.png' if (toggle_on == False) else 'assets/icons/toggle-on.png'
    donation_toggle_icon_ref = Image.open(donation_toggle_icon_path)
    donation_toggle_icon = ImageTk.PhotoImage(donation_toggle_icon_ref)
    custom_rides_section.delete('donation_toggle_window')
    donation_toggle_button =Button(image=donation_toggle_icon, background='#ffffff', borderwidth=0, highlightthickness=0, command=toggle_donation_payment_option)
    custom_rides_section.image_names = [donation_toggle_icon]
    custom_rides_section.create_window(820, 410, anchor = NW, window = donation_toggle_button, tags="donation_toggle_window")
    custom_rides_section.update()
    if (toggle_on == True):
        travel_cost += 50
        custom_rides_section.create_text(700, 430, anchor=NW, text=f'Donation included.', tags="donation_on_message")
    else:
        custom_rides_section.delete('donation_on_message')
        travel_cost -= 50
    custom_rides_section.delete('travel_cost')
    custom_rides_section.create_text(700, 340, anchor = NW, text = f"Travel cost: {str(travel_cost)} zł", fill='#101828', font=('Inter 14'), tag='travel_cost')
    custom_rides_section.update()
        

def place_a_map():
    # Get the google maps map view
    global map_widget
    map_widget = tkintermapview.TkinterMapView(width = 600, height = 450)
    map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
    # Add command menu that appears on the right click on the map
    map_widget.add_left_click_map_command(set_route_marker_point)
    # Place the map in the custom rides section
    custom_rides_section.create_window(30, 100, anchor=NW, window = map_widget)
    custom_rides_section.grid_propagate(False)
    # Set map to point to Zakopane
    map_widget.set_position(49.299171, 19.949020)
    map_widget.set_zoom(15)

def delete_markers():
     global departure_point
     global destination_point
     custom_rides_section.delete("travel_distance")
     custom_rides_section.delete("travel_time")
     custom_rides_section.delete("travel_cost")
     map_widget.delete_all_marker()
     map_widget.delete_all_path()
     # Clear the departure and destination input fields
     departure_input.delete(0, END)
     destination_input.delete(0, END)
     departure_point = ''
     destination_point = ''

def display_ride_booking_info(travel_distance, travel_time, travel_cost):
    custom_rides_section.delete('travel_distance')
    custom_rides_section.delete('travel_time')
    custom_rides_section.delete('travel_cost')
    custom_rides_section.create_text(700, 280, anchor = NW, text = f"Travel distance: {str(travel_distance)} km", fill='#101828', font=('Inter 14'), tag='travel_distance')
    custom_rides_section.create_text(700, 310, anchor = NW, text = f"Travel time: {str(travel_time)} min", fill='#101828', font=('Inter 14'), tag='travel_time')
    custom_rides_section.create_text(700, 340, anchor = NW, text = f"Travel cost: {str(travel_cost)} zł", fill='#101828', font=('Inter 14'), tag='travel_cost')

def get_departure_city_and_housenumber_text():
    global departure_housenumber
    global departure_city
    if departure_housenumber is None:
            departure_housenumber = ''
    else:
        departure_housenumber= f" {departure_housenumber}"
    if departure_city is None:
        departure_city = ''
    else:
        departure_city = f", {departure_city}"

def get_destination_city_and_housenumber_text():
    global destination_housenumber
    global destination_city
    global destination_address
    destination_city = destination_address.city
    destination_housenumber = destination_address.housenumber
    if destination_housenumber is None:
        destination_housenumber = ''
    else:
        destination_housenumber = f" {destination_housenumber}"
        if destination_city is None:
            destination_city = ''
        else:
            destination_city= f", {destination_city}"

def set_map_zoom_to_fit_points():
    if (destination_point != ''):
        if (departure_point[0] > destination_point[0]):
            if (departure_point[1] > destination_point [1]):
                map_widget.fit_bounding_box((departure_point[0], destination_point[1]), (destination_point[0], departure_point[1]))
            else:
                map_widget.fit_bounding_box((departure_point[0], departure_point[1]), (destination_point[0], destination_point[1]))
        else:
            if (departure_point[1] > destination_point[1]):
                map_widget.fit_bounding_box((destination_point[0], destination_point[1]), (departure_point[0], departure_point[1]))
            else:
                map_widget.fit_bounding_box((destination_point[0], departure_point[1]), (departure_point[0], destination_point[1]))

def set_route_marker_point(coordinates_tuple):
    global departure_point
    global destination_point
    global destination_address
    global destination_housenumber
    global destination_city
    global departure_city
    global departure_housenumber
    global travel_cost
    # Add a marker where the menu was opened by right clicking on the map
    map_widget.set_marker(coordinates_tuple[0], coordinates_tuple[1])
    custom_rides_section.update()
    map_widget.update()
    if (departure_point == ''):
        departure_point = coordinates_tuple
    else:
        # update address input fields to match markers
        destination_point = coordinates_tuple
        departure_address = tkintermapview.convert_coordinates_to_address(departure_point[0], departure_point[1])
        departure_city = departure_address.city
        departure_housenumber = departure_address.housenumber
        get_departure_city_and_housenumber_text()
        departure_input.insert(0, f"{departure_address.street}{departure_housenumber}{departure_city}, {departure_address.postal}".replace("None", ''))
        set_map_zoom_to_fit_points()
        destination_address = tkintermapview.convert_coordinates_to_address(destination_point[0], destination_point[1])
        get_destination_city_and_housenumber_text()
        destination_input.insert(0, f"{destination_address.street}{destination_housenumber}{destination_city}, {destination_address.postal}".replace("None", ''))
        # Display ride booking info
        get_travel_duration_and_distance_info()
        display_ride_booking_info(travel_distance, travel_time, travel_cost)

def get_travel_duration_and_distance_info():
        global travel_distance
        global travel_time
        global travel_cost
        client = openrouteservice.Client(key='5b3ce3597851110001cf62486678e596c0334206847ae65b0135b440')
        coords =((departure_point[1], departure_point[0]), (destination_point[1], destination_point[0]))
        res = client.directions(coordinates=coords, profile='driving-car', format='geojson')
        # Draw the path between departure and destination points
        map_widget.set_path([departure_point, destination_point])
        # Calculate the travel distance and time
        travel_distance = round(res['features'][0]['properties']['segments'][0]['distance']/1000,1)
        travel_time= round(res['features'][0]['properties']['segments'][0]['duration']/60,1)
        travel_cost += travel_distance * 5

if __name__ == '__main__':
    load_custom_rides_section()
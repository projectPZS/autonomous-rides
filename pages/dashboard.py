from tkinter import *
from PIL import ImageTk, Image
from datetime import date
import pages.login as login
import pages.basket as basket
import pages.previous_view as previous_view
import pages.touristic_routes  as touristic_routes
import pages.custom_ride as custom_ride
import pages.rides_history as rides_history

def create_dashboard_header():
    global today
    # Create dashboard header container
    dashboard_header_container = Canvas(dashboard, width = 1030, height=100, borderwidth=0,\
                             highlightthickness=0)
    # Create the today's ride section
    dashboard_header_text_container = Canvas(parent, width=150, height=50, borderwidth=0,\
                             highlightthickness=0)
    dashboard_header_container.create_window(50, 25, anchor=NW, window=dashboard_header_text_container)
    dashboard_header_text_container.create_text(0, 0, anchor=NW, text = "Today's ride", fill='#101828', font=('Inter 15 bold'))
    # Display the current date
    today = date.today().strftime("%B %d, %Y")
    dashboard_header_text_container.create_text(0, 30, anchor=NW, text = today, fill='#101828', font=('Inter 10'))
    # Create the basket icon
    basket_icon_ref = Image.open('assets/images/basket.png') 
    basket_icon= ImageTk.PhotoImage(basket_icon_ref)
    basket_button = Button(image=basket_icon, background=None, borderwidth=0, highlightthickness=0, command=basket.load_basket)
    dashboard_header_container.create_window(973, 21, anchor = NW, window=basket_button)
    dashboard_header_container.image_names= [basket_icon]
    # Display the username
    dashboard_header_container.create_text(870, 22, anchor=NW, text = login.user_first_name, fill='#101828', font=('Inter 15 bold'))
    dashboard_header_container.create_text(870, 52, anchor=NW, text = login.user_last_name, fill='#101828', font=('Inter 15 bold'))
    # Put the header inside the dashboard container
    dashboard.create_window(0, 0, anchor=NW, window=dashboard_header_container)

def create_rides_history_card():
    # Create the rides history card
    rides_history_card_container = Canvas(dashboard_cards_container, width = 565, height=175, borderwidth=1,\
                             highlightthickness=1, bg="#d3e0c8")
    # Create the rides history card text
    rides_history_card_container.create_text(25, 25, anchor=NW, text ='Rides history', fill='#101828', font=('Inter 15 bold'))
    rides_history_card_container.create_text(25, 50, anchor=NW, text ='Look for previous rides', fill='#101828', font=('Inter 10'))
    # Create the rides history card image
    rides_history_image_ref = Image.open('assets/icons/rides-history.png') 
    rides_history_image = ImageTk.PhotoImage(rides_history_image_ref)
    # Put the rides history image inside the card
    rides_history_card_container.create_image(470, 20, anchor=NW, image=rides_history_image)
    rides_history_card_container.image_names= [rides_history_image]
    # Create the rides history card button
    rides_history_card_button = Button(text="Get your ride", padx=15, font = ('Inter 12 bold'), background='white', fg='black', command=rides_history.load_rides_history)
    rides_history_card_container.create_window(25, 130, anchor=NW, window=rides_history_card_button)
    # Put the card inside the dashboard 
    dashboard_cards_container.create_window(0, 50, anchor=NW, window=rides_history_card_container)

def create_custom_ride_card():
    global dashboard_cards_container
    # Create the custom ride card container
    custom_ride_card_container = Canvas(dashboard_cards_container, width = 275, height=225, borderwidth=1,\
                             highlightthickness=1, bg="#f5d6cb")
    # Create the custom ride card button
    custom_ride_card_button = Button(text="View history", padx=15, font = ('Inter 12 bold'), background='white', fg='black')
    # Create the card text
    custom_ride_card_container.create_text(62, 25, anchor=NW, text ='Get your own ride', fill='#101828', font=('Inter 12 bold'))
    custom_ride_card_container.create_text(65, 50, anchor=NW, text ='Choose your custom route', fill='#101828', font=('Inter 8'))
    # Create the card image
    custom_ride_image_ref = Image.open('assets/images/car-custom-ride.png') 
    custom_ride_image = ImageTk.PhotoImage(custom_ride_image_ref)
    custom_ride_card_container.create_image(90, 80, anchor=NW, image=custom_ride_image)
    custom_ride_card_container.image_names = [custom_ride_image]
    # Create the card button
    custom_ride_card_button = Button(text="Get your ride", padx=15, font = ('Inter 12 bold'), background='white', fg='black', command=custom_ride.load_custom_rides_section)
    custom_ride_card_container.create_window(55, 180, anchor=NW, window=custom_ride_card_button)
    # Put the card inside the dashboard
    dashboard_cards_container.create_window(0, 245, anchor=NW, window=custom_ride_card_container)

def create_touristic_routes_card():
    global touristic_routes_card_container
    # Create the touristic routes card
    touristic_routes_card_container = Canvas(dashboard_cards_container, width = 275, height=225, borderwidth=1,\
                             highlightthickness=1, bg="#f5d6cb")
    # Create the card image
    touristic_routes_card_image_ref = Image.open('assets/images/bus.png') 
    touristic_routes_card_image = ImageTk.PhotoImage(touristic_routes_card_image_ref)
    touristic_routes_card_container.create_image(85, 80, anchor=NW, image=touristic_routes_card_image)
    touristic_routes_card_container.image_names = [touristic_routes_card_image]
    # Create the card text
    touristic_routes_card_container.create_text(48, 25, anchor=NW, text ='Choose a touristic route', fill='#101828', font=('Inter 12 bold'))
    touristic_routes_card_container.create_text(70, 50, anchor=NW, text ='Select a famous destination', fill='#101828', font=('Inter 8'))
    # Create the card button
    touristic_routes_card_button = Button(text="Choose a route", padx=15, font = ('Inter 12 bold'), background='white', fg='black', command=touristic_routes.load_touristic_routes)
    touristic_routes_card_container.create_window(55, 180, anchor=NW, window=touristic_routes_card_button)
    # Put the card inside the dashboard
    dashboard_cards_container.create_window(295, 245, anchor=NW, window=touristic_routes_card_container)
    
def create_dashboard_cards():
    global dashboard_cards_container
    if (previous_view.previous_view != ''):
        previous_view.previous_view.destroy()
    dashboard_cards_container = Canvas(dashboard, width = 565, height=475, borderwidth=0,\
                             highlightthickness=0, bg="#ffffff")
    dashboard_cards_container.create_text(10, 0, anchor=NW, text="Get your autonomous ride fast and cheap!", fill='#101828', font=('Inter 20 bold'))
    create_rides_history_card()
    create_custom_ride_card()
    create_touristic_routes_card()
    dashboard.create_window(210, 165, anchor=NW, window=dashboard_cards_container)
    previous_view.previous_view = dashboard_cards_container

def load_dashboard(parent_, parent_dimensions):
    global parent
    global parent_container_width
    global parent_container_height
    global dashboard
    # Get the root container
    parent = parent_
    parent_container_width = parent_dimensions[0]
    parent_container_height = parent_dimensions[1]
    # Create the dashboard container
    dashboard = Canvas(parent, width= 1030, height=780, borderwidth=0,\
                             highlightthickness=0, bg="#ffffff")
    parent.create_window(250, 0, anchor=NW, window=dashboard)
    parent.update()
    # Create dashboard sections
    create_dashboard_header()
    create_dashboard_cards()

if __name__ == '__main__':
    load_dashboard()
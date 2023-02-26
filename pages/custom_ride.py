from tkinter import *
import pages.dashboard as dashboard
import pages.previous_view as previous_view

def load_custom_rides_section():
    global touristic_routes_section
    dashboard.dashboard_cards_container.destroy()
    if (previous_view.previous_view != ''):
        previous_view.previous_view.destroy()
    custom_rides_section = Canvas(dashboard.dashboard, width=360, height = 50, borderwidth=0, highlightthickness=0, background="#ffffff")
    custom_rides_section.create_text(0, 10, anchor = NW, text = "Custom ride", fill='#101828', font=('Inter 20 bold'))
    dashboard.dashboard.create_window(210, 165, anchor = NW, window = custom_rides_section)
    previous_view.previous_view = custom_rides_section
    
if __name__ == '__main__':
    load_custom_rides_section()
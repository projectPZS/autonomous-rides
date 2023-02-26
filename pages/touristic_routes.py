from tkinter import *
import pages.dashboard as dashboard
import pages.previous_view as previous_view

def load_touristic_routes():
    global touristic_routes_section
    dashboard.dashboard_cards_container.destroy()
    if (previous_view.previous_view != ''):
        previous_view.previous_view.destroy()
    touristic_routes_section = Canvas(dashboard.dashboard, width=360, height = 50, borderwidth=0, highlightthickness=0, background="#ffffff")
    touristic_routes_section.create_text(0, 10, anchor = NW, text = "Touristic routes", fill='#101828', font=('Inter 20 bold'))
    dashboard.dashboard.create_window(210, 165, anchor = NW, window = touristic_routes_section)
    previous_view.previous_view = touristic_routes_section
    
if __name__ == '__main__':
    load_touristic_routes()
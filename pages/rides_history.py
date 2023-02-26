from tkinter import *
import pages.dashboard as dashboard
import pages.previous_view as previous_view

def load_rides_history():
    global rides_history_section
    dashboard.dashboard_cards_container.destroy()
    if (previous_view.previous_view != ''):
        previous_view.previous_view.destroy()
    rides_history_section = Canvas(dashboard.dashboard, width=360, height = 50, borderwidth=0, highlightthickness=0, background="#ffffff")
    rides_history_section.create_text(0, 10, anchor = NW, text = "Rides history", fill='#101828', font=('Inter 20 bold'))
    dashboard.dashboard.create_window(210, 165, anchor = NW, window = rides_history_section)
    previous_view.previous_view = rides_history_section
    
if __name__ == '__main__':
    load_rides_history()
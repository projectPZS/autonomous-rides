from tkinter import *
import pages.dashboard as dashboard
import pages.previous_view as previous_view

def load_basket():
    global basket_section
    if (previous_view.previous_view != ''):
        previous_view.previous_view.destroy()
    basket_section = Canvas(dashboard.dashboard, width=360, height = 50, borderwidth=0, highlightthickness=0, background="#ffffff")
    basket_section.create_text(0, 10, anchor = NW, text = "Basket", fill='#101828', font=('Inter 20 bold'))
    dashboard.dashboard.create_window(210, 165, anchor = NW, window = basket_section)
    previous_view.previous_view = basket_section
    
if __name__ == '__main__':
    load_basket()
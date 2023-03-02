from tkinter import *
import pages.dashboard as dashboard
import pages.previous_view as previous_view
import pages.mocks.users as users
from PIL import ImageTk, Image

def load_discount_points_section():
    global discount_points_section
    if (previous_view.previous_view != ''):
        previous_view.previous_view.destroy()
    discount_points = users.current_user['discount_points']
    discount_points_section = Canvas(dashboard.dashboard, width=600, height = 600, borderwidth=0, highlightthickness=0, background="#ffffff")
    card = Canvas(discount_points_section, width=400, height = 290, borderwidth=0, highlightthickness=0, background="#d6b88b")
    discount_points_section.create_text(0, 10, anchor = NW, text = "Discount points", fill='#101828', font=('Inter 20 bold'))
    discount_points_section.create_text(0, 50, anchor = NW, text = f"You have {discount_points} discount_points!", fill='orange', font=('Inter 16 bold'))
    discount_points_section.create_text(0, 90, anchor = NW, text = f"Collect {1000-discount_points} more to upgrade to silver card and get all rides 10% off.", fill='grey', font=('Inter 12 bold'))
    discount_points = discount_points_section.create_window(0, 120, anchor=NW,  window=card)
    discount_points = users.current_user['discount_points']
    # Create the card data
    logo_ref = Image.open('assets/icons/logo.ico')
    logo = ImageTk.PhotoImage(logo_ref)
    card.create_image(170, 100, anchor = NW, image=logo)
    card.image_names = [logo]
    card.update()
    card.create_text(330, 260, anchor = NW, text=f"{discount_points}/1000", fill='#101828', font=('Inter 12 bold'))
    dashboard.dashboard.create_window(190, 165, anchor = NW, window = discount_points_section)
    previous_view.previous_view = discount_points_section
    
if __name__ == '__main__':
    load_discount_points_section()
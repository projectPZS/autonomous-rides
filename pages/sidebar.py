from tkinter import *
from PIL import ImageTk, Image
import pages.login as login
import pages.settings as settings
import pages.discount_points as discount_points
import pages.dashboard as dashboard
import pages.mocks.users as users

def logout():
    parent.destroy()
    login.load_login_page(login.root, (login.root_container_width, login.root_container_height))
    users.current_user = ''

def create_sidebar_navigation():
    global dashboard_icon, settings_icon, discount_icon
    # Dashboard option
    create_dashboard_redirect_buttons()
    # Discount card option
    create_discount_points_section_buttons()
    # Settings option
    create_settings_buttons()
    

def load_dashboard_cards():
    print('redirect dashboard cards')

def load_discount_points_section():
    print('discount points section')

def load_settings():
    print('settings')

def create_dashboard_redirect_buttons():
    global dashboard_icon
    dashboard_icon_ref = Image.open('assets/icons/chart-dashboard=redirect.png')
    dashboard_icon = ImageTk.PhotoImage(dashboard_icon_ref)
    # Create the logout icon button
    dashboard_button = Button(image=dashboard_icon, background='#d2e5f7', borderwidth=0, highlightthickness=0, command=dashboard.create_dashboard_cards, cursor='hand2')
    sidebar.create_window(60, 150, anchor = NW, window=dashboard_button)
    # Create the dashboard text button
    dashboard_text_button = Button(background='#d2e5f7', borderwidth=0, highlightthickness=0, text="Dashboard", foreground='#101828', font=('Inter 12 bold'), command=dashboard.create_dashboard_cards, cursor='hand2')
    sidebar.create_window(110, 158, anchor = NW, window=dashboard_text_button)

def create_discount_points_section_buttons():
    global discount_icon
    discount_icon_ref = Image.open('assets/icons/discount-card.png')
    discount_icon = ImageTk.PhotoImage(discount_icon_ref)
    discount_button = Button(image=discount_icon, background='#d2e5f7', borderwidth=0, highlightthickness=0, command=discount_points.load_discount_points_section, cursor='hand2')
    sidebar.create_text(110, 218, anchor = NW, text='Discound Points', fill='#101828', font=('Inter 12 bold'))
    sidebar.create_window(60, 208, anchor = NW, window=discount_button)
    # Create the logout text button
    sidebar_text_button = Button(background='#d2e5f7', borderwidth=0, highlightthickness=0, text="Discount Points", foreground='#101828', font=('Inter 12 bold'), command=discount_points.load_discount_points_section, cursor='hand2')
    sidebar.create_window(110, 218, anchor = NW, window=sidebar_text_button)

def create_settings_buttons():
    global settings_icon
    settings_icon_ref = Image.open('assets/icons/settings.png')
    settings_icon = ImageTk.PhotoImage(settings_icon_ref)
    sidebar.create_text(110, 265, anchor = NW, text='Settings', fill='#101828', font=('Inter 12 bold'))
    settings_button = Button(image=settings_icon, background='#d2e5f7', borderwidth=0, highlightthickness=0, command=settings.load_settings, cursor='hand2')
    sidebar.create_window(65, 263, anchor = NW, window=settings_button)
    # Create the logout text button
    settings_text_button = Button(background='#d2e5f7', borderwidth=0, highlightthickness=0, text="Settings", foreground='#101828', font=('Inter 12 bold'), command=settings.load_settings, cursor='hand2')
    sidebar.create_window(110, 265, anchor = NW, window=settings_text_button)

def create_logout_buttons():
    global logout_icon
    # Create the logout icon button
    logout_icon_ref = Image.open('assets/icons/logout.png')
    logout_icon = ImageTk.PhotoImage(logout_icon_ref)
    logout_button = Button(image=logout_icon, background='#d2e5f7', borderwidth=0, highlightthickness=0, command=logout, cursor='hand2')
    sidebar.create_window(25, 650, anchor = NW, window=logout_button)
    # Create the logout text button
    logout_text_button = Button(background='#d2e5f7', borderwidth=0, highlightthickness=0, text="Log Out", foreground='#101828', font=('Inter 12 bold'), command=logout, cursor='hand2')
    sidebar.create_window(70, 654, anchor = NW, window=logout_text_button)

def load_sidebar(parent_, parent_dimensions):
    global parent, parent_container_width, parent_container_height
    global logo
    global sidebar
    # Get the parent container
    parent = parent_
    parent_container_width = parent_dimensions[0]
    parent_container_height = parent_dimensions[1]
    # Create the sidebar container
    sidebar = Canvas(parent, width= 250, height=780, borderwidth=0,\
                             highlightthickness=0, background="#d2e5f7")
    parent.create_window(0, 0, anchor=NW, window=sidebar)
    parent.update()
    # Create the sidebar logo
    logo_ref = Image.open('assets/icons/logo.ico')
    logo = ImageTk.PhotoImage(logo_ref)
    sidebar.create_image(85, -10, anchor = NW, image=logo)
    sidebar.create_text(10, 55, anchor = NW, text='Zakopane Autonomous Rides', fill='#101828', font=('Inter 12 bold'))
    # Creathe the navigation
    create_sidebar_navigation()
    # Create the logout buttons
    create_logout_buttons()
    # Make all the icons visible in the sidebar
    sidebar.image_names = [logo, logout_icon, dashboard_icon, discount_icon, settings_icon]
    
if __name__ == '__main__':
    load_sidebar()
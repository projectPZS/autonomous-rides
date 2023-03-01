from tkinter import *
from PIL import ImageTk, Image
import pages.register as registration
import tkintermapview
from pages.main_content import load_main_content_page
import pages.mocks.users as user_list

def create_login_section_container():
    global login_section
    login_section = Canvas(login_page, width=root_container_width/2, height = root_container_height,\
                           bg='#ffffff', borderwidth=0, highlightthickness=0)
    login_section.grid(row=0, column=0)
    login_section.grid_propagate(False)

def load_background_image():
    # Load the image
    background_image_ref = Image.open('assets/images/login-background.jpg')
    background_image = ImageTk.PhotoImage(background_image_ref)
    # Put the image in the image section
    image_wrapper = Label(image_section, image=background_image, width=root_container_width/2, height=root_container_height)
    image_wrapper.image_names = [background_image]
    image_wrapper.pack()

def create_image_section():
    global image_section
    # Create the section container
    image_section = Canvas(login_page, width=root_container_width/2, height = root_container_height, borderwidth=0, highlightthickness=0)
    image_section.grid(row=0, column=1)
    image_section.grid_propagate(False)
    # Load the background image and put it in the container
    load_background_image()

def create_login_form_container():
    global login_form_container
    login_form_container = Canvas(login_section, width=450, height = 450, bg = '#ffffff', borderwidth=0, highlightthickness=0)
    login_form_container.create_text(0, 4, anchor=NW, text = 'Welcome back', fill='#101828', font=('Inter 30 bold'))
    login_form_container.create_text(0, 64, anchor=NW, text = 'Welcome back! Please enter your details',\
                                     font=('Inter 16 normal'), fill='#475467')

def create_email_field():
    global email_input
    global email_placeholder
    email_placeholder = 'Enter your email'
    login_form_container.create_text(0, 118, anchor = NW, text = 'Email', font = ('Inter 14 normal'), fill='#344054')
    email_field = Canvas(login_form_container, width=360, height = 1,  borderwidth=0, highlightthickness=0)
    # Create the email input field and fill it with placeholder
    email_input = Entry(email_field, fg = '#667085', font = ('Inter 16 normal'), border=0, highlightthickness=2,\
                        highlightcolor='#d0d5dd', highlightbackground='#d0d5dd')
    email_input.insert(0, 'Enter your email')
    email_field.create_window(0, 34, anchor=NW, width=360, window=email_input)
    email_input.pack(ipadx=3, ipady=3)
    # Remove the placeholder on focus
    email_input.bind('<FocusIn>', lambda args: email_input.delete('0', 'end'))
    # Put the field inside the login form container
    login_form_container.create_window(0, 144, anchor=NW, window=email_field)

def create_password_field():
    global password_input
    global password_placeholder
    password_placeholder = 'Enter your password'
    login_form_container.create_text(0, 208, anchor = NW, text = 'Password', font = ('Inter 14 normal'), fill='#344054')
    password_field = Canvas(login_form_container, width=360, height = 50, borderwidth=0, highlightthickness=0)
    # Create the password input field and fill it with placeholder
    password_input = Entry(password_field, fg = '#667085', font = ('Inter 16 normal'), border=0,\
                           highlightbackground='#d0d5dd', highlightthickness=2, highlightcolor='#d0d5dd', show = '*')
    password_input.insert(0, password_placeholder)
    password_field.create_window(0, 0, anchor=NW, width=360, window=password_input)
    password_input.pack(ipadx=3, ipady=3)
    # Remove the placeholder on focus
    password_input.bind('<FocusIn>', lambda args: password_input.delete('0', 'end'))
    # Put the field inside the login form container
    login_form_container.create_window(0, 234, anchor=NW, window=password_field)

def register():
    login_page.destroy()
    registration.load_register_page(root,(root_container_width, root_container_height))

def is_login_validation_approved():
    global user_first_name, user_last_name
    # Get login data
    given_email = email_input.get()
    given_password = password_input.get()
    if (given_email == '' or given_email == email_placeholder or given_password == '' or given_password == password_placeholder):
        login_form_container.delete("invalid_message")
        login_form_container.create_text(0, 88, anchor = NW, text = 'Please fill in both fields.', font = ('Inter 14 bold'), fill='red', tag="invalid_message")
        return False
    else:
        users_with_given_email = list(filter(lambda user: user['email'] == given_email, user_list.users))
        if (len(users_with_given_email) == 0):
            login_form_container.delete("invalid_message")
            login_form_container.create_text(0, 88, anchor = NW, text = 'Incorrect email or password.', font = ('Inter 14 bold'), fill='red', tag="invalid_message")
            return False
        elif (users_with_given_email[0]['password'] != given_password):
            login_form_container.delete("invalid_message")
            login_form_container.create_text(0, 88, anchor = NW, text = 'Incorrect email or password.', font = ('Inter 14 bold'), fill='red', tag="invalid_message")
            return False
        user_list.current_user = users_with_given_email[0]
        user_first_name = users_with_given_email[0]['first_name']
        user_last_name = users_with_given_email[0]['last_name']
        return True
            
def login():
    if (is_login_validation_approved()):
        login_page.destroy()
        # Switch to the main content page
        load_main_content_page(root, (root_container_width, root_container_height))

def create_login_form_action_buttons():
    login_form_container.create_text(120, 285, anchor = NW, text = 'Forgot password',\
                                     font = ('Inter 12 bold'), fill='#6941c6')
    # Create the sign in button
    login_button = Button(text='Sign in', padx=85, font = ('Inter 14 bold'), background='#7F56D9', fg='#ffffff', command=login, cursor = 'hand2')
    login_form_container.create_window(0, 329, anchor=NW, window=login_button)
    # Link to the create an account page
    login_form_container.create_text(0, 398, anchor = NW, text = "Don't have an account?", font = ('Inter 14 normal'), fill='#475467')
    # Create sign up button
    register_button = Button(text='Sign up', font=('Inter 12 bold'), background='#ffffff', fg='#7F56D9', activebackground="#ffffff", bd=0, cursor='hand2', command=register)
    login_form_container.create_window(195, 396, anchor=NW, window=register_button)
    
def create_login_form():
    create_login_form_container()
    # Create the form fields
    create_email_field()
    create_password_field()
    # Create the form action buttons
    create_login_form_action_buttons()
    # Put the login form inside the login section
    login_section.create_window(150, 150, anchor=NW, window=login_form_container)

def load_header_logo():
    # Load the logo image
    header_logo_ref = Image.open('assets/icons/logo.ico') 
    header_logo = ImageTk.PhotoImage(header_logo_ref)
    # Put the logo inside the header
    login_section_header.create_image(0, 0, anchor=NW, image=header_logo)
    login_section_header.image_names = [header_logo]

def create_login_header():
    global login_section_header
    # Create the header
    login_section_header = Canvas(login_section, width=430, height = 64, bg = '#ffffff', borderwidth=0, highlightthickness=0)
    login_section_header.create_text(100, 32, anchor = NW, text='Zakopane Autonomous Rides', font=('Inter 15 bold'), fill='#101828')
    load_header_logo()
    # Put the header in the login section
    login_section.create_window(32, 0, anchor=NW, window=login_section_header)

def create_login_section():
    create_login_section_container()
    create_login_header()
    create_login_form()
    # Create the login section footer
    login_section.create_text(32, root_container_height-32, anchor=NW, text='© Zakopane Autonomous Rides 2023',\
                              font = ('Inter 12 normal'), fill='#475467')
    
def load_login_page(root_, root_dimensions):
    global root
    global login_page
    global root_container_width
    global root_container_height
    global textt
    textt = ''
    # Get the root container
    root = root_
    root_container_width = root_dimensions[0]
    root_container_height = root_dimensions[1]
    # Create the login_page_container
    global login_page
    login_page = Canvas(root, width=root_container_width, height=root_container_height, borderwidth=0,
                        highlightthickness=0)
    login_page.pack()
    # Create login page sections
    create_login_section()
    create_image_section()
    
if __name__ == '__main__':
    load_login_page()
    
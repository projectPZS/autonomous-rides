from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def create_register_section_container():
    global register_section
    register_section = Canvas(register_page, width=root_container_width / 2, height=root_container_height, \
                           bg='#ffffff', borderwidth=0, highlightthickness=0)
    register_section.grid(row=0, column=0)
    register_section.grid_propagate(False)

def load_background_image():
    # Load the image
    background_image_ref = Image.open('assets/images/login-background.jpg')
    background_image = ImageTk.PhotoImage(background_image_ref)
    # Put the image in the image section
    image_wrapper = Label(image_section, image=background_image, width=root_container_width / 2,
                          height=root_container_height)
    image_wrapper.image_names = [background_image]
    image_wrapper.pack()


def create_image_section():
    global image_section
    # Create the section container
    image_section = Canvas(register_page, width=root_container_width / 2, height=root_container_height, borderwidth=0,
                           highlightthickness=0)
    image_section.grid(row=0, column=1)
    image_section.grid_propagate(False)
    # Load the background image and put it in the container
    load_background_image()


def create_register_form_container():
    global register_form_container
    register_form_container = Canvas(register_section, width=450, height=450, bg='#ffffff', borderwidth=0,
                                  highlightthickness=0)
    register_form_container.create_text(0, 0, anchor=NW, text='Create an account', fill='#101828', font=('Inter 26 bold'))


def create_name_field():
    register_form_container.create_text(0, 46, anchor=NW, text='Name', font=('Inter 14 normal'), fill='#344054')
    name_field = Canvas(register_form_container, width=360, height=1, borderwidth=0, highlightthickness=0)
    # Create the name input field and fill it with placeholder
    name_input = Entry(name_field, fg='#667085', font=('Inter 14 normal'), border=0, highlightthickness=2, \
                        highlightcolor='#d0d5dd', highlightbackground='#d0d5dd')
    name_input.insert(0, 'Enter your name')
    name_field.create_window(0, 34, anchor=NW, width=360, window=name_input)
    name_input.pack(ipadx=3, ipady=1)
    # Remove the placeholder on focus
    name_input.bind('<FocusIn>', lambda args: name_input.delete('0', 'end'))
    # Put the field inside the login form container
    register_form_container.create_window(0, 70, anchor=NW, window=name_field)
    return name_input
def create_lastname_field():
    register_form_container.create_text(0, 116, anchor=NW, text='Last name', font=('Inter 14 normal'), fill='#344054')
    lname_field = Canvas(register_form_container, width=360, height=1, borderwidth=0, highlightthickness=0)
    # Create the last name input field and fill it with placeholder
    lname_input = Entry(lname_field, fg='#667085', font=('Inter 14 normal'), border=0, highlightthickness=2, \
                        highlightcolor='#d0d5dd', highlightbackground='#d0d5dd')
    lname_input.insert(0, 'Enter your last name')
    lname_field.create_window(0, 34, anchor=NW, width=360, window=lname_input)
    lname_input.pack(ipadx=3, ipady=1)
    # Remove the placeholder on focus
    lname_input.bind('<FocusIn>', lambda args: lname_input.delete('0', 'end'))
    # Put the field inside the login form container
    register_form_container.create_window(0, 140, anchor=NW, window=lname_field)
    return lname_input
def create_email_field():
    register_form_container.create_text(0, 186, anchor=NW, text='Email', font=('Inter 14 normal'), fill='#344054')
    email_field = Canvas(register_form_container, width=360, height=1, borderwidth=0, highlightthickness=0)
    # Create the email input field and fill it with placeholder
    email_input = Entry(email_field, fg='#667085', font=('Inter 14 normal'), border=0, highlightthickness=2, \
                        highlightcolor='#d0d5dd', highlightbackground='#d0d5dd')
    email_input.insert(0, 'Enter your email')
    email_field.create_window(0, 34, anchor=NW, width=360, window=email_input)
    email_input.pack(ipadx=3, ipady=1)
    # Remove the placeholder on focus
    email_input.bind('<FocusIn>', lambda args: email_input.delete('0', 'end'))
    # Put the field inside the login form container
    register_form_container.create_window(0, 210, anchor=NW, window=email_field)
    return email_input

def create_password_field():
    register_form_container.create_text(0, 256, anchor=NW, text='Password', font=('Inter 14 normal'), fill='#344054')
    password_field = Canvas(register_form_container, width=360, height=1, borderwidth=0, highlightthickness=0)
    # Create the password input field and fill it with placeholder
    password_input = Entry(password_field, fg='#667085', font=('Inter 14 normal'), border=0, highlightthickness=2, \
                        highlightcolor='#d0d5dd', highlightbackground='#d0d5dd', show='*')
    password_input.insert(0, 'Enter your password')
    password_field.create_window(0, 34, anchor=NW, width=360, window=password_input)
    password_input.pack(ipadx=3, ipady=1)
    # Remove the placeholder on focus
    password_input.bind('<FocusIn>', lambda args: password_input.delete('0', 'end'))
    # Put the field inside the login form container
    register_form_container.create_window(0, 280, anchor=NW, window=password_field)
    return password_input

def create_cpassword_field():
    register_form_container.create_text(0, 326, anchor=NW, text='Confirm password', font=('Inter 14 normal'), fill='#344054')
    cpassword_field = Canvas(register_form_container, width=360, height=1, borderwidth=0, highlightthickness=0)
    # Create the confrim password input field and fill it with placeholder
    cpassword_input = Entry(cpassword_field, fg='#667085', font=('Inter 14 normal'), border=0, highlightthickness=2, \
                        highlightcolor='#d0d5dd', highlightbackground='#d0d5dd', show='*')
    cpassword_input.insert(0, 'Confirm your password')
    cpassword_field.create_window(0, 34, anchor=NW, width=360, window=cpassword_input)
    cpassword_input.pack(ipadx=3, ipady=1)
    # Remove the placeholder on focus
    cpassword_input.bind('<FocusIn>', lambda args: cpassword_input.delete('0', 'end'))
    # Put the field inside the login form container
    register_form_container.create_window(0, 350, anchor=NW, window=cpassword_field)
    return cpassword_input



def show_password():
    root.close_eye = PhotoImage(file='assets/icons/hide.png')
    hide_button = Button(root, image=root.close_eye, command=hide_password, relief=FLAT, activebackground='#ffffff', bd=0, background='#ffffff', cursor='hand2')
    hide_button.place(x=356, y= 435)
    field = create_password_field()
    field.config(show='')

def hide_password():
    show_button = Button(root, image=root.open_eye, command=show_password, relief=FLAT, activebackground='#ffffff', bd=0, background='#ffffff', cursor='hand2')
    show_button.place(x=356, y= 435)
    field = create_password_field()
    field.config(show='*')

def show_cpassword():

    hide_button2 = Button(root, image=root.close_eye, command=hide_cpassword, relief=FLAT, activebackground='#ffffff', bd=0, background='#ffffff', cursor='hand2')
    hide_button2.place(x=356, y= 505)
    field = create_cpassword_field()
    field.config(show='')

def hide_cpassword():
    show_button2 = Button(root, image=root.open_eye, command=show_cpassword, relief=FLAT, activebackground='#ffffff', bd=0, background='#ffffff', cursor='hand2')
    show_button2.place(x=356, y= 505)
    field = create_cpassword_field()
    field.config(show='*')

def create_buttons():

    # Create the sign up button
    register_button = Button(text='Sign up', padx=60, font=('Inter 14 bold'), background='#7F56D9', fg='#ffffff', cursor='hand2')
    register_form_container.create_window(13, 440, anchor=NW, window=register_button)
    # Create show buttons
    root.open_eye=PhotoImage(file='assets/icons/show.png')
    show_button1 = Button(root, image=root.open_eye, relief=FLAT, activebackground='#ffffff', bd=0, background='#ffffff', cursor='hand2', command=show_password)
    show_button1.place(x=356, y= 435)
    show_button2 = Button(root, image=root.open_eye, relief=FLAT, activebackground='#ffffff', bd=0, background='#ffffff', cursor='hand2', command=show_cpassword )
    show_button2.place(x=356, y=505)
    # Create check button
    check_button = Checkbutton(root, text = 'I agree to the Terms & Conditions', font=('Inter 10 bold'), fg='#7F56D9', bg='#ffffff', activebackground='#ffffff', activeforeground='#7F56D9', cursor='hand2')
    check_button.place(x=150, y=550)

def create_register_form():
    create_register_form_container()
    # Create the form fields
    create_name_field()
    create_lastname_field()
    create_email_field()
    create_password_field()
    create_cpassword_field()
    # Create the form action buttons
    create_buttons()
    # Put the login form inside the login section
    register_section.create_window(150, 150, anchor=NW, window=register_form_container)


def load_header_logo():
    # Load the logo image
    header_logo_ref = Image.open('assets/icons/logo.ico')
    header_logo = ImageTk.PhotoImage(header_logo_ref)
    # Put the logo inside the header
    register_section_header.create_image(0, 0, anchor=NW, image=header_logo)
    register_section_header.image_names = [header_logo]


def create_register_header():
    global register_section_header
    # Create the header
    register_section_header = Canvas(register_section, width=430, height=64, bg='#ffffff', borderwidth=0,
                                  highlightthickness=0)
    register_section_header.create_text(100, 32, anchor=NW, text='Zakopane Autonomous Rides', font=('Inter 15 bold'),
                                     fill='#101828')
    load_header_logo()
    # Put the header in the login section
    register_section.create_window(32, 0, anchor=NW, window=register_section_header)


def create_register_section():
    create_register_section_container()
    create_register_header()
    create_register_form()
    # Create the login section footer
    register_section.create_text(32, root_container_height - 32, anchor=NW, text='© Zakopane Autonomous Rides 2023', \
                              font=('Inter 12 normal'), fill='#475467')

def load_register_page(root_, root_dimensions):
    global root
    global register_page
    global root_container_width
    global root_container_height
    # Get the root container
    root = root_
    root_container_width = root_dimensions[0]
    root_container_height = root_dimensions[1]
    # Create the login page container
    register_page = Canvas(root, width=root_container_width, height=root_container_height, borderwidth=0,
                        highlightthickness=0)
    register_page.pack()
    # Create login page sections
    create_register_section()
    create_image_section()


if __name__ == '__main__':
    load_register_page()


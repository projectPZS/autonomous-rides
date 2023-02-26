from tkinter import *
from pages.dashboard import load_dashboard
from pages.sidebar import load_sidebar
    
def load_main_content_page(parent_, parent_dimensions):
    global parent
    global parent_container_width
    global parent_container_height
    global main_content_page
    # Get the root container
    parent = parent_
    root_container_width = parent_dimensions[0]
    root_container_height = parent_dimensions[1]
    # Create the main-content page container
    main_content_page = Canvas(parent, width=root_container_width, height=root_container_height, borderwidth=0,\
                             highlightthickness=0, bg="#faf8f2")
    main_content_page.pack()
    # Create main-content page sections
    load_dashboard(main_content_page, (main_content_page.winfo_width(), main_content_page.winfo_height()))
    load_sidebar(main_content_page, (main_content_page.winfo_width(), main_content_page.winfo_height()))
if __name__ == '__main__':
    load_main_content_page()
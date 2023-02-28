from tkinter import *
from pages.login import load_login_page


def set_root_dimensions():
    global root_container_width
    global root_container_height
    root.geometry('1280x720'.format(root.winfo_screenwidth, root.winfo_screenheight))
    root.resizable(False, False)
    root.update()
    root_container_width = root.winfo_width()
    root_container_height = root.winfo_height()

def create_root_container():
    global root
    root = Tk()
    root.title('Zakopane Autonomous Rides')
    # Root dimensions settings
    set_root_dimensions()
    # Set the little icon in the application's top left corner
    root.iconbitmap('assets/icons/logo.ico')
    
    return (root_container_width, root_container_height)

if __name__ == '__main__':
    root_dimensions = create_root_container()
    load_login_page(root, root_dimensions)
    root.mainloop()
from tkinter import *
import pages.dashboard as dashboard
import pages.previous_view as previous_view
import pages.touristic_routes as tr


def load_morskie_oko():
    global morskie_oko_section
    dashboard.dashboard_cards_container.destroy()
    if (previous_view.previous_view != ''):
        previous_view.previous_view.destroy()

    morskie_oko_section = Canvas(dashboard.dashboard, width=1100, height=600, borderwidth=0, highlightthickness=0,
                                      background="#ffffff")
    morskie_oko_section.create_text(400, 0, anchor=NW, text="Morskie Oko", fill='#101828',
                                         font=('Inter 20 bold'))
    dashboard.dashboard.create_window(0, 125, anchor=NW, window=morskie_oko_section)
    previous_view.previous_view = morskie_oko_section
    morskie_oko_section.create_text(75, 50, anchor=NW, text="Chrancówki 35 Station", fill='#36454F',
                                       font=('Inter 16 bold'))

    morskie_oko_section.create_text(75, 130, anchor=NW, text="Schedule:", fill='#36454F',
                                       font=('Inter 16 bold'))
    morskie_oko_section.create_text(75, 80, anchor=NW, text="Duration of the course:", fill='#36454F',
                                       font=('Inter 10 normal'))
    morskie_oko_section.create_text(75, 100, anchor=NW, text="Distance of the course:", fill='#36454F',
                                       font=('Inter 10 normal'))

    morskie_oko_section.create_text(75, 170, anchor=NW, text="Departue at: ", fill='#36454F',
                                       font=('Inter 12 normal'))
    morskie_oko_section.create_text(275, 170, anchor=NW, text="Price: ", fill='#36454F',
                                       font=('Inter 12 normal'))

    morskie_oko_section.book_img = PhotoImage(file='assets/icons/basket.png')
    book_button1 = Button(morskie_oko_section, image = morskie_oko_section.book_img, relief=FLAT, activebackground='#ffffff', bd=0, background='#ffffff', cursor='hand2',)
    book_button1.place(x=220, y=155)

    morskie_oko_section.create_text(650, 50, anchor=NW, text="Al. 3 Maja Dolne Station",
                                       fill='#36454F',
                                       font=('Inter 16 bold'))
    morskie_oko_section.create_text(650, 130, anchor=NW, text="Schedule:", fill='#36454F',
                                       font=('Inter 16 bold'))
    morskie_oko_section.create_text(650, 80, anchor=NW, text="Duration of the course: ", fill='#36454F',
                                       font=('Inter 10 normal'))
    morskie_oko_section.create_text(650, 100, anchor=NW, text="Distance of the course: ", fill='#36454F',
                                       font=('Inter 10 normal'))
    morskie_oko_section.create_text(650, 170, anchor=NW, text="Departue at: ", fill='#36454F',
                                       font=('Inter 12 normal'))
    morskie_oko_section.create_text(850, 170, anchor=NW, text="Price: ", fill='#36454F',
                                       font=('Inter 12 normal'))
    book_button2 = Button(morskie_oko_section, image=morskie_oko_section.book_img, relief=FLAT,
                          activebackground='#ffffff', bd=0, background='#ffffff', cursor='hand2', )
    book_button2.place(x=795, y=155)
    morskie_oko_section.narrow = PhotoImage(file='assets/icons/narrow.png')
    back_button = Button(morskie_oko_section, image=morskie_oko_section.narrow, font=('Inter 12 bold'), relief=FLAT, activebackground='#ffffff', bd=0,
                         background='#ffffff', cursor='hand2', command=back)
    back_button.place(x=20, y=0)

def back():
    previous_view.previous_view.destroy()
    tr.load_touristic_routes()


if __name__ == '__main__':
    load_morskie_oko()
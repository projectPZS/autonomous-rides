from tkinter import *
import pages.dashboard as dashboard
import pages.previous_view as previous_view
import pages.touristic_routes as tr


def load_dolina_koscieliska():
    global dolina_koscielisk_section
    dashboard.dashboard_cards_container.destroy()
    if (previous_view.previous_view != ''):
        previous_view.previous_view.destroy()

    dolina_koscielisk_section = Canvas(dashboard.dashboard, width=1100, height=600, borderwidth=0, highlightthickness=0,
                                      background="#ffffff")
    dolina_koscielisk_section.create_text(350, 0, anchor=NW, text="Dolina Koscieliska", fill='#101828',
                                         font=('Inter 20 bold'))
    dashboard.dashboard.create_window(0, 125, anchor=NW, window=dolina_koscielisk_section)
    previous_view.previous_view = dolina_koscielisk_section
    dolina_koscielisk_section.create_text(75, 50, anchor=NW, text="Chrancówki 35 Station", fill='#36454F',
                                       font=('Inter 16 bold'))

    dolina_koscielisk_section.create_text(75, 130, anchor=NW, text="Schedule:", fill='#36454F',
                                       font=('Inter 16 bold'))
    dolina_koscielisk_section.create_text(75, 80, anchor=NW, text="Duration of the course:", fill='#36454F',
                                       font=('Inter 10 normal'))
    dolina_koscielisk_section.create_text(75, 100, anchor=NW, text="Distance of the course:", fill='#36454F',
                                       font=('Inter 10 normal'))

    dolina_koscielisk_section.create_text(75, 170, anchor=NW, text="Departue at: ", fill='#36454F',
                                       font=('Inter 12 normal'))
    dolina_koscielisk_section.create_text(275, 170, anchor=NW, text="Price: ", fill='#36454F',
                                       font=('Inter 12 normal'))

    dolina_koscielisk_section.book_img = PhotoImage(file='assets/icons/basket.png')
    book_button1 = Button(dolina_koscielisk_section, image = dolina_koscielisk_section.book_img, relief=FLAT, activebackground='#ffffff', bd=0, background='#ffffff', cursor='hand2',)
    book_button1.place(x=220, y=155)

    dolina_koscielisk_section.create_text(650, 50, anchor=NW, text="Al. 3 Maja Dolne Station",
                                       fill='#36454F',
                                       font=('Inter 16 bold'))
    dolina_koscielisk_section.create_text(650, 130, anchor=NW, text="Schedule:", fill='#36454F',
                                       font=('Inter 16 bold'))
    dolina_koscielisk_section.create_text(650, 80, anchor=NW, text="Duration of the course: ", fill='#36454F',
                                       font=('Inter 10 normal'))
    dolina_koscielisk_section.create_text(650, 100, anchor=NW, text="Distance of the course: ", fill='#36454F',
                                       font=('Inter 10 normal'))
    dolina_koscielisk_section.create_text(650, 170, anchor=NW, text="Departue at: ", fill='#36454F',
                                       font=('Inter 12 normal'))
    dolina_koscielisk_section.create_text(850, 170, anchor=NW, text="Price: ", fill='#36454F',
                                       font=('Inter 12 normal'))
    book_button2 = Button(dolina_koscielisk_section, image=dolina_koscielisk_section.book_img, relief=FLAT,
                          activebackground='#ffffff', bd=0, background='#ffffff', cursor='hand2', )
    book_button2.place(x=795, y=155)
    dolina_koscielisk_section.narrow = PhotoImage(file='assets/icons/narrow.png')
    back_button = Button(dolina_koscielisk_section, image=dolina_koscielisk_section.narrow, font=('Inter 12 bold'), relief=FLAT, activebackground='#ffffff', bd=0,
                         background='#ffffff', cursor='hand2', command=back)
    back_button.place(x=20, y=0)

def back():
    previous_view.previous_view.destroy()
    tr.load_touristic_routes()

if __name__ == '__main__':
    load_dolina_koscieliska()
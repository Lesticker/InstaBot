from tkinter import *


class Settings:
    def __init__(self, top):
        frame_e = Frame(top)
        frame_e.pack()
        self.entered_login = StringVar()
        self.entered_password = StringVar()
        self.entered_hashtag = StringVar()
        self.entered_number_of_likes = IntVar()

        login_label = Label(frame_e, text="User Name: ")
        login_label.pack()
        login = Entry(frame_e, textvariable=self.entered_login, bg="white")
        login.pack()
        login.focus_force()

        password_label = Label(frame_e, text="password: ")
        password_label.pack()
        password = Entry(frame_e, textvariable=self.entered_password, show='*', bg="white")
        password.pack()

        hashtag_label = Label(frame_e, text="hashtag: ")
        hashtag_label.pack()
        hashtag = Entry(frame_e, textvariable=self.entered_hashtag, bg="white")
        hashtag.pack()

        number_of_likes_label = Label(frame_e, text="how many likes?: ")
        number_of_likes_label.pack()
        likes = Entry(frame_e, textvariable=self.entered_number_of_likes, bg="white")
        likes.pack()

        button = Button(frame_e, text="Accept", command=self.naming)
        button.pack(side=BOTTOM, anchor=S)

    def naming(self):
        self.entered_login = self.entered_login.get()
        self.entered_password = self.entered_password.get()
        self.entered_hashtag = self.entered_hashtag.get()
        self.entered_number_of_likes = self.entered_number_of_likes.get()
        root.destroy()


root = Tk()
root.geometry = "100x100+100+50"

settings_data = Settings(root)

root.mainloop()

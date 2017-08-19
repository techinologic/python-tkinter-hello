from tkinter import *
from tkinter import ttk


class HelloUser:
    def __init__(self, master):
        self.label = ttk.Label(master, text="Hello, who are you?")
        self.label.grid(row=0, column=0, columnspan=2)

        ttk.Button(master, text="Paopao",
                   command=self.paopao_hello).grid(row=1, column=0)
        ttk.Button(master, text="Zenzen",
                   command=self.zenzen_hello).grid(row=1, column=1)

    def paopao_hello(self):
        self.label.config(text="Hello, Paopao!")

    def zenzen_hello(self):
        self.label.config(text="Hello, Zenzen!")


def main():
    root = Tk()
    app = HelloUser(root)
    root.mainloop()


if __name__ == "__main__": main()

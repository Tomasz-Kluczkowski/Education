from tkinter import *
from book_database_backend_OOP import Database


class GuiBookStore(Tk):
    def __init__(self):
        super().__init__()
            
        self.l1 = Label(self, text="Title")
        self.l1.grid(row=0, column=0)
    
        self.l2 = Label(self, text="Author")
        self.l2.grid(row=0, column=2)
        
        self.l3 = Label(self, text="Year")
        self.l3.grid(row=1, column=0)
        
        self.l4 = Label(self, text="ISBN")
        self.l4.grid(row=1, column=2)
        
        self.title_text = StringVar()
        self.e1 = Entry(self, textvariable=self.title_text)
        self.e1.grid(row=0, column=1)
    
        self.author_text = StringVar()
        self.e2 = Entry(self, textvariable=self.author_text)
        self.e2.grid(row=0, column=3)
        
        self.year_text = StringVar()
        self.e3 = Entry(self, textvariable=self.year_text)
        self.e3.grid(row=1, column=1)
        
        self.isbn_text = StringVar()
        self.e4 = Entry(self, textvariable=self.isbn_text)
        self.e4.grid(row=1, column=3)
        
        self.list1 = Listbox(self, height=6, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)
    
        self.sb1 = Scrollbar(self)
        self.sb1.grid(row=2, column=2, rowspan=6)
    
        self.list1.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.list1.yview)

        self.list1.bind("<<ListboxSelect>>", self.get_selected_row)

        button_names = ["View all", "Search entry", "Add entry", "Update selected", "Delete selected", "Close"]
        command_list = [self.view_command, self.search_command, self.add_command, self.update_command,
                        self.delete_command, self.destroy]
        self.buttons = {}

        for button_name, command, row in zip(button_names, command_list, range(2, 8)):
            self.buttons[button_name] = Button(self, text=button_name, width=12, command=command)
            self.buttons[button_name].grid(row=row, column=3)

    def get_selected_row(self, event):
        global selected_tuple
        try:
            index = self.list1.curselection()[0]
            selected_tuple = self.list1.get(index)
            for i, entry in enumerate([self.e1, self.e2, self.e3, self.e4]):
                entry.delete(0, END)
                entry.insert(END, selected_tuple[i+1])
        except IndexError:
            pass

    def view_command(self):
        self.list1.delete(0, END)
        for row in database.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(),
                                   self.isbn_text.get()):
            self.list1.insert(END, row)

    def add_command(self):
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.
                                isbn_text.get()))

    def delete_command(self):
        database.delete(selected_tuple[0])

    def update_command(self):
        database.update(selected_tuple[0], self.title_text.get(), self.author_text.get(), self.year_text.get(),
                        self.isbn_text.get())


database = Database("books.db")
app = GuiBookStore()
app.mainloop()

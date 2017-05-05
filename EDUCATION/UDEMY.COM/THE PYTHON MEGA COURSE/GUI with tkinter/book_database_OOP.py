from tkinter import *
from book_database_backend_OOP import Database


class GUI_book_store(Tk):
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
    
        self.list1.configure(yscrollcommand=sb1.set)
        self.sb1.configure(command=list1.yview)
    
        self.list1.bind("<<ListboxSelect>>", get_selected_row)

        button_names = ["View all", "Search entry", "Add entry", "Update selected", "Delete selected", "Close"]
        command_list = [view_command, search_command, add_command, update_command, delete_command, self.destroy]
        self.buttons = {}

        for button_name, command, row in zip(button_names, command_list, range(2, 8)):
            self.buttons[button_name] = Button(self, text=button_name, width=12, command=command)
            self.buttons[button_name].grid(row=row, column=3)

        # b1 = Button(self, text="View all", width=12, command=view_command)
        # b1.grid(row=2, column=3)
        #
        # b2 = Button(self, text="Search entry", width=12, command=search_command)
        # b2.grid(row=3, column=3)
        #
        # b3 = Button(self, text="Add entry", width=12, command=add_command)
        # b3.grid(row=4, column=3)
        #
        # b4 = Button(self, text="Update selected", width=12, command=update_command)
        # b4.grid(row=5, column=3)
        #
        # b5 = Button(self, text="Delete selected", width=12, command=delete_command)
        # b5.grid(row=6, column=3)
        #
        # b6 = Button(self, text="Close", width=12, command=self.destroy)
        # b6.grid(row=7, column=3)



# def get_selected_row(event):
#     global selected_tuple
#     try:
#         index = list1.curselection()[0]
#         selected_tuple = list1.get(index)
#         e1.delete(0, END)
#         e1.insert(END, selected_tuple[1])
#         e2.delete(0, END)
#         e2.insert(END, selected_tuple[2])
#         e3.delete(0, END)
#         e3.insert(END, selected_tuple[3])
#         e4.delete(0, END)
#         e4.insert(END, selected_tuple[4])
#     except IndexError:
#         pass
#
#
# def view_command():
#     list1.delete(0, END)
#     for row in database.view():
#         list1.insert(END, row)
#
#
# def search_command():
#     list1.delete(0, END)
#     for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
#         list1.insert(END, row)
#
#
# def add_command():
#     database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
#     list1.delete(0, END)
#     list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
#
#
# def delete_command():
#     database.delete(selected_tuple[0])
#
#
# def update_command():
#     database.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


database = Database("books.db")
app = GUI_book_store()
app.mainloop()

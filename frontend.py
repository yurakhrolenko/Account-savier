import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import pyperclip

# my modules
import backend


class Window:

    def __init__(self, window):
        """
        Basicly frontend of the main window
        """

        # initializing
        self.db = backend.Database()
        self.key = 'ghbdtnhf'
        window_height = 620
        window_width = 840
        self.bg = 'LightBlue1'
        self.window = window
        self.window.geometry(f'{window_width}x{window_height}')
        self.window.resizable(width=False, height=False)
        self.window.wm_title("Accounts Savier")
        self.window.configure(bg=self.bg)

        # all LABLES widgets on the main window
        label_login = tk.Label(self.window, text='Add New Login')
        label_login.config(font=("Comic 25 italic"), bg=self.bg)
        label_login.place(x=300, y=10)

        label_login = tk.Label(self.window, text='Login: ')
        label_login.config(font=("Comic 12 italic"), bg=self.bg)
        label_login.place(x=30, y=70)

        label_password = tk.Label(self.window, text='Password: ')
        label_password.config(font=("Comic 12 italic"), bg=self.bg)
        label_password.place(x=30, y=105)

        label_password = tk.Label(self.window, text='Site: ')
        label_password.config(font=("Comic 12 italic"), bg=self.bg)
        label_password.place(x=30, y=140)

        label_comment = tk.Label(self.window, text='Comment: ')
        label_comment.config(font=("Comic 12 italic"), bg=self.bg)
        label_comment.place(x=430, y=70)

        label_results = tk.Label(self.window, text='Accounts: ')
        label_results.config(font=("Courier", 10), bg=self.bg)
        label_results.place(x=30, y=250)

        # all INPUTS widgets on the main window
        self.login_input_var = tk.StringVar()
        self.login_entry = tk.Entry(self.window,
                                    font=("Comic 12 italic"),
                                    textvariable=self.login_input_var)
        self.login_entry.place(x=170, y=70, width=230, height=30)

        self.password_input_var = tk.StringVar()
        self.password_entry = tk.Entry(self.window,
                                       font=("Comic 12 italic"),
                                       show="*",
                                       textvariable=self.password_input_var)
        self.password_entry.place(x=170, y=105, width=230, height=30)

        self.site_input_var = tk.StringVar()
        self.site_entry = tk.Entry(self.window,
                                   font=("Comic 12 italic"),
                                   textvariable=self.site_input_var)
        self.site_entry.place(x=170, y=140, width=230, height=30)

        self.search_entry = EntryWithPlaceholder(self.window, 'write here to find')
        self.search_entry.place(x=30, y=500, width=387, height=30)

        self.comment_text = ScrolledText(self.window, width=30, height=6)
        self.comment_text.place(x=540, y=70)

        # all BUTTONS widgets on the main window
        button_clear = tk.Button(self.window, text='Clear', command=self.clear)
        button_clear.config(width="10",
                            height="1",
                            font=("Comic 12 italic"),
                            activebackground='SpringGreen2',
                            bd=1)
        button_clear.place(x=700, y=175)

        button_submit = tk.Button(self.window, text='Submit', command=self.submit)
        button_submit.config(width="15",
                             height="2",
                             font=("Comic 15 italic"),
                             activebackground='SpringGreen2',
                             bd=1)
        button_submit.place(x=360, y=180)

        button_delete = tk.Button(self.window, text='Delete', command=self.delete_account)
        button_delete.config(width=15,
                             height=2,
                             font=("Comic 12 italic"),
                             activebackground='SpringGreen2',
                             bd=1)
        button_delete.place(x=650, y=390)

        button_update = tk.Button(self.window, text='Update', command=self.update_account)
        button_update.config(width=15,
                             height=2,
                             font=("Comic 12 italic"),
                             activebackground='SpringGreen2',
                             bd=1)
        button_update.place(x=650, y=330)

        button_refresh = tk.Button(self.window, text='Refresh', command=self.view_accounts)
        button_refresh.config(width=15,
                              height=2,
                              font=("Comic 12 italic"),
                              activebackground='SpringGreen2',
                              bd=1)
        button_refresh.place(x=650, y=270)

        button_close = tk.Button(self.window, text='Close', command=self.window.destroy)
        button_close.config(width=15,
                            height=2,
                            font=("Comic 12 italic"),
                            activebackground='SpringGreen2',
                            bd=1)
        button_close.place(x=650, y=450)

        button_copy_login = tk.Button(self.window, text='Copy\nLogin', command=self.copy_login)
        button_copy_login.config(width=12,
                                 height=2,
                                 font=("Comic 12 italic"),
                                 activebackground='SpringGreen2',
                                 bd=1)
        button_copy_login.place(x=30, y=440)

        button_copy_password = tk.Button(self.window, text='Copy\nPassword', command=self.copy_password)
        button_copy_password.config(width=12,
                                    height=2,
                                    font=("Comic 12 italic"),
                                    activebackground='SpringGreen2',
                                    bd=1)
        button_copy_password.place(x=160, y=440)

        button_copy_site = tk.Button(self.window, text='Copy\nSite', command=self.copy_site)
        button_copy_site.config(width=12,
                                height=2,
                                font=("Comic 12 italic"),
                                activebackground='SpringGreen2',
                                bd=1)
        button_copy_site.place(x=290, y=440)

        button_read_comment = tk.Button(self.window, text='Read\nComment', command=self.read_comment)
        button_read_comment.config(width=12,
                                   height=2,
                                   font=("Comic 12 italic"),
                                   activebackground='SpringGreen2',
                                   bd=1)
        button_read_comment.place(x=420, y=440)

        button_search = tk.Button(self.window, text='Search', command=self.search)
        button_search.config(width=12,
                             height=1,
                             font=("Comic 12 italic"),
                             activebackground='SpringGreen2',
                             bd=1)
        button_search.place(x=420, y=500)

        # more widgets on the main window
        self.listbox = tk.Listbox(self.window, font=("Comic 12 italic"))
        self.listbox.bind('<<ListboxSelect>>', self.get_selected_row)
        self.listbox.place(x=30, y=275, width=500, height=150)

        scrollbar = tk.Scrollbar(self.window)
        scrollbar.place(x=535, y=275, height=150)

        self.listbox.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.listbox.yview)
        self.view_accounts()

        self.var = tk.IntVar()
        self.var.set(0)

        all_radio = tk.Radiobutton(self.window, text='Search in all fields', variable=self.var, value=0, bg=self.bg)
        all_radio.place(x=30, y=550)

        login_radio = tk.Radiobutton(self.window, text="Login", variable=self.var, value=1, bg=self.bg)
        login_radio.place(x=175, y=550)

        password_radio = tk.Radiobutton(self.window, text="Password", variable=self.var, value=2, bg=self.bg)
        password_radio.place(x=175, y=580)

        site_radio = tk.Radiobutton(self.window, text="Site", variable=self.var, value=3, bg=self.bg)
        site_radio.place(x=300, y=550)

        comment_radio = tk.Radiobutton(self.window, text="Comment", variable=self.var, value=4, bg=self.bg)
        comment_radio.place(x=300, y=580)

    def get_search_mode(self):
        """
        Takes selected radio widget from main window to set search mode

        :return: int (returns '' if search data is not valid)
        """
        var = self.var.get()
        search_request = self.search_entry.get()
        if search_request == 'write here to find' or search_request == '':
            self.error_sellect('== Write your search request first in Search field ==')
            results = ''
        elif var == 0:
            results = self.db.search(login=search_request,
                                     password=search_request,
                                     site=search_request,
                                     comment=search_request)
        elif var == 1:
            results = self.db.search(login=search_request)
        elif var == 2:
            results = self.db.search(password=search_request)
        elif var == 3:
            results = self.db.search(site=search_request)
        elif var == 4:
            results = self.db.search(comment=search_request)
        else:
            results = ''
        return [results]

    def search(self):
        """
        Inserts all search results in self.listbox

        :return: None
        """
        search_mode = self.get_search_mode()
        if search_mode != ['']:
            self.listbox.delete(0, tk.END)
            for item in search_mode:
                self.listbox.insert(tk.END, item)


    def clear(self):
        """
        Clear all input fields at the main window
        :return: None
        """
        self.login_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.site_entry.delete(0, tk.END)
        self.comment_text.delete("1.0", tk.END)

    def view_accounts(self):
        """
        Gets all rows from database and inserting it into self.listbox
        :return: None
        """
        self.listbox.delete(0, tk.END)
        for item in self.db.view_all():
            self.listbox.insert(tk.END, item)

    def get_selected_row(self, event):
        """
        Creates a tuple that have been selected in self.listbox with data from selected row.
        :param event:
        :return: tuple
        """
        try:
            index = self.listbox.curselection()[0]
            self.selected_tuple = self.listbox.get(index)
        except IndexError:
            self.selected_tuple = ('', '', '', '', '')
        return self.selected_tuple

    def delete_account(self):
        """
        Delete selected row from database.
        :return: None
        """
        if self.get_selected_row(self) != ('', '', '', '', ''):
            selected_row = self.get_selected_row(self)
            self.db.delete(selected_row[0])
            self.view_accounts()
        else:
            self.error_sellect("A row shoud be selected first!")

    def update_account(self):
        """
        Creates class object (and separate window) with inputs to update
        :return: None
        """
        if self.get_selected_row(self) != ('', '', '', '', ''):
            selected_row = self.get_selected_row(self)
            window_update = tk.Tk()
            UpdateWindow(window_update, selected_row)
            window_update.mainloop()
        else:
            self.error_sellect("A row shoud be selected!")

    def error_sellect(self, text):
        """
        Raise a popup window when trying to do  action without selection but action needs to have selection
        in self.listbow and det a tuple from self.listbox

        :param test: str
        :return: None
        """
        messagebox.showerror("Error", text)

    def submit(self):
        """
        Creates tuple with data from self.login_entry, self.password_entry, self.site_entry, self.comment_text and
        saves it into database as a new row.
        :return: None
        """

        login = self.login_input_var.get()
        password = self.password_input_var.get()
        site = self.site_input_var.get()
        comment = self.comment_text.get("1.0", tk.END)
        if (login, password, site, comment) != ('', '', '', '\n'):
            self.db.insert((login, password, site, comment))
            self.view_accounts()

    def copy_login(self):
        """
        Saves login field from selected row in to the exchange bucher
        :return: None
        """
        if not self.get_selected_row(self) == ('', '', '', '', ''):
            pyperclip.copy(self.get_selected_row(self)[1])
        else:
            self.error_sellect("A row shoud be selected first!")

    def copy_password(self):
        """
        Saves password field from selected row in to the exchange bucher
        :return: None
        """
        if not self.get_selected_row(self) == ('', '', '', '', ''):
            pyperclip.copy(self.get_selected_row(self)[2])
        else:
            self.error_sellect("A row shoud be selected first!")

    def copy_site(self):
        """
        Saves site field from selected row in to the exchange bucher
        :return: None
        """
        if not self.get_selected_row(self) == ('', '', '', '', ''):
            pyperclip.copy(self.get_selected_row(self)[3])
        else:
            self.error_sellect("A row shoud be selected first!")

    def read_comment(self):
        """
        Creates tkinter popup window with bigger font inside comment input field to make it more readable.
        Also updates data in comment field in selected row in listbox
        :return: None
        """
        if not self.get_selected_row(self) == ('', '', '', '', ''):
            selected_row = self.get_selected_row(self)
            window_comment = tk.Tk()
            CommentWindow(window_comment, selected_row)
            window_comment.mainloop()
        else:
            self.error_sellect("A row shoud be selected first!")


class EntryWithPlaceholder(tk.Entry):
    """
    Entry class that that creates an object widget with placeholder in it.
    """

    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        """
        Inserting a placeholder text into the entry widget
        :return: None
        """
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        """
        Clears widget field while focus is on widget
        :return:
        """
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        """
        Inserts placeholder's text into widget if it's unfocused
        :return:
        """
        if not self.get():
            self.put_placeholder()


class CommentWindow:
    """
    Creates tkinter popup window with biger font in text widget to make it more reasable.
    Changes in text widget will update comment field in selected row from Window.listbox in database
    """

    def __init__(self, win, selected_row):
        self.win = win
        self.selected_row = selected_row

        window_height = 250
        window_width = 515
        self.bg = 'LightBlue1'
        self.win.geometry(f'{window_width}x{window_height}')
        self.win.resizable(width=False, height=False)
        self.win.wm_title("Accounts Savier")
        self.win.configure(bg=self.bg)

        label_login = tk.Label(self.win, text='Comment: ')
        label_login.config(font=("Comic 12 italic"))
        label_login.place(x=20, y=10)

        self.comment_text = tk.Text(self.win, font=("Comic 16 italic"), width=39, height=6)
        self.comment_text.place(x=20, y=40)

        button_ok = tk.Button(self.win, text='OK', command=self.ok_command)
        button_ok.place(x=150, y=200, width=100)

        button_cancel = tk.Button(self.win, text='Cancel', command=self.win.destroy)
        button_cancel.place(x=270, y=200, width=100)

        self.comment_text.insert(tk.END, self.selected_row[4])

        self.db = backend.Database()

    def ok_command(self):
        """
        Saves changes in comment field for selected row and closes the popup window
        :return: None
        """
        comment = self.comment_text.get("1.0", tk.END)
        self.db.update(id=self.selected_row[0],
                       login=self.selected_row[1],
                       password=self.selected_row[2],
                       site=self.selected_row[3],
                       comment=comment)
        self.win.destroy()


class UpdateWindow:
    """
    Creates update popup window to set all changes in database for selected in listbow row row
    """

    def __init__(self, window_update, selected_row):
        self.db = backend.Database()
        self.bg = 'LightBlue1'
        self.window_update = window_update

        self.window_update.geometry("330x500")
        self.window_update.resizable(width=False, height=False)
        self.window_update.wm_title("Account Updating")

        self.selected_row = selected_row

        # all label widgets
        label_login = tk.Label(self.window_update, text='Login: ')
        label_login.config(font=("Comic 12 italic"), bg=self.bg)
        label_login.place(x=20, y=10)

        label_password = tk.Label(self.window_update, text='Password: ')
        label_password.config(font=("Comic 12 italic"), bg=self.bg)
        label_password.place(x=20, y=95)

        label_site = tk.Label(self.window_update, text='Site: ')
        label_site.config(font=("Comic 12 italic"), bg=self.bg)
        label_site.place(x=20, y=180)

        label_comment = tk.Label(self.window_update, text='Comment: ')
        label_comment.config(font=("Comic 12 italic"), bg=self.bg)
        label_comment.place(x=20, y=265)

        # all entry widgets
        self.update_login_input_var = tk.StringVar()
        self.login_entry = tk.Entry(self.window_update,
                                    font=("Comic 12 italic"),
                                    textvariable=self.update_login_input_var)
        self.login_entry.insert(0, self.selected_row[1])
        self.login_entry.place(x=20, y=50, width=290, height=30)

        self.update_password_input_var = tk.StringVar()
        self.password_entry = tk.Entry(self.window_update,
                                       font=("Comic 12 italic"),
                                       textvariable=self.update_password_input_var)
        self.password_entry.insert(0, self.selected_row[2])
        self.password_entry.place(x=20, y=135, width=290, height=30)

        self.update_site_input_var = tk.StringVar()
        self.site_entry = tk.Entry(self.window_update,
                                   font=("Comic 12 italic"),
                                   textvariable=self.update_site_input_var)
        self.site_entry.insert(0, self.selected_row[3])
        self.site_entry.place(x=20, y=220, width=290, height=30)

        self.update_comment_text = ScrolledText(self.window_update, font=("Comic 12 italic"), width=30, height=6)
        self.update_comment_text.insert("1.0", self.selected_row[4])
        self.update_comment_text.place(x=20, y=305)

        # all button widgets
        button_submit_update = tk.Button(self.window_update, text='OK', command=self.submit_update)
        button_submit_update.config(width=10,
                                    height=1,
                                    font=("Comic 12 italic"),
                                    activebackground='SpringGreen2',
                                    bd=1)
        button_submit_update.place(x=40, y=450)

        button_cancel_update = tk.Button(self.window_update, text='Cancel', command=window_update.destroy)
        button_cancel_update.config(width=10,
                                    height=1,
                                    font=("Comic 12 italic"),
                                    activebackground='SpringGreen2',
                                    bd=1)
        button_cancel_update.place(x=180, y=450)

    def submit_update(self):
        """
        Gets all data from all entry widgets and and updates with it selected row
        :return: None
        """
        id = self.selected_row[0]
        login = self.login_entry.get()
        password = self.password_entry.get()
        site = self.site_entry.get()
        comment = self.update_comment_text.get("1.0", tk.END)
        self.db.update(id, login, password, site, comment)
        self.window_update.destroy()


if __name__ == '__main__':
    window = tk.Tk()
    Window(window)
    window.mainloop()

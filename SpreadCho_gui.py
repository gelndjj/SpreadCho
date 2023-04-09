"""
.d8888. d8888b. d8888b. d88888b  .d8b.  d8888b.  .o88b. db   db  .d88b.  
88'  YP 88  `8D 88  `8D 88'     d8' `8b 88  `8D d8P  Y8 88   88 .8P  Y8. 
`8bo.   88oodD' 88oobY' 88ooooo 88ooo88 88   88 8P      88ooo88 88    88 
  `Y8b. 88~~~   88`8b   88~~~~~ 88~~~88 88   88 8b      88~~~88 88    88 
db   8D 88      88 `88. 88.     88   88 88  .8D Y8b  d8 88   88 `8b  d8' 
`8888Y' 88      88   YD Y88888P YP   YP Y8888D'  `Y88P' YP   YP  `Y88P'  
                                                                                                                                                 
"""

import tkinter as tk, customtkinter as ck, os, random as r, csv, pandas as pd, shutil
import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog, messagebox
from faker import Faker

fk = Faker()

columns = ('first_name','last_name','age','address','email','phone','job_title','city')

dict_columns = {'First Name': 0,
                    'Last Name': 1,
                    'Age': 2,
                    'Address':3,
                    'Email':4,
                    'Phone':5,
                    'Job Title':6,
                    'City':7}

dict_groupby = {'First Name': 'first_name',
                'Last Name': 'last_name',
                'Age': 'age',
                'Address': 'address',
                'Email':'email',
                'Phone':'phone',
                'Job Title':'job_title',
                'City':'city'}

dict_groupby_func = {'Mean': 'mean',
                     'Min':'min',
                     'Max':'max',
                     'Size':'size',
                     'CumCount':'cumcount'}

dict_groupby_naming = {'Mean': 'mean',
                     'Min':'min',
                     'Max':'max',
                     'Count':'Occurence'}

dict_file_type = {'CSV': 0,
                  'XLS': 1}

def save_data():
    global file

    if not os.path.exists(f'{os.getcwd()}/user_infos.csv'):
        with open(f'{os.getcwd()}/user_infos.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            writer.writerow({
                'first_name':first_name_entry.get(),
                'last_name':last_name_entry.get(),
                'age':age_entry.get(),
                'address':address_entry.get(),
                'email':email_entry.get(),
                'phone':phone_entry.get(),
                'job_title':job_title_entry.get(),
                'city':city_entry.get()
            })
    else:
        with open(f'{os.getcwd()}/user_infos.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writerow({
                'first_name':first_name_entry.get(),
                'last_name':last_name_entry.get(),
                'age':age_entry.get(),
                'address':address_entry.get(),
                'email':email_entry.get(),
                'phone':phone_entry.get(),
                'job_title':job_title_entry.get(),
                'city':city_entry.get()
            })

        first_name_entry.delete(0, tk.END)
        last_name_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        job_title_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        city_entry.delete(0, tk.END)
    
    display_data()

def save_rand_data():

    nb = int(nb_users_entry.get())

    if not os.path.exists(f'{os.getcwd()}/user_infos.csv'):
        with open(f'{os.getcwd()}/user_infos.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()

            for user in range(nb):
                first_name = fk.first_name()
                last_name = fk.last_name()
                age = r.randint(19,65)
                address = fk.address()
                domain = fk.free_email_domain()
                email = f'{first_name}.{last_name}@{domain}'
                phone = f'({r.randint(100,1000)}) {r.randint(100,1000)}-{r.randint(1000,10000)}'
                job_title = fk.job()
                city = fk.city()

                writer.writerow({
                    'first_name':first_name,
                    'last_name':last_name,
                    'age':age,
                    'address':address,
                    'email':email.lower(),
                    'phone':phone,
                    'job_title':job_title,
                    'city':city
                })
    else:
        with open(f'{os.getcwd()}/user_infos.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=columns)

            for user in range(nb):
                first_name = fk.first_name()
                last_name = fk.last_name()
                age = r.randint(19,65)
                address = fk.address()
                domain = fk.free_email_domain()
                email = f'{first_name}.{last_name}@{domain}'
                phone = f'({r.randint(100,1000)}) {r.randint(100,1000)}-{r.randint(1000,10000)}'
                job_title = fk.job()
                city = fk.city()

                writer.writerow({
                    'first_name':first_name,
                    'last_name':last_name,
                    'age':age,
                    'address':address,
                    'email':email.lower(),
                    'phone':phone,
                    'job_title':job_title,
                    'city':city

            })
    display_data()
    count_rows()

def generate_users_mul():

    nb_users = int(nb_users_entry.get())
    nb_ss = int(nb_files_entry.get())
    occ = 1
    file = 'users_info_mul.csv'
    file_raw = os.path.splitext(file)[0]
    file_ext = os.path.splitext(file)[1]
    
    while occ < nb_ss:

        with open(f'{file_raw}%s{file_ext}' % occ,'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()

            for i in range(nb_users):
                first_name = fk.first_name()
                last_name = fk.last_name()
                age = r.randint(19,65)
                address = fk.address()
                domain = fk.free_email_domain()
                email = f'{first_name}.{last_name}@{domain}'
                phone = f'({r.randint(100,1000)}) {r.randint(100,1000)}-{r.randint(1000,10000)}'
                job_title = fk.job()
                city = fk.city()

                writer.writerow({
                    'first_name':first_name,
                    'last_name':last_name,
                    'age':age,
                    'address':address,
                    'email':email.lower(),
                    'phone':phone,
                    'job_title':job_title,
                    'city':city
                })
        occ += 1
        print('done')

def display_data():
    if not os.path.isfile(f'{os.getcwd()}/user_infos.csv'):
        messagebox.showinfo(title='File not found', message='Please Generate Data Before Displaying')
        pass
    
    else:
        clear_frame()
        table = Frame(display_frame, width=600)
        table.pack(side=TOP)

        scrollbarx = Scrollbar(table, orient=HORIZONTAL)
        scrollbary = Scrollbar(table, orient=VERTICAL)
        tree = ttk.Treeview(table, columns=columns, height=300, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)

        tree.heading('first_name', text="First Name", anchor=W)
        tree.heading('last_name', text="Last Name", anchor=W)
        tree.heading('age', text="Age", anchor=W)
        tree.heading('address', text="Address", anchor=W)
        tree.heading('email', text="Email", anchor=W)
        tree.heading('phone', text="Phone", anchor=W)
        tree.heading('job_title', text="Job Title", anchor=W)
        tree.heading('city', text="City", anchor=W)

        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=20, width=110)
        tree.column('#2', stretch=NO, minwidth=20, width=110)
        tree.column('#3', stretch=NO, minwidth=20, width=50, anchor=CENTER)
        tree.column('#4', stretch=NO, minwidth=20, width=250)
        tree.column('#5', stretch=NO, minwidth=20, width=220)
        tree.column('#6', stretch=NO, minwidth=20, width=150, anchor=CENTER)
        tree.column('#7', stretch=NO, minwidth=20, width=250)
        tree.column('#8', stretch=NO, minwidth=20, width=150, anchor=CENTER)

        tree.pack()

        with open(f'{os.getcwd()}/user_infos.csv', 'r') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                firstname = row['first_name']
                lastname = row['last_name']
                age = row['age']
                address = row['address']
                email = row['email']
                phone = row['phone']
                job_title = row['job_title']
                city = row['city']
                tree.insert("", 0, values=(firstname, 
                                            lastname,
                                            age,
                                            address,
                                            email,
                                            phone,
                                            job_title,
                                            city))
        count_rows()
        dupl_rows()

def clear_frame():
    for items in display_frame.winfo_children():
        items.destroy()  

def del_row():
    count_lbl_rows.destroy()
    count_dup_lbl.destroy()

    if not os.path.isfile(f'{os.getcwd()}/user_infos.csv'):
        messagebox.showinfo(title='File not found', message='Please Generate Data Before Deleting')
        pass

    else:

        # Open the CSV file
        with open(f'{os.getcwd()}/user_infos.csv', 'r') as file:
            reader = csv.reader(file)
            rows_to_keep = []

            for row in reader:
                column_name = check_list.get()
                idx_column = dict_columns[column_name]
                if row[idx_column] != f'{string_del_entry.get()}':
                    rows_to_keep.append(row)

        with open(f'{os.getcwd()}/user_infos.csv', 'w', newline='') as file:
            writer = csv.writer(file)

            for row in rows_to_keep:
                writer.writerow(row)

        file.close()
        display_data()

def edit_row():
    
    if not os.path.isfile(f'{os.getcwd()}/user_infos.csv'):
        messagebox.showinfo(title='File not found', message='Please Generate Data Before Deleting')
        pass

    else:
        column_name = check_list.get()
        idx_column = dict_groupby[column_name]

        if idx_column == 'age':
                
                df1 = pd.read_csv(f'{os.getcwd()}/user_infos.csv')
                df1[idx_column].replace({int(f'{string_ren_entry_2.get()}'):int(f'{string_ren_entry.get()}')}, inplace=True)
                df1.to_csv(f'{os.getcwd()}/user_infos.csv')
        else:

            df1 = pd.read_csv(f'{os.getcwd()}/user_infos.csv')
            df1[idx_column].replace({f'{string_ren_entry_2.get()}':f'{string_ren_entry.get()}'}, inplace=True)
            df1.to_csv(f'{os.getcwd()}/user_infos.csv')

    display_data()

def groupby():

    if not os.path.isfile(f'{os.getcwd()}/user_infos.csv'):
        messagebox.showinfo(title='File not found', message='Please Generate Data Before Using Group By')
        pass
    
    else:
        clear_frame()

        column_name = check_group.get()
        nm_column = dict_groupby[column_name]

        func_name = check_group_func.get()
        nm_column_for_func = dict_groupby_func[func_name]

        csv_file = pd.read_csv(f'{os.getcwd()}/user_infos.csv')
        grouped = csv_file.groupby([nm_column]).agg(nm_column_for_func)

        grouped.to_csv(f'{os.getcwd()}/user_infos_groupby.csv')
        csv_file_grpby = pd.read_csv(f'{os.getcwd()}/user_infos_groupby.csv')

        clear_frame()

        table = Frame(display_frame, width=600)
        table.pack(side=TOP)

        tree = ttk.Treeview(display_frame, height=40, columns=list(csv_file_grpby.columns))
        
        scrollbarx = Scrollbar(table, orient=HORIZONTAL)
        scrollbary = Scrollbar(table, orient=VERTICAL)
        tree = ttk.Treeview(table, columns=columns, height=300, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)

        for column in tree["columns"]:
            tree.column(column, width=200)
            tree.heading(column, text=column)

        for i, row in csv_file_grpby.iterrows():
            tree.insert("", "end", text=i, values=list(row))

        tree.pack(expand=True)

def export():
        
    if not os.path.isfile(f'{os.getcwd()}/user_infos.csv'):
        messagebox.showinfo(title='File not found', message='Please Generate Data Before Exporting')
        pass
    
    else:
        ftype = export_file.get()
        f_type = dict_file_type[ftype]

        if f_type == 0:
            csv_file = f'{os.getcwd()}/user_infos.csv'
            path = filedialog.askdirectory()
            full_path = f'{path}/'
            shutil.copy(csv_file, full_path)
            messagebox.showinfo(title='Export Success', message='CSV File Exported')

        if f_type == 1:
            csv_file = f'{os.getcwd()}/user_infos.csv'
            path = filedialog.askdirectory()
            full_path = f'{path}/'

            read_file = pd.read_csv(csv_file)
            read_file.to_excel(f'{full_path}%s.xls' % os.path.splitext(os.path.basename(csv_file))[0], index=None, header=True)
            messagebox.showinfo(title='Export Success', message='XLS File Exported')

def export_direct():

    if not os.path.isfile(f'{os.getcwd()}/user_infos_groupby.csv'):
        messagebox.showinfo(title='File not found', message='Please Generate Data Before Exporting')
        pass
    
    else:
            csv_file = f'{os.getcwd()}/user_infos_groupby.csv'
            path = filedialog.askdirectory()
            full_path = f'{path}/'
            shutil.copy(csv_file, full_path)
            messagebox.showinfo(title='Export Success', message='CSV File Exported')

def count_rows():

    global count_lbl_rows

    csv_file = pd.read_csv(f'{os.getcwd()}/user_infos.csv')
    count_lbl_rows = ck.CTkLabel(data_frame_inf,text=f'Total row(s): {len(csv_file)}', text_color='red')
    count_lbl_rows.place(x=3,y=5)
def dupl_rows():

    global count_dup_lbl

    csv_file = pd.read_csv(f'{os.getcwd()}/user_infos.csv')
    count_dup_lbl = ck.CTkLabel(data_frame_inf,text=f'Duplicate(s): {len(csv_file[csv_file.duplicated()])}', text_color='red')
    count_dup_lbl.place(x=4,y=30)

def on_entry_change(*args):
    if first_name_entry.get():
        save_button.configure(state=NORMAL)
    else:
        save_button.configure(state=DISABLED)

def quit():
    dict_ext = {'spreadsheet':('.csv','.xls')}
    try:
        for file in os.listdir():
            if file.endswith(dict_ext['spreadsheet']):
                os.remove(file)
        window.destroy()
    except FileNotFoundError:
        window.destroy()

def clean():
        dict_ext = {'spreadsheet':('.csv','.xls')}
        for file in os.listdir():
            if file.endswith(dict_ext['spreadsheet']):
                os.remove(file)
        clear_frame()

"""def onclose(event):
    quit()"""

 # GUI STUFF
window = tk.Tk()
window.title('SpreadCho')
width = 1200
height = 750
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/4) - (height/4)
window.geometry("%dx%d+%d+%d" % (width, height, x, y))
window.resizable(0, 0)

# FRAMES
data_frame = tk.Frame(window, width=200, bg='#c5cca5')
data_frame.pack(fill=Y, side=LEFT)
display_frame = tk.Frame(window, width=1000, bg='grey')
display_frame.pack( fill=Y, side=RIGHT)

# LABELS FRAME
data_frame_infos = tk.LabelFrame(data_frame, text='Users Informations', fg='black', background='#c5cca5', bd=3, foreground='red', font='Loma 13')
data_frame_infos.grid(row=0,column=0, padx=5, pady=5)
data_frame_fake = tk.LabelFrame(data_frame, text='Random Users Informations', fg='black', background='#c5cca5', bd=3, foreground='red', font='Loma 13', width=285, height=90)
data_frame_fake.place(x=5,y=285)
data_frame_del_row = tk.LabelFrame(data_frame, text='Delete or Replace Row(s)', fg='black', background='#c5cca5', bd=3, foreground='red', font='Loma 13', width=285, height=90)
data_frame_del_row.place(x=5,y=385)
data_frame_group = tk.LabelFrame(data_frame, text='Group by', fg='black', background='#c5cca5', bd=3, foreground='red', font='Loma 13', width=285, height=90)
data_frame_group.place(x=5,y=485)
data_frame_export = tk.LabelFrame(data_frame, text='Export', fg='black', background='#c5cca5', bd=3, foreground='red', font='Loma 13', width=135, height=90)
data_frame_export.place(x=5,y=590)
data_frame_inf = tk.LabelFrame(data_frame, text='Infos - Main File', fg='black', background='#c5cca5', foreground='red', font='Loma 12', bd=3, width=135, height=90)
data_frame_inf.place(x=155,y=590)

# LABELS
nb_users = ck.CTkLabel(data_frame_fake, text='Number of Users', text_color='black')
nb_users.place(x=10,y=5)
nb_files = ck.CTkLabel(data_frame_fake, text='Number of Files', text_color='black')
nb_files.place(x=10,y=40)
lbl_is = ck.CTkLabel(data_frame_del_row, text='is', text_color='black')
lbl_is.place(x=120,y=5)
lbl_to = ck.CTkLabel(data_frame_del_row, text='to', text_color='black')
lbl_to.place(x=112,y=40)
lbl_is_2 = ck.CTkLabel(data_frame_del_row, text='is', text_color='black')
lbl_is_2.place(x=5,y=40)
first_name_label = ck.CTkLabel(data_frame_infos, text='First Name', text_color='black')
first_name_label.grid(row=0, column=0)
last_name_label = ck.CTkLabel(data_frame_infos, text='Last Name', text_color='black')
last_name_label.grid(row=1, column=0)
age_label = ck.CTkLabel(data_frame_infos, text='Age', text_color='black')
age_label.grid(row=2, column=0)
address_label = ck.CTkLabel(data_frame_infos, text='Address', text_color='black')
address_label.grid(row=3, column=0)
email_label = ck.CTkLabel(data_frame_infos, text='Email', text_color='black')
email_label.grid(row=4, column=0)
phone_label = ck.CTkLabel(data_frame_infos, text='Phone', text_color='black')
phone_label.grid(row=5, column=0)
job_title_label = ck.CTkLabel(data_frame_infos, text='Job Title', text_color='black')
job_title_label.grid(row=6, column=0)
city_label = ck.CTkLabel(data_frame_infos, text='City', text_color='black')
city_label.grid(row=7, column=0)

# ENTRIES
first_name_entry_var = StringVar()
first_name_entry_var.trace('w', on_entry_change)
first_name_entry = ck.CTkEntry(data_frame_infos, textvariable=first_name_entry_var)
first_name_entry.grid(row=0, column=1)
last_name_entry = ck.CTkEntry(data_frame_infos)
last_name_entry.grid(row=1, column=1)
age_entry = ck.CTkEntry(data_frame_infos)
age_entry.grid(row=2, column=1)
address_entry = ck.CTkEntry(data_frame_infos)
address_entry.grid(row=3, column=1)
email_entry = ck.CTkEntry(data_frame_infos)
email_entry.grid(row=4, column=1)
phone_entry = ck.CTkEntry(data_frame_infos)
phone_entry.grid(row=5, column=1)
job_title_entry = ck.CTkEntry(data_frame_infos)
job_title_entry.grid(row=6, column=1)
city_entry = ck.CTkEntry(data_frame_infos)
city_entry.grid(row=7, column=1)
nb_users_entry_int = IntVar()
nb_users_entry = ck.CTkEntry(data_frame_fake, textvariable=nb_users_entry_int, width=50)
nb_users_entry.place(x=139,y=5)
nb_files_entry = ck.CTkEntry(data_frame_fake, width=50)
nb_files_entry.place(x=139,y=40)
string_del_entry = ck.CTkEntry(data_frame_del_row, width=80)
string_del_entry.place(x=139,y=5)
string_ren_entry = ck.CTkEntry(data_frame_del_row, width=80)
string_ren_entry.place(x=130,y=40)
string_ren_entry_2 = ck.CTkEntry(data_frame_del_row, width=80)
string_ren_entry_2.place(x=25,y=40)

# BUTTONS
save_button = ck.CTkButton(data_frame_infos, text='Add User', fg_color='#626653', hover_color='black', border_width=3,state=DISABLED, text_color='white' ,command=save_data)
save_button.grid(row=8, column=0)
display_button = ck.CTkButton(data_frame_infos, text='Display Spreadsheat', fg_color='#626653', hover_color='black', text_color='white', border_width=3,command=display_data)
display_button.grid(row=8, column=1)
generate_button = ck.CTkButton(data_frame_fake, text='Generate', fg_color='#626653', hover_color='black', border_width=3, width=74, command=save_rand_data)
generate_button.place(x=205,y=5)
generateM_button = ck.CTkButton(data_frame_fake, text='Generate', fg_color='#626653', hover_color='black', border_width=3, width=74, command=generate_users_mul)
generateM_button.place(x=205,y=40)
del_button = ck.CTkButton(data_frame_del_row, text='Delete', fg_color='#626653', hover_color='black', border_width=3,width=56,command=del_row)
del_button.place(x=223,y=5)
ren_button = ck.CTkButton(data_frame_del_row, text='Replace', fg_color='#626653', hover_color='black', border_width=3,width=64,command=edit_row)
ren_button.place(x=215,y=40)
group_button = ck.CTkButton(data_frame_group, text='Group', fg_color='#626653', hover_color='black', border_width=3,width=120,command=groupby)
group_button.place(x=159,y=5)
export_group_button = ck.CTkButton(data_frame_group, text='Export GrpBy Results', fg_color='#626653', hover_color='black', border_width=3,width=150,command=export_direct)
export_group_button.place(x=129,y=40)
export_button = ck.CTkButton(data_frame_export, text='Export', fg_color='#626653', hover_color='black', border_width=3,width=120,command=export)
export_button.place(x=0,y=40)
clear_button = ck.CTkButton(data_frame, text='Clear', fg_color='#626653', hover_color='red', border_width=3,width=120,command=clear_frame)
clear_button.place(x=8,y=687)
clear_button_all = ck.CTkButton(data_frame, text='Clean Files', fg_color='#626653', hover_color='red', border_width=3,width=120,command=clean)
clear_button_all.place(x=8,y=717)
quit_button = ck.CTkButton(data_frame, text='Quit', fg_color='#626653', hover_color='red', border_width=3,width=120,command=quit)
quit_button.place(x=164,y=697)

# COMBOBOXES
check_list = ck.CTkComboBox(data_frame_del_row, values=['First Name', 'Last Name','Age', 'Address', 'Email', 'Phone', 'Job Title', 'City'], width=110)
check_list.place(x=0, y=5)
export_file = ck.CTkComboBox(data_frame_export, values=['CSV', 'XLS'], width=120)
export_file.place(x=0, y=5)
check_group = ck.CTkComboBox(data_frame_group, values=['First Name', 'Last Name','Age', 'Address', 'Email', 'Phone', 'Job Title', 'City'], width=120)
check_group.place(x=0, y=5)
check_group_func = ck.CTkComboBox(data_frame_group, values=['Mean', 'Min', 'Max', 'Size', 'CumCount'], width=120)
check_group_func.place(x=0, y=40)

# BINDING
nb_users_entry.bind('<FocusIn>', lambda event: nb_users_entry.delete(0,END))

#window.protocol('WM_DELETE_WINDOW', lambda: onclose(window))
window.mainloop()

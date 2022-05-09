from tkinter import *
from tkinter import messagebox
import os
from lin import *

obj_option = [
    "Maximize",
    "Minimize"
]

opti_type = [
    "Linear",
    "Non-Linear"
]


def add_constr(*args):  # Function when pressing enter
    var_box_arr = []

    if len(constr_entry.get()) == 0:
        return
    if constr_lstbox.size() == 0:
        rem = Button(root, text="Remove Constraint", command=rem_constr)
        rem.grid(column=(constr_column + 1), row=10)
        rem.bind("<Return>", rem_constr)

    for i in range(var_lstbox.size()):
        var_box_arr.append(var_lstbox.get(i))

    # checks if variable in the constraint is in the variable box
    constr_char_count = len(constr_entry.get())

    if constr_char_count < 3:
        messagebox.showerror('error', "Invalid constraint. Constraint is too short.")
        return

    if validate_variables(str(constr_entry.get())):
        constr_lstbox.insert(END, constr_entry.get())
        constr_entry.delete(0, END)

    return


def rem_constr(*args):
    if "keysym=Delete" in str(args):
        indx = constr_lstbox.curselection()
        constr_lstbox.delete(indx, indx)
    else:
        constr_lstbox.delete(END, END)
    if constr_lstbox.size() == 0:
        for i in root.grid_slaves(10, (constr_column + 1)):  # Location of Remove Constraint Button
            i.grid_forget()
    return


def add_var(*args):
    if len(var_entry.get()) == 0:
        return
    if var_lstbox.size() == 0:
        rem = Button(root, text="Remove Variable", command=rem_var)
        rem.grid(column=(var_column + 1), row=10)
        rem.bind("<Return>", rem_var)

    if str(var_entry.get()).isalpha() and len(var_entry.get()) == 1:
        var_lstbox.insert(END, var_entry.get())
        var_entry.delete(0, END)
        return
    else:
        messagebox.showerror('error', "Please enter a single letter per variable")


def rem_var(*args):
    if "keysym=Delete" in str(args):
        indx = var_lstbox.curselection()
        var_lstbox.delete(indx, indx)
    else:
        var_lstbox.delete(END, END)

    if var_lstbox.size() == 0:
        for i in root.grid_slaves(10, (var_column + 1)):  # Location of Remove Variable Button
            i.grid_forget()
    return


def opti():

    var = []
    constr = []
    x_list = []
    status_list = ["Optimization proceeding nominally.", "Iteration limit reached.", "Problem appears to be infeasible.", "Problem appears to be unbounded.", "Numerical difficulties encountered."]
    obj = obj_entry.get()
    maxi = is_max()
    linear = is_linear()

    for i in range(var_lstbox.size()):
        var.append(var_lstbox.get(i))

    for i in range(constr_lstbox.size()):
        constr.append(constr_lstbox.get(i))

    if validate_empty_lists():
        return

    if validate_variables(str(obj_entry.get())):
        obj_result_value = result(var, constr, obj, maxi)
        #print(obj_result_value)
        fun = "Result: " + str(round(obj_result_value.get('fun'), 3))
        message = "message: " + str(obj_result_value.get('message'))
        status = obj_result_value.get('status')
        x = obj_result_value.get('x')

        for i in range(len(var)):
            x_list.append(str(var[i]) + ": " + str(round(x[i], 3)))

        opti_root = Tk()
        opti_root.title("Result")
        frame = Frame(opti_root)
        frame.pack(fill=BOTH, expand=True, padx=40, pady=40)
        #w = Text(frame, height=1, borderwidth=0, font=20, background='light gray')
        #w.insert(1.0, "Hi")
        #w.pack()
        #w.configure(state="disabled")

        for i in range(len(status_list)):
            if status == i:
                status_output = "Exit code " + str(status) + ": " + status_list[i]

        if obj_result_value.get('success'):
            Label(frame, text="Program ran successfully!", font=20).pack()
            Label(frame, text=status_output, font=5).pack()
            Label(frame, text=fun, font=5).pack()
            Label(frame, text=message, font=5).pack()
            Label(frame, text=x_list, font=5).pack()
        else:
            Label(frame, text="Run was not successful!", font=20).pack()
            Label(frame, text=status_output, font=5).pack()

        root.mainloop()

    return


def is_max():
    if clicked.get() == obj_option[0]:
        return True
    else:
        return False


def is_linear():
    if clicked2.get() == opti_type[0]:
        return True
    else:
        return False


def validate_variables(input_equation):
    var_box_arr = []
    is_found_var = False
    alpha_count = 0
    constr_char_count = len(input_equation)

    for i in range(var_lstbox.size()):
        var_box_arr.append(var_lstbox.get(i))

    for i in range(len(input_equation)):
        if input_equation[i].isalpha():
            alpha_count = alpha_count + 1
            if alpha_count > 1:
                is_found_var = False
                messagebox.showerror('error', "Please include an * if multiplying")
                return False
            if any(input_equation[i] in string for string in var_box_arr):
                is_found_var = True
            else:
                is_found_var = False
                x = input_equation[i] + " is not in the variable list"
                messagebox.showerror('error', x)
                return False
        else:
            alpha_count = 0

    if not is_found_var:
        messagebox.showerror('error', "Please enter a valid equation")
        return False

    return True


def validate_empty_lists():
    # check if variable listbox is empty
    if var_lstbox.size() == 0:
        messagebox.showerror('error', "Please Enter Variables")
        return True

    # check if constraint listbox is empty
    if constr_lstbox.size() == 0:
        messagebox.showerror('error', "Please Enter Constraints")
        return True

    # check if objective function is empty
    if len(obj_entry.get()) == 0:
        messagebox.showerror('error', "Please Enter an Objective Function")
        return True

    return False


def clear():
    var_lstbox.delete(0, END)
    constr_lstbox.delete(0, END)
    obj_entry.delete(0, END)
    var_entry.delete(0, END)
    constr_entry.delete(0, END)

    if var_lstbox.size() == 0:
        for i in root.grid_slaves(10, (var_column + 1)):  # Location of Remove Variable Button
            i.grid_forget()

    if constr_lstbox.size() == 0:
        for i in root.grid_slaves(10, (constr_column + 1)):  # Location of Remove Constraint Button
            i.grid_forget()


def open_file():
    os.startfile("README.md")


# Root Window
root = Tk()
root.title("Optimization Calculator")

helpMe_button = Button(root, text="Help Me!", command=open_file)
helpMe_button.grid(column=0, row=0)

# Variable Category
var_column = 0
var_label = Label(root, text="Variables").grid(column=var_column, row=9)

var_lstbox = Listbox(root, width=10)
var_lstbox.grid(column=var_column, row=10, padx=10, pady=10)
var_lstbox.bind('<Delete>', rem_var)

var_entry = Entry(root, width=10)
var_entry.grid(column=var_column, row=11)
var_entry.bind('<Return>', add_var)

add_var = Button(root, text="Add Variable", command=add_var)
add_var.grid(column=(var_column + 1), row=11)

# Constraint Category
constr_column = 5
constr_label = Label(root, text="Constraints").grid(column=constr_column, row=9)

constr_lstbox = Listbox(root, width=30)
constr_lstbox.grid(column=constr_column, row=10, padx=10, pady=10)
constr_lstbox.bind("<Delete>", rem_constr)

constr_entry = Entry(root, width=30)

constr_entry.grid(column=constr_column, row=11, padx=10, pady=10)
constr_entry.bind("<Return>", add_constr)

add_constr = Button(root, text="Add Constraint", command=add_constr)
add_constr.grid(column=(constr_column + 1), row=11, padx=10, pady=10)

# Objective Function
obj_column = 3
obj_label = Label(root, text="Objective Function:")
obj_label.grid(column=(obj_column - 1), row=0, padx=10, pady=10)
clicked = StringVar(root)
obj_entry = Entry(root, width=25)
obj_entry.grid(column=obj_column, row=0, padx=10, pady=10)
clicked.set(obj_option[0])
obj_dropbox = OptionMenu(root, clicked, *obj_option).grid(column=(obj_column + 1), row=0, padx=10, pady=10)

# Optimization Types
clicked2 = StringVar(root)
clicked2.set(opti_type[0])
opti_drop = OptionMenu(root, clicked2, *opti_type).grid(column=(obj_column + 2), row=0, padx=10, pady=10)

# Optimize
opti_button = Button(root, text="Optimize", command=opti)
opti_button.grid(column=obj_column, row=12, padx=10, pady=10)

# Clear
clear_button = Button(root, text="Clear", bg='black', fg='white', command=clear)
clear_button.grid(column=obj_column + 1, row=12, padx=10, pady=10)

# Loop
root.mainloop()
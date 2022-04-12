# Basic Calculator, Jon Connell 2022
# CSE 111

import tkinter as tk

def main():
    # create root Tk object
    root = tk.Tk()

    # create main window/grame
    frm_main = tk.Frame(root)
    frm_main.master.title("EZ-CALC")
    frm_main.pack(padx=25, pady=15, fill=tk.BOTH, expand=1)

    # call populate_main_window function to add elements to window
    populate_main_window(frm_main)

    # Start tkinter loop to process user events
    root.mainloop()


def populate_main_window(frm_main):
    """Populate main window with labels, text entry, and buttons

    Parameters: 
        frm_main: main window/frame
    
    Return:
        Nothing
    """
    def clear():
        """ Clear input box
        """
        ent_num.delete(0, tk.END)

    def operator_click(operator_input):
        """ Sets global variables for first number and operator
        Parameters:
            operator: Operator pressed by user
        Return:
            Nothing
        """
        # set integer global variable for first number entered
        global first_num
        first_get = ent_num.get()
        first_num = float(first_get)
        ent_num.delete(0, tk.END)

        # set global variable for operator used
        global operator
        operator = operator_input


    def equals_click():
        """ Calculate result based on first and second number variables and operator used
        Parameters:
            None
        Return:
            Nothing
        """
        result = 0
        second_get = ent_num.get()
        second_num = float(second_get)

        # perform appropriate calculation for sign used
        if operator == "+":
            result = first_num + second_num
        if operator == "-":
            result = first_num - second_num
        if operator == "x":
            result = first_num * second_num
        if operator == "÷":
            result = first_num / second_num

        # insert result into text box
        ent_num.delete(0, tk.END)
        ent_num.insert(0, result)


    def num_click(number):
        """ Concatenates number button pressed to previous numbers entered
        Parameters:
            number: value of button pressed
        
        Return:
            Nothing
        """
        old_num = ent_num.get()
        ent_num.delete(0, tk.END)
        ent_num.insert(0, str(old_num) + str(number))

    # create entry widget for number entry/results display
    ent_num = tk.Entry(frm_main, width=18)

    # create buttons for numbers 0-9
    button_1 = tk.Button(frm_main, text="1", command=lambda: num_click("1"))
    button_2 = tk.Button(frm_main, text="2", command=lambda: num_click("2"))
    button_3 = tk.Button(frm_main, text="3", command=lambda: num_click("3"))
    button_4 = tk.Button(frm_main, text="4", command=lambda: num_click("4"))
    button_5 = tk.Button(frm_main, text="5", command=lambda: num_click("5"))
    button_6 = tk.Button(frm_main, text="6", command=lambda: num_click("6"))
    button_7 = tk.Button(frm_main, text="7", command=lambda: num_click("7"))
    button_8 = tk.Button(frm_main, text="8", command=lambda: num_click("8"))
    button_9 = tk.Button(frm_main, text="9", command=lambda: num_click("9"))
    button_0 = tk.Button(frm_main, text="0", command=lambda: num_click("0"))

    # create operator buttons (add, subtract, multiply, divide, and equals/enter)
    btn_add = tk.Button(frm_main, text="+", command=lambda: operator_click("+"))
    btn_subt = tk.Button(frm_main, text="-", command=lambda: operator_click("-"))
    btn_mult = tk.Button(frm_main, text="x", command=lambda: operator_click("x"))
    btn_div = tk.Button(frm_main, text="÷", command=lambda: operator_click("÷"))
    btn_enter = tk.Button(frm_main, text="=", command=equals_click)
    btn_clear = tk.Button(frm_main, text="C", command=clear)

    # organize number buttons in grid
    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)
    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)
    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)
    button_0.grid(row=4, column=1)

    # organize operator elements in grid
    ent_num.grid(row=0, column=0, padx=5, pady=3, columnspan=4)
    btn_add.grid(row=4, column=3, padx=5, pady=3)
    btn_subt.grid(row=3, column=3, padx=5, pady=3)
    btn_mult.grid(row=2, column=3, padx=5, pady=3)
    btn_div.grid(row=1, column=3, padx=5, pady=3)
    btn_clear.grid(row=4, column=0, padx=5, pady=3)
    btn_enter.grid(row=4, column=2, padx=5, pady=3)


if __name__ == "__main__":
    main()
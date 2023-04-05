import tkinter as tk
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes

c = CurrencyRates()
s = CurrencyCodes()
# Create a list of currency options
currency_options = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY']

class AFM:
    def __init__(self, master):
        self.master = master
        self.master.title("Auto Forex Machine")
        self.master.geometry("500x400")

        self.label1 = tk.Label(self.master, text="Welcome to AFM", font=("Arial", 20))
        self.label1.pack(pady=20)

        self.label2 = tk.Label(self.master, text="Enter your PIN:", font=("Arial", 12))
        self.label2.pack()

        self.entry = tk.Entry(self.master, show="*")
        self.entry.pack(pady=10)

        self.button = tk.Button(self.master, text="Enter", command=self.login, font=("Arial", 12))
        self.button.pack(pady=10)

    def animate(self, label, colors):
        current_color = label.cget("fg")
        if current_color in colors:
            next_index = (colors.index(current_color) + 1) % len(colors)
            next_color = colors[next_index]
        else:
            next_color = colors[0]
        label.config(fg=next_color)
        label.after(500, self.animate, label, colors)
    def login(self):
        pin = self.entry.get()

        if pin == "1234":
            self.entry.pack_forget()
            self.label1.configure(text="Login successful!")
            self.label2.configure(text="Good day computer scientist!")
            self.label3 = tk.Label(self.master, text="What would you like to do today?")
            self.label3.pack()
            self.button.pack_forget()

            self.buy_button = tk.Button(self.master, text="Buy", command=self.show_buy_options)
            self.buy_button.pack()

            self.sell_button = tk.Button(self.master, text="Sell", command=self.show_sell_options)
            self.sell_button.pack()

            self.logout_button = tk.Button(self.master, text="Logout", command=self.logout)
            self.logout_button.pack()

        else:
            self.label1.configure(text="Invalid PIN, please try again.")

    def show_buy_options(self):
        self.entry.pack_forget()
        self.label2.pack_forget()
        self.label3.pack_forget()
        self.label1.configure(text="Cash or Remittance?")
        self.buy_button.pack_forget()
        self.sell_button.pack_forget()
        self.logout_button.pack_forget()

        self.cash_button = tk.Button(self.master, text="Cash", command=self.buy_cash)
        self.cash_button.pack()

        self.remit_button = tk.Button(self.master, text="Remittance", command=self.buy_remit)
        self.remit_button.pack()

    def show_sell_options(self):
        self.entry.pack_forget()
        self.label2.pack_forget()
        self.label3.pack_forget()
        self.label1.configure(text="Cash or Remittance?")
        self.buy_button.pack_forget()
        self.sell_button.pack_forget()
        self.logout_button.pack_forget()

        self.cash_button = tk.Button(self.master, text="Cash", command=self.sell_cash)
        self.cash_button.pack()

        self.remit_button = tk.Button(self.master, text="Remittance", command=self.sell_remit)
        self.remit_button.pack()

    def buy_cash(self):
        self.label1.pack_forget()
        self.cash_button.pack_forget()
        self.remit_button.pack_forget()

        self.input_label = tk.Label(self.master, text="Input currency:")
        self.input_label.pack()

        # Create StringVars to store the selected currencies
        self.input_currency = tk.StringVar()
        self.output_currency = tk.StringVar()

        # Create the dropdown menus
        self.input_currency_dropdown = tk.OptionMenu(self.master, self.input_currency, *currency_options)
        self.input_currency_dropdown.pack()

        self.output_label = tk.Label(self.master, text="Output currency:")
        self.output_label.pack()

        self.output_currency_dropdown = tk.OptionMenu(self.master, self.output_currency, *currency_options)
        self.output_currency_dropdown.pack()

        self.amount_label = tk.Label(self.master, text="Amount to be exchanged:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(self.master, show="")
        self.amount_entry.pack()

        self.confirm_button = tk.Button(self.master, text="Confirm", command=self.cash_buy_in)
        self.confirm_button.pack()

    def buy_remit(self):
        self.label1.pack_forget()
        self.cash_button.pack_forget()
        self.remit_button.pack_forget()

        self.input_label = tk.Label(self.master, text="Input currency:")
        self.input_label.pack()

        # Create StringVars to store the selected currencies
        self.input_currency = tk.StringVar()
        self.output_currency = tk.StringVar()

        # Create the dropdown menus
        self.input_currency_dropdown = tk.OptionMenu(self.master, self.input_currency, *currency_options)
        self.input_currency_dropdown.pack()

        self.output_label = tk.Label(self.master, text="Output currency:")
        self.output_label.pack()

        self.output_currency_dropdown = tk.OptionMenu(self.master, self.output_currency, *currency_options)
        self.output_currency_dropdown.pack()

        self.amount_label = tk.Label(self.master, text="Amount to be exchanged:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(self.master, show="")
        self.amount_entry.pack()

        self.confirm_button = tk.Button(self.master, text="Confirm", command=self.remit_buy_in)
        self.confirm_button.pack()

    def cash_buy_in(self):
            self.input_currency_dropdown.pack_forget()
            self.output_currency_dropdown.pack_forget()
            self.amount_entry.pack_forget()
            self.confirm_button.pack_forget()
            input_currency = self.input_currency.get()
            output_currency = self.output_currency.get()
            input_amount = float(self.amount_entry.get())
            if input_currency != output_currency:
                rate = c.get_rate(input_currency, output_currency)
                output_amount = float(input_amount) * rate * 0.98
                rounded_output = round(output_amount, 2)
                symbol = s.get_symbol(output_currency)
                self.input_label.configure(text="The output amount is " + symbol + str(rounded_output))
                self.output_label.configure(text="Please wait for your cash to be dispensed!")
                self.amount_label.configure(text="Thank you for choosing The Bank of Computer Scientist!", fg="black")
                self.animate(self.amount_label, ["black", "blue", "red", "green"])
                if self.label4.winfo_exists():
                    self.label4.pack_forget()
                else:
                    pass
            else:
                self.label4 = tk.Label(self.master, text="Please select different currencies!")
                self.label4.pack()
    def remit_buy_in(self):
        self.input_currency_dropdown.pack_forget()
        self.output_currency_dropdown.pack_forget()
        self.amount_entry.pack_forget()
        self.confirm_button.pack_forget()
        input_currency = self.input_currency.get()
        output_currency = self.output_currency.get()
        input_amount = float(self.amount_entry.get())
        if input_currency != output_currency:

            rate = c.get_rate(input_currency, output_currency)
            output_amount = float(input_amount) * rate * 0.99
            rounded_output = round(output_amount, 2)
            symbol = s.get_symbol(output_currency)
            self.input_label.configure(text="The output amount is " + symbol + str(rounded_output))
            self.output_label.configure(text="It has already been transferred to your "+ output_currency+" account!")
            self.amount_label.configure(text="Thank you for choosing The Bank of Computer Scientist!")
            self.animate(self.amount_label, ["black", "blue", "red", "green"])
            if self.label4.winfo_exists():
                self.label4.pack_forget()
            else:
                pass
        else:
            self.label4 = tk.Label(self.master, text="Please select different currencies!")
            self.label4.pack()

    def sell_cash(self):
        self.label1.pack_forget()
        self.cash_button.pack_forget()
        self.remit_button.pack_forget()

        self.input_label = tk.Label(self.master, text="Input currency:")
        self.input_label.pack()

        # Create StringVars to store the selected currencies
        self.input_currency = tk.StringVar()
        self.output_currency = tk.StringVar()

        # Create the dropdown menus
        self.input_currency_dropdown = tk.OptionMenu(self.master, self.input_currency, *currency_options)
        self.input_currency_dropdown.pack()

        self.output_label = tk.Label(self.master, text="Output currency:")
        self.output_label.pack()

        self.output_currency_dropdown = tk.OptionMenu(self.master, self.output_currency, *currency_options)
        self.output_currency_dropdown.pack()

        self.amount_label = tk.Label(self.master, text="Amount to be exchanged:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(self.master, show="")
        self.amount_entry.pack()

        self.confirm_button = tk.Button(self.master, text="Confirm", command=self.cash_sell_out)
        self.confirm_button.pack()

    def sell_remit(self):
        self.label1.pack_forget()
        self.cash_button.pack_forget()
        self.remit_button.pack_forget()

        self.input_label = tk.Label(self.master, text="Input currency:")
        self.input_label.pack()

        # Create StringVars to store the selected currencies
        self.input_currency = tk.StringVar()
        self.output_currency = tk.StringVar()

        # Create the dropdown menus
        self.input_currency_dropdown = tk.OptionMenu(self.master, self.input_currency, *currency_options)
        self.input_currency_dropdown.pack()

        self.output_label = tk.Label(self.master, text="Output currency:")
        self.output_label.pack()

        self.output_currency_dropdown = tk.OptionMenu(self.master, self.output_currency, *currency_options)
        self.output_currency_dropdown.pack()

        self.amount_label = tk.Label(self.master, text="Amount to be exchanged:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(self.master, show="")
        self.amount_entry.pack()

        self.confirm_button = tk.Button(self.master, text="Confirm", command=self.remit_sell_out)
        self.confirm_button.pack()

    def cash_sell_out(self):

        self.input_currency_dropdown.pack_forget()
        self.output_currency_dropdown.pack_forget()
        self.amount_entry.pack_forget()
        self.confirm_button.pack_forget()
        input_currency = self.input_currency.get()
        output_currency = self.output_currency.get()
        input_amount = float(self.amount_entry.get())
        if input_currency != output_currency:

            rate = c.get_rate(input_currency, output_currency)
            output_amount = float(input_amount) * rate * 1.02
            rounded_output = round(output_amount, 2)
            symbol = s.get_symbol(output_currency)
            self.input_label.configure(text="The output amount is " + symbol + str(rounded_output))
            self.output_label.configure(text="Please wait for your cash to be dispensed!")
            self.amount_label.configure(text="Thank you for choosing The Bank of Computer Scientist!")
            self.animate(self.amount_label, ["black", "blue", "red", "green"])
            if self.label4.winfo_exists():
                self.label4.pack_forget()
            else:
                pass
        else:
            self.label4 = tk.Label(self.master, text="Please select different currencies!")
            self.label4.pack()

    def remit_sell_out(self):
        self.input_currency_dropdown.pack_forget()
        self.output_currency_dropdown.pack_forget()
        self.amount_entry.pack_forget()
        self.confirm_button.pack_forget()
        input_currency = self.input_currency.get()
        output_currency = self.output_currency.get()
        input_amount = float(self.amount_entry.get())
        if input_currency != output_currency:

            rate = c.get_rate(input_currency, output_currency)
            output_amount = float(input_amount) * rate * 1.01
            rounded_output = round(output_amount, 2)
            symbol = s.get_symbol(output_currency)
            self.input_label.configure(text="The output amount is " + symbol + str(rounded_output))
            self.output_label.configure(text="It has already been transferred to your " + output_currency + " account!")
            self.amount_label.configure(text="Thank you for choosing The Bank of Computer Scientist!")
            self.animate(self.amount_label, ["black", "blue", "red", "green"])
            if self.label4.winfo_exists():
                self.label4.pack_forget()
            else:
                pass
        else:
            self.label4 = tk.Label(self.master, text="Please select different currencies!")
            self.label4.pack()
    def logout(self):
        self.master.destroy()
        
root = tk.Tk()

my_gui = AFM(root)
root.mainloop()

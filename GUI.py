import tkinter as tk


class AFM:
    def __init__(self, master):
        self.master = master
        self.master.title("Auto Forex Machine")
        self.master.geometry("500x400")

        self.label1 = tk.Label(self.master, text="Welcome to AFM")
        self.label1.pack()

        self.label2 = tk.Label(self.master, text="Enter your PIN:")
        self.label2.pack()

        self.entry = tk.Entry(self.master, show="*")
        self.entry.pack()

        self.button = tk.Button(self.master, text="Enter", command=self.login)
        self.button.pack()

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
        self.IC_entry = tk.Entry(self.master, show="")
        self.IC_entry.pack()

        self.output_label = tk.Label(self.master, text="Output currency:")
        self.output_label.pack()
        self.OC_entry = tk.Entry(self.master, show="")
        self.OC_entry.pack()

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
        self.IC_entry = tk.Entry(self.master, show="")
        self.IC_entry.pack()

        self.output_label = tk.Label(self.master, text="Output currency:")
        self.output_label.pack()
        self.OC_entry = tk.Entry(self.master, show="")
        self.OC_entry.pack()

        self.amount_label = tk.Label(self.master, text="Amount to be exchanged:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(self.master, show="")
        self.amount_entry.pack()

        self.confirm_button = tk.Button(self.master, text="Confirm", command=self.remit_buy_in)
        self.confirm_button.pack()

    def cash_buy_in(self):

        input_currency = self.IC_entry.get()
        output_currency = self.OC_entry.get()
        input_amount = float(self.amount_entry.get())
        if input_currency.lower() == 'cny' and output_currency.lower() == 'usd':
            self.IC_entry.pack_forget()
            self.OC_entry.pack_forget()
            self.amount_entry.pack_forget()
            self.confirm_button.pack_forget()

            output_amount = float(input_amount) * 6.8781
            self.input_label.configure(text="The output amount is $" + str(output_amount))
            self.output_label.configure(text="Please wait for your cash to be dispensed!")
            self.amount_label.configure(text="Thank you for choosing The Bank of Computer Scientist!")
            if self.label4.winfo_exists():
                self.label4.pack_forget()

        else:
            self.label4 = tk.Label(self.master, text="Unknown currency!")
            self.label4.pack()

    def remit_buy_in(self):
        input_currency = self.IC_entry.get()
        output_currency = self.OC_entry.get()
        input_amount = float(self.amount_entry.get())
        if input_currency.lower() == 'cny' and output_currency.lower() == 'usd':
            self.IC_entry.pack_forget()
            self.OC_entry.pack_forget()
            self.amount_entry.pack_forget()
            self.confirm_button.pack_forget()

            output_amount = float(input_amount) * 6.8781
            self.input_label.configure(text="The output amount is $" + str(output_amount))
            self.output_label.configure(text="It has already been deposited to your "+ output_currency.upper() + " account!")
            self.amount_label.configure(text="Thank you for choosing The Bank of Computer Scientist!")
            if self.label4.winfo_exists():
                self.label4.pack_forget()

        else:
            self.label4 = tk.Label(self.master, text="Unknown currency!")
            self.label4.pack()

    def sell_cash(self):
        self.label1.pack_forget()
        self.cash_button.pack_forget()
        self.remit_button.pack_forget()

        self.input_label = tk.Label(self.master, text="Input currency:")
        self.input_label.pack()
        self.IC_entry = tk.Entry(self.master, show="")
        self.IC_entry.pack()

        self.output_label = tk.Label(self.master, text="Output currency:")
        self.output_label.pack()
        self.OC_entry = tk.Entry(self.master, show="")
        self.OC_entry.pack()

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
        self.IC_entry = tk.Entry(self.master, show="")
        self.IC_entry.pack()

        self.output_label = tk.Label(self.master, text="Output currency:")
        self.output_label.pack()
        self.OC_entry = tk.Entry(self.master, show="")
        self.OC_entry.pack()

        self.amount_label = tk.Label(self.master, text="Amount to be exchanged:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(self.master, show="")
        self.amount_entry.pack()

        self.confirm_button = tk.Button(self.master, text="Confirm", command=self.remit_sell_out)
        self.confirm_button.pack()

    def cash_sell_out(self):

        input_currency = self.IC_entry.get()
        output_currency = self.OC_entry.get()
        input_amount = float(self.amount_entry.get())
        if input_currency.lower() == 'cny' and output_currency.lower() == 'usd':
            self.IC_entry.pack_forget()
            self.OC_entry.pack_forget()
            self.amount_entry.pack_forget()
            self.confirm_button.pack_forget()

            output_amount = float(input_amount) * 6.7934
            self.input_label.configure(text="The output amount is $" + str(output_amount))
            self.output_label.configure(text="Please wait for your cash to be dispensed!")
            self.amount_label.configure(text="Thank you for choosing The Bank of Computer Scientist!")
            if self.label4.winfo_exists():
                self.label4.pack_forget()

        else:
            self.label4 = tk.Label(self.master, text="Unknown currency!")
            self.label4.pack()

    def remit_sell_out(self):
        input_currency = self.IC_entry.get()
        output_currency = self.OC_entry.get()
        input_amount = float(self.amount_entry.get())
        if input_currency.lower() == 'cny' and output_currency.lower() == 'usd':
            self.IC_entry.pack_forget()
            self.OC_entry.pack_forget()
            self.amount_entry.pack_forget()
            self.confirm_button.pack_forget()

            output_amount = float(input_amount) * 6.8491
            self.input_label.configure(text="The output amount is $" + str(output_amount))
            self.output_label.configure(text="It has already been deposited to your "+ output_currency.upper() + " account!")
            self.amount_label.configure(text="Thank you for choosing The Bank of Computer Scientist!")
            if self.label4.winfo_exists():
                self.label4.pack_forget()

        else:
            self.label4 = tk.Label(self.master, text="Unknown currency!")
            self.label4.pack()
    def logout(self):
        self.master.destroy()


root = tk.Tk()

my_gui = AFM(root)
root.mainloop()

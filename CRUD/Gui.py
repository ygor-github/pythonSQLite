from tkinter import *

class Gui():
    """Graphic Interface Class"""
    x_pad = 5
    y_pad = 3
    width_entry = 30
    
    #Create Windows (Fantasy Name "PYSQL")
    window = Tk()
    window.wm_title('PYSQL version 1.0')
    
    #Create Variables
    
    txtName = StringVar()
    txtLastName = StringVar()
    txtEmail = StringVar()
    txtCPF = StringVar()
    
    #Create Objects
    lblname = Label(window, text='Name')
    lblLastName = Label(window, text='LastName')
    lblemail = Label(window, text='Email')
    lblcpf = Label(window, text='CPF')
    entName = Entry(window, textvariable=txtName, width=width_entry)
    entLastName = Entry(window, textvariable=txtLastName,width=width_entry)
    entEmail = Entry(window, textvariable=txtEmail, width=width_entry)
    entCPF = Entry(window, textvariable=txtCPF, width=width_entry)
    listClients = Listbox(window,width=100)
    scrollClients = Scrollbar(window)
    btnViewAll = Button(window, text='Ver todos')
    btnSearch = Button(window, text = 'Buscar')
    btnInsert = Button(window, text = 'Inserir')
    btnUpdate = Button(window,  text= 'Atualizar Seleccionados')
    btnDel = Button(window, text= 'Deletar Selecionados')
    btnClose = Button(window, text='Fechar')

    #Grid
    lblname.grid(row=0,column=0)
    lblLastName.grid(row=1,column=0)
    lblemail.grid(row=2,column=0)
    lblcpf.grid(row=3,column=0)
    entName.grid(row=0,column=1, padx=50, pady=50)
    entLastName.grid(row=1, column=1)
    entEmail.grid(row=2, column=1)
    entCPF.grid(row=3, column=1)
    listClients.grid(row=0, column=2, rowspan=10)
    scrollClients.grid(row=0,column=6, rowspan=10)
    btnViewAll.grid(row=4, column=0, columnspan=2)
    btnSearch.grid(row=5, column=0, columnspan=2)
    btnInsert.grid(row=6, column=0, columnspan=2)
    btnUpdate.grid(row=7, column=0, columnspan=2)
    btnDel.grid(row=8, column=0, columnspan=2)
    btnClose.grid(row=9, column=0, columnspan=2)
    
    
    #Scrollbar with Listbox
    listClients.configure(yscrollcommand=scrollClients.set)
    scrollClients.configure(command=listClients.yview)
    
    #Swag
    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == 'Button':
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == 'Listbox':
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == 'Scrollbar':
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')
            
    def run(self):
        Gui.window.mainloop()
            
if __name__ == "__main__":
    gui = Gui()
    gui.run()
    
    
    
    
    
    
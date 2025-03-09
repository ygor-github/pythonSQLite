from Gui import *
from Backend import TransactionObject as Core

app = None
selected = None

def view_command():
    rows = Core.view()
    app.listClients.delete(0, END)
    for r in rows:
        app.listClients.insert(END, r)
        
def search_command():
    app.listClients.delete(0, END)
    rows= Core.search(app.txtName.get(), app.txtLastName.get(), app.txtEmail.get(), app.txtCPF.get())
    for r in rows:
        app.listClients.insert(END, r)
        
def insert_command():
    if Core.insert(app.txtName.get(), app.txtLastName.get(), app.txtEmail.get(), app.txtCPF.get()):
        view_command()
        app.entName.delete(0, END)
        app.entLastName.delete(0, END)
        app.entEmail.delete(0, END)
        app.entCPF.delete(0, END)
        app.entName.focus_set()

    
def update_command():
    if selected is not None:
        try:
            Core.update(selected[0],app.txtName.get(),app.txtLastName.get(), app.txtEmail.get(), app.txtCPF.get())
            view_command()
        except IndexError:
            print("Error: Please select a client to update.")
    else:
        print("Error: Please select a client to update.")
    
def del_command():
    if selected is not None:
        user_id = selected[0]
        Core.delete(user_id)
        view_command()
    else:
        print("Error: Please, Select a Client to Delete.")
    
def get_selected_row():
    global selected
    try:
        selection = app.listClients.curselection()
        if selection:
            index = selection[0]
            selected = app.listClients.get(index)
            app.entName.delete(0, END)
            app.entName.insert(END, selected[1])
            app.entLastName.delete(0,END)
            app.entLastName.insert(END, selected[2])
            app.entEmail.delete(0,END)
            app.entEmail.insert(END, selected[3])
            app.entCPF.delete(0,END)
            app.entCPF.insert(END, selected[4])
            return selected
        else:
            print("Error: Please, select a row")
    except IndexError:
        print("Error: Please, select a row")

if __name__ == '__main__':
    app = Gui()
    app.listClients.bind('<<ListboxSelect>>', get_selected_row)
    app.btnViewAll.configure(command=view_command)
    app.btnSearch.configure(command=search_command)
    app.btnInsert.configure(command=insert_command)
    app.btnDel.configure(command=del_command)
    app.btnUpdate.configure(command=update_command)
    app.btnClose.configure(command=app.window.destroy)
    app.run()
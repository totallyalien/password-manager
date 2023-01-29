import random
import pandas
import tkinter as tk
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
sym = ["!","@","#","$","^","&","*","(",")","_"]
num = [1,2,3,4,5,6,7,8,9,0]
comb = [alp,num,sym]

def password_genr():
    password = ""
    for x in range(0,10):
        temp = random.choice(random.choice(comb))
        if (temp in alp) and (x%2 == 0):
            password+= temp.upper()
        else:
            password+=str(temp)
    webs = site_box.get()
    site_box.delete(0,20)
    email = email_box.get()
    email_box.delete(0,20)
    passord_box.delete(0,20)
    passord_box.insert(0,password)
    temp = pandas.DataFrame({"website":[webs],
      "email":[email],
      "password":[password]})
    temp.to_csv("password_stor.csv",mode="a",index=False,header=False)
    window.clipboard_clear()
    window.clipboard_append(password)

def reset():
    email_box.delete(0,20)
    site_box.delete(0,20)
    passord_box.delete(0,20)

def sea(req):
    temp_pass=data[data["website"]==req]
    print(temp_pass)
    passord_box.delete(0,20)
    passord_box.insert(0,temp_pass.iloc[0][-1])
    email_box.delete(0,20)
    email_box.insert(0,temp_pass.iloc[0][-2])
    window.clipboard_clear()
    window.clipboard_append(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

data = pandas.read_csv("password_stor.csv")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.minsize(width=150,height=250)
window.config(pady=10,padx=10)
canva = tk.Canvas(bg="silver",width=350,height=350)
log = tk.PhotoImage(file="logo.png")
canva.create_image(170,100,image=log)
canva.pack()


site_label = tk.Label(text="SITE",bg="silver")
site_label.place(x=50,y=200)
site_box = tk.Entry(width=25)
site_box.place(x=130,y=200)
site_box.focus()

email_label = tk.Label(text="EMAIL",bg="silver")
email_label.place(x=50,y=220)
email_box = tk.Entry(width=25)
email_box.place(x=130,y=220)
password = tk.Label(text="PASSWORD",bg="silver")
password.place(x=50,y=240)
passord_box = tk.Entry(width=25)
passord_box.place(x=130,y=240)


search = tk.Button(text="SEARCH",command=lambda :sea(site_box.get()))
search.place(x=50,y=280)
generate = tk.Button(text="GENERATE",command=password_genr)
generate.place(x=140,y=280)
reset = tk.Button(text="RESET",command=reset)
reset.place(x=250,y=280)






window.mainloop()

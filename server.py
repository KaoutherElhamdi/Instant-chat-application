import socket
from tkinter import *
from tkinter.messagebox import *
from threading import Thread


Host = "127.0.0.1"
Port = 65432

#-----------------Interface_graphique------------------#
Mafenetre = Tk()
Mafenetre.title('Username')

Label1 = Label(Mafenetre, text = 'Your username ? : ')
Label1.pack(side = LEFT, padx = 5, pady = 5)

def validation():
    Mafenetre.destroy()

usernameserver = StringVar()
Champ = Entry(Mafenetre, textvariable= usernameserver, bg ='bisque', fg='maroon')
Champ.focus_set()
Champ.bind("<Return>", lambda event:validation())
Champ.pack(side = LEFT, padx = 5, pady = 5)


Bouton = Button(Mafenetre, text ='Valider',command = validation)
Bouton.pack(side = LEFT, padx = 5, pady = 5)

#Champ.bind("<Return>", validation)
Champ.pack(side = LEFT, padx = 5, pady = 5)
Mafenetre.mainloop()
usernameserver = usernameserver.get()
print("Your username : ",usernameserver)
#------------------------------------------------------#
def send() :
    msg_to_send1=msg_to_send.get()
    conn.send(msg_to_send1.encode())
    msg_list.insert(END, "You :  "+msg_to_send1)
    if msg_to_send1.lower() == "bye" :
            top.destroy()

def receive():
    while True:
        try :
            msg_received = conn.recv(1024).decode()
            msg_list.insert(END, "{} : {}".format(username,msg_received))
            
        except OSError :
            msg_list.insert(END, "Discussion terminé")
            break


#usernameserver =input("Your username ? : ")
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s :

#********************************
    top = Tk()
    top.title("Chat")

    messages_frame = Frame(top)
    msg_to_send = StringVar()  # For the messages to be sent.
    msg_to_send.set("Type your message here ")

    
    scrollbar = Scrollbar(messages_frame)
    msg_list = Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)
    msg_list.pack(side=LEFT, fill=BOTH)
    msg_list.pack()
    messages_frame.pack()


    entry_field = Entry(top, textvariable=msg_to_send)
    entry_field.bind("<Return>", lambda event:send())
    entry_field.pack()
    
    send_button = Button(top, text="Send", command=send)
    send_button.pack()
#********************************
    s.bind((Host,Port))
    s.listen()

    conn , addr = s.accept()

    print("We're connected to {}".format(addr))
    conn.send(("Welcome! Please give me your username. Mine is {}".
               format(usernameserver)).encode())
    username = conn.recv(1024).decode()
    
    receive_thread = Thread(target=receive)
    receive_thread.start()
    mainloop()

    conn.close()
        

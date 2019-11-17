from threading import Thread
import socket
from tkinter import *
from tkinter.messagebox import *

Host = "127.0.0.1"
Port = 65432

def send() :
    msg_to_send1=msg_to_send.get()
    s.send(msg_to_send1.encode())
    msg_list.insert(END, "You :  "+msg_to_send1)

def receive():
    while True:
        try :
            msg_received = s.recv(1024).decode()
            msg_list.insert(END, "{} : {}".format(usernameserver,msg_received))

        except OSError :
            msg_list.insert(END, "Discussion terminé")
            break


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s :
    s.connect((Host,Port))
    msg = s.recv(1024).decode()
    #-----------------Interface_graphique------------------#
    Mafenetre = Tk()
    Mafenetre.title('Username')


    def validation():
        Mafenetre.destroy()

    Label1 = Label(Mafenetre, text = msg)
    Label1.pack(padx = 5, pady = 5)

    username = StringVar()
    Champ = Entry(Mafenetre, textvariable= username, bg ='bisque', fg='maroon')
    Champ.focus_set()
    Champ.bind("<Return>", lambda event:validation())
    Champ.pack(padx = 5, pady = 5)

    Bouton = Button(Mafenetre, text ='Valider',command = validation)
    Bouton.pack( padx = 5, pady = 5)

    Mafenetre.mainloop()
    username = username.get()
    print(username)

    #------------------------------------------------------#

    usernameserver = msg[47:]
    s.send(username.encode())

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
    
    receive_thread = Thread(target=receive)
    receive_thread.start()
    mainloop()

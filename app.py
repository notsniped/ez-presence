### ------------------------------------------------------- ###
###      EZ PRESENCE - DEVELOPED AND MANAGED BY NOTSNIPED   ###
### ------------------------------------------------------- ###
###            thoseArchLinuxCoders 2021-2022               ###
### ------------------------------------------------------- ###

## Imports

import os
try:
    import pypresence
except:
    os.system('pip install pypresence')
try:
    from tkinter import *
except:
    print('Failed to initialize GUI. Try installing tk.\n  On Arch Linux: sudo pacman -S tk\n  On Debian/Ubuntu: sudo apt-get tk')
    raise SystemExit

## Init
root = Tk()
root.title('EZPresence - Easy Discord RPC')
root.geometry('500x500')
root.resizable(False, False)
try:
    icon = PhotoImage(file = "~/Desktop/EZ_presence/icons/500x500.png")
    root.iconphoto(False, icon)
except:
    print('WARN: Unable to load \'/icons/500x500.png\', running without icons.')
rpc = pypresence.Presence(947710719770632234, pipe=0, loop=None, handler=None)
#root.configure(background='#121212')  [Uncomment for Dark Mode (Later)!]

## Tk Design
label1 = Label(root, text='Details:')
input1 = Entry(root, width=30)
label1.place(relx=0.1, rely=0.1)
input1.place(relx=0.5, rely=0.1)
label2 = Label(root, text='State:')
input2 = Entry(root, width=30)
label2.place(relx=0.1, rely=0.2)
input2.place(relx=0.5, rely=0.2)
label3 = Label(root, text='Large Image Text:')
input3 = Entry(root, width=30)
label3.place(relx=0.1, rely=0.3)
input3.place(relx=0.5, rely=0.3)
label4 = Label(root, text='Small Image Text:')
input4 = Entry(root, width=30)
label4.place(relx=0.1, rely=0.4)
input4.place(relx=0.5, rely=0.4)
label5 = Label(root, text='Start Timestamp (UNIX):')
input5 = Entry(root, width=30)
label5.place(relx=0.1, rely=0.5)
input5.place(relx=0.5, rely=0.5)
label6 = Label(root, text='End Timestamp (UNIX):')
input6 = Entry(root, width=30)
label6.place(relx=0.1, rely=0.6)
input6.place(relx=0.5, rely=0.6)
label7 = Label(root, text='Party Size:')
input7 = Entry(root, width=30)
label7.place(relx=0.1, rely=0.7)
input7.place(relx=0.5, rely=0.7)
label8 = Label(root, text='Max Party Size:')
input8 = Entry(root, width=30)
label8.place(relx=0.1, rely=0.8)
input8.place(relx=0.5, rely=0.8)

label9 = Label(root, text='beta1.0')
label9.place(relx=0.03, rely=0.91)

## Functions and Classes
def startRPC():
    try:
        i1 = None
        i2 = None
        i3 = "EZPresence"
        i4 = "EZPresence"
        i5 = None
        i6 = None
        if input1.get() != "": i1 = input1.get()
        if input2.get() != "": i2 = input2.get()
        if input3.get() != "": i3 = input3.get()
        if input4.get() != "": i4 = input4.get()
        if input5.get() != "": i5 = input5.get()
        if input6.get() != "": i6 = input6.get()
        rpc.connect()
        rpc.update(state=str(i2), details=str(i1), start=i5, end=i6, large_text=str(i3), small_text=str(i4)) #large_text=str(i3), small_text=str(i4)#
        label9['fg'] = 'green'
        label9['text'] = 'Discord RPC started!'
    except Exception as e:
        label9['fg'] = '#FF0000'
        print(e)
        if e == 'Child "activity" fails because child "assets" fails because child "large_text" fails because "large_text" length must be at least 2 characters long\n':
            label9['text'] = '\'Large Image Text\' needs to be 2 or longer.'
        elif e == 'Child "activity" fails because child "assets" fails because child "small_text" fails because "small_text" length must be at least 2 characters long':
            label9['text'] = '\'Small Image Text\' needs to be 2 or longer.'
        else:
            label9['text'] = 'An error occured! Check console for info.'
        
        

def closeRPC():
    rpc.close()
    label9['fg'] = 'green'
    label9['text'] = 'Discord RPC closed.'

## Tk Design (Continuation XD)
btn1 = Button(root, text='Start RPC', command=startRPC)
btn1.place(relx=0.755, rely=0.9)
btn2 = Button(root, text='Close RPC', command=closeRPC)
btn2.place(relx=0.555, rely=0.9)

## Do Not Edit!
root.mainloop()
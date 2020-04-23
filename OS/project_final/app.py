import subprocess
import os
import time
from tkinter import *


app = Tk()
app.title("Banker's Algorithm")
app.geometry('600x600')

top_frame = Frame(app)
top_frame.pack(side = LEFT)

out_frame = Frame(app)
out_frame.pack(side = RIGHT)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

Button(top_frame, text="Restart", command=restart_program).pack()

Label(top_frame, text='No of Processes').pack()
prc = Entry(top_frame)
prc.pack()

Label(top_frame, text='No of Resources').pack()
rcs = Entry(top_frame)
rcs.pack()


def GiveInput():
    if os.path.exists("Output.osproject"):
        os.remove('Output.osproject')
    NoOfProcesses = int(prc.get())
    NoOfResources = int(rcs.get())

    Label(top_frame, text=f'Available Resources Space separated... {NoOfResources} Entries required').pack()
    ar = Entry(top_frame)
    ar.pack()

    AlWd = []
    for _ in range(NoOfProcesses):
        Label(top_frame, text=f'Allocated Resource for Process {_+1} Space separated... {NoOfResources} Entries required').pack()
        temp = Entry(top_frame)
        temp.pack()
        AlWd.append(temp)

    MaxWd = []
    for _ in range(NoOfProcesses):
        Label(top_frame, text=f'Max Resource for Process {_+1} Space separated... {NoOfResources} Entries required').pack()
        temp = Entry(top_frame)
        temp.pack()
        MaxWd.append(temp)

    def Compute():
        with open('data.osproject','w') as file:
            file.write(f"{NoOfProcesses}\n")
            file.write(f"{NoOfResources}\n")
            file.write(ar.get()+"\n")
            for _ in AlWd:
                file.write(_.get()+"\n")
            for _ in MaxWd:
                file.write(_.get()+"\n")


        # time.sleep(1)
        cmd = ["Algo.exe"]
        returned_value = subprocess.call(cmd)
        # print('returned value:', returned_value)
        # os.system("Algo2.exe")
        

        # os.system("./Algo2 >> Output.osproject")
        # os.system("./Algo")
        # print(x)

        # time.sleep(10)
        with open('Output.osproject','r') as f:
            Output = f.read()
        # print(Output)

        X = Label(out_frame, text=Output)
        X.pack()


    Compute = Button(top_frame, text='Compute', command = Compute)
    Compute.pack()


GiveInput = Button(top_frame, text='GiveInput', command = GiveInput)
GiveInput.pack()

app.mainloop()

import tkinter as tk
import time

class ChecklistBox(tk.Frame):
    def __init__(self, parent, choices, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)

        self.vars = []
        bg = self.cget("background")
        for choice in choices:
            var = tk.StringVar(value=choice)
            self.vars.append(var)
            cb = tk.Checkbutton(self, var=var, text=choice,
                                onvalue=choice, offvalue="",
                                anchor="w", width=20, background=bg,
                                relief="flat", highlightthickness=0
            )
            cb.pack(side="top", fill="x", anchor="w")


    def getCheckedItems(self):
        values = []
        for var in self.vars:
            value =  var.get()
            if value:
                values.append(value)
        return values

class Pomodoro(tk.Frame):

    def countdownTimer(self):
        times = int(self.min.get())*60 + int(self.sec.get())
        while times > -1:
            minute,second = (times // 60 , times % 60)
            if minute > 60:
                minute = minute % 60
            self.sec.set(second)
            self.min.set(minute)
            #Update the time
            self.update()
            time.sleep(1)
            if (times == 0):
                self.isBreak = not self.isBreak
                if not self.isBreak:
                    self.sec.set('00')
                    self.min.set('25')
                else:
                    self.sec.set('00')
                    self.min.set('05')
            times -= 1


    def __init__(self, root):
        tk.Frame.__init__(self, root)

        l = tk.Label(self, anchor="c", width=10, height=5)
        b = tk.Button(self, text="Start Timer", width=50, height=25, 
                      bg="red", fg="white", 
                      command=self.countdownTimer)
        
        c = ChecklistBox(self, ["Fix bugs", "Review PR", "Implement methods"])
        c.pack()

        l.pack(side="top", fill="both", expand=True)
        b.pack(side="top", fill="both", expand=True)

        self.min = tk.StringVar()
        self.sec = tk.StringVar()
        self.isBreak = False

        self.min.set('25')
        self.sec.set('00')
        tk.Entry(self, textvariable=self.min, width=2, font = 'Helvetica 14').place(x=150, y=90)
        tk.Entry(self, textvariable=self.sec, width=2, font = 'Helvetica 14').place(x=175, y=90)

if __name__=='__main__':
    root = tk.Tk()
    root.resizable(False, False)
    view = Pomodoro(root)
    view.pack(side="top", fill="both", expand=True)
    root.mainloop()
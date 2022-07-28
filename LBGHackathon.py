import tkinter as tk
import time

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
            if(times == 0):
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
        b = tk.Button(self, text="Start Timer", width=50, height=25, bg="red", fg="white", command=self.countdownTimer)
        l.pack(side="top", fill="both", expand=True)
        t = tk.Text().pack()
        b.pack(side="top", fill="both", expand=True)

        self.min = tk.StringVar()
        self.sec = tk.StringVar()
        self.isBreak = False

        self.min.set('25')
        self.sec.set('00')
        tk.Entry(self, textvariable=self.min, width=2, font = 'Helvetica 14').place(x=250, y=35)
        tk.Entry(self, textvariable=self.sec, width=2, font = 'Helvetica 14').place(x=275, y=35)

if __name__=='__main__':
    root = tk.Tk()
    root.resizable(False, False)
    view = Pomodoro(root)
    view.pack(side="top", fill="both", expand=True)
    root.mainloop()
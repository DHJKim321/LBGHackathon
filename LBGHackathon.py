import tkinter as tk

class Pomodoro(tk.Frame):
    todos = ""

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        l = tk.Label(self, text="Pomodoro Technique", anchor="c", width=10, height=10)
        b = tk.Button(self, text="Start Timer", width=100, height=50, bg="red", fg="white")
        l.pack(side="top", fill="both", expand=True)
        b.pack(side="top", fill="both", expand=True)
        t = tk.Entry()
        t.pack(side="bottom")
        self.todos = t.get()
        print(self.todos)

    def completeEnter(self, event):
        pass

if __name__=='__main__':
    root = tk.Tk()
    view = Pomodoro(root)
    view.pack(side="top", fill="both", expand=True)
    root.mainloop()
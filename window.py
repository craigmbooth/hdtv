import os
import Tkinter as tk
import ttk


class App(tk.Frame):
    def __init__(self, master, input_dict):
        """Make the window"""
        tk.Frame.__init__(self, master)

        self.tree = ttk.Treeview(self)
        ysb = ttk.Scrollbar(self, orient='vertical', command=self.tree.yview)
        xsb = ttk.Scrollbar(self, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)
        self.tree.heading('#0', text='Path', anchor='w')


        root_node = self.tree.insert('', 'end', text="Root", open=True)
        self.process_directory(root_node, input_dict)

        self.tree.grid(row=0, column=0)
        ysb.grid(row=0, column=1, sticky='ns')
        xsb.grid(row=1, column=0, sticky='ew')
        self.grid()

    def process_directory(self, parent, input_dict):
        """Given a parent object and pinput_dict, go for it."""
        for p, v in input_dict.iteritems():
            abspath = p
            isdict = isinstance(v, dict)
            oid = self.tree.insert(parent, 'end', text=p, open=False)
            if isdict:
                self.process_directory(oid, v)

root = tk.Tk()
root_dict = {"a": 1, "b": {"c": {"d": 1}}}
app = App(root, root_dict)
app.mainloop()

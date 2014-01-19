""""""
import os
import Tkinter as tk
import ttk
import pandas

MAX_LEN_IN_TREE = 10

class App(tk.Frame):
    def __init__(self, master, input_dict):
        """Make the window"""
        tk.Frame.__init__(self, master)

        self.tree = ttk.Treeview(self,columns=("type", "val"))
        ysb = ttk.Scrollbar(self, orient='vertical', command=self.tree.yview)
        xsb = ttk.Scrollbar(self, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)
        self.tree.heading('#0', text='Path', anchor='w')
        self.tree.heading('#1', text='Type', anchor='w')
        self.tree.heading('#2', text='Value', anchor='w')

        root_node = self.tree.insert('', 'end', text="root", open=True)
        self.parse_dict(root_node, input_dict)


        self.tree.grid(row=0, column=0)
        #self.tree.pack(side="left")
        ysb.grid(row=0, column=1, sticky='ns')
        xsb.grid(row=1, column=0, sticky='ew')
        self.grid()

    def value_properties(self, v):
        """

        :param v:
        :type v: Anything.
        """
        if type(v) in (str, int, float, unicode):
            return(type(v).__name__, v)
        else:
            return(type(v).__name__, "")


    def parse_dict(self, parent, input_dict):
        """Given a parent object and pinput_dict, go for it."""
        for p, v in input_dict.iteritems():
            oid = self.tree.insert(parent, 'end', text=p, open=False,
                                   value=self.value_properties(v))

            if isinstance(v, dict):
                self.parse_dict(oid, v)


if __name__ == "__main__":
    root = tk.Tk()

    longass_string = "dsfhads;ofhdasijfhdaslifjhadsifuhadsi;fuhadsi;fkhjasdi;fhuasd;ifuhdsafiadhsf;iadshufasdi;fhdsaljkfhsdaljhfbadsljhfbgadslfjhdsafjkhlsdaf"

    root_dict = {"a": 1, "a2": longass_string, "a3": u"unicode",
                 "a4": pandas.DataFrame(),
                 "b": {"c": {"d": 1}}}
    app = App(root, root_dict)
    app.mainloop()

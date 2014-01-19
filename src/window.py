""""""
import os
import Tkinter as tk
import ttk
import pandas
from handlers import *
import datetime

HANDLER_DICT = {
    str: summarize_str,
    unicode: summarize_str,
    float: summarize_float,
    dict: summarize_dict,
    datetime.datetime: summarize_datetime,
    datetime.date: summarize_date,
    list: summarize_list,
    int: summarize_int}

class DictView():
    def __init__(self, input_dict):
        """Make the window"""
        root = self.__initialize_gui()
        self.__populate_tree(input_dict)
        root.mainloop()


    def __populate_tree(self, input_dict):
        """AAAA"""
        root_node = self.tree.insert('', 'end', text="root", open=True)
        self.parse_dict(root_node, input_dict)


    def __initialize_gui(self):
        """Initialize elements in the GUI"""

        root = tk.Tk()

        self.frame = tk.Frame(root)

        self.tree = ttk.Treeview(self.frame,columns=("type", "val"))
        ysb = ttk.Scrollbar(root, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscroll=ysb.set)

        self.tree.heading('#0', text='Path', anchor='w')
        self.tree.heading('#1', text='Type', anchor='w')
        self.tree.heading('#2', text='Value', anchor='w')

        self.tree.column('#0', width=300)
        self.tree.column('#1', width=100, stretch=False)
        self.tree.column('#2', width=500)

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)

        root.grid()

        self.frame.grid(row=0, column=0, sticky=(tk.N+tk.S+tk.E+tk.W))
        self.tree.grid(row=0, column=0, sticky=(tk.N+tk.S+tk.E+tk.W))
        ysb.grid(row=0, column=1, sticky='nsew')

        return root

    def value_properties(self, v):
        """
        Given any value in a dictionary, return its type and a summary of its
        contents.

        :param v: Input variable
        :type v: Anything.

        :return: A tuple with two elements.  The first is the string
            representation of the type of the variable, the second is a string
            containing a short string summary of the contents of the variable,
            or if it is not handled, the string "unhandled variable type"
        :rtype: ``tuple`` containing two strings
        """
        if type(v) in HANDLER_DICT:
            return(type(v).__name__, HANDLER_DICT[type(v)](v))
        else:
            return(type(v).__name__, "Unhandled variable type")


    def parse_dict(self, parent, input_dict):
        """Given a parent object and input_dict, go for it."""
        for p, v in input_dict.iteritems():
            oid = self.tree.insert(parent, 'end', text=p, open=False,
                                   value=self.value_properties(v))
            if isinstance(v, dict):
                self.parse_dict(oid, v)


if __name__ == "__main__":


    longass_string = "dsfhads;ofhdasijfhdaslifjhadsifuhadsi;fuhadsi;fkhjasdi;fhuasd;ifuhdsafiadhsf;iadshufasdi;fhdsaljkfhsdaljhfbadsljhfbgadslfjhdsafjkhlsdaf"

    root_dict = {"a": 1, "a2": longass_string, "a3": u"unicode",
                 "a5": datetime.datetime(2013, 10, 10, 12, 12, 12),
                 "a6": datetime.date(2013, 10, 10),
                 "a4": pandas.DataFrame(),
                 "a9": [1, 2, 3],
                 "a10": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                 "b": {"c": {"d": 1}}}
    DictView(root_dict)

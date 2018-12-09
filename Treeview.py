#!/usr/bin/env python2
    #
    # FILE:     SO_33290969.py
    # CREATED:  2015-10-28

import tkinter as tk
from tkinter import ttk

from tkinter import *

class some_Class(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.master=args[0]
        self.grid()

        self.some_function()

    def some_function(self):
        self.tree = ttk.Treeview(self.master)
        ttk.Style().configure("displayField", background="#850664", foreground="#000000", fieldbackground="#FFFFFF")
        ysb = ttk.Scrollbar(self.master, command=self.tree.yview, orient=tk.VERTICAL)
        xsb = ttk.Scrollbar(self.master, command=self.tree.xview, orient=tk.HORIZONTAL)
        self.tree.configure(yscrollcommand=ysb.set)
        self.tree.configure(xscrollcommand=xsb.set)

        self.tree["columns"]=("trackNumber", "trackTitle", "artistCat", "artistDisplay", "trackArtist", "album",
                          "albumLabel", "composer", "year", "trackDuration", "albumAsin", "albumItunes", "ISRC",
                          "filename", "albumCoverName", "notes")
        self.tree.column("trackNumber", stretch=0,  anchor=N)
        self.tree.column("trackTitle", stretch=0,  anchor=N)
        self.tree.column("artistCat", stretch=0,  anchor=N)
        self.tree.column("artistDisplay", stretch=0,  anchor=N)
        self.tree.column("trackArtist", stretch=0,  anchor=N)
        self.tree.column("album", stretch=0,  anchor=N)
        self.tree.column("albumLabel", stretch=0,  anchor=N)
        self.tree.column("composer", stretch=0, anchor=N)
        self.tree.column("year", stretch=0,  anchor=N)
        self.tree.column("trackDuration", stretch=0, anchor=N)
        self.tree.column("albumAsin", stretch=0, anchor=N)
        self.tree.column("albumItunes", stretch=0, anchor=N)
        self.tree.column("filename", stretch=0,  anchor=N)
        self.tree.column("albumCoverName", stretch=0,  anchor=N)
        self.tree.column("notes", stretch=0, anchor=N)
        self.tree.heading("trackNumber", text="Track Number")
        self.tree.heading("trackTitle", text="Track Title")
        self.tree.heading("artistCat", text="Artist CAT")
        self.tree.heading("artistDisplay", text="Artist Display")
        self.tree.heading("trackArtist", text="Track Artist")
        self.tree.heading("album", text="Album")
        self.tree.heading("albumLabel", text="Album Label")
        self.tree.heading("composer", text="Composer")
        self.tree.heading("year", text="Year")
        self.tree.heading("trackDuration", text="Track Duration")
        self.tree.heading("albumAsin", text="Album ASIN")
        self.tree.heading("albumItunes", text="Album iTunes")
        self.tree.heading("ISRC", text="ISRC")
        self.tree.heading("filename", text="File Name")
        self.tree.heading("albumCoverName", text="Album Cover Filename")
        self.tree.heading("notes", text="Notes")
        self.tree.grid(in_=self.master, row=0, column=0, sticky=tk.NW+tk.SE)
        ysb.grid(in_=self.master, row=0, column=1, sticky=tk.NS)
        xsb.grid(in_=self.master, row=1, column=0, sticky=tk.EW)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)

        self.loadUI()

    def loadUI(self, event=None):
        tk.Button(self.master, text="filter columns", command=self.some_other_function).grid(row=2, column=0)
        tk.Button(self.master, text="load data", command=self.loadData).grid(row=2, column=1)

    def loadData(self, event=None):
        self.tree.insert("", tk.END, values=(["data%s"%col for col in self.tree["columns"]]))

    def some_other_function(self):
        if len(self.tree["displaycolumns"]) != 2:
            print("Hiding Columns")
            self.tree["displaycolumns"]=("artistCat", "artistDisplay")
        else:
            print("Showing all columns")
            self.tree["displaycolumns"]=self.tree["columns"]

        print("Visible:   %s"%','.join([ "%s"%col for col in self.tree["displaycolumns"] ]))
        print("Available: %s"%','.join([ "%s"%col for col in self.tree["columns"] ]))
        print("Done.")

if __name__=="__main__":
        root=tk.Tk()
        app=some_Class(root)
        app.grid()
        root.mainloop()
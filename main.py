#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

abuilder = Gtk.Builder()
abuilder.add_from_file("forms.glade")
# now the builde got our gui

class Handler:
    def on_button_clicked(self, button):
        print("Hello World!")


ourForm1 = abuilder.get_object("Form1")
abuilder.connect_signals(Handler())

ourForm1.show_all() 
Gtk.main()

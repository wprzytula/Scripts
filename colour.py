import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
gi.require_version("Gdk", "3.0")
from gi.repository import Gdk

import sys

datum = str(sys.argv[1])
def parse(x):
    if x.startswith('#'):
        x = x[1:]
    x = list(x)
    while x:
        a = x.pop(0) + x.pop(0)
        yield int(a, 16)

next_colour = parse(datum)

def create_window():
    window = Gtk.Window()
    window.set_default_size(200, 200)
    window.connect('destroy', Gtk.main_quit)
    #red = next_colour
    #green = next_colour
    #blue = next_colour
    color = Gdk.RGBA(next(next_colour), next(next_colour), next(next_colour))
    window.override_background_color(Gtk.StateFlags.NORMAL, color)

    window.maximize()
    window.show()

create_window()
Gtk.main()

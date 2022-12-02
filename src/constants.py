"""
    Constants
"""
TITLE = "Calculator"

# Resizable Tuple[bool] (is-resizable-x?, is-resizable-y?):
RESIZABLE = (False, False)

"""
    Tkinter widget properties
"""
# Properties of the master Tkinter widget
MASTER = {
    'bg': "#000",

}

# NOTE: The Widgets are declaration is arranged in alphabetical order

# Properties of any Entry Widget
ENTRY = {
    'font': "Roboto",
    'bg': "#fff",
    'fg': "#001",
    'width': 50,
    'justify': 'right',
}

# NOTE: The pack, grid and place method arguments are here for each widget
ENTRY_PACK = {
    'ipadx': 5,
    'ipady': 5,
    'padx': 10,
    'pady': 10,
}
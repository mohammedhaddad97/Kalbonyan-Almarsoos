'''
    Tuples are immutable meaning; once they're created they cannot be changed or modified.
'''

import tkinter

def mouse_click(event):
    coords = root.winfo_pointerxy()
    print('coords: {}'.format(coords))  
    print('X: {}'.format(coords[0]))
    print('Y: {}'.format(coords[1]))

root = tkinter.Tk()
root.bind('<Button>', mouse_click)
root.mainloop()

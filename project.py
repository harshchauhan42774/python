from tkinter import *
from tkcalendar import Calendar

def show_calendar():
    top = Toplevel(root)
    top.title("Calendar")
    
    cal = Calendar(top, font="Arial 14", selectmode="day", cursor="hand1", year=2023, month=12, day=23)
    cal.pack(fill="both", expand=True)
        
    def get_date():
        selected_date = cal.get_date()
        selected_date_label.config(text=f"Selected Date: {selected_date}")
    
    ok_button = Button(top, text="OK", command=get_date)
    ok_button.pack(pady=10)
    
    selected_date_label = Label(top, text="")
    selected_date_label.pack(pady=10)

root = Tk()
root.title("Calendar Application")

show_calendar_button = Button(root, text="Show Calendar", command=show_calendar)
show_calendar_button.pack(pady=20)

root.mainloop()

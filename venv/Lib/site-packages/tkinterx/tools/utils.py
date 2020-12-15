from tkinter import ttk, Toplevel


class ToolTip:
    """
    Create a tooltip for a given widget
    (inspired by https://stackoverflow.com/a/36221216)
    This is an INTERNALLY USED only class.  Users should not refer to this class at all.
    """

    def __init__(self, widget, text, timeout=400):
        """
        :param widget: The tkinter widget
        :type widget: widget type varies
        :param text: text for the tooltip. It can inslude \n
        :type text: str
        :param timeout: Time in milliseconds that mouse must remain still before tip is shown
        :type timeout: int
        """
        self.widget = widget
        self.text = text
        self.timeout = timeout
        # self.wraplength = wraplength if wraplength else widget.winfo_screenwidth() // 2
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)

    def enter(self, event=None):
        """
        Called by tkinter when mouse enters a widget
        :param event:  from tkinter.  Has x,y coordinates of mouse

        """
        self.x = event.x
        self.y = event.y
        self.schedule()

    def leave(self, event=None):
        """
        Called by tktiner when mouse exits a widget
        :param event:  from tkinter.  Event info that's not used by function.

        """
        self.unschedule()
        self.hidetip()

    def schedule(self):
        """
        Schedule a timer to time how long mouse is hovering
        """
        self.unschedule()
        self.id = self.widget.after(self.timeout, self.showtip)

    def unschedule(self):
        """
        Cancel timer used to time mouse hover
        """
        if self.id:
            self.widget.after_cancel(self.id)
        self.id = None

    def showtip(self):
        """
        Creates a topoltip window with the tooltip text inside of it
        """
        if self.tipwindow:
            return
        x = self.widget.winfo_rootx() + self.x + 0
        y = self.widget.winfo_rooty() + self.y + 20
        self.tipwindow = Toplevel(self.widget)
        self.tipwindow.wm_overrideredirect(True)
        self.tipwindow.wm_geometry("+%d+%d" % (x, y))
        self.tipwindow.wm_attributes("-topmost", 1)

        label = ttk.Label(self.tipwindow, text=self.text, justify='left',
                          background="#ffffe0", relief='solid', borderwidth=1)
        label.pack()

    def hidetip(self):
        """
        Destroy the tooltip window
        """
        if self.tipwindow:
            self.tipwindow.destroy()
        self.tipwindow = None

import customtkinter as ctk
from hPyT import title_bar, maximize_minimize_button


class STk(ctk.CTk):
    """A slightly modified version of CTK class using the hPyT module."""
    
    
    def rem_titlebar(self):
        """Removes the title bar from the window safely."""
        title_bar.hide(self)
        
    def rem_mini_maximize_button(self):
        """Remove the minimize and maximize buttons from the window safely."""
        maximize_minimize_button.hide(self)
        
        
        
class STkTopLevel(ctk.CTkToplevel):
    """A slightly modified version of CTKToplevel class using the hPyT module."""
    
    def rem_titlebar(self):
        """Removes the title bar from the toplevel window safely."""
        title_bar.hide(self)
    
    def rem_mini_maximize_button(self):
        """Remove the minimize and maximize buttons from the toplevel window safely."""
        maximize_minimize_button.hide(self)
        
        
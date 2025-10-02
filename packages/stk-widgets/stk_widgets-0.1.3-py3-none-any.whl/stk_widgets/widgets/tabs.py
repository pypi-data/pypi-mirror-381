import customtkinter as ct


class TabbedFrame(ct.CTkFrame):
    def __init__(
        self,
        master,
        spacing: bool = True,
        fg_color: str|tuple[str, str] = "transparent",
        hover_color:str|tuple[str, str]=("#F0F0F0", "grey30"),
        text_color:str|tuple[str, str]=("black", "white"),
        select_color:str|tuple[str, str]="blue",
        selected_hover_color:str|tuple[str, str]="#00008B",
        **kwargs
    ):
        """
        A frame with tab management.
        
        :param master: the parent widget or window.
        :param spacing: whether to allow spacing between the tab frame and the main frame
        :param fg_color: regular ctk fg.
        :param hover_color: regular ctk hover.
        :param text_color: regular ctk text color.
        :param select_color: the color of the currently selected tab.
        :param selected_hover_color: the hover color of the currently selected tab.
        """
        super().__init__(master, **kwargs)
        
        self._fg_color = fg_color
        self._hover_color = hover_color
        self._text_color = text_color
        self._select_color = select_color
        self._selected_hover_color = selected_hover_color
        self._spacing = 5 if spacing else 0
        
        # Layout configuration
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        
        # Tab bar
        self._tab_frame = ct.CTkFrame(self, fg_color=self._fg_color)
        self._tab_frame.grid(row=0, column=0, sticky="ew", padx=self._spacing, pady=self._spacing)
        self._tab_frame.rowconfigure(0, weight=1)
        
        # Main content frame
        self._main_frame = ct.CTkFrame(self, fg_color=self._fg_color)
        self._main_frame.grid(row=1, column=0, sticky="nsew", padx=self._spacing, pady=self._spacing)
        self._main_frame.rowconfigure(0, weight=1)
        self._main_frame.columnconfigure(0, weight=1)
        
        # Tabs storage
        self._tab_buttons = []
        self._tab_frames = {}
        self._relation = {}
    
    def add_tab(self, name: str, image: ct.CTkImage = None) -> ct.CTkFrame:
        """Add a new tab and return its content frame."""
        btn = ct.CTkButton(
            self._tab_frame,
            text=name,
            fg_color=self._fg_color,
            text_color=self._text_color,
            hover_color=self._hover_color,
            image=image,
            corner_radius=1000,
            command=lambda: self.open_tab(name)
        )
        btn.bind("<Button-1>", lambda _: self._update_tabs(btn))
        self._tab_buttons.append(btn)
        self._reposition_tabs()  # Ensure all tabs share space equally
        
        # Create associated frame
        frame = ct.CTkFrame(self._main_frame, fg_color=self._fg_color)
        self._tab_frames[name] = frame
        self._relation[name] = btn
        return frame
    
    def _update_tabs(self, tab_button:ct.CTkButton):
        for btn in self._tab_buttons:
            btn.configure(fg_color=self._fg_color, hover_color=self._hover_color)
        tab_button.configure(fg_color=self._select_color, hover_color=self._selected_hover_color)
    
    def _reposition_tabs(self):
        """Ensure all tab buttons share equal width."""
        for index, btn in enumerate(self._tab_buttons):
            btn.grid(row=0, column=index, sticky="ew", padx=(self._spacing // 2, self._spacing // 2))
            self._tab_frame.columnconfigure(index, weight=1)
    
    def open_tab(self, name: str):
        """Show the tab associated with 'name'."""
        frame = self._tab_frames.get(name)
        if not frame:
            return
        for widget in self._main_frame.winfo_children():
            widget.grid_forget()
        frame.grid(row=0, column=0, sticky="nsew", padx=self._spacing, pady=self._spacing)
    
    def set(self, name: str):
        """Set initial tab programmatically."""
        self.open_tab(name)
        self._update_tabs(self._relation[name])


if __name__ == "__main__":
    win = ct.CTk()
    win.geometry("500x300")
    
    tab = TabbedFrame(win)
    tab.pack(fill="both", expand=True)
    
    home = tab.add_tab("Home")
    ct.CTkLabel(home, text="Home").pack(fill="both", expand=True)
    
    settings = tab.add_tab("Settings")
    ct.CTkLabel(settings, text="Settings").pack(fill="both", expand=True)
    
    about = tab.add_tab("About")
    ct.CTkLabel(about, text="About").pack(fill="both", expand=True)
    
    tab.set("Home")
    win.mainloop()
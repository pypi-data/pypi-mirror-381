import customtkinter as ctk
from PIL import Image, ImageDraw, ImageFont, ImageTk

class ChatBubble(ctk.CTkCanvas):
    def __init__(self, master, text,
                 light_color=None, dark_color=None,
                 text_color=("black", "white"),
                 font=("Arial", 14),
                 padding=(12, 8),
                 max_width=250,
                 command=None,
                 **kwargs):
        super().__init__(master, highlightthickness=0, bg=master.cget("bg"), **kwargs)

        self.text = text
        self.light_color = light_color or "#e0e0e0"
        self.dark_color = dark_color or self.light_color
        self.text_color = text_color
        self.font = font
        self.padding = padding
        self.max_width = max_width
        self.command = command

        self.hovered = False

        # Pillow font
        self.pil_font = ImageFont.truetype("arial.ttf", self.font[1]) if isinstance(self.font, tuple) else self.font

        # Bind click & hover events
        self.bind("<Button-1>", self._on_click)
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)

        self._draw()

    def _get_current_colors(self):
        mode = ctk.get_appearance_mode().lower()
        bg_color = self.light_color if mode == "light" else self.dark_color
        if self.hovered:
            # Slightly darken/lighten for hover
            bg_color = self._adjust_color(bg_color, factor=0.85)
        return bg_color, self.text_color[0] if mode=="light" else self.text_color[1]

    def _adjust_color(self, hex_color, factor=0.9):
        """Darken or lighten a hex color."""
        hex_color = hex_color.lstrip('#')
        r = int(int(hex_color[0:2], 16) * factor)
        g = int(int(hex_color[2:4], 16) * factor)
        b = int(int(hex_color[4:6], 16) * factor)
        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))
        return f"#{r:02x}{g:02x}{b:02x}"

    def _wrap_text_pixel(self, text, draw):
        """Wrap text so each line fits max_width in pixels."""
        words = text.split()
        lines = []
        current_line = ""

        for word in words:
            test_line = f"{current_line} {word}".strip()
            bbox = draw.textbbox((0, 0), test_line, font=self.pil_font)
            width = bbox[2] - bbox[0]
            if width <= self.max_width - 2*self.padding[0]:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)

        # Handle explicit line breaks
        final_lines = []
        for line in lines:
            final_lines.extend(line.split("\n"))
        return final_lines

    def _draw(self, *args):
        bubble_color, text_color = self._get_current_colors()

        dummy_img = Image.new("RGB", (1, 1))
        draw = ImageDraw.Draw(dummy_img)

        # Wrap text based on pixel width
        lines = self._wrap_text_pixel(self.text, draw)

        # Measure size
        line_heights = []
        max_line_width = 0
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=self.pil_font)
            w = bbox[2] - bbox[0]
            h = bbox[3] - bbox[1]
            max_line_width = max(max_line_width, w)
            line_heights.append(h)

        # Pill shape: height = sum of text + padding + line spacing
        w = max_line_width + self.padding[0]*2
        h = sum(line_heights) + self.padding[1]*2 + (len(lines)-1)*2  # 2px line spacing

        # Ensure fully pill-shaped: radius = half of height
        radius = h//2

        # Create bubble image with transparency
        img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Draw fully pill-shaped background
        draw.rounded_rectangle((0, 0, w, h), radius=radius, fill=bubble_color)

        # Draw text line by line, centered vertically
        y = self.padding[1]
        for line, line_h in zip(lines, line_heights):
            draw.text((self.padding[0], y), line, font=self.pil_font, fill=text_color)
            y += line_h + 2

        self.photo = ImageTk.PhotoImage(img)

        self.config(width=w, height=h, bg=self.master.cget("bg"))
        self.delete("all")
        self.create_image(0, 0, image=self.photo, anchor="nw")

    def _on_click(self, event):
        if self.command:
            self.command()

    def _on_enter(self, event):
        self.hovered = True
        self._draw()

    def _on_leave(self, event):
        self.hovered = False
        self._draw()


# Example usage
if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()

    long_text = ("This is a really long text that should wrap automatically into multiple lines "
                 "so that the chat bubble looks like a proper message in a chat app.")

    def on_click():
        print("Bubble clicked!")

    bubble1 = ChatBubble(root, long_text,
                         light_color="#d1f0ff",
                         dark_color="#1e3d5f",
                         command=on_click)
    bubble1.pack(padx=20, pady=20)

    bubble2 = ChatBubble(root, "Single line bubble",
                         light_color="#a8d8a8",
                         command=lambda: print("Second bubble clicked!"))
    bubble2.pack(padx=20, pady=20)

    root.mainloop()
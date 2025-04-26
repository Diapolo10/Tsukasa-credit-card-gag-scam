"""Display a fake credit card scam joke window."""

import sys
import tkinter as tk
from pathlib import Path

from PIL import Image, ImageSequence, ImageTk

FRAME_DELAY = 140  # in ms, roughly equivalent to ~7 FPS


def resource_path(relative_path: str | Path) -> Path:
    """
    Get absolute path to resource.

    Works for dev and for PyInstaller.
    """
    base_dir = Path(__file__).parent

    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_dir = Path(sys._MEIPASS)  # noqa: SLF001

    return base_dir / relative_path


def intro_text() -> None:
    """Show the main text label."""
    intro = tk.Label(
        text="H-hi there...\nDo you th-think I could have your\ncredit card information, p-please?",
        bg="#FFFFFF",
        fg="#000000",
        font=("Arial", 15),
        padx=0,
        pady=0,
    )
    intro.grid(row=0, rowspan=1, column=1, columnspan=3)


def text_w_entrybox(
    root: tk.Tk,
    text_label_sentence: str,
    text_row: int,
    text_rowspan: int,
    text_column: int,
    text_columnspan: int,
    entry_row: int,
    entry_rowspan: int,
    entry_column: int,
    entry_columnspan: int,
) -> None:
    """Create the entry box."""
    text_label = tk.Label(
        root,
        text=text_label_sentence,
        bg="#FFFFFF",
        fg="#000000",
        font=("Arial", 15),
    )
    text_label.grid(
        row=text_row,
        rowspan=text_rowspan,
        column=text_column,
        columnspan=text_columnspan,
    )

    entry_box = tk.Entry(root, width=35)
    entry_box.grid(
        row=entry_row,
        rowspan=entry_rowspan,
        column=entry_column,
        columnspan=entry_columnspan,
        sticky=tk.W,
    )


class AnimatedGIF:
    """A wrapper for displaying GIF animations."""

    def __init__(self: "AnimatedGIF", parent: tk.Tk, file_path: Path) -> None:
        """Initialise the GIF wrapper."""
        self.parent = parent

        # size of the image (500x286 is the original gif size)
        self.canvas = tk.Canvas(parent, width=278, height=286, bg="#FFFFFF")
        self.canvas.grid(row=0, rowspan=5, column=0, columnspan=1)

        self.sequence = []
        with Image.open(file_path) as image_file:
            for img in ImageSequence.Iterator(image_file):
                self.sequence.append(ImageTk.PhotoImage(img))

        self.frame = 0

        # Make the number of this 0.5 the size of the image
        self.image = self.canvas.create_image(139, 143, image=self.sequence[self.frame])

    def increment_frame(self: "AnimatedGIF") -> None:
        """Update the current frame index."""
        self.frame = (self.frame + 1) % len(self.sequence)

    def animate(self: "AnimatedGIF") -> None:
        """Handle the animation by re-rendering the current frame."""
        self.increment_frame()
        self.parent.after(FRAME_DELAY, self.animate)
        self.canvas.itemconfig(self.image, image=self.sequence[self.frame])


def main() -> None:
    """Run the main program."""
    # Resources
    root = tk.Tk()
    window_icon = resource_path(Path("data") / "icon_ico.ico")
    tsukasa_gif_file = resource_path(Path("data") / "tsukasa.gif")
    thx_button = resource_path(Path("data") / "thanks_button.png")

    thanksbutton_image = tk.PhotoImage(file=thx_button)
    button_quit = tk.Button(
        root,
        image=thanksbutton_image,
        command=root.quit,
        bg="#FFFFFF",
        borderwidth=0,
    )

    # Window Info
    root.geometry("")
    root.title("Totally Not Malware")
    root.iconbitmap(window_icon)
    root.configure(background="#FFFFFF")
    root.resizable(width=False, height=False)  # Disables window resizing

    # Main display stuff
    gif = AnimatedGIF(root, tsukasa_gif_file)
    gif.animate()
    intro_text()
    text_w_entrybox(root, "Card number:", 1, 1, 1, 1, 1, 1, 2, 2)
    text_w_entrybox(root, "Expiry date:", 2, 1, 1, 1, 2, 1, 2, 2)
    text_w_entrybox(root, "Security code:", 3, 1, 1, 1, 3, 1, 2, 2)
    button_quit.grid(row=4, column=2, sticky=tk.W)

    # Main loop
    root.mainloop()


if __name__ == "__main__":
    main()

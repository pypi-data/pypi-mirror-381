import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from customtkinter import CTkImage
import time
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk, ImageSequence
import importlib.resources as ires
import traceback
import os

icons = {
    'user': os.path.join(os.path.dirname(__file__), 'icon/circle-user.png'),
    'lock': os.path.join(os.path.dirname(__file__), 'icon/lock.png'),
    'eye': os.path.join(os.path.dirname(__file__), 'icon/eye.png'),
    'search': os.path.join(os.path.dirname(__file__), 'icon/search.png'),
    'cart': os.path.join(os.path.dirname(__file__), 'icon/shopping-cart.png'),
    'crossed_eye': os.path.join(os.path.dirname(__file__), 'icon/crossed-eye.png'),
    'app': os.path.join(os.path.dirname(__file__), 'icon/app.ico'),
}


def config(title, width=0, height=0):
    root = tk.Tk()
    root.title(title)
    if width > 0 and height > 0:
        root.geometry(f"{width}x{height}")
    else:
        root.state('zoomed')
    return root

def ImageGif(parent, gif_path, width=None, height=None):
    """
    Menampilkan GIF animasi di Tkinter.
    
    Parameters:
    - parent: widget induk
    - gif_path: path file GIF
    - width, height: opsional, resize GIF
    """
    label = tk.Label(parent)
    label.pack()

    pil_gif = Image.open(gif_path)

    # Resize jika diminta
    frames = []
    for frame in ImageSequence.Iterator(pil_gif):
        if width and height:
            frame = frame.resize((width, height))
        frames.append(ImageTk.PhotoImage(frame))

    def animate(counter=0):
        label.config(image=frames[counter])
        parent.after(100, animate, (counter + 1) % len(frames))

    animate()
    return label

def textView(parent, text, fontSize=12, textColor='black'):
    label = tk.Label(
        parent,
        text=text,
        fg=textColor,
        bg=None,
        font=("Arial", fontSize)
    )
    return label

def safe_callback(callback):
    def wrapper(*args, **kwargs):
        try:
            return callback(*args, **kwargs)
        except Exception as e:
            now = time.strftime('%H:%M:%S')
            print(f"[{now}] Error di callback:\n{traceback.format_exc()}")

            # Tampilkan popup juga jika mau
            messagebox.showerror("Terjadi Error", f"{type(e).__name__}: {str(e)}")
    return wrapper
def Colors():
    return {
        'primary': '#0d6efd',
        'secondary': '#6c757d',
        'success': '#198754',
        'danger': '#dc3545',
        'warning': '#ffc107',
        'info': '#0dcaf0',
        'light': '#f8f9fa',
        'dark': '#212529'
    }

colors = {
    'primary': '#0d6efd',
    'secondary': '#6c757d',
    'success': '#198754',
    'danger': '#dc3545',
    'warning': '#ffc107',
    'info': '#0dcaf0',
    'light': '#f8f9fa',
    'dark': '#212529'
}

def buttonView(
    parent,
    text="Click",
    backgroundColor=None,
    textColor="white",
    borderOutline=False,
    radius=10,
    width=120,
    height=40,
    command=None
):
    colors = Colors()

    if borderOutline:
        # Tombol outline: background transparan, border berwarna primary
        bg = "transparent"
        fg_border = backgroundColor if backgroundColor else colors['primary']
    else:
        bg = backgroundColor if backgroundColor else colors['primary']
        fg_border = None

    # Hover color
    hover = "#0b5ed7" if not backgroundColor else backgroundColor

    return ctk.CTkButton(
        parent,
        text=text,
        width=width,
        height=height,
        corner_radius=radius,
        fg_color=bg,
        hover_color=hover,
        text_color=textColor,
        border_width=2 if borderOutline else 0,
        border_color=fg_border,
        command=command
    )




def progressView(parent, length=100, max=100, value=20, mode='determinate', orient='horizontal'):
    return ttk.Progressbar(
        parent,
        length=length,
        mode=mode,
        orient=orient,
        maximum=max,
        value=value
    )

def styleInput(width, backgroundColor=None, border=2, textColor='white', fontFamily="Arial", fontSize=10, relief='groove'):
    style = {
        'width': width,
        'fg': textColor,
        'font': (fontFamily, fontSize),
        'bd': border,
        'relief': relief
    }
    if backgroundColor is not None:
        style['bg'] = backgroundColor
    return style

def load_icon(name, size=(20, 20)):
    try:
        with ires.files("chaeruldesktop.icons").joinpath(name).open("rb") as f:
            img = Image.open(f)
            return CTkImage(img, size=size)
    except Exception as e:
        print("Gagal load icon:", e)
        return None
    
def inputView(
    parent,
    icon=None,
    eyeIcon=False,
    placeholder="",
    width=200,
    height=30,
    textColor="black",
    backgroundIconColor=None,
    borderColor=None,
    border=1,
    fontSize=12,
    radius=6,
    show=None
):
    frame = ctk.CTkFrame(parent, fg_color="transparent")

    # Kurangi width jika ada eyeIcon supaya totalnya tidak terlalu besar
    if eyeIcon:
        width -= 30  # sesuaikan dengan lebar tombol mata

    # Ikon kiri
    if icon is not None:
        try:
            pil_img = Image.open(icon)
            img = CTkImage(pil_img, size=(20, 20))
            label_icon = ctk.CTkLabel(frame, image=img, text="")
            label_icon.image = img
            label_icon.pack(side="left", padx=(0, 5))
        except Exception as e:
            print("Gagal load icon:", e)

    # Entry field
    entry_var = tk.StringVar()
    entry = ctk.CTkEntry(
        frame,
        textvariable=entry_var,
        placeholder_text=placeholder,
        width=width,
        height=height,
        corner_radius=radius,
        border_width=border,
        border_color=borderColor,
        fg_color=backgroundIconColor,
        text_color=textColor,
        font=("Arial", fontSize),
        show=show
    )
    entry.pack(side="left", fill="x", expand=True)

    # Tombol toggle mata (eye icon)
    if eyeIcon:
        width -= 30  # sesuaikan dengan lebar tombol mata
        show_state = {"visible": False}

        try:
            eye_open = CTkImage(Image.open(icons['eye']), size=(20, 20))
            eye_closed = CTkImage(Image.open(icons['crossed_eye']), size=(20, 20))
        except Exception as e:
            print("Gagal load icon mata:", e)
            eye_open = eye_closed = None

        def toggle_show():
            if show_state["visible"]:
                entry.configure(show="*")
                if eye_button and eye_closed:
                    eye_button.configure(image=eye_closed)
            else:
                entry.configure(show="")
                if eye_button and eye_open:
                    eye_button.configure(image=eye_open)
            show_state["visible"] = not show_state["visible"]

        eye_button = ctk.CTkButton(
            frame,
            text="",
            width=30,
            height=30,
            fg_color="transparent",
            hover=False,
            image=eye_closed,
            command=toggle_show
        )
        eye_button.pack(side="left", padx=(5, 0))
    else:
        width -= 10
    frame.entry = entry
    return frame




def ImageViewPilLow(parent, image_path, width=100, height=100, top=5, bottom=5, left=5, right=5):
    pil_image = Image.open(image_path)
    pil_image = pil_image.resize((width, height))
    img = ImageTk.PhotoImage(pil_image)
    label = tk.Label(parent, image=img)
    label.image = img
    label._padding = {'padx': (left, right), 'pady': (top, bottom)}
    return label
def appDesktop(
    title="App",
    backgroundColor="transparent",
    backgroundImage=None,
    icon=None,
    width=400,
    height=600,
    body=[],
    on_ready=None,
    align='start'
):
    import time
    input_ = {}

    try:
        root = tk.Tk()
        root.title(title)
        root.geometry(f"{width}x{height}")

        # ICON SETUP
        try:
            if icon:
                root.iconbitmap(icon)
            else:
                if icons.get('app'):
                    icon_path = icons['app']
                    if icon_path.lower().endswith(".ico"):
                        root.iconbitmap(icon_path)
                    else:
                        from PIL import Image
                        pil_img = Image.open(icon_path)
                        ico_path = os.path.join(os.path.dirname(__file__), "app_auto.ico")
                        pil_img.save(ico_path, format="ICO")
                        root.iconbitmap(ico_path)
        except Exception as e:
            now = time.strftime('%H:%M:%S')
            print(f"[{now}] File icon harus .ico")
            print(f"[{now}] Pesan Error :", e)

        # FRAME UTAMA
        frame = tk.Frame(root)
        frame.pack(fill='both', expand=True)

        bg_label = None
        bg_img_obj = None

        if backgroundImage:
            from PIL import Image, ImageTk
            pil_bg = Image.open(backgroundImage).resize((width, height))
            bg_img_obj = ImageTk.PhotoImage(pil_bg)
            bg_label = tk.Label(frame, image=bg_img_obj)
            bg_label.image = bg_img_obj
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        elif backgroundColor:
            frame.config(bg=backgroundColor if backgroundColor != "transparent" else root.cget('bg'))

        # BIND RESIZE UNTUK RESPONSIVE BACKGROUND IMAGE
        if backgroundImage:
            def resize_bg(event):
                new_w, new_h = event.width, event.height
                pil_bg = Image.open(backgroundImage).resize((new_w, new_h))
                new_bg = ImageTk.PhotoImage(pil_bg)
                bg_label.config(image=new_bg)
                bg_label.image = new_bg

            frame.bind("<Configure>", resize_bg)

        # ALIGNMENT
        try:
            container = tk.Frame(frame)
            container.place(relx=0, rely=0, anchor='nw')  # default start
            if align == 'center':
                container.place(relx=0.5, rely=0.5, anchor='center')
            elif align in ('center|start', 'start|center', 'top|center', 'center|top'):
                container.pack(fill='x', side='top')
            elif align in ('center|end', 'end|center', 'bottom|center', 'center|bottom'):
                container.pack(fill='x', side='bottom')
            elif align in ('left|center', 'center|left'):
                container.place(relx=0, rely=0.5, anchor='w')
            elif align in ('right|center', 'center|right'):
                container.place(relx=1, rely=0.5, anchor='e')
            elif align == 'end':
                container.pack(fill='both', expand=True)
                bottom_right = tk.Frame(container)
                bottom_right.pack(side='bottom', anchor='e', padx=10, pady=10)
                container = bottom_right

            for builder in body:
                widget = builder(container)
                if isinstance(widget, tk.Widget):
                    widget.pack(pady=5)
        except Exception as e:
            now = time.strftime('%H:%M:%S')
            print(f"[{now}] Pesan Error :", e)

        # CALLBACK ON_READY
        try:
            if callable(on_ready):
                on_ready(input_)
        except Exception as e:
            now = time.strftime('%H:%M:%S')
            print(f"[{now}] Pesan Error :", e)

        root.mainloop()

    except Exception as e:
        now = time.strftime('%H:%M:%S')
        print(f"[{now}] Pesan Error :", e)

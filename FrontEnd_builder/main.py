import tkinter as tk

from DataProduct import products
from module.func import add_to_cart, clear_cart
from module import save_file
from module import Print_Receipt

product_data = save_file.load_products()

BG = "#F5F1EB"
DARK = "#3E2723"
BROWN = "#6F4E37"
LIGHT_BROWN = "#A67B5B"
WHITE = "#FFFFFF"
GREEN = "#4CAF50"
RED = "#D9534F"
GRAY = "#777777"
light = "#F5F5F5"


window = tk.Tk()

window.title("Coffee Shop POS")
window.geometry("1200x700")
window.configure(bg=BG)



# CART


cart = []



# HEADER


header = tk.Frame(
    window,
    bg=BROWN,
    height=70
)

header.pack(fill="x")
header.pack_propagate(False)

title = tk.Label(
    header,
    text="Coffee Shop",
    font=("Arial", 12, "bold"),
    bg=BROWN,
    fg=WHITE,
)

title.pack(
    side="left",
    padx=25
)


cashier = tk.Label(
    header,
    text="Cashier",
    font=("Arial", 12, "bold"),
    bg=BROWN,
    fg=WHITE,
)

cashier.pack(
    side="right",
    padx=25
)



# MAIN FRAME


main_frame = tk.Frame(
    window,
    bg=light
)

main_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)


# PRODUCT AREA


products_Frame = tk.Frame(
    main_frame,
    bg=WHITE
)

products_Frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 10)
)


products_title = tk.Label(
    products_Frame,
    text="Products",
    font=("Arial", 20, "bold"),
    bg=WHITE
)

products_title.pack(
    anchor="w",
    padx=20,
    pady=20
)
products_canvas = tk.Canvas(
    products_Frame,
    bg = WHITE,
    highlightthickness=0
)
product_scrollbar = tk.Scrollbar(
    products_Frame,
    orient="vertical",
    command=products_canvas.yview,
)
product_grid = tk.Frame(
    products_canvas,
    bg=WHITE
)

product_grid.bind(
    "<Configure>",
    lambda event: products_canvas.configure(
        scrollregion=products_canvas.bbox("all")
    )
)
products_canvas.create_window(
    (0,0),
    window=product_grid,
    anchor="nw",

)
products_canvas.configure(
    yscrollcommand=product_scrollbar.set
)
products_canvas.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(20,0),
    pady = 10

)
product_scrollbar.pack(
    side="right",
    fill="y",
    pady=10
)

# ORDER AREA


order_frame = tk.Frame(
    main_frame,
    bg=WHITE,
    width=350
)

order_frame.pack(
    side="right",
    fill="y"
)

order_frame.pack_propagate(False)


order_title = tk.Label(
    order_frame,
    text="Current Orders",
    font=("Arial", 20, "bold"),
    bg=WHITE
)

order_title.pack(
    anchor="w",
    padx=20,
    pady=20
)


order_list = tk.Listbox(
    order_frame,
    font=("Arial", 12),
    height=15
)

order_list.pack(
    fill="both",
    padx=20,
    pady=10
)



# TOTALS


subtotal_label = tk.Label(
    order_frame,
    text="Subtotal: $0.00",
    font=("Arial", 13),
    bg=WHITE
)

subtotal_label.pack(
    anchor="w",
    padx=20,
    pady=5
)


tax_label = tk.Label(
    order_frame,
    text="Tax: $0.00",
    font=("Arial", 13),
    bg=WHITE
)

tax_label.pack(
    anchor="w",
    padx=20,
    pady=5
)


total_label = tk.Label(
    order_frame,
    text="Total: $0.00",
    font=("Arial", 13),
    bg=WHITE
)

total_label.pack(
    anchor="w",
    padx=20,
    pady=5
)



# BUTTONS
button_frame = tk.Frame(
    order_frame,
    bg=WHITE
)

button_frame.pack(
    fill="x",
    padx=20,
    pady=20
)


clear_button = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 12, "bold"),
    bg=RED,
    fg=WHITE,
    height=2,
    command=lambda: clear_cart(
        cart,
        order_list,
        subtotal_label,
        tax_label,
        total_label
    )
)

clear_button.pack(
    side="left",
    fill="x",
    expand=True,
    padx=(0, 5)
)


pay_button = tk.Button(
    button_frame,
    text="Pay",
    font=("Arial", 12, "bold"),
    bg=GREEN,
    fg=WHITE,
    height=2,
    command =lambda :Print_Receipt.print_receipt(
        cart ,
        subtotal_label,
        tax_label,
        total_label
    )

)

pay_button.pack(
    side="right",
    fill="x",
    expand=True,
    padx=(5, 0)
)
# loop product
for index, product in enumerate(product_data):

    row = index // 3
    column = index % 3

    name = product["name"]
    price = product["price"]

    button = tk.Button(
        product_grid,
        text=f"{name}\n${price:.2f}",
        font=("Arial", 13, "bold"),
        width=15,
        height=5,
        bg="#EFE2D0",
        activebackground="#D7B899",
        relief="flat",

        command=lambda n=name, p=price: add_to_cart(
            n,
            p,
            cart,
            order_list,
            subtotal_label,
            tax_label,
            total_label
        )
    )

    button.grid(
        row=row,
        column=column,
        padx=10,
        pady=10
    )



# RUN APPLICATION


window.mainloop()

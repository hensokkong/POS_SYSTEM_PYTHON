import tkinter as tk

from tkinter import messagebox

from module import save_file




product_data = save_file.load_products()

#run function
def add_product():
    name = product_name_entry.get().strip()
    price = product_price_entry.get().strip()
    category = product_category_entry.get().strip()

    if name == "":
        messagebox.showwarning("Warning", "Product Name is required")
        return
    #check price
    try:
        price = float(price)
    except ValueError:
        messagebox.showwarning("Warning", "Please enter valid price")
        return
    if price <= 0:
        messagebox.showwarning("Warning", "Price is must be more than 0")
        return
    if category == "":
        messagebox.showwarning("Warning", "Product Category is required")
        return
    new_product ={
        "id": len(product_data) + 1,
        "name": name,
        "price": price,
        "category": category,
        "quantity": 1,
    }
    #add new product to product_data
    product_data.append(new_product)
    save_file.save_products(product_data)
    #show success mesage
    messagebox.showinfo("Success", f"{name} added successfully")

    #clear textbox
    product_name_entry.delete(0, "end")
    product_price_entry.delete(0, "end")
    product_category_entry.delete(0, "end")
    print(product_data)


#Create Window
window = tk.Tk()
window.title("Admin")
window.geometry("500x550")
#Main Frame
main_frame = tk.Frame(
    window,
    bg="white",
    highlightbackground="#2196F3",
    highlightthickness=2,
)
main_frame.pack(
    fill="both",
    expand=True,
    padx=4,
    pady=4
)
#Title
title = tk.Label(
    main_frame,
    text="Add Product",
    font=("Arial", 18),
    bg="white",
    fg="black",
)
title.pack(pady =(15,30))

#product nam4
name_label = tk.Label(
    main_frame,
    text="Product's Name",
    font=("Arial", 13),
    bg="white",
    anchor="w",
)
name_label.pack()
#Input Field
product_name_entry = tk.Entry(
    main_frame,
    width=30,
    font=("Arial", 14),
    bg="#d3d3d3",
    relief="flat"
)
product_name_entry.pack(
    ipady=7,
    pady=(5,15)
)
#Product Price
cost_label = tk.Label(
    main_frame,
    text="Product's Cost",
    font=("Arial", 13),
    bg="white",
    anchor="w",
)
cost_label.pack()

product_price_entry = tk.Entry(
    main_frame,
    width=30,
    font=("Arial", 14),
    bg="#d3d3d3",
    relief="flat"
)
product_price_entry.pack(
    ipady=7,
    pady=(5,15)
)
#add category
category_label = tk.Label(
    main_frame,
    text="Product's Category",
    font=("Arial", 13),
    bg="white",
    anchor="w",
)
category_label.pack()
product_category_entry = tk.Entry(
    main_frame,
    width=30,
    font=("Arial", 14),
    bg="#d3d3d3",
    relief="flat"
)
product_category_entry.pack(
    ipady=7,
    pady=(5,15)
)
#Add button
add_button = tk.Button(
    main_frame,
    text="Add",
    font=("Arial", 13 , "bold"),
    bg = "#72BCE5",
    activebackground="#5AAEDB",
    relief="flat",
    width=12,
    cursor="hand2",
    command=add_product
)
add_button.pack(pady=10)
# key control
window.bind("<Return>", lambda event: add_product())
window.bind("<Escape>", lambda event: window.destroy())

##footer
foot_label = tk.Label(
    main_frame,
    text="Heng Heng Admin",
    font=("Arial", 10),
    bg="white",
    fg="#333333"
)
foot_label.pack(
    side = "bottom",
    pady=12
)
window.mainloop()
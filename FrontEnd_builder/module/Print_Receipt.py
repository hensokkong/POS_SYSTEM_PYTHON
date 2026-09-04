import os
import tkinter as tk
from datetime import datetime

def show_receipt_window(receipt):
    receipt_window = tk.Toplevel()
    receipt_window.title("Receipt")
    receipt_window.geometry("450x600")
    receipt_window.configure(bg="white")


    title = tk.Label(
        receipt_window,
        text="Receipt",
        font=("Arial", 20, "bold"),
        bg="white"
    )
    title.pack(pady=15)


    receipt_text = tk.Text(
        receipt_window,
        width=45,
        height=25,
        font=("Courier New", 11),
        bg="#F5F5F5",
        relief="flat"
    )

    receipt_text.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=10
    )

    # Put receipt inside Text widget
    receipt_text.insert("1.0", receipt)

    # Don't allow editing
    receipt_text.config(state="disabled")

    # Close button
    close_button = tk.Button(
        receipt_window,
        text="Close",
        font=("Arial", 11, "bold"),
        bg="#D9534F",
        fg="white",
        width=10,
        command=receipt_window.destroy
    )

    close_button.pack(pady=15)


def print_receipt(
    cart,
    subtotal_label,
    tax_label,
    total_label
):
    if not cart:
        return

    subtotal = sum(item["price"] * item["quantity"] for item in cart)
    tax = subtotal * 0.10
    total = subtotal + tax

    receipt = ""

    receipt += "********************************\n"
    receipt += "          COFFEE SHOP\n"
    receipt += "********************************\n"
    receipt += f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    receipt += "--------------------------------\n"

    for item in cart:
        name = item["name"]
        quantity = item["quantity"]
        price = item["price"]

        item_total = price * quantity

        receipt += (
            f"{name:<15} "
            f"x{quantity:<3} "
            f"${item_total:>7.2f}\n"
        )

    receipt += "--------------------------------\n"
    receipt += f"Subtotal:              ${subtotal:.2f}\n"
    receipt += f"Tax (10%):             ${tax:.2f}\n"
    receipt += f"TOTAL:                 ${total:.2f}\n"
    receipt += "================================\n"
    receipt += "       Thank You!\n"
    receipt += "================================\n"

    # Save receipt
    os.makedirs("Hold_Receipt", exist_ok=True)

    filename = f"receipt_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    file_path = os.path.join("Hold_Receipt", filename)

    with open(file_path, "w") as file:
        file.write(receipt)
    print(receipt)
    show_receipt_window(receipt)
    return file_path



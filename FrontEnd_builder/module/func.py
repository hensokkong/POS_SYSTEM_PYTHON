def update_cart(cart, order_list, subtotal_label, tax_label, total_label):
    order_list.delete(0, "end")

    subtotal = 0

    for item in cart:
        item_total = item["quantity"] * item["price"]

        order_list.insert(
            "end",
            f"{item['name']}       x{item['quantity']}      ${item_total:.2f}"
        )

        subtotal += item_total

    tax = subtotal * 0.10
    total = subtotal + tax

    subtotal_label.config(
        text=f"Subtotal: ${subtotal:.2f}"
    )

    tax_label.config(
        text=f"Tax: ${tax:.2f}"
    )

    total_label.config(
        text=f"Total: $   {total:.2f}"
    )


def add_to_cart(
    name,
    price,
    cart,
    order_list,
    subtotal_label,
    tax_label,
    total_label
):
    for item in cart:
        if name == item["name"]:
            item["quantity"] += 1

            update_cart(
                cart,
                order_list,
                subtotal_label,
                tax_label,
                total_label
            )

            return

    cart.append({
        "name": name,
        "price": price,
        "quantity": 1
    })

    update_cart(
        cart,
        order_list,
        subtotal_label,
        tax_label,
        total_label
    )


def clear_cart(cart, order_list, subtotal_label, tax_label, total_label):
    cart.clear()

    update_cart(
        cart,
        order_list,
        subtotal_label,
        tax_label,
        total_label
    )

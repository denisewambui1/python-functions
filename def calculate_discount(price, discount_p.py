def calculate_discount(price, discount_percent):
  """
  Calculates the final price after applying a discount.

  Args:
      price (float): Original price of the item.
      discount_percent (float): Discount percentage (between 0 and 100).

  Returns:
      float: Final price after applying the discount.
  """
  if discount_percent >= 20:
    # Apply the discount
    discounted_price = price * (1 - discount_percent / 100)
    return discounted_price
  else:
    # No discount applied
    return price


# Example usage:
original_price = 1700.0
discount_percent = 25.0

# Calculate the final price using the function
final_price = calculate_discount(original_price, discount_percent)

# Print the result
print(f"Final price after applying the discount: ${final_price:.2f}")
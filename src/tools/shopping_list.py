"""Shopping list builder tool for MealMate agent."""
from strands.tools import tool


@tool
def build_shopping_list(
    meal_plan: str = "",
    available_ingredients: str = "",
) -> str:
    """Build a shopping list based on a meal plan, excluding ingredients already available.
    
    Args:
        meal_plan: The meal plan to generate a shopping list for
        available_ingredients: Ingredients already at home (to exclude from list)
    
    Returns:
        A categorised shopping list grouped by aisle.
    """
    context = f"""Based on this meal plan, create a shopping list:

Meal plan: {meal_plan if meal_plan else 'No meal plan provided yet — ask the user first'}
Already available: {available_ingredients if available_ingredients else 'Not specified'}

Rules:
- Exclude anything listed as available
- Group items by supermarket section (Produce, Dairy, Meat, Pantry, Frozen)
- Combine quantities where the same ingredient appears in multiple meals
- Flag items that might already be in a typical kitchen (salt, oil, basic spices)

Format:
🥬 Produce:
  - [item] — [quantity]

🥛 Dairy:
  - [item] — [quantity]
"""
    return context
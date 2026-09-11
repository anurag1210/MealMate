"""Meal planning tool for MealMate agent."""
from strands.tools import tool


@tool
def plan_meals(
    num_days: int = 7,
    cuisine_preferences: str = "",
    dietary_restrictions: str = "",
    available_ingredients: str = "",
    family_size: int = 4,
) -> str:
    """Plan meals for the specified number of days based on family preferences.
    
    Args:
        num_days: Number of days to plan meals for (default 7)
        cuisine_preferences: Preferred cuisines (e.g. "Indian, Chinese")
        dietary_restrictions: Any dietary restrictions (e.g. "no red meat, nut allergy")
        available_ingredients: Ingredients currently available at home
        family_size: Number of family members to cook for
    
    Returns:
        A structured meal plan with breakfast, lunch, and dinner for each day.
    """
    context = f"""Generate a {num_days}-day meal plan for a family of {family_size}.

Preferences: {cuisine_preferences if cuisine_preferences else 'No specific preference'}
Dietary restrictions: {dietary_restrictions if dietary_restrictions else 'None'}
Available ingredients to use first: {available_ingredients if available_ingredients else 'Not specified'}

Rules:
- No meal should repeat within the week
- Weeknight dinners should take 30 minutes or less
- Include at least 2 cuisines across the week for variety
- Use available ingredients first to reduce waste
- Each meal should list key ingredients needed

Format each day as:
Day X:
  Breakfast: [meal] — [key ingredients]
  Lunch: [meal] — [key ingredients]  
  Dinner: [meal] — [key ingredients]
"""
    return context
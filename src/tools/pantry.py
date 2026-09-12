"""Pantry tracker tool for MealMate — maintains ingredient inventory."""
import json
import os
from strands.tools import tool

PANTRY_FILE = "./data/pantry/inventory.json"


def _load_pantry() -> dict:
    """Load pantry inventory from file."""
    if os.path.exists(PANTRY_FILE):
        with open(PANTRY_FILE, "r") as f:
            return json.load(f)
    return {"ingredients": []}


def _save_pantry(pantry: dict):
    """Save pantry inventory to file."""
    os.makedirs(os.path.dirname(PANTRY_FILE), exist_ok=True)
    with open(PANTRY_FILE, "w") as f:
        json.dump(pantry, f, indent=2)


@tool
def update_pantry(ingredients: str, action: str = "add") -> str:
    """Update the pantry inventory with ingredients.

    Args:
        ingredients: Comma-separated list of ingredients to add or remove
        action: Either "add" to add ingredients or "remove" to remove used ones

    Returns:
        Updated pantry status.
    """
    pantry = _load_pantry()
    items = [i.strip() for i in ingredients.split(",")]

    if action == "add":
        for item in items:
            if item not in pantry["ingredients"]:
                pantry["ingredients"].append(item)
        _save_pantry(pantry)
        return f"Added to pantry: {', '.join(items)}. Current pantry: {', '.join(pantry['ingredients'])}"

    elif action == "remove":
        removed = []
        for item in items:
            if item in pantry["ingredients"]:
                pantry["ingredients"].remove(item)
                removed.append(item)
        _save_pantry(pantry)
        return f"Removed from pantry: {', '.join(removed)}. Current pantry: {', '.join(pantry['ingredients'])}"

    return "Invalid action. Use 'add' or 'remove'."


@tool
def check_pantry() -> str:
    """Check what ingredients are currently in the pantry.

    Returns:
        List of all ingredients currently tracked in the pantry.
    """
    pantry = _load_pantry()
    if not pantry["ingredients"]:
        return "Pantry is empty. Upload a fridge photo or tell me what you have!"
    return f"Current pantry: {', '.join(pantry['ingredients'])}"
"""Long-term memory for MealMate — remembers family preferences across sessions."""
from strands.memory import MemoryManager
from strands.vended_memory_stores.test_memory_store import TestMemoryStore


def create_memory_manager() -> MemoryManager:
    """Create a memory manager with local file-based storage.
    
    Stores family preferences, dietary restrictions, likes/dislikes 
    as persistent memories that survive across sessions.
    """
    store = TestMemoryStore(
        name="family-preferences",
        path="./data/memory/family-preferences.json",
    )

    memory_manager = MemoryManager(
        stores=[store],
        search_tool_config=True,     # agent can search memories
        add_tool_config=True,        # agent can save new memories
        injection=True,              # auto-inject relevant memories before each response
    )

    return memory_manager
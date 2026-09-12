"""Session management for MealMate — persists conversation history across sessions."""
from strands.session.file_session_manager import FileSessionManager
import os


def create_session_manager(session_id: str = "default-family") -> FileSessionManager:
    """Create a file-based session manager for conversation persistence.
    
    Args:
        session_id: Unique identifier for this family's session
    
    Returns:
        FileSessionManager configured with local storage
    """
    storage_dir = os.path.join(os.path.dirname(__file__), "../../data/sessions")
    os.makedirs(storage_dir, exist_ok=True)
    
    session_manager = FileSessionManager(
        session_id=session_id,
        storage_dir=storage_dir,
    )
    
    return session_manager
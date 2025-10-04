_project_path = None

def set_project_path(path: str):
    """Set the path to the project this package should operate on."""
    global _project_path
    _project_path = path

def get_project_path():
    """Get the currently set project path."""
    if _project_path is None:
        raise ValueError("Project path not set. Call set_project_path(path) first.")
    return _project_path


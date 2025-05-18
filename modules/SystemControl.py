import os
def control_pc(command):
    """Perform system operations like shutdown, restart, open apps, and custom folders."""
    
    # Dictionary to store custom folder paths
    folders = {
        "downloads": "C:/Users/Public/Downloads",
        "documents": "C:/Users/Public/Documents",
        "pictures": "C:/Users/Public/Pictures",
        "my projects": "C:/Users/YourUsername/MyProjects",  # Replace with your actual folder path
        "workspace": "C:/Users/YourUsername/Workspace"  # Replace with your actual folder path
    }
    
    # System commands
    if "shutdown" in command:
        os.system("shutdown /s /t 5")
        return "Shutting down..."
    elif "restart" in command:
        os.system("shutdown /r /t 5")
        return "Restarting..."
    elif "kholo notepad" in command:
        os.system("notepad")
        return "kholdiya Notepad..."
    elif "kholo calculator" in command:
        os.system("calc")
        return "kholdiya Calculator..."
    elif "kholo command prompt" in command or "open cmd" in command:
        os.system("start cmd")
        return "kholdiya Command Prompt..."
    elif "kholo task manager" in command:
        os.system("taskmgr")
        return "kholdiya Task Manager..."
    elif "kholo file explorer" in command:
        os.system("explorer")
        return "kholdiya File Explorer..."

    # Open a custom folder
    for key, path in folders.items():
        if key in command:
            os.startfile(path)
            return f"kholdiya {key} folder..."

    return "Command not recognized."

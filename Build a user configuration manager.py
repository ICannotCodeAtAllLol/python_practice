test_settings = {
    "theme": "light",
    "theme": "dark"
}

def add_setting(settings: dict, setting_pair: tuple):
    key, value = setting_pair
    key = key.lower()
    value = value.lower()
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings: dict, setting_pair: tuple):
    key, value = setting_pair
    key = key.lower()
    value = value.lower()
    if key in settings:
        settings[key] = value 
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
def delete_setting(settings: dict, key:str):
    key = key.lower()
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"
def view_settings(settings: dict):
    if not settings:
        return "No settings available."
    output = "Current User Settings:\n"
    for key, value in settings.items():
        output += f"{key.capitalize()}: {value}\n"
    return output
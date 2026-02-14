test_settings = {
    'Theme': 'Light',
    'Volume': 'High',
    'Brightness': 'Dark',
    'Color': 'Dark'
}

def add_setting(settings, kv_pair):
    key, value = kv_pair
    key = key.lower()
    value = value.lower()

    if any(k.lower() == key for k in settings):
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, kv_pair):
    key, value = kv_pair
    key = key.lower()
    value = value.lower()

    for existing_key in settings:
        if existing_key.lower() == key:
            settings[existing_key] = value
            return f"Setting '{key}' updated to '{value}' successfully!"
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = key.lower()
    
    for existing_key in list(settings.keys()):
        if existing_key.lower() == key:
            del settings[existing_key]
            return f"Setting '{key}' deleted successfully!"
    return f"Setting not found!"

def view_settings(settings):
    if not settings:
        return "No settings available."
    result = "Current User Settings:"
    for k, v in settings.items():
        result += f"\n{k.capitalize()}: {v}"
    result += "\n"
    return result
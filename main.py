def add_setting(settings, new_setting):
    raw_key, raw_value = new_setting
    key = raw_key.lower()
    value = raw_value.lower()

    if settings.get(key, None):
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, updated_setting):
    raw_key, raw_value = updated_setting
    key = raw_key.lower()
    value = raw_value.lower()

    if settings.get(key, None):
        settings.update({ key: value })
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, raw_key):
    key = raw_key.lower()

    if settings.get(key, None):
        settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(settings):
    if not settings:
        return 'No settings available.'
    else:
        answer = "Current User Settings:\n"
        for key, value in settings.items():
            answer += f"{key.title()}: {value}\n"
        return answer

test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
}

print(view_settings(test_settings))

from pathlib import Path


def get_resource_path():
    return Path(__file__).parent.parent / "resources"


def get_images_path():
    return get_resource_path() / "images"


def get_turf_images_path():
    return get_images_path() / "turf"


def get_characters_path():
    return get_images_path() / "characters"


def get_user_character_path():
    return get_characters_path() / "UserCharacter"


def get_hud_screen_path():
    return get_images_path() / "HUD"


def get_object_path():
    return get_images_path() / "objects"


def get_gem_object_path():
    return get_object_path() / "gems"


def get_npcs_path():
    return get_characters_path() / "npcs"


def get_shopkeeper_path():
    return get_npcs_path() / "shopkeeper"


special_character_lookup = {
    " ": "space",
    ".": "period",
    "?": "questionmark",
    ":": "colon",
    ",": "comma",
    "'": "apostrophe",
    '"': "quotationmark",
    ";": "semicolon"
}


def get_character(character):
    if character in special_character_lookup.keys():
        return special_character_lookup[character]
    elif character.isupper():
        return character + character
    else:
        return character


text_screen_size_images = {
    "small": "text_screen_small.png",
    "medium": "text_screen_medium.png",
    "large": "text_screen_large.png"
}

text_screen_sizes = {
    "small": (240, 75),
    "medium": (150, 350),
    "large": (475, 220)
}

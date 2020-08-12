
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

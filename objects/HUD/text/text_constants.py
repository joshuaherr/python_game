
special_character_lookup = {
    " ": "space",
    ".": "period",
    "?": "questionmark",
    ":": "colon"
}


def get_character(character):
    if character in special_character_lookup.keys():
        return special_character_lookup[character]
    return character

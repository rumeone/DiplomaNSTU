from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    note last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Example:
        >>> parse_music('o o| .|  o| o| .| .|   .| .| o  o ')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    beats = []
    i = 0
    length = len(music_string)

    while i < length:
        # Skip spaces
        if music_string[i] == ' ':
            i += 1
            continue

        # Check for whole note 'o'
        if music_string[i] == 'o':
            # Check if next character is '|' for half note
            if i + 1 < length and music_string[i + 1] == '|':
                beats.append(2)
                i += 2  # Skip 'o|'
            else:
                beats.append(4)
                i += 1  # Skip 'o'
        # Check for quarter note '.|'
        elif music_string[i] == '.':
            if i + 1 < length and music_string[i + 1] == '|':
                beats.append(1)
                i += 2  # Skip '.|'
            else:
                # Invalid pattern, skip the dot
                i += 1
        else:
            # Invalid character, skip it
            i += 1

    return beats
"""Module for parsing ASCII music notation into beat durations."""

from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in ASCII format and return
    a list of integers corresponding to how many beats each note lasts.

    Legend:
    'o'  - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    Example:
        >>> parse_music('o o| .|  o| o| .| .|   .| .| o  o ')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    if not music_string or not music_string.strip():
        return []

    beats: List[int] = []
    i = 0
    length = len(music_string)

    while i < length:
        char = music_string[i]

        if char.isspace():
            i += 1
            continue

        if char == "o":
            # Check if this is a half note 'o|'
            if i + 1 < length and music_string[i + 1] == "|":
                beats.append(2)
                i += 2
            else:
                beats.append(4)
                i += 1
        elif char == ".":
            # Check for quarter note '.|'
            if i + 1 < length and music_string[i + 1] == "|":
                beats.append(1)
                i += 2
            else:
                # Invalid input, but per spec we treat lone '.' as invalid.
                # For robustness we skip it.
                i += 1
        else:
            # Unknown character, skip
            i += 1

    return beats
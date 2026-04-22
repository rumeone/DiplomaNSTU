from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    note last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Example:
        >>> parse_music('o o| .|  o| o| .| .|   .| .| o  o ')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    notes = []
    i = 0
    s = music_string.strip()
    while i < len(s):
        if s[i] == ' ':
            i += 1
            continue
        if s[i] == 'o':
            if i + 1 < len(s) and s[i + 1] == '|':
                notes.append(2)
                i += 2
            else:
                notes.append(4)
                i += 1
        elif s[i] == '.':
            if i + 1 < len(s) and s[i + 1] == '|':
                notes.append(1)
                i += 2
            else:
                # Invalid but according to spec we assume correct input
                i += 1
        else:
            i += 1
    return notes
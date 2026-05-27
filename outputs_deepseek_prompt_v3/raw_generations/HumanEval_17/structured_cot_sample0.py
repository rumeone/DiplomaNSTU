from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in ASCII format and return
    a list of integers corresponding to the duration of each note in beats.

    Legend:
    'o'   - whole note (4 beats)
    'o|'  - half note (2 beats)
    '.|'  - quarter note (1 beat)

    Example:
        >>> parse_music('o o| .|  o| o| .| .|   .| .| o  o ')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    return [note_map[note] for note in music_string.split() if note]
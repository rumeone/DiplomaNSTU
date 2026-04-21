from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in ASCII format and return
    a list of integers corresponding to the number of beats each note lasts.

    Legend:
    'o'   - whole note, lasts four beats
    'o|'  - half note, lasts two beats
    '.|'  - quarter note, lasts one beat

    Example:
        >>> parse_music('o o| .|  o| o| .| .|   .| .| o  o ')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    beat_map = {'o': 4, 'o|': 2, '.|': 1}
    notes = music_string.split()
    return [beat_map[note] for note in notes if note in beat_map]
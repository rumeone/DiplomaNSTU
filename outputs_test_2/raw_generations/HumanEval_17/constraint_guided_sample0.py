"""Parse musical notes in ASCII format to their beat durations."""

from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of beat durations.

    The input string contains musical notes separated by whitespace:
    'o'   - whole note (4 beats)
    'o|'  - half note (2 beats)
    '.|'  - quarter note (1 beat)

    Args:
        music_string: A string containing musical notes.

    Returns:
        A list of integers representing the beat duration of each note.

    Example:
        >>> parse_music('o o| .|  o| o| .| .|   .| .| o  o ')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    beat_map = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    notes = music_string.split()
    beats = [beat_map[note] for note in notes if note in beat_map]
    return beats
from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return list of beat durations.

    Args:
        music_string: String containing musical notes separated by spaces.
            'o' - whole note (4 beats)
            'o|' - half note (2 beats)
            '.|' - quarter note (1 beat)

    Returns:
        List of integers representing beat durations for each note.

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
    return [beat_map[note] for note in notes if note in beat_map]
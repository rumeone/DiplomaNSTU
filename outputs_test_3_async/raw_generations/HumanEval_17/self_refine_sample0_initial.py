"""
Parse musical notes in ASCII format to their corresponding beat durations.
"""

from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes and return a list of beat durations.

    The input string contains musical notes separated by whitespace:
    - 'o' represents a whole note (4 beats)
    - 'o|' represents a half note (2 beats)
    - '.|' represents a quarter note (1 beat)

    Args:
        music_string: A string containing musical notes in ASCII format.

    Returns:
        A list of integers representing the beat duration of each note.

    Example:
        >>> parse_music('o o| .|  o| o| .| .|   .| .| o  o ')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    if not music_string:
        return []

    # Split the string by whitespace to get individual notes
    notes = music_string.split()

    # Map each note to its corresponding beat duration
    beat_map = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Convert each note to its beat duration using the mapping
    return [beat_map[note] for note in notes]
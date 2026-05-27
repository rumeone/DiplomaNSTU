from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse a string of musical notes in ASCII format and return a list of
    integers representing the number of beats each note lasts.

    Legend:
    'o' - whole note (4 beats)
    'o|' - half note (2 beats)
    '.|' - quarter note (1 beat)

    Args:
        music_string: A string containing musical notes separated by spaces.

    Returns:
        A list of integers representing the beats for each note.
    """
    note_to_beats = {'o': 4, 'o|': 2, '.|': 1}
    notes = music_string.split()
    beats = []
    for note in notes:
        if note in note_to_beats:
            beats.append(note_to_beats[note])
    return beats
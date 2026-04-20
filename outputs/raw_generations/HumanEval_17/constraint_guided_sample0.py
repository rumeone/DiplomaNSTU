from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Parse musical notes string and return list of beat durations.
    'o' - whole note (4 beats)
    'o|' - half note (2 beats)
    '.|' - quarter note (1 beat)
    """
    notes = music_string.split()
    beats = []
    
    for note in notes:
        if note == 'o':
            beats.append(4)
        elif note == 'o|':
            beats.append(2)
        elif note == '.|':
            beats.append(1)
    
    return beats
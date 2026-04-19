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
    beats = []
    i = 0
    n = len(music_string)
    
    while i < n:
        # Skip spaces
        if music_string[i] == ' ':
            i += 1
            continue
        
        # Check for quarter note
        if music_string[i] == '.':
            beats.append(1)
            i += 2  # Skip '.|'
            continue
        
        # Handle 'o' or 'o|'
        if music_string[i] == 'o':
            if i + 1 < n and music_string[i + 1] == '|':
                beats.append(2)
                i += 2
            else:
                beats.append(4)
                i += 1
    
    return beats
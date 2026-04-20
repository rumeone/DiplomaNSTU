from typing import List

def parse_music(music_string: str) -> List[int]:
    beats = []
    i = 0
    n = len(music_string)
    
    while i < n:
        if music_string[i] == ' ':
            i += 1
            continue
        
        if music_string[i] == 'o':
            if i + 1 < n and music_string[i + 1] == '|':
                beats.append(2)
                i += 2
            else:
                beats.append(4)
                i += 1
        elif music_string[i] == '.':
            if i + 1 < n and music_string[i + 1] == '|':
                beats.append(1)
                i += 2
            else:
                i += 1
        else:
            i += 1
    
    return beats
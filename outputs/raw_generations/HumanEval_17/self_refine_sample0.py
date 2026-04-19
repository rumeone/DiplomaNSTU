from typing import List


def parse_music(music_string: str) -> List[int]:
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
            # Ensure there's enough space for '.|'
            if i + 1 < n and music_string[i + 1] == '|':
                beats.append(1)
                i += 2
            else:
                # Invalid pattern, skip or handle as needed
                i += 1
            continue

        # Handle 'o' or 'o|'
        if music_string[i] == 'o':
            if i + 1 < n and music_string[i + 1] == '|':
                beats.append(2)
                i += 2
            else:
                beats.append(4)
                i += 1
            continue

        # If we encounter an unexpected character, skip it
        i += 1

    return beats
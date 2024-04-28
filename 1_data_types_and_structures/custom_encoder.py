reference_string = 'abcdefghijklmnopqrstuvwxyz'

def custom_encoder(data: str):
    positions = []
    for ch in data.lower():
        if ch in reference_string:
            positions.append(reference_string.index(ch))
        else:
            positions.append(-1)
    return positions


print(custom_encoder('Test!'))  # [19, 4, 18, 19, -1]
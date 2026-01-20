def custom_encoder(text):
    reference_string = 'abcdefghijklmnopqrstuvwxyz'
    positions = []
    for char in text:
        char = char.lower()
        if char in reference_string:
            positions.append(reference_string.index(char))
        else:
            positions.append(-1)
    return positions



class TrebCalibrator():

    def get_digit_from_line(line: str):

        characters = list(line)
        for character in characters:
            if character.isdigit():
                return character

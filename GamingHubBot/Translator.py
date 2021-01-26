# This class represents a Translator. It's job is to detect the language used for the user input (out of two
# possibilities, L33TSpeak and English), and translate it into the other language appropriately.

class Translator:
    def __init__(self):
        self.eng_to_l33t = {}
        self.populate_dictionary()

    # This function detects if the input string is l33tspeak or english, and translates accordingly.
    def translator_insight(self, input_string):
        if all(x.isalpha() or x.isspace() for x in input_string):
            return self.english_to_l33tspeak(input_string)
        else:
            return self.l33tspeak_to_english(input_string)

    # This function adds all necessary translation rules to the L33TSpeak dictionary.
    def populate_dictionary(self):
        self.eng_to_l33t['A'] = '4'
        self.eng_to_l33t['B'] = '6'
        self.eng_to_l33t['E'] = '3'
        self.eng_to_l33t['I'] = '|'
        self.eng_to_l33t['L'] = '1'
        self.eng_to_l33t['M'] = '(V)'
        self.eng_to_l33t['N'] = '(\\)'
        self.eng_to_l33t['O'] = '0'
        self.eng_to_l33t['S'] = '5'
        self.eng_to_l33t['T'] = '7'
        self.eng_to_l33t['V'] = '\\ /'
        self.eng_to_l33t['W'] = '` //'

    # This function translates an english sentence into l33tspeak.
    def english_to_l33tspeak(self, user_input):
        result = ''

        for letter in user_input:
            is_match = False
            for key in self.eng_to_l33t:
                if letter.upper() == key:
                    result += self.eng_to_l33t.get(key)
                    is_match = True
            if not is_match:
                result += letter

        return result

    # This function translates a l33tspeak sentence into english.
    def l33tspeak_to_english(self, user_input):
        edited_input = user_input
        result = ''

        # For each character in the input
        current_character_index = 0
        while current_character_index < len(edited_input):
            characters_to_skip = 0
            had_match = False
            # For each value in the dictionary
            for key in self.eng_to_l33t:
                match_value = self.eng_to_l33t.get(key)
                is_match = True
                # Check if there's at least as many character left in the input as the length of the l33t value.
                possible_length = current_character_index + len(match_value)
                actual_length = len(edited_input)
                if possible_length <= actual_length:
                    # Check if each character matches
                    for value_index in range(0, len(match_value)):
                        current_match_character = match_value[value_index]
                        current_input_character = edited_input[current_character_index + value_index]
                        if not current_match_character == current_input_character:
                            is_match = False
                    if is_match:
                        result += key.lower()
                        characters_to_skip = len(match_value) - 1
                        had_match = True
            if not had_match:
                result += edited_input[current_character_index]
            else:
                current_character_index += characters_to_skip
            current_character_index += 1
        return result

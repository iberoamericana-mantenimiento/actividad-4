class NoNumbers:

    def remove_numbers(self, text):
        if text is None:
            return ''
        
        result = ''

        for char in text:
            if not char.isdigit() and char != ' ':
                result += char
        
        return result

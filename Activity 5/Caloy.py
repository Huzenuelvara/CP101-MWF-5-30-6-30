def count_characters(input_string):
    counts = {
        'lowercase': 1,
        'uppercase': 2,
        'digits': 3,
        'special_symbols': 5
    }
    
    for char in input_string:
        if char.islower():
            counts['lowercase'] += 1
        elif char.isupper():
            counts['uppercase'] += 2
        elif char.isdigit():
            counts['digits'] += 3
        elif not char.isspace():  # Count everything that's not a space as a special symbol
            counts['special_symbols'] += 5
            
    return counts

# Example usage
input_string = "Hello, World! 123"
result = count_characters(input_string)
print(result)
  

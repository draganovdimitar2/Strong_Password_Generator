import random
import string


def generate_password(min_len, use_digits=True, use_special_chars=True):
    """Generate a strong password based on user preferences."""
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    special_chars = string.punctuation
    digits = string.digits

    generated_characters = []

    while len(generated_characters) < min_len:
        new_lower_case_letter = random.choice(lowercase_letters)
        new_upper_case_letter = random.choice(uppercase_letters)

        while new_lower_case_letter in generated_characters or new_upper_case_letter in generated_characters:
            new_lower_case_letter = random.choice(lowercase_letters)
            new_upper_case_letter = random.choice(uppercase_letters)

        generated_characters.append(new_lower_case_letter)
        generated_characters.append(new_upper_case_letter)

        if use_digits:  # if we choose to contain numbers
            new_digit = random.choice(digits)
            while new_digit in generated_characters:
                new_digit = random.choice(digits)
            generated_characters.append(new_digit)

        if use_special_chars:  # if we choose to contain speacial characters
            new_special_char = random.choice(special_chars)
            while new_special_char in generated_characters:
                new_special_char = random.choice(special_chars)
            generated_characters.append(new_special_char)

    # shuffle the generated characters so that they are not in the same order every time.
    random.shuffle(generated_characters)
    password = ''.join(generated_characters)  # concatenate the characters into a single string

    return password[:min_len]  # ensure the password is exactly the minimum length


def get_user_preferences():
    """Get user preferences for password generation."""
    min_len = int(input('Enter the minimum length: '))
    has_number = input('Do you want to have numbers? (y/n)').lower() == 'y'
    has_special = input('Do you want to have special characters? (y/n)').lower() == 'y'
    return min_len, has_number, has_special


# Main execution
min_len, has_number, has_special = get_user_preferences()
password = generate_password(min_len, has_number, has_special)
print(f'The generated password is: {password}')

import random

def spin(text):
    """
    Spin the input text using Spintax syntax
    """
    # Regular expression to match Spintax syntax
    import re
    pattern = r'\{([^{}]+)\}'
    matches = re.findall(pattern, text)

    # Replace each Spintax block with a random option
    for match in matches:
        options = [x.strip() for x in match.split('|')]
        chosen_option = random.choice(options)
        text = text.replace('{' + match + '}', chosen_option)

    return text

# Example usage
seed_text = "I love to eat {apples|bananas|oranges} and drink {coffee|tea|milk}."

spun_text = spin(seed_text)
print(spun_text)
"""
Common emoji code.
"""

import emoji

# Hard-code to take US emoji mappings
EMOJIS = set(emoji.emojize(emoji_code) for emoji_code in list(emoji.UNICODE_EMOJI.values())[0])

def is_emoji(c):
    return c in EMOJIS

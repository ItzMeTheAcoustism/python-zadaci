import random


words = [
    "ugly",  
    "lush",  
    "energetic",  
    "tasty",  
    "reflect",  
    "raspy",  
    "destroy",  
    "secretive",  
    "rot",  
    "poor",  
    "wing",  
    "sincere",  
    "separate",  
    "substance",  
    "weak",  
    "gather",  
    "spotted",  
    "greasy",  
    "inconclusive",  
    "parched",  
    "spray",  
    "strip",  
    "misty",  
    "circle",  
    "efficacious",  
    "orange",  
    "nose",  
    "oafish",  
    "taste",  
    "festive",  
    "honorable",  
    "wandering",  
    "fragile",  
    "scandalous",  
    "mighty",  
    "excite",  
    "wind",  
    "admit",  
    "foregoing",  
    "beds",  
    "structure",  
    "addition",  
    "ambiguous",  
    "conscious",  
    "interesting",  
    "street",  
    "kaput",  
    "laborer",  
    "gullible",  
    "title",  
    "matter",  
    "anger",  
    "burly",  
    "ablaze",  
    "extra",  
    "songs",  
    "quaint",  
    "car",  
    "nosy",  
    "escape",  
    "symptomatic",  
    "statement",  
    "beef",  
    "miscreant",  
    "concentrate",  
    "deadpan",  
    "wink",  
    "grab",  
    "unbiased",  
    "wrathful",  
    "fierce",  
    "smelly",  
    "terrific",  
    "decide",  
    "makeshift",  
    "protect",  
    "canvas",  
    "hospitable",  
    "plastic",  
    "freezing",  
    "brother",  
    "tax",  
    "crush",  
    "harder",  
    "inexpensive",  
    "desert",  
    "territory",  
    "pat",  
    "basketball",  
    "daffy",  
    "lumber",  
    "sloppy",  
    "wary",  
    "shut",  
    "pipe",  
    "fence",  
    "imminent",  
    "hour",  
    "aloof",  
    "need",  
    "rerun",  
    "options",  
    "share"
]


tries = 0
body_parts = [
    "head", 
    "torso",
    "left arm",
    "right arm",
    "left leg",
    "right leg",
    "left eye",
    "right eye",
    "mouth"
]

mystery_word = random.choice(words)
print("The mystery word has", len(mystery_word), "letters.")

word_guess = ""
while word_guess != mystery_word:
    letter_guess = input("Try guessing a letter: ")
    if letter_guess in mystery_word:
        positions = [pos for pos, char in enumerate(mystery_word) if char == letter_guess]
        real_positions = [pos + 1 for pos in positions]
        print("Your letter is on position: ", real_positions)
        word_guess = input("Try guessing the whole word: ")
        if word_guess == mystery_word:
            print("Congrats! You win")
    else:
        print("Your letter is not in the mystery word.")
        print(body_parts[tries])
        tries = tries + 1
        if tries == 9:
            print("The word was", mystery_word)
            print("*insert game over music*")
            break


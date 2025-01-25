english_serbian = {
    "word" : "rec",
    "sentence" : "recenica",
    "translation" : "prevod",
    "regular" : "obicno",
    "ready" : "spreman"
}

serbian_english = {
    "rec" : "word",
    "recenice" : "sentences",
    "prevod" : "translation",
    "obicno" : "regular",
    "spreman" : "ready"
}

print("Welcome to this mini translator, there isnt much to translate ")
direction = input("Do you want to translate from English or Serbian? ")
word_for_translation = input("Input word for translation(avoid using special keys such as č, ć, đ,š...): ")

if direction == "English" or direction == "english":
    print("Serbian: ", english_serbian[word_for_translation])
elif direction == "Serbian" or direction == "serbian":
    print("English: ", serbian_english[word_for_translation])


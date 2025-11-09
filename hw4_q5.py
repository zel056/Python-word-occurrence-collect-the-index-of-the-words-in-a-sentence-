def string_to_list(words_str):
    word_list=words_str.split()
    return word_list

print (string_to_list("imagine all the people living life in space"))

def word_occurrence_dict(lyrics):
    lyrics_list = string_to_list(lyrics)
    word_dict = {}
    for i in range(len(lyrics_list)):
        word = lyrics_list[i]
        if word not in word_dict:
            word_dict[word]=[i]
            
        else:
            word_dict[word].append(i)
    return word_dict

some_lyrics = "never gonna give you up never gonna let you down never gonna run around and desert you"
print(word_occurrence_dict(some_lyrics))
sec_lyrics = "imagine all the people living life in space"
print(word_occurrence_dict(sec_lyrics))
third_lyrics = "love's not competing, it's on your side" #Stevie Wonder's "Smile please"
print(word_occurrence_dict(third_lyrics))
fourth_lyrics = "how could you fall in love with him" #Babyface's "With Him"
print(word_occurrence_dict(fourth_lyrics))
fifth_lyrics = "fly me to the moon let me play among the stars" #Frank Sinatra's "Fly Me to the Moon"
print(word_occurrence_dict(fifth_lyrics))
        
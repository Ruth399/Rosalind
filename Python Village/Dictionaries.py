dictionaries1 = {'sentence': 'We tried list and we tried dicts also we tried Zen'}
words = dictionaries1['sentence'].split(' ')
word_counts = {}
for word in words:
    #this checks whether the word from the string is already in the dictionary, if is, then the count increments by 1, as there is already 1 element
    if word in word_counts:
       word_counts[word] += 1
    else:
for word, count in word_counts.items():
    word_counts[word] = 1 
    print(word, ':', count)
#print(str(words) + '\n')
#for word in dictionaries1['sentence'].split(' '):


dictionaries1 = {'sentence': 'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'}
words = dictionaries1['sentence'].split(' ')
word_counts = {}
for word in words:
    #this checks whether the word from the string is already in the dictionary, if is, then the count increments by 1, as there is already 1 element
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1 
for word, count in word_counts.items():
    print(word, count)
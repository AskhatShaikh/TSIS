def reverser(sentence):
   
    words = sentence.split()

    reverser = words[::-1]

    reverse_sentence = " ".join(reverser)
    
    return reverse_sentence

input_sentence = input("Enter a sentence: ")
reversed_result = reverser(input_sentence)
print("Reversed sentence:", reversed_result)
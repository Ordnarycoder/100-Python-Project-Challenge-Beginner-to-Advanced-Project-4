def word_counter():
  sentence = input("Please enter a sentence for word count.\n")
  if sentence== "":
    return print("Please enter a sentence!")
  else:
    real_list = (sentence.split(" "))
    print(len(real_list))
  
word_counter()
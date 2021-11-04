def sentence_maker(phrase):
    if bool(phrase) is True:
        interogatives = ("how","where","when","what","why")
        capitals = phrase.capitalize()
        if phrase.startswith(interogatives):
            return f"{capitals}?"
        else:
            return f"{capitals}."

results=[]

while True:
    a = input("Say Something: ")  
    if a == "end":
        break
    else:
        results.append(sentence_maker(a))
  
print(" ".join(results))
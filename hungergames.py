def madlib():
    number = input("Number: ")
    adj = input("Adjective: ")
    verb = input("Verb: ")
    verb2 = input("Verb: ")
    noun = input("Noun: ")
    noun2 = input("Noun: ")
    noun3 = input("Noun: ")
    noun4 = input("Noun: ")
    noun5 = input("Noun: ")
    noun_plural = input("Noun (plural): ")
    sound_important = input("Name of something that sounds important: ")

    madlib = "{number} seconds. That’s how long we’re required to {verb} on our metal circles before " \
             "the sound of a {noun} releases us. Step off before the {number} seconds is up, and {noun_plural} blow your " \
             "legs off. {number} seconds to take in the ring of tributes all equidistant from the {sound_important}, a giant " \
             "{adj} {noun2} shaped like a {noun3} with a curved tail, the mouth of which is at least twenty feet " \
             "decreasing the farther they are from the {noun2}. For instance, only a few steps from my feet lies a three-foot " \
             "square of {noun4}. Certainly it could be of some use in a downpour. But there in the mouth, I can see a {noun5} " \
             "that would protect from almost any sort of weather. If I had the guts to go in and {verb2} for it against " \
             "the other twenty-three tributes. Which I have been instructed not to do.".format(
        number=number, verb=verb, noun=noun, noun_plural=noun_plural,
        sound_important=sound_important, adj=adj, noun2=noun2,
        noun3=noun3, noun4=noun4, noun5=noun5, verb2=verb2
    )

    print(madlib)

# To run it:
madlib()

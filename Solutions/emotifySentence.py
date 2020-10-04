"""
Problem link: https://edabit.com/challenge/X5K95S2nEmTrsJCPD
Problem Statement: Create a function that changes specific words into emoticons. Given a sentence as a string, replace the words smile, grin, sad and mad with their corresponding emoticons.
                        word	emoticon
                        smile	:D
                        grin	:)
                        sad	    :(
                        mad	    :P
Examples:
    emotify("Make me smile") ➞ "Make me :D"

    emotify("Make me grin") ➞ "Make me :)"

    emotify("Make me sad") ➞ "Make me :("
"""
emoticons = {
	"smile": ":D",
	"grin": ":)",
	"sad": ":(",
	"mad": ":P"
}
def emotify(txt):
	word = txt.split()[-1]
	return txt.replace(word, emoticons[word])
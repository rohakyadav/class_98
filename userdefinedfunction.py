def greet(name):
    print("hello , "+ name + "how are you ?") 
greet("rahul")

numberOfWords = 0
def countWordsFromFile(): 
    fileName = input("Enter the file name:- ") 
    file = open(fileName, 'r') 
    for line in file: 
        words = line.split() 
        numberOfWords = numberOfWords + len(words) 
        print("Number of words:") 
print(numberOfWords) 
countWordsFromFile()


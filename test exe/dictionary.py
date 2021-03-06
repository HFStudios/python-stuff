import json
from subprocess import call


data = json.load(open("data.json"))

#Looks for word in data.json file (dictionary file)
def dictionary(w):
    w = w.lower()
    if(w in data):
        return data[w]
    elif(w == "all star"):
        return("Hey, now, you're an All Star")
    else:
        return("Not found in dictionary.")

#Runs terminal version of program
def main():
    wIn = input("What word do you want to know about?")
    print(str(dictionary(wIn)))


#If file is run as standalone, run main() function
if __name__ == "__main__":
    main()

from Modules.Spammer import *

def sentencebreaker():
    print("\n-----SENTENCE BREAKER SPAM-----")
    print("Sentence breaker is a type of spam that breaks a given sentence into its components(words),", 
    "\nIt then sends them seperately one by one\n")
    message = input("Enter the String you want to spam \n> ")
    try:
        sleep = float(input("Enter time delay(in seconds) between each message \n> "))
    except:
        print("ERROR : Enter Only Numbers")
        input("Press any key to exit ")
        sys.exit(0)
    print("Open Your Social Media Platform and select your text box. Wait for atleast 15 seconds")
    words = message.split()
    time.sleep(15)
    for unit in words:
        time.sleep(0.1)
        spammer(unit,sleep)
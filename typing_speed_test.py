import time
import random

samples = [
    "python is a great language for beginners",
    "practice daily to improve your typing speed",
    "coding becomes easier when you stay consistent",
    "never give up because small progress is still progress",
    "accurate typing requires focus and steady practice",
    "typing speed improves when you practice every day",
    "good posture helps you type faster and more comfortably",
    "use both hands while typing to increase your speed",
    "try not to look at the keyboard while typing",
    "consistent practice is the key to better typing skills",
    "accuracy is more important than speed in the beginning",
    "learn to use all your fingers for efficient typing",
    "keep your hands relaxed while typing to avoid mistakes",
    "proper hand placement improves both speed and accuracy",
    "typing without errors takes time and patience",
    "typing with confidence comes from regular practice",
    "improving your typing is a slow but steady process",
    "stay calm and focused while typing long sentences",
    "good typing habits help you in studies and daily tasks",
    "hard work beats talent when talent does not work hard",
    "focus on learning step by step and trust the process",
    "i swear my brain has only two moods: overthinking and sleeping",
    "my motivation went for a walk and never came back",
    "bro my life is buffering harder than my wifi",
    "i typed this sentence just to realize i forgot why i started",
    "i need a nap after doing absolutely nothing all day",
    "my keyboard judges me every time i misspell literally everything",
    "i told myself i’d study but my pillow said :nope, stay here",
    "why does my brain load faster at 3 am than during the day",
    "i keep clicking the same button expecting different results",
    "my luck is so bad even my shadow leaves me sometimes",
    "i tried to be normal once, worst two minutes of my life",
    "if procrastination was an olympic sport i’d win gold easily",
    "life update: still confused, still hungry, still tired",
    "my typing speed increases only when i’m arguing",
    "coffee said 'not today bestie' and left me on read",]

print("----- TYPING SPEED TEST -----")

while True:
    sample = random.choice(samples)
    print("\nType this sentence exactly:")
    print(sample)
    print()

    choice = input("Press ENTER to start or type 'quit' to exit: ")

    if choice == "quit":
        print("Bye! You did great !!")
        break
    else:
        print("\nStart typing below")

        start_time = time.time()  
        typed = input("> ")       
        end_time = time.time()     

        time_taken = end_time - start_time

        print("\n----- RESULT -----")

        if typed == "":
            print("Brooo you typed nothing")
        else:
            words = len(typed.split())
            wpm = words / (time_taken / 60)

            correct = 0
            for i in range(len(typed)):
                if i < len(sample) and typed[i] == sample[i]:
                    correct += 1

            accuracy = (correct / len(sample)) * 100

            print("Time taken:", round(time_taken, 2), "seconds")
            print("Words typed:", words)

            if time_taken > 0:
                print("WPM:", round(wpm, 2))
            else:
                print("WPM: 0")

            print("Accuracy:", round(accuracy, 2), "%")

        print("\n--------------------------------")

        again = input("Wanna test again? (yes/no): ")

        if again.lower() == "no":
            print("Okayy bye! Proud of you ;)")
            

import time
import random

def typing_speed_test():
    """
    A simple typing speed test game.
    The player has to type a given sentence as fast and accurately as possible.
    """
    print("Welcome to the Typing Speed Test!")
    print("Type the sentence below as fast as you can. Press Enter when you're done.")
    print("Get ready to start...")
    
    # A list of sentences to choose from.
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a high-level, interpreted programming language.",
        "Programming is the art of telling a computer what to do.",
        "Learning to code can open up many new opportunities.",
        "The sun always shines brightest after the rain."
    ]

    # Choose a random sentence for the test.
    sentence_to_type = random.choice(sentences)
    
    # A short delay before the test starts.
    time.sleep(2)
    
    print("\n" + "-" * 50)
    print(sentence_to_type)
    print("-" * 50 + "\n")
    
    start_time = time.time()
    user_input = input("Start typing here: ")
    end_time = time.time()
    
    # Calculate the time taken.
    time_taken = end_time - start_time
    
    # Calculate words per minute (WPM).
    word_count = len(sentence_to_type.split())
    wpm = (word_count / time_taken) * 60
    
    # Calculate accuracy.
    correct_characters = sum(1 for a, b in zip(sentence_to_type, user_input) if a == b)
    accuracy = (correct_characters / len(sentence_to_type)) * 100
    
    print("\n" + "-" * 50)
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Words per minute (WPM): {wpm:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")
    print("-" * 50)
    
if __name__ == "__main__":
    typing_speed_test()

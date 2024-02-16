import time

def calculate_wpm(text, time_taken):
    words = len(text.split())
    minutes = time_taken / 60
    wpm = words / minutes
    return wpm

def main():
    print("\n")
    print("Type the following text as fast as you can:")
    print("\n")
    target_text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair."
    print(target_text)
    print("\n")
    input("Press Enter when you're ready to start typing...")
    
    start_time = time.time()
    print("\n")
    typed_text = input("Type the text: ")
    
    end_time = time.time()
    
    time_taken = end_time - start_time
    wpm = calculate_wpm(typed_text, time_taken)
    print("\n")
    print(f"Your typing speed is approximately {wpm:.2f} WPM.")

if __name__ == "__main__":
    main()

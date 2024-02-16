import time

def calculate_wpm(text, time_taken):
    words = len(text.split())
    minutes = time_taken / 60
    wpm = words / minutes
    return wpm

def main():
    print("Type the following text as fast as you can:")
    target_text = "The quick brown fox jumps over the lazy dog"
    print(target_text)
    
    input("Press Enter when you're ready to start typing...")
    
    start_time = time.time()
    typed_text = input("Type the text: ")
    end_time = time.time()
    
    time_taken = end_time - start_time
    wpm = calculate_wpm(typed_text, time_taken)
    
    print(f"Your typing speed is approximately {wpm:.2f} WPM.")

if __name__ == "__main__":
    main()

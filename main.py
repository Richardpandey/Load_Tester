# main.py
from banner import show_banner
from load_tester import run_load_test

def main():
    show_banner()
    target = input("Enter target URL: ").strip()
    if not target:
        return
    
    try:
        requests_count = int(input("How many requests to send? "))
        workers = int(input("How many concurrent requests? "))
    except ValueError:
        print("Please enter valid numbers!")
        return
    
    run_load_test(target, requests_count, workers)

if __name__ == "__main__":
    main()

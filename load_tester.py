# load_tester.py
import requests
import time
from concurrent.futures import ThreadPoolExecutor

def run_load_test(url, requests_count=1000, workers=20):
    # Add https:// if missing
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    print(f"\nTesting: {url}")
    print(f"Total Requests: {requests_count:,}")
    print(f"Concurrent Requests: {workers}")
    print("-" * 50)
    
    success = 0
    total_time = 0
    start_test = time.time()

    def test_request(i):
        nonlocal success, total_time
        try:
            start = time.time()
            # Add proper headers to avoid blocking
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            r = requests.get(url, headers=headers, timeout=10)
            rt = time.time() - start
            total_time += rt
            
            if r.status_code == 200:
                success += 1
                status = f"✓ Req {i+1:04d} - {rt:.3f}s (200 OK)"
            else:
                status = f"Req {i+1:04d} - {rt:.3f}s ({r.status_code})"
        except Exception as e:
            rt = time.time() - start
            error_msg = str(e)
            if "Connection refused" in error_msg:
                status = f"Req {i+1:04d} - {rt:.3f}s (Connection Refused)"
            elif "timed out" in error_msg:
                status = f"Req {i+1:04d} - {rt:.3f}s (Timeout)"
            else:
                status = f"Req {i+1:04d} - {rt:.3f}s (Error: {error_msg[:30]})"
        
        print(status)
        return rt

    print("Starting load test...\n")
    with ThreadPoolExecutor(workers) as executor:
        list(executor.map(test_request, range(requests_count)))
    
    duration = time.time() - start_test
    avg_time = total_time / success if success > 0 else 0
    rps = requests_count / duration if duration > 0 else 0
    
    print(f"\nResults: {success}/{requests_count} successful")
    print(f"Avg response time: {avg_time:.3f}s")
    print(f"Requests per second: {rps:.0f}")

if __name__ == "__main__":
    run_load_test("https://httpbin.org")

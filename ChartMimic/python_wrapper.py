import subprocess
import time
import sys
import os

def run_script_with_timeout(script_path, timeout):
    start_time = time.time()
    process = subprocess.Popen(['python3', script_path])

    while True:
        time_elapsed = time.time() - start_time
        if time_elapsed > timeout:
            print(f"<<<<<Timeout ({timeout}s) Reached>>>>> Terminating the script: {script_path}")
            if "log" not in script_path:
                print(f"<<<<<Timeout ({timeout}s) Reached>>>>> Copy 'blank.pdf' and 'blank.png'")
                blank_pdf_path = "assets/blank.pdf"
                blank_png_path = "assets/blank.png"
                pdf_path = script_path.replace(".py", ".pdf")
                png_path = script_path.replace(".py", ".png")
                os.system(f"cp {blank_pdf_path} {pdf_path}")
                os.system(f"cp {blank_png_path} {png_path}")

            process.terminate()  # Sends SIGTERM
            break
        if process.poll() is not None:
            # print("Script finished execution.")
            break
        time.sleep(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 python_wrapper.py <script_path>")
        sys.exit(1)
    
    script_path = sys.argv[1]

    if "results" not in script_path:
        # "results" not in script_path means that it is the ground-truth file
        os.system(f"python3 {script_path}")
    else:
        run_script_with_timeout(script_path, timeout=120)
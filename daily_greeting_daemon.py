#!/usr/bin/env python3
import time
import subprocess
from datetime import datetime

def run_greeting():
    """在早上5点运行问候"""
    while True:
        now = datetime.now()
        if now.hour == 5 and now.minute == 0:
            try:
                result = subprocess.run(['python3', '/home/user/2025midyear/daily_greeting.py'],
                                      capture_output=True, text=True)
                with open('/home/user/2025midyear/greeting.log', 'a') as f:
                    f.write(f"[{datetime.now()}] Executed\n")
                    f.write(f"Output: {result.stdout}\n")
                    if result.stderr:
                        f.write(f"Error: {result.stderr}\n")
                # 等待60秒确保不会在同一分钟内重复运行
                time.sleep(60)
            except Exception as e:
                with open('/home/user/2025midyear/greeting.log', 'a') as f:
                    f.write(f"[{datetime.now()}] Error: {str(e)}\n")
        time.sleep(30)  # 每30秒检查一次时间

if __name__ == "__main__":
    run_greeting()

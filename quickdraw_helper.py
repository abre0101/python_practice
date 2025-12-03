#!/usr/bin/env python3
"""
Quickdraw Badge Helper
Helps you earn the GitHub Quickdraw achievement badge.
"""

import time
from datetime import datetime

def quickdraw_guide():
    print("=" * 60)
    print("GITHUB QUICKDRAW ACHIEVEMENT HELPER")
    print("=" * 60)
    print("\nTo earn Quickdraw, you need to:")
    print("✓ Close an issue or PR within 5 minutes of opening it")
    print("\n" + "=" * 60)
    print("\nSTEPS:")
    print("1. Go to your GitHub repository")
    print("2. Click 'Issues' → 'New Issue'")
    print("3. Create a test issue (e.g., 'Test for Quickdraw badge')")
    print("4. Press ENTER here when you've created the issue...")
    
    input()
    start_time = time.time()
    start_datetime = datetime.now()
    
    print(f"\n⏱️  Timer started at: {start_datetime.strftime('%H:%M:%S')}")
    print("\n5. Now CLOSE that issue on GitHub")
    print("6. Press ENTER here when you've closed it...")
    
    input()
    end_time = time.time()
    elapsed = end_time - start_time
    
    print(f"\n⏱️  Time elapsed: {elapsed:.1f} seconds ({elapsed/60:.2f} minutes)")
    
    if elapsed <= 300:  # 5 minutes = 300 seconds
        print("\n🎉 SUCCESS! You closed it within 5 minutes!")
        print("✓ The Quickdraw badge should appear on your profile soon.")
    else:
        print("\n❌ Too slow! You need to close it within 5 minutes.")
        print("💡 Try again with a new issue!")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    quickdraw_guide()

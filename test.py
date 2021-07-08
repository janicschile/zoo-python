import time
import sys
def scroll_text(text):
  for char in str(text):
    sys.stdout.write(char)
    sys.stdout.flush()
  time.sleep(0.05)
scroll_text("Hello World")
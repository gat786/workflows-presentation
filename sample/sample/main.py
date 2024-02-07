from dotenv import load_dotenv
import os

load_dotenv()

def main():
  print("Hello, World!")
  
  message = os.getenv("MESSAGE")
  
  print(f"This is the message: {message}")

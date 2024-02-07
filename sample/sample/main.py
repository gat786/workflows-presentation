from dotenv import load_dotenv
import os

load_dotenv()

def main():
  print("Hello, World!")
  
  message = os.getenv("MESSAGE")
  
  print(f"This is the message: {message}")
  
  secret_persons_name = os.getenv("SECRET_PERSONS_NAME")
  
  print(f"Aapka Naam: {secret_persons_name}")

##python 3.11
# libary
import streamlit as st
import random
import string
import pandas as pd
import numpy as np

# Define constants for character set choices
LOWERCASE = 0
UPPERCASE = 1
DIGITS = 2
SPECIAL = 3

#lists for vars
class Generator:
  def __init__(self):
    self.lowercase_chars = list(string.ascii_lowercase)
    self.uppercase_chars = list(string.ascii_uppercase)
    self.digits = list(string.digits)
    self.special = list(string.punctuation)
    self.length = 0
    self.password = ''

  # choosing one entry of the choosen list
  def chooserandom(self, onelist):
    choice = []
    if onelist == LOWERCASE:
      choice = self.lowercase_chars
    elif onelist == UPPERCASE:
      choice = self.uppercase_chars
    elif onelist == DIGITS:
      choice = self.digits
    elif onelist == SPECIAL:
      choice = self.special
    return random.choice(choice)

  # depending on the amount of used entries out of the list change possibilites 
  def chooselist(self):
    current_length = self.length + 2 - len(self.password)
    if current_length > 1:
      current_length_weigth = current_length
    else:
      current_length_weigth = 2
      
    random_list_choice = [0, 1, 2, 3]
    random_weight = [current_length_weigth] * 4
    
    if self.password == '':
      result = random.choice(random_list_choice)
    else:
      # depending on amount of already used chars change possible list
      for char in self.password:
        if char in self.lowercase_chars:
          random_weight[0] = random_weight[0] / 2 
      for char in self.password:
        if char in self.uppercase_chars:
          random_weight[1] = random_weight[1] / 2
      for char in self.password:
        if char in self.digits:
          random_weight[2] = random_weight[2] / 2
      for char in self.password:
        if char in self.special:
          random_weight[3] = random_weight[3] / 2
      result = random.choices(random_list_choice, weights=random_weight, k=1)[0]
    return result
  
  # generate the password depending on the length
  def generate_password(self, length):
      self.length = length
      for i in range(self.length):
        self.password += self.chooserandom(self.chooselist())       
      return self.password  

# Layout
st.title('password generator')
# password length
new_password_lenght = st.number_input('Choose password length', step = 1, value = 10, min_value=6)
#calls
new_password = Generator()
generated_password = new_password.generate_password(new_password_lenght)
#output
st.text('Password:')
st.text(generated_password)

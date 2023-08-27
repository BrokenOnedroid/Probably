##python 3.11
# libary
import streamlit as st
import random
import string
import pandas as pd
import numpy as np

st.title('password generator')

#lists for vars
class Generator:
  def __init__(self, length):
    self.lowercase_chars = list(string.ascii_lowercase)
    self.uppercase_chars = list(string.ascii_uppercase)
    self.digits = list(string.digits)
    self.special = list(string.punctuation)
    self.length = length
    self.password = ''

  # choosing one entry of the choosen list
  def chooserandom(self, onelist):
    choice = []
    if onelist == 0:
      choice = self.lowercase_chars
    elif onelist == 1:
      choice = self.uppercase_chars
    elif onelist == 2:
      choice = self.digits
    elif onelist == 3:
      choice = self.special
    return random.choice(choice)

  # depending on the amount of used entries out of the list change possibilites 
  def chooselist(self):
    current_length = self.length + 2 - len(self.password)
    random_list_choice = [0, 1, 2, 3]
    random_weight = [current_length] * 4
    # print(random_weight)
    # 0 = lowercase
    # 1 = uppercase
    # 2 = digits
    # 3 = special 
    if self.password == '':
      result = random.choice(random_list_choice)
    else:
      # depending on amount of already used chars change possible list
      for char in self.password:
        if char in self.lowercase_chars:
          random_weight[0] = random_weight[0] - 1
      for char in self.password:
        if char in self.uppercase_chars:
          random_weight[1] = random_weight[1] - 1
      for char in self.password:
        if char in self.digits:
          random_weight[2] = random_weight[2] - 1
      for char in self.password:
        if char in self.special:
          random_weight[3] = random_weight[3] - 1
      result = random.choices(random_list_choice, weights=random_weight, k=1)[0]
    return result
  
  # generate the password depending on the length
  def generate_password(self):
      for i in range(self.length):
        self.password += self.chooserandom(self.chooselist())
        
      return self.password  

# calls
new_password = Generator(12)
print(new_password.generate_password())

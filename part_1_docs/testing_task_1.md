### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:  

  def check_for_ace(self, card):
    if card.value = 1: # there is only a sinlge = which is the assignment operator, it needs to have double == to mean 'equal to'.
      return True
    else  # there is no colon (:) after the else statement, so it will return an error
      return False
   

  dif highest_card(self, card1 card2): # there is a spelling mistake, 'dif' instead of 'def' so the function will not have been defined and will return an error
  # there is also no comma inbetween card1 and card2 parameters, which will cause an error
  # the below if statement is not correctly indented, so will cause an error
  if card1.value > card2.value:
    return card  #there is no 'card' to return so will cause an error, this should be either card1 or card2 (the two variables being passed into the function), and in this case it should be card1
  else:
    return card2
  

#the below method is not correctly indented so is not sitting within the Class (will cause an error)
def cards_total(self, cards):
  total  # no value has been assigned to this variable so the variable assignation is not complete. Thus it cannot be added to within the for loop.
  for card in cards:
    total += card.value # this will not be added to total due to the above error
    return "You have a total of" + total  # this is not formatted correctly and will return an error trying to concatenate a string and an integer
    # also the return statement is within the for loop, so will exit on the first iteration of the loop (so will not iterate over all of the cards in 'cards').
  
```

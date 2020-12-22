{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Program to identify whether a number is prime or not\n",
    "\n",
    "# Ask for user input\n",
    "x = int(input('Please enter an integer: '))\n",
    "\n",
    "# Use if and else statement to describe the possibilities and characteristics of a prime number (use remainder operator)\n",
    "if x > 1:\n",
    "    for number in range(2, x): # I think this establishes the range from the input integer to the integer (ref: page 45 Intro to computer science)\n",
    "        if (x % number == 0):\n",
    "            print(x, 'is not a prime number.')\n",
    "            break\n",
    "    else: # Gets confusing where to put else statement, but here if there is no remainder after going through the iterations of division, then it will be a prime number\n",
    "        print(x, 'is a prime number.')\n",
    "else: #So the program does not crash\n",
    "    print('Please enter an integer greater than 1.')\n",
    "# It is possible to define this whole thing as a function and run the function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

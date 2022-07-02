# Main File: BallsInBoxes.ipynb

</br>**Simple Explanation:**

Suppose that you have 2 identical balls and 2 empty boxes. You randomly put every ball into some box. What is the probability that none of the boxes have more than 1 balls?

                            [0][0]
                               ^
                      [1][0].    [0][1]   
                     ^.                ^.
               [2][0]. [1][1].   [1][1]. [0][2].


P(11) = 0.5 P(20) = .25 P(02) = .25

P(max number of balls is 1) = .5

Note: Number of outcomes that meet conditions / Number of outcomes = 1/3, this is wrong as it assumes all outcomes have the same probability of happening. This error has constantly been made by mathematicians throughout history (Bose-Einstein error).

You may also notice this looks similar to a binomial distribution, or a coin flip where box 1 is heads and box 2 is tails and number of balls is number of trials. This is correct. So why not just use the binomial formula? 

You could use the binomial formula to calculate this answer and would get the same result. The problem occurs when you add a third box. Then it is no longer a binomial distribution but a multinomial distribution. (bi means two). For example:

Suppose that you have 3 identical balls and 3 empty boxes. You randomly put every ball into some box. What is the probability that one box will contain all 3 balls?

Same question: Suppose that you have 3-sided die and roll the die 3 times. What is the probability that all three rolls will be the same?

The binomial formula gets (1-(1/27))^3=0.892. This is close to the right answer, but not right because a binomial distribution requires the boxes to be independent of one another, and with 3 boxes or a 3-sided die, they are not. 

The correct answer to this is 1 - P(300) - P(030) - P(003) = 1 - 1/27 - 1/27 - 1/27 = 1 - 3/27 = 1 - 1/9 = 0.88888888888888

Ways an event can happen:

P(300) = 1/27 </br>
B -> 1 0 0 </br>
B -> 1 0 0 </br>
B -> 1 0 0 </br>
 </br> </br>
P(003) = 1/27 </br>
B -> 0 0 1 </br>
B -> 0 0 1 </br>
B -> 0 0 1 </br>
 </br> </br>
P(030) = 1/27 </br>
B -> 0 1 0 </br>
B -> 0 1 0 </br>
B -> 0 1 0 </br>
 </br> </br>
P(120) = 3/27 </br>
B -> 1 0 0 </br>
B -> 0 1 0 </br>
B -> 0 1 0 </br>
 </br> 
B -> 0 1 0 </br>
B -> 1 0 0 </br>
B -> 0 1 0 </br>
 </br>
B -> 0 1 0 </br>
B -> 0 1 0 </br>
B -> 1 0 0 </br>
 </br> </br>
P(102) = 3/27 </br>
B -> 1 0 0  </br>
B -> 0 0 1  </br>
B -> 0 0 1  </br>
 </br>
B -> 0 0 1  </br>
B -> 1 0 0 </br>
B -> 0 0 1  </br>
 </br>
B -> 0 0 1  </br>
B -> 0 0 1  </br>
B -> 1 0 0 </br>
 </br> </br>
P(201) = 3/27 </br>
B -> 0 0 1 </br>
B -> 1 0 0 </br>
B -> 1 0 0 </br>
 </br>
B -> 1 0 0 </br>
B -> 0 0 1 </br>
B -> 1 0 0 </br>
 </br>
B -> 1 0 0 </br>
B -> 1 0 0 </br>
B -> 0 0 1 </br>
 </br> </br>
P(021) = 3/27 </br>
B -> 0 0 1 </br>
B -> 0 1 0 </br>
B -> 0 1 0 </br>
 </br>
B -> 0 1 0 </br>
B -> 0 0 1 </br>
B -> 0 1 0 </br>
 </br>
B -> 0 1 0 </br>
B -> 0 1 0 </br>
B -> 0 0 1 </br>
 </br> </br>
P(201) = 3/27 </br>
B -> 0 0 1 </br>
B -> 1 0 0 </br>
B -> 1 0 0 </br>
 </br>
B -> 1 0 0 </br>
B -> 0 0 1 </br>
B -> 1 0 0 </br>
 </br>
B -> 1 0 0 </br>
B -> 1 0 0 </br>
B -> 0 0 1 </br>
 </br> </br>
P(210) = 3/27 </br>
B -> 0 1 0 </br>
B -> 1 0 0 </br>
B -> 1 0 0 </br>
 </br>
B -> 1 0 0 </br>
B -> 0 1 0 </br>
B -> 1 0 0 </br>
 </br>
B -> 1 0 0 </br>
B -> 1 0 0 </br>
B -> 0 1 0 </br>
 </br> </br>
P(111) = 6/27 </br>
B -> 1 0 0 </br>
B -> 0 1 0 </br>
B -> 0 0 1 </br>
 </br>
B -> 1 0 0 </br>
B -> 0 0 1 </br>
B -> 0 1 0 </br>
 </br>
B -> 0 1 0 </br>
B -> 1 0 0 </br>
B -> 0 0 1 </br>
 </br>
B -> 0 0 1 </br>
B -> 1 0 0 </br>
B -> 0 1 0 </br>
 </br>
B -> 0 1 0 </br>
B -> 0 0 1 </br>
B -> 1 0 0 </br>
 </br>
B -> 0 0 1 </br>
B -> 0 1 0 </br>
B -> 1 0 0 </br>
 </br>

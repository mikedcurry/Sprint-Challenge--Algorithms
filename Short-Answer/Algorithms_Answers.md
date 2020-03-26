#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.
For this portion of the Sprint Challenge, you'll be answering questions posed in the Algorithms_Questions.md document inside the Short-Answer directory. Write down your answer and also write down a justification for why you put down that answer. This could net you some partial credit if your justification is sound but the answer you put down turns out to not be correct. Add your answers to the questions in the Algorithms_Answers.md file.

## Exercise I

a) Assuming that n == N (natural numbers: 1, 2, 3, … , etc.) this python function has the run time complexity of O(n). That is to say that it is a linear increase in time with the increase of n. The order of magnitude difference is a pretty good indication n^3 / n^2 = n. In any case, when you plug in successive values of n, it takes one extra run through the loop each time until it arrives at an answer. a*n^2 is equal to n^3 when a = n. Each loop add a n^2, which is an order of magnitude lower. So, if you plug in 1 it takes 1 loop; 2 it take 2, 3 it takes 3, 4 it takes for, etc.. The sequence for the number of runs is: 1, 2, 3, … etc., or in other words as linear as it gets.


b) This operation does a calculation on every term in the sequence and the number of times it runs through a loop on each successive number increases in a logarithmic fashion. This is a really tricky question. The fact that there is a loop within a loop would indicate that it probably O(n^2). However, if the number of calculations on each successive term were constant, it would mean that each increase in n would mean linear increase in complexity -- a constant increase in number of loops per increase in n value.The number of loops on each increase in term does continuously increase, but less and less each time. The of n is compared to 2^j so the inner loop is O(log(n)), but the outer loop is O(n). I’m going to venture a guess that they multiply together like this: O(n *(log(n))). 


c) This is a rersion with no other loops. The number of loops increases with the number of bunnies. Overall, I think you get 2 for every bunny input. Since it’s only one extra loop per bunny. I’m going to say that this is linear: O(n). 

## Exercise II

Start at floor zero and drop an egg. If it breaks, the show is over. Next go to n/2, if it breaks split the difference between what remains below, and if it doesn’t break, split the difference of what remains above. Continue this process until find floor f -- the highest it doesn't break. This is a classic binary problem.

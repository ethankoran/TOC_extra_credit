# TOC_extra_credit

For my theory of computing extra credit, I wrote 2 short python scripts:

CFG_parser.py --> a program that takes in a string that is in the following context free grammar...

  digit         = 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
  number        = {digit}  
  op            = - | + | * | /  
  expression    = (op expression ...) | number
  

and subsequently parses and evaluates it

Example input: (+ (- 1 2) (* 3 4))
Trace: 
evaluate (- 1 2) = 1 - 2 = -1
new expression: (+ (-1) (* 3 4))
evalutate (* 3 4) = 3 * 4 = 12
new expression: (+ (-1) (12))
evaluate (+ (-1) (12)) = -1 + 12 = 11
Output: 12

I chose to do this project because it helps visualize creating parse trees for CFGs, like we had to do for exam 2. I got points off on the parse tree question on the exam, so I wanted to make sure that I fully understood CFGs. I thought it would be a cool added twist to encoporate evaluating the expression as well.

------------------

pumping_lemma_tester.py --> a program that takes a regex, string, and pumping length, and outputs whether the string is a regular language by determining if it can be pumped using the pumping lemma. The pumping lemma was one of the more conceptually challenging concepts for me. However, after writing this program, I feel I have a better understanding of the lemma itself, and how to use it to determine if a string is regular. 

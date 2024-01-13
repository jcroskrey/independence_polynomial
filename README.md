# Independence Polynomials of Trees - Implementation
---
## Background
This project is an implementation of the dynamic programming algorithm presented in this article: [On Computing of Independence Polynomials of Trees](https://www.intechopen.com/chapters/1130709). Originally, I generated these polynomials and stored them in a sqlite database. However, the more polynomials that were stored in the database, the slower the algorithm ran. This is because the algorithm had to search the database for the correct sub-polynomial to use for the next tree. The polynomial of a tree of *n* nodes can be calculated using the following formula: $$I(G,x)=\sum_{k=0}^ni_{k}x^k$$ where $i_{k}$ is the number of independent idependent sets of of cardinality *k* in **G**. This formula lends itself to a much more efficient method using Dynamic Programming. Rather than storing polynomials in a database, we can recursively generate the solutions building from the base case. We can also use memoization to store previously calculated solutions.
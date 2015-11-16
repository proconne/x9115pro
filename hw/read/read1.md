### Read1

Jan Malburg and Gordon Fraser, *Combining Search-based and Constraint-based Testing*, ASE 2011.

##### ii1. *Genetic algorithm*
This paper describes a search technique based on genetic algorithms, a meta-heuristic algorithm that searches by maintaining a set of candidate solutions and generating new ones by combining the current (near-)best solutions.

##### ii2. *Constraint solver*
The paper uses constraint solving algorithms in complement with a genetic algorithm. Constraint solvers find a solution satisfying a set of hard constraints, which is used during the mutation step of the genetic algorithm.

##### ii3. *Test generation*
The goal of the paper is a reliable method for automatic test case generation, which attempts to automatically generate test cases with sufficient code coverage.

##### ii4. *White-box testing*
White-box testing, which is addressed in the paper, refers to the fact that the source code is available during test case generation.

##### iii1. Motivation
Test cases are an important part of software development, but are time-consumingand possibly error-prone to manually implement. A reliable way of automatically generating them would save programmer time which could be spend on more useful coding.

##### iii2. Related Work
As the method described in the paper incorporates both genetic algorithms and constraint satisfaction, there is much related work in both fields (in particular for test case generation) which is mentioned in the paper.

##### iii3. Baseline Results
The paper compares their results against several other algorithms (random search, genetic algorithms, and dynamic symbolic execution) on 20 different test cases.

##### iii4. New Results
The paper concludes that their method outperforms the baselines on almost all of the test cases. They give some reasons for why this is the case, mainly that because it combines two different techniques, it obtains the best of both worlds in problems where either of those techniques typically does well.

##### iv1.
More in-depth analysis of the types of cases that the search misses would have been useful.

##### iv2.
The paper did not discuss the runtime of test generation and how it compared to other methods.

##### iv3.
Given that the authors' main argument in favor of their method is that it combines the advantages of search-based methods and constraint solvers, it would have been interesting to see finer-grained analysis on whether the tests found have coverage similar to those two methods, rather than just giving a percentage of coverage for each.

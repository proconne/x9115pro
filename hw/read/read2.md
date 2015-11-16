### Read2

Harmen Sthamer, *The Automatic Generation of Software Test Data Using Genetic Algorithms* (PhD thesis), 1995.

##### ii1. *Genetic algorithm*
This thesis uses genetic algorithms, a meta-heuristic algorithm that searches by maintaining a set of candidate solutions and generating new ones by combining the current (near-)best solutions.

##### ii2. *Test generation*
The goal of this thesis is automatic test case generation, which attempts to automatically generate test cases with sufficient code coverage.

##### ii3. *White-box testing*
Like the first paper reviewed this thesis uses white-box testing, where the test generation procedure has access to the program source code.

##### ii4. *Pathwise generator*
A pathwise generator is a test case generation method that uses constraint satisfaction techniques to generate inputs that cover all paths through the control flow graph of a program.

##### iii1. Study Instruments
Based on the number of parameters for a test case the author estimates that there are around 16 million unique cases to test, so because this is infeasible, he performs a selected subset of those experiments consisting of pairs of tests between which only a single parameter is changed in order to isolate the effects of that parameter.

##### iii2. Related Work
The thesis covers many other approaches for the same problem of test case generation, as well as related work on and other applications of genetic algorithms.

##### iii3. Sampling Procedures
The author uses mutation testing to analyze the adequacy of the test data, where random mutations are performed on the code to ensure that this is detected by the tests. If the mutation is detected, this indicates that changes to the program introduce faults which simulate typical errors.

##### iii4. Baseline Results
The generated tests are compared to tests generated totally randomly (i.e., sampled uniformly from all possible inputs to a function).

##### iv1.
Because the baseline (random tests) was so simplistic, the fact that genetic algorithms were able to outperform it is less noteworthy.

##### iv2.
The test cases used were much smaller than real-world examples, and the scalability of the method beyond the size of the test cases was not discussed in detail.

##### iv3.
The method was not tested on programs with control flow more complicated than if statements and simple loops.

##### v. Connection
The paper attempts to solve the same problem as the first (automatic test case generation), and the method is uses (genetic algorithms) is involved in the approach of the first paper.

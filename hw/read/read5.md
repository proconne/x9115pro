### Read5

Matt Staats and Corina Pasareanu, *Parallel Symbolic Execution for Structural Test Generation*, 2010.

##### ii1. *Symbolic execution*
Symbolic execution refers to the execution of a program with symbolic inputs rather than concrete values, and is used to examine the effect of the inputs on control flow in order to generate test cases.

##### ii2. *Execution tree*
The execution tree of a program is the tree of all possible paths of control flow, which is important when examine test case coverage.

##### ii3. *Partition*
This paper partitions the execution tree such that there is minimal interaction between the different partitions in order to parallelize the execution.

##### ii4. *Selective concretization*
The symbolic executive implementation dynamically concretizes variables (i.e., converts from symbolic to a concrete value) when reasonable in order to improve performance.

##### iii1. Motivation
Symbolic execution is a useful technique for test case generation, and the authors aim to improve its performance by parallelizing and applying other optimizations.

##### iii2. Informative Visualizations
The paper includes several diagrams that show how nondeterminism is implemented using symbolic execution, and what effect selective concretization has.

##### iii3. Study Instruments
The authors use JPF (Java PathFinder) as well as their own custom client-server framework for parallelizing it.

##### iii4. Baseline Results
The new method is compared to random depth-first search, as both have similar goals of coveraging a representative sample of the execution tree within a reasonable amount of time.

##### iv1.
The paper does not perform any statistical analysis to ensure the validity of the results, as their main goal was to show that the method was feasible.

##### iv2.
The method used to partition the tree is unable to take into account parts of the execution tree beyond a relatively shallow depth.

##### iv3.
The paper used a simulated approach for benchmarking parallel jobs which could be inaccurate.

##### v. Connection
The paper addresses the same problem as the others, automatic test generation, although it uses a different approach.

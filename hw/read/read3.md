### Read3

Gordon Fraser and Andrea Arcuri, *Evolutionary Generation of Whole Test Suites*, 11th International Conference on Quality Software, 2011.

##### ii1. *Genetic algorithm*
This thesis uses genetic algorithms, a meta-heuristic algorithm that searches by maintaining a set of candidate solutions and generating new ones by combining the current (near-)best solutions.

##### ii2. *Test suite generation*
This paper presents a method for test suite generation, which consists of automatically generating a suite of test cases, distinct from individual test generation in that it considers the coverage of the entire suite combined.

##### ii3. *Branch coverage*
Branch coverage is the fraction of branches of control flow explored by a test suite, which is one of the most important indicators of code coverage.

##### ii4. *Search operator*
The search operators are the operations used to generate new examples for the genetic algorithm. The operators used in this paper are adding and removing statements in test cases, and changing statements by modifying either numeric values or replacing compatible methods in a statement with another.

##### iii1. Hypotheses
The authors predict that considering the entire test suite instead of independently generating invidual tests will allow them to generate a suite with greater code coverage.

##### iii2. Informative Visualizations
The paper includes several visualizations of the genetic algorithm, both on the level of entire test suites and on the level of individual functions, showing how they are mutated.

##### iii3. New Results
The results of the paper show that their method is able to obtain higher code coverage with a smaller test suite than previous approaches to test generation.

##### iii4. Sampling Procedures
The authors tested their method on real projects with the goal of obtaining results that accurately reflected real-world test case generation performance, although they were restricted in the type of code they could test on in that they were forced to avoid "complex interactions with external resources (e.g., databases, networks and filesystem)".

##### iv1.
The approach was only tested on object-oriented systems, although this limitation was mentioned in the conclusions as possible future work.

##### iv2.
The authors did not do much experimentation on the parameters of the genetic algorithm.

##### iv3.
The paper does not fully analyze why the new method is able to outperform previous methods, although some guesses are given.

##### v. Connection
The paper attempts to solve the same problem as the first (automatic test case generation), although its methods differ by evolving an entire test suite as opposed to individual test cases as previously mentioned.

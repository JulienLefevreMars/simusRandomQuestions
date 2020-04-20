# simusRandomQuestions

This code aims at simulating a concrete situation that can be encountered for instance when it comes to generate a large number of exam subjects where one wants to minimize the redundancy between two subjects taken randomly. 
I am grateful to Adrien Wohrer, who suggested the "probabilistic" approach.

1. One consider:
- n students that have to pass an exam (e.g. 500)
- q questions for each subject of the exam (e.g. 20)

2. One assumes that the students are organized in clusters of g students (e.g. 10)

3. For each integer k between q+1 and q*n (situation where all the exam subjects are different)
- we generate g random exam subjects among k (random permutation of {1,2,...,q} )
- we look at the pairwise distance between two random questions (edit distance) or the average number of questions that are not shared by the group

4. The results show curves where the number of shared questions (via the mean pairwise distance and the union of pairwise interesections) decreases with k. It is then possible to estimate the numberk required if one wants an average number of shared questions. If this number is 5 (among 20), we need 70 questions (pairwise) or 500 questions (union of pairwise intersections)


[References]
Note that it is a very crude investigation of a more general combinatoric problem that is related to the "Dobble" game:
https://en.wikipedia.org/wiki/Dobble
http://www.petercollingridge.co.uk/blog/mathematics-toys-and-games/dobble/
https://images.math.cnrs.fr/Dobble-et-la-geometrie-finie.html?lang=fr

In the "Dobble" situation, the number of shared questions would be 1 for any pair of examn subjects considered.

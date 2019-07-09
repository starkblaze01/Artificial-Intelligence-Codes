# Problem Statement:

Suppose Marvin the Martian obtains a large body of English text, such as the “BrownCorpus,” which has about 1,000,000 words. Marvin, who has a working knowledge of HMMs, but no knowledge of English, would like to determine some basic properties of this mysterious writing system. A reasonable question he might ask is whether the characters can be partitioned into sets so that each set is “different” in a statistically significant way. Marvin might consider attempting the following: <br/>
First, remove all punctuation, numbers, etc., and convert all letters to lower case. This leaves 26 distinct letters and word space, for a total of 27 symbols. He could then test the hypothesis that there is an underlying Markov process (of order one) with two states. For each of these two hidden states, he assumes that the 27 symbols are observed according to fixed probability distributions.

Consider 1st 50000 observation from BrownCorpus file to estimate the model.
Estimate state transition probability and observation probability matrix. and try to analyze the hidden states. 

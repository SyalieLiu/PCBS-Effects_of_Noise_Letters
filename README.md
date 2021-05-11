EXPERIMENT

This is a simple decision experiment inspired by the article "Effects of Noise Letters upon the identification of a target letter in a nonsearch task", Eriksen & Eriksen (1974). 

The study aims at understanding the effect of noise on target identification but with a baseline condition : assessing the effect of noise on speed and accuracy in target identification when no visual search is required. By having a nonsearch task where a letter always appears in the same known location, researchers want to eliminate confounders variables due to the fact that search task involves, by definition, processing noise in order to identify the target.

At each trial, a letter is presented at the center of the screen. Participant must press the key 'l' (left) if the letter is H or K, 'r' (right) if it is S and C. Participant must only respond to the letter presented at the center and ignore any other letter. Reaction time of participants is recorded. 

There are 6 blocks in total : 

Block 1: no noise
Block 2: the noise is the same than the target letter
Block 3: the noise is the other letter in the same group as the target letter
Block 4: the noise is one of the two letters (randomly chosen) of the other group than the target letter
Block 5: the noise is the three (randomly sorted) other letters of the same category
Block 6: the noise is the three (randomly sorted) other letters of the other category

In each block, the target letter is at the center of the screen, and noise letters around the target letter.

At each trial, the key pressed by the user and the reaction time are saved in a data file. 

CODE 

noiseletters.py contains the code to run the experiment using expyriment. 

To simplify the explanation, I introduce a new terminology:
- the two "groups" means ["H", "K"] or ["S", "C"]
- the two "category" means ['H', 'K', 'N', 'W', 'Z'] or ['S', 'C', G', 'J', 'Q']
The two categories are meant to be samples of, respectively, "angular" letters and curved" letters, that have been highlighted by psychologists (Eriksen & Eriksen, 1974.

Precision: the number of trials per block has been lowered, for testing reasons. For a normal experiment, it should be 4 times bigger to have 32 trials in total. That is to say, the line:
	TARGETS = ["H", "K", "S", "C"] * 2
should be
	TARGETS = ["H", "K", "S", "C"] * 8.

PREVIOUS CODING EXPERIENCE & PCBS

I had no coding experience on python before. In my internship I use R, but I have never used R for running experiments (only to do statistics on data). I found this course interesting to learn the basics of python and run an experiment, although I find it a bit confusing to juggle between different languages. 



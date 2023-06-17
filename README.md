<h1 align="center">Myelin EEG Data Classification Pipeline</h1>
<h2 align="center"><em>Detecting Anger Using EEG Waves</em></h2>


# Overview
Our goal was to utilize EEG headsets provided by Mentalab to create a classifier for emotion. Over the course of two months, we were able to develop a support vector machine classifier and a multilayer perceptron classifer that can detect anger using EEG waves at 94.7% accuracy.

## Team:
<b>Ilia Popov</b> - Project Lead\
<b>Sofia Andrikou</b> - Classification Pipeline Developer\
<b>Aman Brar</b> - Data Architect\
<b>Alex de la Iglesia</b> - Researcher 

<img src="https://github.com/MyelinGroup/myelin-fuzzy-logic/blob/main/Images/Using_EEG_Headset.jpg?raw=true" alt="Someone putting an EEG headset on someone else" width="200"/>

## Our Purpose

The overarching idea of our project is to understand human emotions using EEG signals, which are the easiest to collect due to the fact that they're non-invasive. We want to do this in order to both better understand human psychology and, in the future, detect undiagnosed mental illnesses (eventually to prevent psychosis episodes). Due to the fact that human emotions are formed by complicated neuron interactions, which are extremely hard to detect due to their weak nature (M. Esslen, 2004), the scientific community has only recently made significant progress in classifying them (S. Bagherzadeh, 2019).
## Initial Findings
Initially, we started the project with the idea of using a fuzzy logic classifier for a wide range of emotions, thinking that collecting data would be straightforward. However, as it turned out, no paper used a method that had robust emotion-inducing results. The best one used a GAPED dataset of images (GAPED, 2011), which provided us with 730 images, which were supposed to induce a wide range of emotions on the arousal-valence scale. However, as it turned out most of the images were inducing emotions lying on the so-called “anger-boredom” line (Athavipach, 2019), which combined with our experience of testing for emotions suggested that making people angry or bored is much easier than inducing any other emotion. So, instead of trying to somehow induce happiness and sadness, we stuck with only one emotion: anger.

<img src="https://github.com/MyelinGroup/myelin-fuzzy-logic/blob/main/Images/Valence_Arousal_Chart.jpg?raw=true" alt="Valence and Arousal chart of emotions " width="300"/>

## Procedure
After having discussions with CEO of Curia, Alex Milenkovic, who worked with professional E-sports teams on collecting EEG data, we came to the conclusion that we should use a video game in order to create an emotion for several reasons:
* Games provide a continuous emotional response rather than burst when shown stimuli (pictures in our case), which could be easily misrepresented as noise
* Players are invested in the game, so their emotional reaction is much stronger than that of any other stimuli
* Games are consistent for repeatable trials

That's when we had the idea of developing an "[Astrobird](https://codesandbox.io/s/flappy-bird-forked-h2h00z)" game, which is a customized version of the infamous game “Flappy Bird”, notoriously known for inducing rage in its players.

To collect our data we used Mentalab's Explore EEG recording headset and software. A player wearing the headset would get into a relaxed state and then begin to play the "Astrobird" game for five minutes. To encourage the player's investment in the game we decided to instill stakes so that if they fail to reach a score of 15 they would have to face some sort of punishment. We recorded 15 five-minute trials of a player's EEG waves while they were playing the game. 

<img src="https://github.com/MyelinGroup/myelin-fuzzy-logic/blob/main/Images/Astrobird.png?raw=true" alt="Astrobird Get Ready screen" width="200"/>

## Analysis and Results
Using the data we collected we analyzed neutral events, 4-second blocks of time during the game, to see how they compared to end events, 4-second blocks of time around when the player would lose a game. After filtering and processing our data we trained seven types of classifiers to see which would perform the best: SVM, Random Forest, Gradient Boosting, KNN, Naïve Bayes, Logistic Regression, and MLP. In the end, our SVM and MLP classifiers would yield the best accuracy with a 94.7% success rate in detecting anger based on a user's EEG waves.

<sub> Here is a look at a singular end event and a singular neutral event.</sub>
<img src="https://github.com/MyelinGroup/myelin-fuzzy-logic/blob/main/Images/Event_Recordings.png?raw=true" alt="Charts showing EEG recording for a neutral event vs. an end event" width="600"/>

<sub> Here are the accuracies of our different classifiers and the confusion matrices to go along with them.</sub>
<img src="https://github.com/MyelinGroup/myelin-fuzzy-logic/blob/main/Images/Results.png?raw=true" alt="Classifier accurcies and confusion matrices" width="600"/>

## Conclusion
While our research was not as extravagant as we initially planned, this experience not only taught us a lot about the challenges researchers face in inducing emotion, but also demonstrates the capabilities of using EEG waves for emotion detection. This baseline research sets us up for further pursuance in the future as we will be better equipped to determine the mental state a person is in (volatile, indifferent). This research could be built upon to create technology that can detect the presence/absence of an undiagnosed mental condition, such as ADHD or depression.

<sub align="center">This project was completed as a part of the Myelin Hacker House, beginning in April 2023 and concluding in June 2023, and was supported by the 1517 Fund, the Mercatus Center, and Mentalab.</sub>

---
## References:
 Athavipach, C.; Pan-ngum, S.; Israsena, P. A Wearable In-Ear EEG Device for Emotion Monitoring. Sensors 19, (2019),. https://doi.org/10.3390/s19184014 

Bagherzadeh, S., Maghooli, K., Farhadi, J. et al. Emotion Recognition from Physiological Signals Using Parallel Stacked Autoencoders. Neurophysiology 50, 428–435 (2018). https://doi.org/10.1007/s11062-019-09775-y

Dan-Glauser, E.S., Scherer, K.R. The Geneva affective picture database (GAPED): a new 730-picture database focusing on valence and normative significance. Behav Res 43, 468–477 (2011). https://doi.org/10.3758/s13428-011-0064-1

M Esslen, R.D Pascual-Marqui, D Hell, K Kochi, D Lehmann, Brain areas and time course of emotional processing, NeuroImage 21, Issue 4, 1189-1203 (2004), https://doi.org/10.1016/j.neuroimage.2003.10.001 

Md. Mustafizur Rahman, Ajay Krishno Sarkar, Md. Amzad Hossain, Md. Selim Hossain, Md. Rabiul Islam, Md. Biplob Hossain, Julian M.W. Quinn, Mohammad Ali Moni, Recognition of human emotions using EEG signals: A review, Computers in Biology and Medicine 136, 104696, (2021). https://doi.org/10.1016/j.compbiomed.2021.104696 

Xiao-Wei Wang, Dan Nie, Bao-Liang Lu, Emotional state classification from EEG data using machine learning approach, Neurocomputing 129, 94-106, (2014). https://doi.org/10.1016/j.neucom.2013.06.046 


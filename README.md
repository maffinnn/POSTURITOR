# POSTURITOR
contributor: @tangyiqwan, @livelycloud, @xinhui

## Inspiration
In recent years, more people start to work and study online using computers and tablets. This is not only the safest option during COVID-19 pandemic, but often the more viable and flexible arrangement for people working and studying abroad. However, during long hours of computer usage, unhealthy sitting posture leads to all kinds of discomfort, even the development of diseases. Thus we feel that a solution to unhealthy postures would be relevant in the age of technology and pandemic.

## What it does
Our Posturitor is a AI-based application that reminds the user to maintain a healthy sitting posture while they are working with a computer.

On the main page, a user can start by calibrating their own healthy and upright sitting position in front of a device.
Images will be taken using the webcam and passed into a machine learning model. A pop-up notification will appear if the user is having a bad posture such as slouching forward, backward, or having an unbalanced shoulder. This will help users maintain good sitting posture throughout the day without wearing any extra devices.
Compliments will also be given to the user for maintaining a good posture.
How we built it

## Posturitor is developed using an AI solution.
We created a novel dataset based on real-life scenarios. For each set of photos, we have one reference photo and a number of healthy postures, and unhealthy postures labeled with "slouch forward", "slouch backward" and "unbalanced shoulders".
13 landmarks were extracted for the upper body using Mediapipe pose, on top of that, features like Eye & shoulder alignment and Displacement from standard posture are analysed
We then built a deep neural network model to Identify 3 different types of incorrect postures
Then we built a web application incorporating our model to achieve its functions

## Challenges we ran into
As there is no readily available dataset out there, we created our own novel dataset based on real-life scenarios. This leads to a limited data size. However, we believe that scaling of the dataset is achievable if we can collect data from our users with their approval.
We face some difficulty in incorporating our model in web app as they are written in two different programming languages.
Due to covid-19, many people are wearing their masks when using computers. However, we observe that MediaPipe Pose cannot extract landmarks efficiently if a person wears a mask. This rendered a small proportion of our dataset ineffective as landmarks cannot be extracted.

## Accomplishments that we're proud of
With limited time and resources, we managed to brainstorm ideas, collect data, build a model and web application to solve a real-life problem using the power of AI.
Our model achieved high accuracy and recall rate, especially for detecting slouching forward (accuracy: 94.1%, recall: 87.5%) and backward (accuracy: 94.1%, recall: 88.5%). When users sit with an unhealthy posture, Posturitor would be able to detect and send reminders to our users.

## What we learned
From the idea pitching workshop, we have to understand the perspectives of investors and judges, and have a rough of how to craft our pitch to convince them. We have learned the importance of data preprocessing in the development of AI solutions. Data cleaning and feature extraction are essential.

## What's next for Posturitor
We would like to develop applications for different devices such as phones and tablets.
We would like to add more customized features.
We would like to build and train our own model to extract upper body landmarks more effectively when users are wearing masks.



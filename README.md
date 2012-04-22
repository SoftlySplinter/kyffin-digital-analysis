#Aberystwyth Disseratation 2012-13

Current state of the Major Project.

##Current Ideas:
* OSGi Concurrency, Memory and Security Management.
* Multiple-language OSGi framework (Java & C++).
* Gesture Magnitude Recognition
* Gaming Agents (minecraft or similar).


###OSGi Concurrency, Memory and Security Management
Suggested by Mark Richards.

First part is to have a thread manager (OSGi already has a Thread Pool Manager). Bundles are then able to specify that they need their own thread pools (for example Java EE frameworks have a set threadpool they can use) or can blacklist themselves, limiting the number of threads they can access.


###Multiple-language OSGi framework
Suggested by Mark Richards.

OSGi is growing and there are similar frameworks starting to exist for C++. However there is no current bridge between the two.

Potential problems: Very complex. Probably a PhD topic.


###Gesture Magnitude Recognition
Suggested by myself/Melanie Hopper.

Gesture recognition is now fairly well researched now-a-days. One thing that has been considered in a side-project is the idea of recognising the strength of a guesture. Sounds pretty interesting.

Potential problems: Confidentiality.


###Gaming Agents
Suggested by Craig Lomax.

Creating agents which would be able to play a game (e.g. Minecraft) intelligently.
#Aberystwyth Disseratation 2012-13

Current state of the Major Project.

##Current Ideas:
* OSGi Concurrency, Memory and Security Management.
* Multiple-language OSGi framework (Java & C++).
* Gesture Magnitude Recognition
* Gaming Agents (minecraft or similar).
* Laser-targeted testing.
* Android: Location and motion based automation.


###OSGi Concurrency, Memory and Security Management
Suggested by Mark Richards.

Concurrecny Management will involve having a thread manager (OSGi already has a Thread Pool Manager). Bundles are then able to specify that they need their own thread pools (for example Java EE frameworks have a set threadpool they can use) or can blacklist themselves, limiting the number of threads they can access.

Memory Management will work in tandem to the JVM's arguments. Mark suggested it being a varaible/method option if possible. If not class-, component- or finally bundle- level.

Security revolves around looking at the current Java security and improving it for OSGi.

Potential Problems: Could end up needing to re-write a whole OSGi framework.

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

Potential problems: Goal functions. Interfacing with the game. Graphics processing. Real-time processing.


###Laser-targeted testing
Suggested by Mark Woolley.

Specifically for z/OS.

Potential problems: IBM Patents/Confidentiality.


###Android: Location and motion based automation
Suggested by myself.

Use Android to automate home systems based on location and motion sensors.

Potential problems: testing Android motion.



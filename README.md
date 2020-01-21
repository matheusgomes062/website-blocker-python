# website-blocker-python
A website blocker made with python. The autonomous way to be productive!

To use the app you need to follow the following steps:

Selecting time and websites:

1. Open the website_block.pyw.
2. Change the line of code that says about the websites and the hours.
3. Press Ctrl + S to save it.

Setting up the program to run as a background process:

1. Open Task Scheduler. If you don't know how to open it, just search in the windows search bar for 'Task' and it will showup as one of the sugestions.
2. Click in Create Basic Task. It's in the right corner.
3. Name it Website Blocker (so you can't forget it).
4. Configure for you Windows versioin.
5. Select "Run with highest privileges".
6. Go to the section Triggers on the same window, and select "Begin the task: "At startup"".
7. Go to the section Actions and select Start a Program and select the website_blocker.pyw from files.
8. Go to the section Conditions and deselect "Start the task only if the computer is on AC power".
Good to go!

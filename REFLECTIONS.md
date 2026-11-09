# Reflections

1. Share one aspect of building this project you found challenging and how you
   overcame it.

One aspect that I found challenging while building my project was having different modules instead of just 1 and finding out which functions should be imported to which module. After doing this, it ended up looking so much more organized to separate the whole code into separate files and use the import feature into main. Using this helped me learn that the import feature can be used this way to connect different files in my project, I have only used import to access the standard library for random in my experience so far with coding. This project not having a lot of functions was a good starter for myself to deepen my understanding of how to separate functions in different files knowing that in the future we may be working with projects that require so much more functions. One thing I did to better my understanding was draw out a mental model of boxes with the file names and connected them with lines to get a clear picture of which functions will be needed in which files. This helped deepen my understanding and it is something I look forward to doing in future projects.  

2. Share one technical concept that you gained a deeper understanding of
   through building this project. Explain that concept in simple terms and
   explain how it is used in your project.

One technical concept I understand better after using it in my project is try and except. When I ran my code and clicked to view stats immediately without starting a round, an error appeared, so I decided to add a try and except statement. This was really helpful in my stats functions in my code because a ZeroDivisionError occurs when calculating the win percentage with no games played yet. Try and except lets your code keep running: instead of an error breaking the program in the terminal, the except part allows Python to catch that specific error and display a message instead. In my example I used except ZeroDivisionError: because it’s the only error I have encountered so far while coding, though leaving it as just except: would catch any possible error. Being specific with except ZeroDivisionError: also helped me clearly explain to my audience which error I encountered and how I solved the issue.

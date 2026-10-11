# PawPal+ Project Reflection

## 1. System Design

Manage Pet Profiles: Allow the users to create and update pet information
Customize Pet Care Task: Allow users to set task with specific preferences and priorities 
Generate a Personalized Daily Plan: Allows users to create and view schedule that explains why certain task were prioritized based on avaibility. 

**a. Initial design**

1. The initial UML diagram took four classes: Owner, Pet, Scheduler, and Task. The Owner has pets, the Pet has tasks that need to be completed, and the Scheduler organizes those tasks.

2. The responsibilities for each class are that the Task class stores tasks based on their duration and priority. The Scheduler takes those tasks and uses them to generate a schedule based on the owner's availability, as well as explain the tasks. The Pet class stores the pet's name and species, and the Owner class manages the pets and makes updates to their information and preferences.
- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

**b. Design changes**

Yes I did make a change after reviewing my initial design with AI, I added the available_minutes attribute to the Owner class. The reason I made this change is because in the original design it did not consider how much time the owner had available when organizing tasks. So by adding this attribute it will now allow the Scheduler to use the owner's available time when creating a daily schedule.
- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

1. The Constraints my scheduler considers is the amount of time the owner has available as well as task duration, priority, and due dates. Making the highest priority task highest priority while still making the task fit the availible time. 
2. I decided that the task priority mattered the most because the whole point of putting priority order on task is to complete them first or get them done as fast as possible. So to me it made most sense to make this the emphasis seeing how this was a major reason for the schedule in the first place 
**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

1. One tradeoff my scheduler makes is that it only detects a conflict when they have the same date and start time it doesn't check if two things with different times will overlap 
2. I thinks its reasonable because it keeps the app simple while still being able to function properly. As it's still able to identify basic scheduling conflicts without the need for a complicated algorithm. 
---

## 3. AI Collaboration

**a. How you used AI**

1. I used the co-pilot thoughout the project in order to help design classes, debugging issues, implementing the scheduler and creating test. It also helped with updating the UML diagram and improving the streamlit interface allowing me to focus more on how the system should work and using it to help me implement that. 

2. The most helpful prompts were the ones where I gave co pilot very specific and detailed instructions about what it needed to do and not do. This helped because I wouldn't have to worry about it pushing certain changes to git hub or making changes to code unless it asked if it could do so. 

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

1. One moment I did not accept the AI suggestion as is was when the co-pilot was trying to change the class structure I had already implemented but, I wanted to keep the existing structure and make the new features work with what I have. 

2. I verified the AI suggestion by using automated test as well as making sure the implementation actually matched what the assingment was asking for instead of just trusting it blindly. 

3. Seperate chat sessions helped me stay organize because each chat focused on a specifci part of the assignment so it was easy to seperate the different parts and make sure co pilot didn't get mixed up with instructions or anything .

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

1. The behaviors I tested were the main scheduler features which included creating pets and task, detecting scheduling conflicts, and other features. I also made sure to test different edge cases to test the scheduler and mad sure it can handle different situations effectively. 

2. These test are important because it made sure the scheduler worked properly under various conditions. It also makes sure the changes that were made by co pilot not only worked but didn't disrupt the existing functionality. 

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

1. I woudl rate my confidence 4 out 5 stars because all 19 of my test passed and my streamlit application opened succesfully the reason it's not a 5 out of 5 however is because I know you can't cover every possible scenario with the test. 

2. The egdge cases I would add would be situations where several pets have tasked that are scheduled at the same time as well as how recurring task would cross over into a follwoing month or year and how it would hadle a large number and pets and task. 
---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

1. I am most satisfied with how the scheduler went from a simple class design into a into a working app using streamlit. Also being able to do task like filtering, sorting and dectecting conflicts making it a usable app and not just basic functions. 

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

2. If I had another iteration I would improve the user interface to making the scheduling system more more flexible. I would also consider adding notification for upcoming task and allow them to edit existing task more useful. 
**c. Key takeaway**

3. One important thing I learned is that you can't blindly accept the changes proposed to by the AI you have to check and verify even after the changes are made. Espiecally as an lead architect I still need to make decisions about the system design review the code and make sure everything is working properly. 

- What is one important thing you learned about designing systems or working with AI on this project?

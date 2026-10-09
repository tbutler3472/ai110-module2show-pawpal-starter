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
Yes, after reviewing my initial design with AI, I added the available_minutes attribute to the Owner class. The reason I made this change is because in the original design it did not consider how much time the owner had available when organizing tasks. So by adding this attribute it will now allow the Scheduler to use the owner's available time when creating a daily schedule.
- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

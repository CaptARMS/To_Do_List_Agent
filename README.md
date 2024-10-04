# To_Do_List_Agent

04-10-2024 19:08
-Created the main.py file 
-Created two classes: Task and TaskManager
-Added a buffer function LLMs() to make the choice
-Added Simulate_agent to carry the operation of the agent
-Added code for outputing each operation in Log file 

04-10-2024 19:45
-Created a dummy file LLM.py to test the groq API LLM model

04-10-2024 20:45
-Removed the API key which was uploaded on git by mistake

04-10-2024 21:51
-Created generalized prompts for all 3 cases asked to LLM
-Added system information to the LLM
-Modified the simulate_agent function in main.py to ask LLM to choose random task 
-Modified the simulate_agent function to ask LLM to give name and deadline of the task
-Stripped the deadline of error strings to fit it in proper format
-task_log.txt file is created that keeps the log of all the task executed with time and information

04-10-2024 22:20
-Added current date in the prompt for deadlines
-Initialize the list to have n task added at the start

04-10-2024 22
-Added user profession in the content of LLM to increase the relevancy of task suggestion
-Modified LLM.py function so that the deadline is suggested based on the average time to complete the suggested task
-Modifited the LLM.py to consider the current state of the to-do list while suggesting tasks
-Modified the LLM.py to avoid redundant addition and erroneous edits
# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Student Management System With Python

![gif](https://media.giphy.com/media/IqFH0yMll9wl2/giphy.gif)

| Language | Type          | Start date  | Due date | Author     |
| -------- | ------------- | ----- | ---- | -------------------- |
| Python   | Project 1 | 12/03/2020 | 12/10/2020 | Suresh Melvin Sigera |

## Prompt

ACME is a student management system which utilizes the following dictionary structure.

```python
data = {
	10001:
		{
			'first_name': 'Chris',
			'last_name': 'Herzog',
			'email': 'chriher22@aol.com',
			'classes_taken': ('CSC126', 'CSC211', 'CSC326'),
			'grades_received': ('A', 'C', 'F'),
			'type': 'student'
		},
	10002:
		{
			'first_name': 'Joseph',
			'last_name': 'Smith',
			'email': 'JosephSSmith@rhyta.com',
			'classes_taken': ('CSC456', 'CSC121', 'ENG151'),
			'grades_received': ('A', 'C', 'A'),
			'type': 'student'
		},
 
 ...

	10007:
		{
			'first_name': 'Ann',
			'last_name': 'Chatman',
			'email': 'AnnBChatman@ms.edu',
			'password': 'J&hqweh12e7d2n28qq1',
			'type': 'staff'
		},
}
```

## Student structure

| account_id | first_name | last_name | email | classes_taken | grades_received| type | 
| -------- | ------------- | ----- | ---- | ---------- |---------- |---------- |
| 10001 | Chris | Herzog | chriher22@aol.com | ('CSC126', 'CSC211', 'CSC326') | ('A', 'C', 'F') | student
| 10002 | Joseph | Smith | JosephSSmith@rhyta.com | ('CSC456', 'CSC121', 'ENG151') | ('A', 'C', 'A') | student
| ... | ... | ... | ... | ... | ... | ... |

## Staff structure

| account_id | first_name | last_name | email | password | type | 
| -------- | ------------- | ----- | ---- | ---------- |---------- |
| 10007 | Ann | Chatman | AnnBChatman@ms.edu | J&hqweh12e7d2n28qq1 | staff
| ... | ... | ... | ... | ... | ... |

Given the above dictionary structure for the ACME system, write the entire Python program using functions to meet the functional requirements below. (Starter code is provided in `main.py` in this repository.)

## Requirements:

You should have **a minimum of** 6 functions.

### Your app should have the following functionality:
As an administrator (an account with type `"staff"`) the user must be able to `login` to the system using the `account_id`, `email` and `password` to perform the following tasks.

1. Add a new student
2. List all students
3. Search students
4. Remove a student
5. Display single student record
     * first name
     * last name
     * email
     * course and letter grade received
     * GPA

## Get started!
![gif](https://media.giphy.com/media/9P56GiCDX2sGBZToJS/giphy.gif)


## Additional resources:
- [Pretty-print tabular data in Python, a library and a command-line utility](https://pypi.org/project/tabulate/)
- [Command line colors](https://pypi.org/project/termcolor/)
- [Command line menu](https://pypi.org/project/simple-term-menu/)

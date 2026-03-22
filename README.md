# Python learning journey
i will be learning from scratch untill i reach the advanced level.
Day 1: Variables and data Types;
# Task: Build a Simple User Profile Script
Requirements
1. Create Variables

Define the following:

name → string
age → integer
height → float (in meters)
is_student → boolean
nickname → None
2. Print a Profile Summary

Output something like:

Name: Ethan
Age: 20
Height: 1.75m
Student: True
Nickname: None

#  Task 2: Student Eligibility System

You’re going to build a small decision system—the kind used in real applications.

##  Objective

Create a file:

```bash
student_eligibility.py
```

---

# 📌 Requirements

## 1. Collect Input

Ask the user for:

* `name` → string
* `age` → integer
* `grade` → float (0–100)
* `is_registered` → yes/no → convert to boolean

---

## 2. Decision Logic (This is the core)

### Rule 1:

If NOT registered:

```text
"Access Denied: Not registered"
```

---

### Rule 2:

If registered AND age < 16:

```text
"Access Denied: Too young"
```

---

### Rule 3:

If registered AND age >= 16:

Now check grade:

* grade ≥ 75 → `"Eligible for Advanced Program"`
* grade ≥ 50 → `"Eligible for Standard Program"`
* grade < 50 → `"Not eligible - Improve your grade"`

---

## 3. Output Clean Result

Example:

```text
Name: Ethan
Status: Eligible for Advanced Program
```

---

# ⚠️ Important Constraints

* You MUST use:

  * `if`, `elif`, `else`
  * Boolean logic
* Do NOT hardcode values
* Do NOT skip input conversion

---

# 🧱 Expected Structure

```python
# inputs

# process boolean

# main decision logic

# final output
```

#  Bonus (Do This If You’re Serious)

Add input validation:

* If grade > 100 → print error
* If grade < 0 → print error

#  Why This Matters

This is no longer just variables.

You are now learning:

* Decision trees
* Control flow
* Real-world logic

This is the backbone of:

* Login systems
* Payment approvals
* Access control

# DAY 2: LOOPS

# Task 3: Create A Menu Driven User Eligibilty System.
Your challenge is:

👉 Turn this into a menu-driven system

Where user sees:

1. Check Eligibility
2. Exit

And the program loops until they exit.
You have Already Learnt how to handle; 
* Control Flow 
* The if elif else statements now you just have to understand looping.
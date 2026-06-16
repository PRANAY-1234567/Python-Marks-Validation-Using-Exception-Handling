# Python Marks Validation Using Exception Handling

## 📌 Overview

This project demonstrates how to use **exception handling** and the **raise statement** in Python to validate user input.

The program accepts marks from the user and verifies whether they fall within the valid range of **0 to 100**. If the entered marks are outside this range, an exception is raised and an appropriate error message is displayed.

This project is useful for learning input validation and custom error generation in Python.

---

## 🚀 Features

* Accepts marks from the user
* Validates marks range (0–100)
* Uses the `raise` statement
* Handles exceptions gracefully
* Prevents invalid data entry
* Beginner-friendly implementation

---

## 🛠️ Technologies Used

* Python 3

---

## 📂 Project Structure

```text
├── marks_validation.py
├── README.md
```

---

## 💻 Source Code

```python
try:
    marks = int(input("Enter the marks (0-100) : "))

    if marks < 0 or marks > 100:
        raise Exception("Invalid marks")

    print("Valid marks entered")

except Exception as e:
    print("Error :", e)
```

---

## ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/your-username/python-marks-validation.git
cd python-marks-validation
```

### Run the Program

```bash
python marks_validation.py
```

---

## 📋 Sample Outputs

### Valid Input

```text
Enter the marks (0-100) : 85
Valid marks entered
```

### Marks Greater Than 100

```text
Enter the marks (0-100) : 120
Error : Invalid marks
```

### Negative Marks

```text
Enter the marks (0-100) : -10
Error : Invalid marks
```

### Invalid Input

```text
Enter the marks (0-100) : abc
Error : invalid literal for int() with base 10: 'abc'
```

---

## 🧠 Concepts Covered

* Exception Handling
* Input Validation
* `try-except` Blocks
* `raise` Statement
* User Input Processing
* Error Handling

---

## 🔍 How It Works

### Step 1: Accept User Input

```python
marks = int(input("Enter the marks (0-100) : "))
```

The program reads marks from the user.

---

### Step 2: Validate Range

```python
if marks < 0 or marks > 100:
```

Checks whether the marks are outside the valid range.

---

### Step 3: Raise Exception

```python
raise Exception("Invalid marks")
```

Generates an exception when invalid marks are entered.

---

### Step 4: Handle Exception

```python
except Exception as e:
```

Catches the exception and displays the error message.

---

## 🎯 Learning Objectives

By completing this project, you will learn:

* How to validate user input
* How to generate exceptions using `raise`
* How to handle runtime errors
* Best practices for data validation
* How exception handling improves program reliability

---

## 📚 Real-World Applications

This concept is commonly used in:

* Student Management Systems
* Online Examination Portals
* School and College Applications
* Data Entry Systems
* Form Validation Software

---

## 🔮 Future Improvements

* Create a custom `InvalidMarksException`
* Validate marks for multiple students
* Calculate grades automatically
* Store records in a file or database
* Develop a GUI version using Tkinter

---

## 👨‍💻 Author

**Pranay Jadhao**

Electronics & Telecommunication Engineer

Aspiring Software & Embedded Systems Engineer

LinkedIn: [www.linkedin.com/in/pranayjadhao](http://www.linkedin.com/in/pranayjadhao)

GitHub: https://github.com/

---

## 📄 License

This project is open-source and available for educational and learning purposes.

<img width="639" height="584" alt="image" src="https://github.com/user-attachments/assets/28186ca6-70a4-45a0-8728-ff1f71c70e0e" />

# Use pre-existing components (ICTPRG439)
## Changes in this fork

### Components added

| Library | Issue | Purpose |
|---|---|---|
| `python-dateutil` | #1 | Reads dates like `01-12-2030`, `1/12/2030`, `1 Dec 2030` and stores them as `DD-MM-YYYY` |

### How to run and test

```bash
pip install -r requirements-dev.txt
python main.py
python -m unittest discover
```
---

## **Overview**

This activity requires you to:

- Investigate and incorporate reusable components into an existing application.
- Debug and improve the provided **Task Management CLI App**.
- Use **GitHub Issues** for tracking bugs and improvements.
- Write unit tests to verify issues and fixes.
- Open and update **Pull Requests (PRs)**.
- Update and maintain project documentation.
- Demonstrate effective use of Git and GitHub workflows.

---

## **Workflow**

---

### 1. Familiarise Yourself with the Project

1. **Clone the repository**:

```bash
git clone <repository-url>
cd pin_civ_assessment_ipos_portfolio_2
```

2. Use the Virtual Environment

NOTE: **activate a virtual environment** in Python, the command varies depending on your **operating system** and the **shell/terminal** you are using. Here's a clear step-by-step guide:

---

### 2. Create a Virtual Environment

Before activating, you must create the virtual environment in your project folder:

```bash
python -m venv .venv
```

`.venv` is the directory name for the virtual environment (you can name it whatever you want).

---

1. **Activate the environment**

**For Windows**:

```cmd
.venv\Scripts\activate
```

```powershell
.\.venv\Scripts\Activate
```

**For Mac/Linux & Gitbash**

In a **Bash** or **Zsh** terminal, run:

```bash
source .venv/bin/activate  #Mac/Linux
source .venv/Scripts/activate #Windows Gitbash
```

**Use the pyproject.toml files to manager the environment & add the scripts to run the app**

```bash
python -m pip install -e .
```

---

2. **To update project dependences dependencies**:

```bash
pip install -r requirements-dev.txt #(may require python -m)
```

3. **Run the application**:

```bash
python main.py #(may require python -m)
```

Explore the current functionality. Try adding, deleting, and listing tasks.

4. **Read the Documentation**:
   - Review the `onboarding.md` file for project setup and guidelines.
   - Examine the current `README.md` and inline comments for existing functionality.

---

### 2. Debugging and Identifying Enhancement Issues

Use debugging tools (e.g., breakpoints, print statements, IDE tools) to identify **two issues** or areas where reusable components can improve the app.

## **Examples of Suggested Components for Application Enhancement**

1. **`click`** – Improve CLI usability and interactivity.
2. **`python-dateutil`** – Ensure robust date validation.
3. **`rich`** – Format task outputs with tables and colors.
4. **`colorama`** – Add terminal colors for task statuses.
5. **`tabulate`** – Format task lists as clean tables.
6. **`SQLAlchemy`** – Use SQLite for structured, scalable storage.
7. **`loguru`** – Add detailed logging for debugging.
8. **`mock`** – Mock file handling and inputs for testing.
9. **`schedule`** – Automate task reminders for due dates.

---

## **Example of Component Use**

1. **User-Friendly CLI**:  
   Combine `click` for CLI commands and `rich` to display tasks as tables with colorful statuses.
2. **Database-Driven Storage**:  
   Replace file-based storage with `SQLAlchemy` to allow structured task management and easy queries.
3. **Robust Testing**:  
   Use `mock` to test task operations without affecting actual data files.
4. **Automated Reminders**:  
   Integrate `schedule` to periodically remind users of due tasks.

---

## **Record your findings** and raise **two GitHub Issues**.

### 3. Raise 2 Issues in GitHub Issues

1. Go to the GitHub repository for this project.
2. Navigate to the **"Issues"** tab.
3. Document each bug/feature as a separate Issue with the repo template, including:
   - A clear title.
   - A description of the problem.
   - Reasoning for enhancement & component selection

---

### 4. Create Local and Remote Branches

1. **Locally**: Create a new branch for each Issue.

```bash
git checkout -b issue-<issue_number>
```

2. **Remotely**: Push the branch to GitHub.

```bash
git push -u origin issue-<issue_number>
```

---

### 5. Add and Test Reusable Components

1. **Select Components**: Research and integrate suitable Python libraries:
2. **Write Test Cases**:  
   Using mock & patch objects write unit tests for the issues you raised using the **`unittest` framework**.
   - Test invalid dates.
   - Test duplicate task prevention.
   - Test new CLI behavior (if applicable).

3. Run tests to confirm that your new test cases fail:

```bash
python -m unittest discover test
```

---

### 6. Fix the Code

1. Incrementally integrate the selected reusable components into the project.
2. Address the bugs/issues raised in your branch.
3. Rerun the tests to ensure they pass:

```bash
python -m unittest discover test
```

---

### 7. Update the Documentation

1. Add or update inline comments explaining changes.
2. Update the **README.md** to include:
   - New dependencies.
   - Instructions for running and testing the updated app.
3. Update the **`requirements-dev.txt`** file with any new libraries:

```bash
pip freeze > requirements.txt
```

---

### 8. Run your workflows locally

**Before pushing your code to GitHub, you should run flake8 locally to check for code quality issues.**

- If flake8 fails locally, your GitHub Actions workflow will also fail.
- You cannot merge without these passing.

1. Run flake8 - from the root of the project (where .flake8 is located):

```bash
python -m flake8 /src

# Optional detailed report
python -m flake8 . --statistics --show-source
```

2. What to do
   - Fix any errors shown in the output
   - Re-run flake8 until no errors remain

3. Thess come from the workflow some common issues you may see
   - Unused imports or variables
   - Line length too long
   - Functions too complex
   - Debug print() statements (not allowed)

---

### 9. Submit a Pull Request (PR)

**Note you must use the PULL and ISSUE templates provided**

1. Open a Pull Request (PR) for each Issue against the `main` branch.
2. Ensure your PR description includes:
   - A clear summary of changes.
   - The Issue number it addresses (`fixes #<issue_number>`).
   - Evidence that the new test cases pass.

3. Push any updates to the branch:

```bash
   git add .
   git commit -m "Fixed <issue_number>: Added date validation"
   git push
```

---

### 10. Seek PR Approval

#### DONT MISS THIS STEP AS YOU WILL HAVE TO REVERT IT BACK

- Request your lecturer as a reviewer on your PR.
- Address any feedback provided.

---

### 11. Close the Issue

When the PR is merged, the Issue will be automatically closed if you included "fixes #\<issue_number\>" in the PR description.

---

### 11. Complete Reflection Questions

1. Complete **KBA Testing Documentation & Reusability**
2. Reflect on the following:
   - What reusable components did you select and why?
   - How did the components improve the project?
   - What challenges did you face when debugging or integrating the components?

---

## **Assessment Criteria**

1. **Identification** of bugs/issues and selection of appropriate reusable components.
2. **Effective use of GitHub**:
   - Properly raised Issues and branches.
   - Clean, descriptive Pull Requests.
3. **Code Quality**:
   - Fixes implemented correctly.
   - Integration of reusable components.
4. **Testing**:
   - Unit tests that expose and confirm fixes.
5. **Documentation**:
   - Updated inline comments and README.md.
   - Updated `requirements-dev.txt`.
6. **PR Workflow**:
   - Demonstrated initial test failures and successful fixes.
   - Approval workflow completed.
7. **Reflection**:
   - Answered knowledge questions with thoughtful insights.

---

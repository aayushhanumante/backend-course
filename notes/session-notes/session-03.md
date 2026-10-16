# Backend Engineering Course
## Session 03: Git Fundamentals and GitHub

### 1. Git basics

- `git status` - shows working tree and staging area status.
- `git add FILE` - stages changes for the next commit.
- `git diff` - shows unstaged changes.
- `git diff --staged` - shows staged changes.
- `git commit -m "message"` - records staged changes in a commit.
- `git log --oneline` - displays compact commit history.

**Key concepts:**

- Working tree: files in the project directory.
- Staging area: changes selected for the next commit.
- Commit: a recorded snapshot of the project.
- Repository history: the sequence of commits.

### 2. The `.gitignore` file

- `.gitignore` specifies files Git should normally ignore when they are untracked.
- Common examples include `__pycache__/`, `.venv/`, and `.env`.
- `git check-ignore -v PATH` - identifies the rule matching a path.

**Important:** `.gitignore` does not automatically stop tracking files already tracked by Git.

### 3. GitHub authentication and remotes

- A remote repository is another Git repository, hosted on GitHub in this project.
- `origin` is the conventional nickname for the configured remote.
- SSH keys can authenticate your Git connection to GitHub.
- Commit author name and email are metadata, separate from SSH authentication.

**Commands:**

- `git remote -v` - displays remote URLs.
- `git push origin main` - pushes local `main` commits to remote `main`.
- `git push -u origin BRANCH` - pushes a branch and configures its upstream.
- `git branch -vv` - displays local branches and their upstream information.

### 4. Branches and `HEAD`

- A branch is a movable reference to a commit.
- `HEAD` identifies the current checkout, normally through the current branch.
- Branches allow development to be isolated from `main`.

**Commands:**

- `git branch` - lists local branches.
- `git switch main` - switches to `main`.
- `git switch -c feature-name` - creates and switches to a new branch.

### 5. Comparing changes and history

- `git diff A..B` - compares content at two endpoints.
- `git log A..B` - lists commits reachable from B but not A.
- `git log --oneline --decorate --graph --all -8` - displays a compact graph of recent commits and branch references.

**Key distinction:**

- `git diff` shows differences in content.
- `git log` shows differences in commit history.

### 6. Local branches and remote-tracking references

These are different concepts:

- `main` - your local branch.
- `origin` - the configured remote nickname.
- `origin/main` - a local reference recording the last known position of the remote's `main` branch.
- GitHub's `main` - the branch in the remote repository.

**Example:**

- Local `main` and `origin/main` point to commit A.
- Someone pushes commit B to GitHub.
- Before fetching, your local references may still point to A.
- After `git fetch origin`, `origin/main` moves to B, while local `main` remains at A.

**Commands:**

- `git fetch origin` - retrieves remote updates without automatically merging them into the current branch.
- `git branch -r` - lists remote-tracking branches.
- `git branch -vv` - displays local branches and upstream information.

### 7. `git fetch`, `git pull`, and `git push`

- `git fetch` - retrieves remote updates and updates remote-tracking references.
- `git pull` - fetches and integrates remote changes into the currently checked-out branch.
- `git push` - publishes local commits to a remote branch.

**Important:** `git pull` does not inherently update local `main`. Its target depends on the currently checked-out branch and its configuration.

### 8. Merging branches

- `git merge BRANCH_NAME` - merges the named branch into the currently checked-out branch.
- The current branch is the destination.
- The named branch is the source.

**Example:** If you are on `practice/api-validation` and run `git merge main`, Git attempts to integrate `main` into `practice/api-validation`.

**Fast-forward merge:**

- Possible when the current branch's tip is an ancestor of the branch being merged.
- Git advances the current branch reference without creating a separate merge commit.

### 9. Pull requests versus `git pull`

- A **pull request (PR)** proposes changes from one branch into another on GitHub, usually for review.
- `git pull` fetches and integrates remote changes into your current local branch.

**Typical pull request workflow:**

- Create a feature branch.
- Implement and commit changes.
- Push the branch to GitHub.
- Open a pull request.
- Address review feedback.
- Merge the pull request when requirements are satisfied.

**Remember:** A pull request is a collaboration workflow. `git pull` is a Git command.

### 10. Practical branch exercise

- Created `practice/git-branches`.
- Created `notes/git-branch-practice.md`.
- Staged the file and reviewed it using `git diff --staged`.
- Created commit `a1c7a23` with message `Branch exercise example`.
- Pushed the branch using `git push -u origin practice/git-branches`.
- Inspected upstream tracking using `git branch -vv`.
- Verified that the practice note was absent from `main` before merging.
- Merged `practice/git-branches` into `main` using a fast-forward merge.
- Pushed the updated `main` branch to GitHub.

**Result:** Immediately after the merge and push, local `main`, local `practice/git-branches`, `origin/main`, and `origin/practice/git-branches` all pointed to `a1c7a23`.

Later commits advanced `main`. The `labs/` directory remained intentionally untracked.

### 11. Key takeaways

- Stage changes before committing them.
- Use branches to isolate development.
- `origin` is a remote nickname, not the repository itself.
- `origin/main` is a local remote-tracking reference, not a live view of GitHub.
- `git fetch` retrieves updates; `git pull` fetches and integrates them.
- `git merge BRANCH_NAME` merges into the current branch.
- Pull requests support review before merging.
- `.gitignore` does not untrack files already tracked by Git.

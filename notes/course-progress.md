# Backend Engineering Course Progress Ledger

## Current Status

- Phase: Week 0, Developer Tooling
- Last completed session: Day 3, Git Fundamentals and GitHub
- Next session: Week 1, Python Environment Setup and HTTP Fundamentals
- Environment: Windows 11, WSL2 Ubuntu
- Repository: `~/projects/backend-course`
- GitHub: [https://github.com/aayushhanumante/backend-course](https://github.com/aayushhanumante/backend-course)
- Progress tracking: This ledger is the source of truth for completed work, practical evidence, blockers, and next assignments.

## Completed Sessions

### Week 0, Day 1: Linux Filesystem Basics

- Practised `whoami`, `pwd`, `ls -la`, `uname`, `cat`, and `df`.
- Learned absolute and relative paths, `/`, `~`, `.`, `..`, and `cd -`.
- Learned the relationship between the Linux filesystem and Windows drives in WSL2.
- Created the course workspace with `notes/`, `labs/`, and `experiments/`.
- Practised `touch`, `nano`, `mv`, `cp`, `rm`, and `chmod`.
- Learned basic file permissions and permission notation.
- Completed checkpoint questions on directory navigation, permissions, and file copying.
- Saved notes in `notes/session-01.md`.

### Week 0, Day 2: Linux Text Tools and Logs

- Practised `cat`, `less`, `head`, `tail`, `tail -f`, and `grep`.
- Learned how to navigate and search text using `less`.
- Practised output redirection with `>` and `>>`, including the difference between overwriting and appending.
- Created and inspected `labs/sample.log`.
- Practised monitoring log output and stopping a running command with `Ctrl+C`.
- Saved notes in `notes/session-02.md`.

### Week 0, Day 3: Git Fundamentals and GitHub

Topics completed:

- Initialized and maintained a Git repository on `main`.
- Practised staging, commits, status checks, diffs, and history inspection.
- Learned the difference between tracked, untracked, staged, and committed files.
- Created `.gitignore` rules for Python caches, virtual environments, and environment files.
- Verified ignore rules using `git check-ignore -v`.
- Generated an Ed25519 SSH key and configured GitHub SSH authentication.
- Configured the `origin` remote and pushed commits to GitHub.
- Updated commit author metadata to use GitHub's private `noreply` email.
- Learned that `HEAD` identifies the current checkout and that branches are movable references to commits.
- Learned the distinction between local branches and remote-tracking references such as `origin/main`.
- Practised comparing branch contents with `git diff` and inspecting commit history with `git log`.
- Learned that `git diff A..B` compares content at two endpoints, while `git log A..B` lists commits reachable from B but not A.
- Learned that `git push` publishes commits but does not automatically merge branches.
- Learned that `git merge BRANCH_NAME` merges the named branch into the currently checked-out branch.
- Observed a fast-forward merge and pushed the updated `main` branch.
- Discussed the differences between `git fetch`, `git pull`, and `git push`.

Practical evidence:

- Created the branch `practice/git-branches`.
- Created `notes/git-branch-practice.md` on the practice branch.
- Reviewed the staged file using `git diff --staged`.
- Created commit `a1c7a23` with message `Branch exercise example`.
- Pushed the branch using `git push -u origin practice/git-branches`.
- Verified upstream tracking with `git branch -vv`.
- Confirmed the practice note was absent from `main` before merging.
- Fast-forward merged `practice/git-branches` into `main`.
- Pushed `main` to GitHub.
- Verified that `main`, `practice/git-branches`, `origin/main`, and `origin/practice/git-branches` pointed to commit `a1c7a23`.
- Confirmed that `labs/` remained intentionally untracked.

Assessment and remaining practice:

- Demonstrated basic understanding of staging, commits, branch isolation, upstream tracking, merging, and remote synchronization.
- Explained the purpose of `fetch`, `pull`, and `push` correctly at a conceptual level.
- Hands-on execution and verification of `git fetch` remain outstanding.
- Pull requests and basic collaboration workflows remain outstanding.
- Advanced Git recovery, conflict resolution, and rebasing have not yet been assessed.

Session notes: `notes/session-03.md` was not created. The progress record is maintained here until a session note is intentionally added.

## Current Blockers and Outstanding Work

- Complete a hands-on `git fetch` exercise and inspect remote-tracking references.
- Learn the basic pull-request workflow and review how branches are used in collaboration.
- Continue Python environment setup and dependency management.
- Cover HTTP fundamentals before resuming FastAPI revision.
- Keep `labs/` intentionally untracked because its files are temporary practice examples.
- No unresolved Git authentication or remote-tracking blocker was reported at the end of Day 3.

## Next Assignment

- Complete the hands-on `git fetch` exercise and verify the effect on remote-tracking references.
- Review pull requests and basic collaboration workflows.
- Begin Week 1 with Python virtual environments and dependency management.
- Cover HTTP fundamentals, including requests, responses, methods, status codes, headers, and JSON.
- Begin FastAPI revision after the prerequisites have been assessed.
- Record practical evidence and update this ledger at the end of the next session.

## Session Tracking Rules

At the end of every session, record:

- Topics completed.
- Exercises and practical evidence.
- Tests performed and their results.
- Demonstrated understanding and remaining misconceptions.
- Blockers and unresolved questions.
- Time spent, when reported.
- Exact next assignment.

### Teaching Rules

- Teach incrementally, one exercise at a time.
- Give hints before solutions.
- Do not provide complete lab implementations unless explicitly requested.
- Review submitted code rigorously.
- Track demonstrated understanding, not just claimed completion.
- Explain unfamiliar command flags and terminology briefly.
- Do not advance past critical concepts without assessment.
- Keep temporary lab examples untracked unless explicitly required by the curriculum.
- Check this curriculum and ledger at the beginning of each session.
- Update the ledger and relevant session notes after each session.
- Do not claim a command, test, commit, push, or deployment succeeded without supporting evidence.
- Preserve the curriculum as the agreed plan; document changes rather than silently replacing requirements.

This ledger is the source of truth for course progress. The curriculum in `notes/curriculum.md` is the source of truth for course scope, sequencing, projects, and teaching requirements.

## Progress Update Template

### Session: [Week / Day / Date]

Topics completed:

\-&#x20;

Practical evidence:

\-&#x20;

Tests and results:

\-&#x20;

Assessment and weak spots:

\-&#x20;

Blockers:

\-&#x20;

Time spent:

\-&#x20;

Next assignment:

\-&#x20;
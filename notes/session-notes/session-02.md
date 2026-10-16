# Backend Engineering Course
## Session 02: Linux Text Tools and Log Inspection

### 1. Viewing files

- `cat file.txt` — prints the entire file.
- `less file.txt` — opens a file for interactive reading.
  - `Space`: next page
  - `b`: previous page
  - `/keyword`: search
  - `q`: quit
- `head -n 5 file.txt` — prints the first 5 lines.
- `tail -n 5 file.txt` — prints the last 5 lines.
- `tail -f file.txt` — displays the end of a file and follows newly appended content. Press `Ctrl+C` to stop.

### 2. Searching text

- `grep "ERROR" sample.log` — prints lines containing `ERROR`.
- If no lines match, `grep` normally prints nothing.
- `grep` is useful for finding errors or specific events in application logs.

### 3. Output redirection

- `>` redirects output to a file, replacing its existing contents.
- `>>` redirects output to a file by appending to its existing contents.

Examples:

- `echo "Hello" > file.txt` — replaces the file's contents with `Hello`.
- `echo "Hello" >> file.txt` — appends `Hello` to the file.

**Warning:** Using `>` on an existing file can erase its previous contents.

### 4. Practical debugging workflow

- `tail -n 20 sample.log` — inspect recent log entries.
- `grep "ERROR" sample.log` — find error messages.
- `tail -f sample.log` — watch for new entries while an application runs.

### 5. Key concepts

- Absolute paths start from `/`.
- `~` represents the current user's home directory.
- Relative paths are resolved from the current working directory.
- `..` refers to the parent directory.
- `/mnt/c` in WSL2 generally exposes the Windows C: drive.

### Practice evidence

- Created `sample.log` with 20 numbered entries.
- Used `head` and `tail` to select lines.
- Used `tail -f` and exited with `Ctrl+C`.
- Used `grep` to find matching log entries.
- Appended application-style log messages with `>>`.

### Status

Week 0, Day 2: Completed.

Next session: Git fundamentals and version control.

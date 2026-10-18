# Backend Engineering Course Progress Ledger

## Current Status

- Phase: Week 0–1, Developer Tooling and Ramp-up
- Current session: Day 4, Python Environment Setup and HTTP Fundamentals
- Last completed session: Day 3, Git Fundamentals and GitHub
- Current status: Day 4 in progress
- Environment: Windows 11, WSL2 Ubuntu
- Python version: 3.12.3
- Repository: `~/projects/backend-course`
- GitHub: [https://github.com/aayushhanumante/backend-course](https://github.com/aayushhanumante/backend-course?utm_source=chatgpt.com)
- Progress tracking: This ledger is the source of truth for completed work, practical evidence, blockers, and next assignments.
- Temporary practice files under `labs/` remain intentionally untracked.

## Completed Sessions

### Week 0, Day 1: Linux Filesystem Basics

Topics completed:

- Practised `whoami`, `pwd`, `ls -la`, `uname`, and `df`.
- Learned absolute and relative paths, `/`, `~`, `.`, `..`, and `cd -`.
- Learned the relationship between the Linux filesystem and Windows drives in WSL2.
- Created the course workspace with `notes/`, `labs/`, and `experiments/`.
- Practised `touch`, `nano`, `mv`, `cp`, `rm`, and `chmod`.
- Learned basic file permissions and permission notation.
- Completed checkpoint questions on directory navigation, permissions, and file copying.

Session notes: `notes/session-notes/session-01.md`

### Week 0, Day 2: Linux Text Tools and Logs

Topics completed:

- Practised `cat`, `less`, `head`, `tail`, `tail -f`, and `grep`.
- Learned to navigate and search text using `less`.
- Practised output redirection with `>` and `>>`, including overwriting versus appending.
- Created and inspected `labs/sample.log`.
- Practised monitoring log output and stopping a running command with `Ctrl+C`.

Session notes: `notes/session-notes/session-02.md`

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
- Completed a hands-on `git fetch` exercise and inspected synchronization between local and remote-tracking references.
- Confirmed that `labs/` remained intentionally untracked.

Assessment and remaining practice:

- Demonstrated basic understanding of staging, commits, branch isolation, upstream tracking, merging, and remote synchronization.
- Explained `fetch`, `pull`, and `push` conceptually.
- Pull-request collaboration workflows remain to be practised.
- Advanced Git recovery, conflict resolution, and rebasing have not yet been assessed.

Session notes: `notes/session-notes/session-03.md`

## Current Session: Week 0–1, Day 4

### Topics covered so far

#### Python environment setup

- Checked the installed Python version using `python3 --version`.
- Located the system Python interpreter using `which python3`.
- Discovered that `pip` was initially unavailable in the system Python environment.
- Learned why the `python3.12-venv` package is required to create virtual environments on this Ubuntu installation.
- Created a project-local virtual environment named `.venv`.
- Activated the environment using `source .venv/bin/activate`.
- Verified that `python` resolves to `.venv/bin/python`.
- Inspected `sys.executable`, `sys.prefix`, and `sys.base_prefix` to verify interpreter selection and environment isolation.
- Learned that `python -m pip` runs pip through the selected Python interpreter.
- Installed `httpx` inside the virtual environment.
- Inspected installed dependencies using `python -m pip list` and `python -m pip freeze`.
- Generated `requirements.txt` using `python -m pip freeze > requirements.txt`.
- Learned why developers recreate their own environments rather than copying `.venv` between machines.

#### Dependency reproducibility

Practical evidence:

- Python version: `3.12.3`.
- Virtual environment created successfully at `.venv`.
- Confirmed that the active interpreter resolves inside `.venv`.
- Installed `httpx==0.28.1`.
- Captured the installed dependency versions in `requirements.txt`.
- Created a separate temporary environment at `/tmp/backend-course-repro`.
- Installed dependencies in the temporary environment using `pip install -r requirements.txt`.
- Verified that the temporary environment reproduced the listed dependencies and could import `httpx` version `0.28.1`.

Assessment:

- Demonstrated the ability to create and activate a virtual environment.
- Demonstrated that dependency installation can be reproduced from a requirements file.
- Cross-platform compatibility, Python version constraints, and more deliberate dependency pinning remain topics for later assessment.

#### HTTP fundamentals using curl and httpx

Topics covered:

- Learned that `curl` is a command-line HTTP client and that a basic request defaults to GET.
- Used `curl -i` to inspect response headers and bodies.
- Used `curl -v` to inspect request details, response details, and connection diagnostics.
- Learned that `>` lines in verbose output represent outgoing client data and `<` lines represent incoming server data.
- Used `-H` to add request headers.
- Used `-d` to submit request data and observed the default POST behavior.
- Inspected JSON request and response bodies using httpbin endpoints.
- Learned the distinction between `Content-Type`, which describes the message body's media type, and `Accept`, which describes response media types the client can accept.
- Learned that an echoed request header appearing inside a response body does not make it a response header.
- Inspected 2xx, 4xx, and 5xx status codes, including 200, 404, and 500.
- Discussed the difference between a client-related error and a server-related error.
- Inspected URL paths and query parameters.
- Learned that query parameter values received through JSON may be represented as strings.
- Used `httpx.get()` with `params` to construct a query string programmatically.
- Learned that `response.json()` parses a JSON response body into Python objects.

Practical evidence:

- Successfully requested `https://httpbin.org/get`.
- Inspected outgoing requests and incoming responses using verbose curl output.
- Sent a custom `X-Course-Test` header and observed it in the echoed JSON response.
- Submitted JSON data to the httpbin POST endpoint and inspected the parsed result.
- Requested endpoints returning 404 and 500 status codes.
- Sent `Accept: application/json`.
- Tested query parameters using curl and httpx.

Assessment:

- Demonstrated a basic ability to inspect HTTP requests, headers, response bodies, methods, status codes, and query parameters.
- Still need to demonstrate a deeper understanding of request-body framing, connection behavior, malformed requests, and the boundary between raw socket handling and framework behavior.

#### Raw-socket HTTP server

Objective:

Build a minimal HTTP server using Python's `socket` module before relying on FastAPI or another web framework.

Topics covered:

- Created a TCP server using `socket.create_server()`.
- Bound the server to `127.0.0.1` on port `8000`.
- Learned the difference between HTTP and HTTPS when making a request to a local server.
- Learned that sending arbitrary text over a socket is not equivalent to sending a correctly framed HTTP response.
- Constructed an HTTP/1.1 response with a status line, response headers, a blank line, and a body.
- Learned the purpose of `Content-Type`, `Content-Length`, and `Connection: close`.
- Learned that `Content-Length` counts body bytes, not the number of characters in the response's entire HTTP message.
- Used `sendall()` to transmit the response.
- Learned to close an accepted client socket after handling a request.
- Observed that `socket.create_server()` already creates a listening server socket.
- Tested the server directly from the WSL terminal and observed it accept multiple requests while running in a loop.
- Learned that a TCP `recv(1024)` call reads available bytes up to the specified limit; it does not guarantee receipt of an entire HTTP request.
- Began parsing the HTTP request line using string operations.

Practical evidence:

- Created `experiments/raw_http_server.py`.
- Tested the server with curl.
- Observed the HTTP/0.9-related error produced when the server returned plain text without a valid HTTP response structure.
- Corrected the response structure and received an HTTP/1.1 200 response with the body `Request received!`.
- Verified the body length as 17 bytes for that exact body.
- Ran the server directly in the WSL terminal and observed multiple GET requests being accepted.
- Tested a request target containing a query string: `/hello?name=Aayush`.
- Extracted the request method, request target, and HTTP version from the request line.
- Verified the output:

* Method: `GET`
* Request target: `/hello?name=Aayush`
* HTTP version: `HTTP/1.1`

Current code-review findings:

- Removed unnecessary string joining from the request-line parsing.
- Replaced splitting the full request into all lines with a first-line extraction approach.
- Added a check that the request line contains exactly three fields before unpacking.
- The current parsing exercise handles one connection and closes the client and server sockets afterward.
- The response and continuous-server loop are temporarily commented out while request parsing is practised.

Assessment:

- The request-line parsing exercise has passed for a valid GET request.
- The malformed-request validation exercise is the next immediate task.
- The complete raw HTTP server lab is not yet complete.
- The server still needs integrated request parsing, appropriate error handling, and a restored continuous accept loop.
- The current `recv(1024)` approach is suitable only for the introductory exercise. It must not be treated as robust HTTP parsing.

### Day 4: Tests and results

- Python environment creation: passed.
- Virtual environment interpreter verification: passed.
- Dependency installation: passed.
- Dependency reproduction in a second temporary environment: passed.
- HTTP inspection with curl: passed for the requests exercised.
- HTTP inspection with httpx: passed for the query-parameter exercise.
- Raw-socket HTTP response: passed for the observed 200 response.
- Multiple requests accepted in a loop: observed during direct terminal testing.
- Request-line extraction: passed for the tested GET request.
- Invalid request-line handling: pending.
- Full raw HTTP server acceptance criteria: pending.

### Day 4: Assessment and weak spots

- Python environment setup and basic dependency reproduction have been demonstrated practically.
- Basic HTTP request/response inspection has been demonstrated with curl and httpx.
- The request line is currently understood as three fields: method, request target, and HTTP version.
- The request target can include a query string; it is not necessarily only the path.
- HTTP parsing is not equivalent to splitting an arbitrary string. TCP is a byte stream, and a request can arrive across multiple reads.
- Robust request framing, body handling, and connection lifecycle still require practical work.
- Do not begin FastAPI revision until the required HTTP fundamentals and the introductory server exercise have been assessed.

## Current Blockers and Outstanding Work

- Complete request-line validation, including malformed input.
- Restore the raw HTTP server's continuous accept loop after completing the parsing exercise.
- Integrate parsing with valid HTTP responses and ensure client connections are closed appropriately.
- Improve response construction so `Content-Length` is calculated from the actual encoded body.
- Continue studying HTTP headers, methods, status codes, request bodies, and connection behavior.
- Complete the basic pull-request and collaboration workflow in Git.
- Continue Python fundamentals as required by the curriculum, including exceptions, type hints, OOP, dataclasses, decorators, context managers, generators, and iterators.
- Keep `labs/` intentionally untracked because its files are temporary practice examples.
- Time spent on Day 4 has not yet been recorded.

## Next Assignment

1. Complete the request-line validation exercise in `experiments/raw_http_server.py`.
   - Extract the first request line.
   - Split it into fields.
   - Accept exactly three fields.
   - Print the method, request target, and HTTP version for valid input.
   - Reject malformed input such as `GET /hello`.
2. Restore the server's accept loop and integrate request-line parsing with the HTTP response.
3. Test the server with curl and verify the response status, headers, body, and connection behavior.
4. Review the difference between parsing a URL path and parsing query parameters.
5. Continue the required HTTP exercises before resuming FastAPI revision.
6. Record the final test evidence, assessment, time spent, and next assignment when Day 4 ends.
7. At the end of Day 4, create or update `notes/session-notes/session-04.md` with only that session's concepts, commands, and demonstrated evidence.
8. Prepare the next weekly Reading Pack with 4–6 verified resources, short reading chunks, estimated time, and thought questions.

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
- Session notes contain only concepts, commands, and evidence from their own session. Remaining work and future assignments belong in this ledger.

This ledger is the source of truth for course progress. The curriculum in `notes/curriculum.md` is the source of truth for course scope, sequencing, projects, and teaching requirements.

Before committing: verify that the `notes/session-notes/` paths match your current local repository, and inspect the diff to ensure your existing Day 3 evidence hasn't been accidentally removed. Once pushed, the live ledger will be aligned with the progress demonstrated so far.
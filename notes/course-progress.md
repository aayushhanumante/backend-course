Backend Engineering Course Progress Ledger
Current Status
- Phase: Week 0–1, Developer Tooling and Ramp-up
- Current session: Next session, Week 0–1 tooling continuation
- Last completed session: Day 4, Python Environment Setup and HTTP Fundamentals
- Current status: Day 4 complete; Week 0–1 ramp-up continues
- Environment: Windows 11, WSL2 Ubuntu
- Python version: 3.12.3
- Repository: ~/projects/backend-course
- GitHub: https://github.com/aayushhanumante/backend-course
- Progress tracking: This ledger is the source of truth for completed work, practical evidence, blockers, and next assignments.
- Temporary practice files under labs/ remain intentionally untracked.
Completed Sessions
Week 0, Day 1: Linux Filesystem Basics
Topics completed:
- Practised whoami, pwd, ls -la, uname, and df.
- Learned absolute and relative paths, /, ~, ., .., and cd -.
- Learned the relationship between the Linux filesystem and Windows drives in WSL2.
- Created the course workspace with notes/, labs/, and experiments/.
- Practised touch, nano, mv, cp, rm, and chmod.
- Learned basic file permissions and permission notation.
- Completed checkpoint questions on directory navigation, permissions, and file copying.
Session notes: notes/session-notes/session-01.md
Week 0, Day 2: Linux Text Tools and Logs
Topics completed:
- Practised cat, less, head, tail, tail -f, and grep.
- Learned to navigate and search text using less.
- Practised output redirection with > and >>, including overwriting versus appending.
- Created and inspected labs/sample.log.
- Practised monitoring log output and stopping a running command with Ctrl+C.
Session notes: notes/session-notes/session-02.md
Week 0, Day 3: Git Fundamentals and GitHub
Topics completed:
- Initialized and maintained a Git repository on main.
- Practised staging, commits, status checks, diffs, and history inspection.
- Learned the difference between tracked, untracked, staged, and committed files.
- Created .gitignore rules for Python caches, virtual environments, and environment files.
- Verified ignore rules using git check-ignore -v.
- Generated an Ed25519 SSH key and configured GitHub SSH authentication.
- Configured the origin remote and pushed commits to GitHub.
- Updated commit author metadata to use GitHub's private noreply email.
- Learned that HEAD identifies the current checkout and that branches are movable references to commits.
- Learned the distinction between local branches and remote-tracking references such as origin/main.
- Practised comparing branch contents with git diff and inspecting commit history with git log.
- Learned that git diff A..B compares content at two endpoints, while git log A..B lists commits reachable from B but not A.
- Learned that git push publishes commits but does not automatically merge branches.
- Learned that git merge BRANCH_NAME merges the named branch into the currently checked-out branch.
- Observed a fast-forward merge and pushed the updated main branch.
- Discussed the differences between git fetch, git pull, and git push.
Practical evidence:
- Created the branch practice/git-branches.
- Created notes/git-branch-practice.md on the practice branch.
- Reviewed the staged file using git diff --staged.
- Created commit a1c7a23 with message Branch exercise example.
- Pushed the branch using git push -u origin practice/git-branches.
- Verified upstream tracking with git branch -vv.
- Confirmed the practice note was absent from main before merging.
- Fast-forward merged practice/git-branches into main.
- Pushed main to GitHub.
- Verified that main, practice/git-branches, origin/main, and origin/practice/git-branches pointed to commit a1c7a23.
- Completed a hands-on git fetch exercise and inspected synchronization between local and remote-tracking references.
- Confirmed that labs/ remained intentionally untracked.
Assessment and remaining practice:
- Demonstrated basic understanding of staging, commits, branch isolation, upstream tracking, merging, and remote synchronization.
- Explained fetch, pull, and push conceptually.
- Pull-request collaboration workflows remain to be practised.
- Advanced Git recovery, conflict resolution, and rebasing have not yet been assessed.
Session notes: notes/session-notes/session-03.md
Completed Session: Week 0–1, Day 4
Python environment setup
Topics completed:
- Checked the installed Python version using python3 --version.
- Located the system Python interpreter using which python3.
- Discovered that pip was initially unavailable in the system Python environment.
- Installed the Ubuntu package required for virtual-environment support (python3.12-venv).
- Created a project-local virtual environment named .venv and activated it using source .venv/bin/activate.
- Verified that python resolves to .venv/bin/python.
- Inspected sys.executable, sys.prefix, and sys.base_prefix to verify interpreter selection and environment isolation.
- Learned that python -m pip runs pip through the selected Python interpreter.
- Installed httpx inside the virtual environment.
- Inspected installed dependencies using python -m pip list and python -m pip freeze.
- Generated requirements.txt using python -m pip freeze > requirements.txt.
- Learned why developers recreate their own environments rather than copying .venv between machines.
Dependency reproducibility
Practical evidence:
- Python version: 3.12.3.
- Virtual environment created successfully at .venv.
- Confirmed that the active interpreter resolves inside .venv.
- Installed httpx==0.28.1 and its dependencies.
- Captured the installed dependency versions in requirements.txt.
- Created a separate temporary environment at /tmp/backend-course-repro.
- Installed dependencies in the temporary environment using pip install -r requirements.txt.
- Verified that the temporary environment reproduced the listed dependencies and could import httpx version 0.28.1.
Assessment:
- Demonstrated virtual-environment creation and activation.
- Demonstrated basic dependency reproduction from a requirements file.
- Cross-platform compatibility, Python version constraints, and more deliberate dependency management remain topics for later assessment.
HTTP fundamentals using curl and httpx
Topics covered:
- Learned that curl is a command-line HTTP client and that a basic request defaults to GET.
- Used curl -i to inspect response headers and bodies.
- Used curl -v to inspect request details, response details, and connection diagnostics.
- Learned that > lines in verbose output represent outgoing client data and < lines represent incoming responses.
- Used -H to add request headers.
- Used -d to submit request data and observed the default POST behavior.
- Inspected JSON request and response bodies using httpbin endpoints.
- Distinguished Content-Type, which describes a message body's media type, from Accept, which describes response media types the client can accept.
- Learned that an echoed request header appearing inside a response body does not make it a response header.
- Inspected 2xx, 4xx, and 5xx status codes, including 200, 404, and 500.
- Discussed the difference between client-related errors and server-related errors.
- Inspected URL paths and query parameters.
- Learned that query parameter values in JSON responses may be represented as strings.
- Used httpx.get() with params to construct a query string programmatically.
- Learned that response.json() parses a JSON response body into Python objects.
Practical evidence:
- Successfully requested https://httpbin.org/get.
- Inspected outgoing requests and incoming responses using verbose curl output.
- Sent a custom X-Course-Test header and observed it in the echoed JSON response.
- Submitted JSON data to the httpbin POST endpoint and inspected the parsed result.
- Requested endpoints returning 404 and 500 status codes.
- Sent Accept: application/json.
- Tested query parameters using curl and httpx.
Assessment:
- Demonstrated basic inspection of HTTP methods, headers, response bodies, status codes, and query parameters.
- Request framing, bodies, and connection lifecycle received a practical introduction through the raw-socket server exercise.
Raw-socket HTTP server
Objective:

Build a minimal HTTP server using Python's socket module to understand the request/response lifecycle and what a web framework abstracts away.

Topics covered:
- Created a TCP server using socket.create_server() and bound it to 127.0.0.1:8000.
- Learned the difference between HTTP and HTTPS when making requests to the local server.
- Learned that arbitrary text sent over a socket is not a correctly framed HTTP response.
- Constructed HTTP/1.1 response status lines, headers, the blank-line separator, and body bytes.
- Learned the purpose of Content-Length and Connection: close.
- Calculated Content-Length from the encoded response body, not from the full response or the unencoded string.
- Used sendall() to transmit response bytes.
- Learned to close the accepted client socket after responding while keeping the listening socket open for further clients.
- Extracted the request method, request target, and HTTP version from the request line.
- Added a basic check that the request line contains exactly three fields before unpacking.
- Returned a 400 Bad Request response for the malformed request exercised.
- Learned that one recv(1024) call does not guarantee receipt of an entire HTTP request.
Practical evidence:
- Created and tested experiments/raw_http_server.py.
- Observed the HTTP/0.9-related curl error when the server initially returned plain text without a valid HTTP response structure.
- Received HTTP/1.1 200 OK after correcting the response structure.
- The final tested success body was Request received, with Content-Length: 16. An earlier body Request received! was also tested at 17 bytes.
- Tested the request target /hello?name=Aayush and extracted:
  - Method: GET
  - Request target: /hello?name=Aayush
  - HTTP version: HTTP/1.1
- Sent INVALID\r\n\r\n from a separate Python socket client.
- Observed HTTP/1.1 400 Bad Request with an 11-byte Bad Request body.
- Sent a valid curl request after the malformed request and observed another 200 OK, demonstrating that the server remained available.
Assessment:
- Introductory raw-socket server exercise: passed for the tested scenarios.
- Demonstrated basic response framing, body byte length, client-socket closure, and continued acceptance after a malformed request.
- The server is an educational implementation, not a complete HTTP parser. It does not robustly handle requests delivered across multiple reads or fully validate HTTP syntax and request bodies.
Day 4: Tests and results
- Virtual environment creation and interpreter verification: passed.
- Dependency installation and reproduction in a second temporary environment: passed.
- HTTP inspection with curl and httpx: passed for the requests exercised.
- Request-line extraction: passed for the tested GET request.
- Valid HTTP response: passed; final tested body length was 16 bytes.
- Malformed request response: passed; 400 Bad Request body length was 11 bytes.
- Valid request after malformed request: passed.
- Robust TCP request framing and full HTTP syntax validation: not implemented; explicitly outside the scope of this introductory server.
- Time spent: not recorded.
Day 4: Assessment and weak spots
- Demonstrated Python environment setup and basic dependency reproduction.
- Demonstrated basic HTTP inspection with curl and httpx.
- Demonstrated an introductory raw-socket server handling the tested valid and invalid request cases.
- Correctly explained that the accepted client socket is distinct from the listening server socket.
- Initially misunderstood what happens when a request arrives across multiple TCP reads. Correct model: TCP does not label a partial read as HTTP 400; the server must accumulate and parse the message correctly, and then decide how to respond.
- Initially stated that é is not a valid Python character. Correct model: Python strings support Unicode; UTF-8 may encode a character into multiple bytes, and HTTP Content-Length counts body bytes.
- Recheck TCP stream behavior and UTF-8 byte length with brief retrieval questions at the start of the next session. Do not repeat the server lab unless a new failure justifies it.
Current Blockers and Outstanding Work
- Complete the basic GitHub pull-request workflow: branch, push, open a PR, merge, and synchronize local main.
- Cover remaining Week 0–1 Linux/tooling requirements as needed: processes and ports, environment variables, shell pipelines/scripts, and troubleshooting.
- Continue Python fundamentals as required by the curriculum: type hints, exceptions, OOP, dataclasses, decorators, context managers, generators, and iterators. Assess each before assuming mastery.
- Install and use pytest; write basic automated tests.
- Learn Docker images, containers, volumes, and Compose.
- Run PostgreSQL locally in Docker.
- Then build the first FastAPI service with five endpoints, Pydantic request/response models, validation, appropriate status codes, error handling, and pytest coverage.
- Keep labs/ intentionally untracked because its files are temporary practice examples.
- Day 4 hours spent: not reported.
Next Assignment
1. Start with a short retrieval check on TCP stream behavior and UTF-8 byte length. Do not repeat the completed raw-socket exercise.
2. Complete the basic GitHub pull-request workflow, using a small documentation change or other appropriate non-lab file.
3. Review and fill remaining Week 0–1 tooling gaps without repeating demonstrated work.
4. Install pytest and write a small test suite.
5. Learn Docker/Compose fundamentals and run PostgreSQL locally.
6. Build the first FastAPI service only after the required environment, Git workflow, HTTP basics, and testing gates are sufficiently demonstrated.
7. Create or update notes/session-notes/session-04.md with only Day 4 concepts, commands, and demonstrated evidence. Keep future tasks and blockers in this ledger.
8. Provide the next weekly Reading Pack with 4–6 verified resources, short reading chunks, estimated time, and 2–3 thought questions.
Session Tracking Rules
At the end of every session, record:
- Topics completed.
- Exercises and practical evidence.
- Tests performed and their results.
- Demonstrated understanding and remaining misconceptions.
- Blockers and unresolved questions.
- Time spent, when reported.
- Exact next assignment.
Teaching Rules
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
This ledger is the source of truth for course progress. The curriculum in notes/curriculum.md is the source of truth for course scope, sequencing, projects, and teaching requirements.

Changes to this ledger are prepared locally for review. Inspect the diff, then commit and push the changes yourself; this document does not imply that the GitHub repository has been modified.
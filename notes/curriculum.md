# Backend Engineering Curriculum and Course Contract

**Version:** 1.0  
**Duration:** 12-week core curriculum + 4-week mastery extension  
**Primary stack:** Python 3.12+, FastAPI, PostgreSQL 16, SQLAlchemy 2.0 async, Alembic, Redis, Docker, pytest  
**Learning mode:** Code-first, test-driven where appropriate, spec-driven, production-focused  
**Repository:** https://github.com/aayushhanumante/backend-course

---

# 1. Source of Truth and Operating Rules

This file is the authoritative curriculum agreement. It must be consulted at the start of every session when the student asks to continue the course.

Use these files together:

- `notes/curriculum.md`: agreed curriculum, scope, projects, constraints, and teaching rules.
- `notes/course-progress.md`: completed work, practical evidence, assessment results, blockers, time spent, and exact next assignment.
- `notes/session-XX.md`: detailed notes from individual sessions.

**Precedence rules**

1. The curriculum defines what must be learned and built.
2. The progress ledger records what has actually been completed and demonstrated.
3. Session notes provide detailed technical reference material.
4. Do not mark a topic complete merely because it was explained or discussed. Require practical evidence where appropriate.
5. Do not silently remove curriculum requirements. If scope must change, record the change and its reason in the progress ledger.
6. If context is lost, inspect the repository files or ask the student to provide the relevant file content. Never pretend to remember details that cannot be verified.
7. The student may explicitly ask to revise this agreement. Otherwise, preserve its requirements.

---

# 2. Student Background and Constraints

## Starting profile

- Third-year B.Tech student in India.
- Target: build strong backend engineering skills suitable for internships and placement opportunities.
- Python fundamentals are reasonably solid; OOP beyond basic classes needs assessment and reinforcement.
- SQL and PostgreSQL knowledge is basic.
- Linux/terminal and Git/GitHub experience are developing.
- FastAPI has been studied before, but requires revision and practical verification.
- Async Python, testing frameworks, Docker, and production deployment are new or largely unfamiliar.
- Operating environment: Windows 11 with WSL2 Ubuntu.
- Work inside WSL2 for Linux-based development unless a specific task requires Windows.
- Available time: approximately 16 focused hours per week, subject to college and examination demands.

The existing progress ledger takes precedence over assumptions in this initial profile.

## Weekly time allocation

Within 16 focused hours:

| Activity | Weekly target |
|---|---:|
| Coding, labs, debugging, project work | 13 hours |
| Code review, corrections, incidents, design | 2 hours |
| Quiz and weekly review | 1 hour |
| **Total focused work** | **16 hours** |

Commute reading is additional, not included in the 16 hours.

The weekly Reading Pack should take approximately 3–4 hours, divided into mobile-friendly chunks of 15–25 minutes.

Be realistic about scope. If college or examinations reduce availability, use the minimum viable week rather than allowing silent schedule drift.

---

# 3. Learning Objective

Become capable of building, explaining, testing, and operating a reliable backend using FastAPI and PostgreSQL.

The final competency target is to reason through a failure such as:

> A payment gateway loses its primary database during a transaction. An external bank may have debited money, but the gateway has not recorded the result. Detect the discrepancy, recover safely, prevent duplicate charges, reconcile state, and redesign the system to reduce recurrence.

CRUD APIs are the baseline, not the end goal.

The student must understand and demonstrate:

- Transaction boundaries and isolation.
- Concurrency and race conditions.
- Idempotency and safe retries.
- Immutable financial records and reconciliation.
- Database and worker failure recovery.
- Consistency trade-offs and distributed-system failure modes.
- Testing of critical invariants.
- Production observability and incident response.
- Architecture decisions and their trade-offs.

---

# 4. Teaching Contract

## 4.1 Code-first, specification-driven learning

Every substantial topic must include a lab with:

- Problem statement.
- Functional and technical requirements.
- Acceptance criteria.
- Appropriate tests or test scaffolding.
- Practical evidence to submit.
- External reference links.
- Relevant production failure modes.

Provide tests, skeletons, and specifications. The student writes the implementation.

Do not provide complete lab solutions unless explicitly requested and the hint process has been exhausted.

## 4.2 Break it before fixing it

For concurrency, transactions, idempotency, and reliability:

1. Implement a deliberately naive version.
2. Write a test or script that exposes its failure.
3. Reproduce the failure.
4. Explain the observed result.
5. Implement a fix.
6. Repeat the same test.
7. Demonstrate that the fix preserves the required invariants.

Examples include double-spending under concurrent transfers, duplicate processing after retries, deadlocks, and lost updates.

## 4.3 Hint ladder

When the student is stuck, use this sequence:

1. Guiding question.
2. Conceptual hint.
3. Pointer to a specific documentation section.
4. Pseudocode.
5. Minimal snippet of approximately 15 lines or fewer.

The student must attempt each level before moving to the next. If they ask for the full solution prematurely, ask what they have tried and continue with the next appropriate hint.

## 4.4 Senior-level code review

Review submitted code for:

- Correctness and invariants.
- Race conditions and transaction boundaries.
- Error handling and recovery.
- Security and secrets handling.
- Database access patterns and performance.
- Architecture and dependency direction.
- Naming, readability, and testability.
- Operational behavior under failure.

Rank findings:

- **Blocker:** correctness, security, or integrity issue that prevents acceptance.
- **Major:** substantial reliability, performance, maintainability, or design risk.
- **Minor:** localized issue with limited impact.
- **Nit:** optional polish.

Explain why each finding matters in production. The student fixes the findings, then submits the revised code for another review.

## 4.5 Concept checks

After every lab, ask 2–3 questions requiring explanation or scenario-based reasoning.

Do not accept memorized definitions when the student cannot apply the concept.

## 4.6 Honest feedback

- Do not flatter without evidence.
- Identify weak reasoning directly and constructively.
- Require the student to justify design decisions.
- Teach trade-offs rather than slogans.
- Do not claim a test passed unless its result was observed or reliably reported.

## 4.7 Targeted Python instruction

When a lab requires an unfamiliar Python feature, provide a brief explanation and a small exercise before relying on it.

Topics include:

- Classes and object-oriented design.
- Type hints and generics.
- Dataclasses.
- Decorators.
- Context managers.
- Generators and iterators.
- Exceptions.
- Async functions and `await`.
- Dependency injection and resource lifetimes.

## 4.8 Production lens

For every important topic, explain briefly:

- How it can fail under load.
- What logs and metrics reveal the failure.
- What an on-call engineer might observe.
- Which immediate mitigation is safe.
- Which long-term fix addresses the underlying cause.

Keep introductions short. Coding time must not turn into extended lectures.

---

# 5. Curriculum Roadmap

## Week 0–1: Developer tooling and ramp-up

**Goal:** Establish a reliable local development workflow and build a small, tested API.

### Topics

**Linux and terminal**
- Navigation and filesystem operations.
- Permissions and environment variables.
- Processes, ports, and basic process inspection.
- Shell pipelines, redirection, and simple shell scripts.
- Log inspection and troubleshooting inside WSL2.

**Git and GitHub**
- Repository initialization, status, staging, commits, and diffs.
- Branches, switching, merging, and resolving conflicts.
- Remotes, push, pull, and basic pull-request workflow.
- Meaningful commit messages and `.gitignore`.
- Use GitHub from the beginning of every project.

**Python for backend engineering**
- Type hints and exceptions.
- Classes and OOP.
- Dataclasses.
- Decorators and context managers.
- Generators and iterators.
- Virtual environments, `uv` or another appropriate environment workflow.
- Dependency management and packaging basics.

**HTTP by doing**
- Build a tiny raw-socket HTTP echo server.
- Inspect requests and responses using `curl` and `httpx`.
- Headers, methods, status codes, request bodies, and connection behavior.
- Understand what a framework abstracts away.

**Testing and Docker**
- Install and use pytest.
- Write basic automated tests.
- Understand Docker images, containers, volumes, and Compose.
- Run PostgreSQL locally in Docker.

### Lab: First FastAPI service

Build a small service with five endpoints.

Requirements:
- FastAPI routing.
- Pydantic request and response models.
- Input validation.
- Appropriate HTTP status codes.
- Error handling.
- pytest tests for successful and invalid requests.
- GitHub repository and meaningful commits.

### Acceptance criteria

- Student can navigate and troubleshoot the development environment.
- Student can create a branch, commit changes, and push them.
- Student can explain the HTTP request/response lifecycle.
- The API passes its tests.
- The project can be run from documented setup instructions.

### Milestone

A working, tested FastAPI service with a reproducible development setup.

---

## Phase 1: Solid foundations

## Week 2: FastAPI, HTTP, SQL, and application servers

**Goal:** Understand request handling, validation, SQL, and the difference between synchronous and asynchronous execution.

### Topics

- FastAPI routing and dependency injection.
- Pydantic v2 validation and serialization.
- Error handling and background tasks.
- ASGI and Uvicorn fundamentals.
- Sync versus async execution.
- How blocking work can stall an event loop.
- HTTP behavior and API semantics.
- SQL through practical PostgreSQL exercises.
- Joins, aggregation, CTEs, and window functions.
- Financial amounts: use appropriate integer minor units or PostgreSQL `NUMERIC`; never use binary floating-point for exact monetary arithmetic.

### Server experiment

1. Run FastAPI using Uvicorn.
2. Run it with Gunicorn and Uvicorn workers, using a compatible configuration for the selected versions.
3. Vary worker counts.
4. Generate controlled load.
5. Measure throughput, latency, errors, and memory.
6. Explain why more workers do not automatically improve performance.

### Lab

Extend the initial API with validated request models, error cases, and tests. Add SQL exercises with expected results.

### Acceptance criteria

- Explain how a request reaches a FastAPI endpoint.
- Demonstrate request validation and meaningful error responses.
- Explain when synchronous code is appropriate and when blocking work is dangerous.
- Compare server configurations using measured results.
- Demonstrate SQL joins, aggregation, CTEs, and window functions.

---

## Week 3: SQLAlchemy, migrations, and Project 1 completion

**Goal:** Build a properly structured database-backed API.

### Topics

- SQLAlchemy 2.0 async sessions and queries.
- Database connection and session lifetimes.
- Alembic migrations.
- Indexes and query planning.
- `EXPLAIN ANALYZE`.
- Project structure: routers → services → repositories → models.
- Configuration and secrets.
- Structured logging.
- Pagination and API versioning.
- Database integration tests.

### Lab: Query performance

1. Construct a query that performs poorly on a meaningful dataset.
2. Measure it with `EXPLAIN ANALYZE`.
3. Form a hypothesis about the bottleneck.
4. Add or modify an index if justified.
5. Measure again and explain the difference.

### Project 1: Production-grade Orders/Merchant API

Requirements:
- Multi-tenant data model.
- JWT authentication.
- Database persistence.
- Alembic migrations.
- Pagination and error handling.
- pytest suite.
- Dockerized local setup.
- GitHub Actions CI.
- Structured logs.

### Acceptance criteria

- Tests demonstrate tenant isolation.
- Database schema can be created and upgraded using migrations.
- Query plans and index decisions are justified by evidence.
- Business logic is separated from HTTP handling.
- CI executes the test suite.
- Setup instructions work on a clean local environment.

### Milestone exam: End of Week 3

Assess conceptual understanding, debugging, a small live-coding task, and a code review of Project 1.

Do not proceed if a critical database, API, or testing concept is shaky.

---

# Phase 2: Correctness under concurrency

## Week 4: Transactions, isolation, and race conditions

**Goal:** Demonstrate how concurrent operations violate invariants and learn how to prevent it.

### Topics

- ACID transactions.
- PostgreSQL MVCC.
- Isolation levels.
- Lost updates and non-repeatable reads.
- `SELECT ... FOR UPDATE`.
- `SKIP LOCKED`.
- Optimistic versus pessimistic locking.
- Deadlocks and lock ordering.
- Transaction boundaries and rollback behavior.

### Lab: Break a wallet transfer

Start with a naive balance-update implementation.

Requirements:
- Write a concurrent test script.
- Launch many simultaneous transfers.
- Demonstrate a double-spend or lost update.
- Record the resulting balances and invariant violations.
- Investigate locks and isolation.
- Implement a correction.
- Rerun the exact same stress test.

### Acceptance criteria

- Reproduce the failure before fixing it.
- Explain why the race exists.
- Demonstrate that the correction preserves balance invariants under load.
- Explain the trade-offs of locking strategies.
- Cause a deadlock intentionally in a controlled test, then fix the locking order or transaction design.

### Production exercise

Investigate what database logs, lock information, and request metrics might reveal during a hot-row incident.

---

## Week 5: Idempotency, retries, and the payment ledger

**Goal:** Make operations safe when clients retry and external systems behave unpredictably.

### Topics

- Idempotency keys.
- Duplicate requests and concurrent key claims.
- At-most-once and at-least-once processing.
- Timeouts, retry policies, backoff, and jitter.
- Why a timeout does not prove that an operation failed.
- Immutable double-entry ledger entries.
- Derived balances and financial invariants.
- Reconciliation between internal records and external results.

### Project 2: Mini Payment Ledger

Requirements:
- Wallets.
- Transfers.
- Double-entry ledger.
- Idempotency keys.
- Concurrent transfer stress tests.
- Reconciliation job.

### Core invariant

Every completed transfer must preserve the accounting rules. For a balanced internal transfer, total debits must equal total credits, and the system must not create or destroy money.

### Lab

- Submit the same idempotency key repeatedly.
- Submit the same key concurrently.
- Simulate a retry after a timeout.
- Verify that a duplicate request cannot create another transfer.
- Fire hundreds of concurrent transfers.
- Demonstrate conservation of total money.
- Introduce inconsistent data in a controlled test and build a reconciliation process that detects it.

### Acceptance criteria

- Idempotency is enforced by durable storage and appropriate database constraints, not only an in-memory check.
- Duplicate and concurrent requests behave correctly.
- The ledger remains balanced.
- Reconciliation identifies deliberately introduced discrepancies.
- Tests exercise failures, not just successful requests.

---

## Week 6: Authentication, webhooks, and API security

**Goal:** Protect the payment API and complete Project 2.

### Topics

- JWT authentication.
- API keys hashed at rest.
- OAuth2 basics.
- HMAC-signed webhooks.
- Webhook timestamp and replay considerations.
- Rate limiting: token bucket and sliding window.
- Secrets management.
- OWASP API Security Top 10.
- Authentication versus authorization.
- Tenant isolation and abuse prevention.

### Lab

Build authenticated transfer endpoints and signed webhook verification.

Requirements:
- Reject invalid credentials.
- Verify tenant boundaries.
- Store API-key hashes rather than plaintext keys.
- Verify webhook signatures safely.
- Handle duplicate webhook deliveries.
- Implement and test a rate limiter.
- Avoid leaking sensitive information in logs and errors.

### Project 2 completion criteria

- Transfers preserve ledger invariants.
- Idempotency and concurrency tests pass.
- Authentication and authorization tests pass.
- Webhook signatures are verified correctly.
- Reconciliation is operationally documented.
- Design decisions are explained and defended.

### Milestone exam: End of Week 6

Assess transactions, idempotency, financial correctness, debugging, live coding, and Project 2 code review.

---

# Phase 3: Distributed systems and reliability

## Week 7: Redis, caching, and distributed coordination

**Goal:** Understand what changes when state is shared across multiple application instances.

### Topics

- Redis data structures and expiration.
- Cache-aside.
- Cache invalidation and stale data.
- Cache stampede protection.
- TTLs and memory limits.
- Atomic operations and Lua scripting.
- Distributed locking pitfalls.
- Cache failure and degraded operation.
- Why a cache is not automatically the source of truth.

### Lab

Implement a cache for a read-heavy endpoint and a Redis-backed rate limiter.

Requirements:
- Measure cache hit and miss behavior.
- Test expiration.
- Simulate concurrent cache misses.
- Prevent or reduce a cache stampede.
- Observe application behavior when Redis is unavailable.
- Explain when serving stale data is acceptable.

### Acceptance criteria

- Cache behavior is measured rather than assumed.
- Critical financial correctness does not depend on an unprotected cache.
- Rate limiting behaves correctly under concurrent requests.
- Failure behavior is documented.

---

## Week 8: Background workers, outbox, and sagas

**Goal:** Reliably process asynchronous work when components fail independently.

### Topics

- Background worker architecture using Arq or Celery.
- Queue delivery semantics.
- Retries and backoff.
- Dead-letter queues.
- Poison messages.
- Duplicate message handling.
- Transactional outbox pattern.
- Webhook delivery.
- State machines.
- Saga pattern and compensating actions.

### Lab

Build a durable background workflow that sends webhooks.

Requirements:
- Record the business change and outgoing event transactionally.
- Publish events through an outbox-driven worker.
- Retry temporary failures.
- Handle duplicate delivery safely.
- Identify poison messages.
- Send exhausted messages to a dead-letter mechanism.
- Recover after a worker crashes mid-job.

### Acceptance criteria

- No critical event is silently lost between the database transaction and publication.
- Duplicate processing is safe.
- Retry behavior is bounded and observable.
- Failed work can be diagnosed and replayed safely.
- Compensation does not pretend to erase an external action that already happened.

---

## Week 9: PostgreSQL operations and Project 3 completion

**Goal:** Understand the database as an operational system, not just a query interface.

### Topics

- Connection pooling and connection budgets.
- PgBouncer.
- Replication and replication lag.
- Primary and replica behavior.
- Backup and restore.
- Point-in-time recovery concepts.
- Partitioning.
- Vacuum, bloat, and table maintenance.
- Safe migrations and lock duration.
- `pg_stat_statements`.
- Query and connection diagnostics.

### Labs

**Connection-pool experiment**
- Vary application worker counts and database pool sizes.
- Observe connections, latency, and failures.
- Explain why application concurrency and database connection limits must be designed together.

**Replication experiment**
- Run a primary and replica using Docker Compose where feasible.
- Generate writes.
- Observe replication lag and stale reads.
- Explain which operations can tolerate stale data.

**Recovery exercise**
- Practise a local backup and restore workflow.
- Document what recovery evidence is available and what remains untested.

### Project 3: Payment Gateway Simulator

Requirements:
- Payment intents with a state machine: `created → authorized → captured → refunded/failed`.
- Fake bank service that is slow, flaky, and sometimes times out after succeeding.
- Signed webhook delivery with retries.
- Transactional outbox.
- Redis rate limiting.
- Background workers.

### Acceptance criteria

- Payment transitions obey documented state rules.
- Retries do not duplicate financial effects.
- Outgoing events survive worker failures.
- Database pooling is measured and justified.
- Replication lag and recovery limitations are understood.
- Project 3 has a tested, reproducible local environment.

### Milestone exam: End of Week 9

Assess distributed-system failure handling, PostgreSQL operations, debugging, live coding, and Project 3 code review.

---

# Phase 4: Production engineering

## Week 10: Observability and service objectives

**Goal:** Make system health measurable and failures diagnosable.

### Topics

- Structured logging.
- Request and correlation IDs.
- Prometheus metrics.
- RED metrics: rate, errors, and duration.
- Grafana dashboards.
- OpenTelemetry tracing.
- Service-level indicators and objectives.
- Alert thresholds and alert fatigue.
- Sensitive-data redaction.
- Diagnosing latency across application, database, and downstream services.

### Lab

Instrument the Payment Gateway Simulator.

Requirements:
- Correlate requests across logs.
- Measure request rate, latency, and error rate.
- Expose useful metrics.
- Trace a request through relevant components.
- Define a small set of SLIs and SLOs.
- Create alerts for meaningful failure conditions.

### Acceptance criteria

- A simulated incident can be diagnosed using telemetry.
- Metrics have useful names and labels without unbounded cardinality.
- Logs do not expose credentials or sensitive payment data.
- Alerts correspond to user-visible or operationally meaningful failures.

---

## Week 11: Resilience, reverse proxy, and load testing

**Goal:** Exercise production-style traffic handling and recovery.

### Topics

- Timeouts and deadlines.
- Retries with exponential backoff and jitter.
- Circuit breakers.
- Bulkheads.
- Backpressure and load shedding.
- Health checks.
- Graceful shutdown.
- Reverse proxies and forwarded headers.
- TLS termination.
- Load balancing.
- Capacity and bottleneck analysis.

### Deployment lab: Nginx and Docker Compose

Put Nginx in front of the application.

Requirements:
- Run Nginx using Docker Compose.
- Configure it as a reverse proxy.
- Configure TLS termination with a self-signed certificate.
- Handle proxy headers correctly.
- Configure appropriate timeouts.
- Load-balance across two or three application containers.
- Load-test using Locust or k6.
- Record throughput, latency percentiles, errors, and resource use.
- Kill one application container during traffic.
- Observe and explain the resulting behavior.
- Restore service and document the recovery.

### Acceptance criteria

- Reverse-proxy routing works.
- TLS works for the local test setup.
- Client IP and scheme information are handled safely.
- Timeouts and retries do not create uncontrolled retry storms.
- Failure of one application instance is observed and explained.
- Performance claims include measurements and environment details.

---

## Week 12: Capstone hardening and design review

**Goal:** Turn the simulator into a documented, testable engineering project.

### Capstone work

- Harden Project 3.
- Fix critical failure modes discovered in earlier labs.
- Run load and chaos experiments.
- Review correctness invariants.
- Write post-mortems.
- Document architecture decisions.
- Prepare a README and setup instructions.
- Write an operational runbook.
- Produce a final design document.
- Complete a system-design discussion.

### Project 4: Make It Survive

Harden the Payment Gateway Simulator with:
- Observability.
- A measurable load-test target.
- Chaos experiments.
- Recovery procedures.
- Documented invariants.
- Post-mortems for failures.
- Architecture decision records (ADRs).
- README.
- Runbook.
- Architecture diagram.
- Final design document.

### Required chaos experiments

- Kill PostgreSQL during a transaction.
- Kill a worker during job processing.
- Deliver duplicate webhooks.
- Delay a bank response.
- Simulate downstream timeouts.
- Observe retry and recovery behavior.
- Check whether internal and external state can diverge.
- Demonstrate detection and reconciliation of discrepancies.

### Optional real deployment

Only if time permits and after checking current pricing and free-tier terms.

Requirements:
- Use a free-tier service or low-cost host only after reviewing current terms.
- No spending without explicit student approval.
- Configure environment variables and secrets safely.
- Connect a managed PostgreSQL service if appropriate.
- Inspect logs.
- Practise a rollback.
- Document limitations and operational costs.

A real deployment is optional. Correctness, tests, recovery, and documentation take priority.

### Milestone exam: End of Week 12

Assess:
- Conceptual questions.
- Debugging scenario.
- Live-coding task.
- Code review.
- Architecture defence.
- Failure and recovery reasoning.

---

# 6. Weeks 13–16: Mastery Extension

These weeks deepen skills introduced in the core curriculum. They are not permission to skip unfinished critical work from Weeks 1–12.

## Week 13: Database depth and correctness

**Goal:** Strengthen database reasoning beyond ordinary application CRUD.

### Topics
- Revisit SQL joins, aggregation, CTEs, and window functions.
- Query plans and index selection.
- MVCC and transaction isolation.
- Locking, constraints, and transaction boundaries.
- Safe schema changes.
- Database invariants and recovery limitations.

### Labs
- Revisit a slow query and justify an optimization with measurements.
- Write queries that detect ledger inconsistencies.
- Introduce a concurrency bug and prove that a constraint or transaction strategy prevents it.
- Review a migration for lock and compatibility risks.

### Acceptance criteria
- Explain why a chosen index helps or fails to help.
- Identify the boundary between application validation and database-enforced integrity.
- Demonstrate that financial invariants survive concurrent operations.

## Week 14: Concurrency depth

**Goal:** Prove that concurrency fixes are correct, not merely that one test happened to pass.

### Topics
- Repeat ledger stress tests.
- Diagnose race conditions and deadlocks.
- Investigate transaction isolation and locking behavior.
- Review idempotency under simultaneous requests.
- Analyse retry interactions with database transactions.

### Labs
- Reproduce known race conditions.
- Run concurrent transfers and record invariant checks.
- Cause and diagnose a deadlock.
- Apply fixes and rerun the same tests.
- Increase load and look for failures that only emerge under contention.

### Acceptance criteria
- The student can explain the root cause of each reproduced race.
- Fixes preserve the invariants under repeated stress tests.
- Deadlocks are prevented where practical or handled safely when unavoidable.
- Test evidence is recorded in the progress ledger.

## Week 15: Performance and reliability

**Goal:** Measure bottlenecks, respond to incidents, and verify recovery from dependency failures.

### Topics
- Repeat application and database benchmarks.
- Investigate CPU, memory, database, and connection-pool bottlenecks.
- Review timeouts, retries, and backpressure.
- Practise incident response.
- Test recovery after database, worker, Redis, and downstream-service failures.

### Labs
- Reproduce a performance bottleneck and measure a correction.
- Investigate connection-pool exhaustion.
- Simulate a downstream outage and recovery.
- Test worker restart and message redelivery.
- Write a concise incident report with evidence and follow-up actions.

### Acceptance criteria
- Performance changes are justified by comparable measurements.
- The student can distinguish symptoms from root causes.
- Recovery behavior is tested rather than assumed.
- Mitigations and follow-up actions are documented.

## Week 16: Final engineering review

**Goal:** Demonstrate independent engineering judgment.

### Assessment
- Defend the architecture of the Payment Gateway Simulator.
- Complete a debugging assessment.
- Explain transaction boundaries and isolation.
- Explain idempotency and retry semantics.
- Demonstrate that tests protect critical invariants.
- Review a deliberately broken implementation.
- Explain operational trade-offs and recovery limitations.
- Identify weaknesses that remain in the system.

### Final acceptance criteria
- Explain the end-to-end payment flow and state transitions.
- Demonstrate why duplicate requests cannot create duplicate financial effects within the defined system boundary.
- Explain how uncertain external outcomes are detected and reconciled.
- Demonstrate correctness through tests and recorded evidence.
- Defend architectural decisions and acknowledge their limitations.
- Provide a reproducible repository, README, architecture diagram, ADRs, runbook, and post-mortems.

Passing is based on demonstrated competence, not simply reaching the final week.

---

# 7. Core Projects

## Project 1: Production-grade Orders/Merchant API

**Schedule:** Weeks 1–3

Build a multi-tenant API with:
- JWT authentication.
- Database persistence.
- Migrations.
- Pagination.
- Error handling.
- pytest coverage.
- Docker.
- GitHub Actions CI.
- Structured logging.

The student designs the folder structure first. Review dependency direction, module responsibilities, and tenant isolation before implementation grows too large.

## Project 2: Mini Payment Ledger

**Schedule:** Weeks 4–6

Build:
- Wallets.
- Double-entry ledger.
- Transfers.
- Idempotency keys.
- Concurrent stress tests.
- Reconciliation job.

Critical invariant: completed transfers must preserve the documented accounting rules. For balanced transfers, total debits equal total credits.

## Project 3: Payment Gateway Simulator

**Schedule:** Weeks 7–9

Build:
- Payment intents and state machine.
- Fake bank service.
- Timeouts, failures, and ambiguous outcomes.
- Signed webhook delivery.
- Retry logic.
- Transactional outbox.
- Redis rate limiting.
- Background workers.

The fake bank must sometimes time out after succeeding. This exposes the difference between an unknown outcome and a confirmed failure.

## Project 4: Make It Survive

**Schedule:** Weeks 10–12

Harden Project 3 with:
- Observability.
- Load testing.
- Chaos experiments.
- Recovery procedures.
- Post-mortems.
- README.
- Architecture diagram.
- ADRs.
- Runbook.
- Final design document.

After each project, conduct a design review in which the mentor challenges the student's assumptions, trade-offs, failure handling, and operational readiness.

---

# 8. Weekly Coding Drills

Every week, provide 3–5 small, timed coding drills, normally 20–40 minutes each.

Examples:
- Implement a token-bucket rate limiter.
- Write a retry decorator with jitter.
- Write a SQL window-function query for running balances.
- Diagnose a missing `await`.
- Fix an N+1 query.
- Find a database connection leak.
- Repair a transaction boundary.
- Write a test for duplicate webhook delivery.

Review these like coding-interview submissions. Require explanations and corrections rather than immediately providing the answer.

Every two weeks, provide a deliberately broken-code debugging challenge involving a realistic issue such as a race condition, N+1 queries, connection leaks, missing awaits, or incorrect error handling.

---

# 9. Incident Response and System Design

## Weekly incident drills from Week 4

Present one incident per week in a realistic format:
- Symptoms.
- Log and metric snippets.
- Relevant constraints.
- A deadline.
- Requests for hypotheses and mitigation.

Do not reveal the root cause until the student commits to a hypothesis.

The student must:
1. State what is known and unknown.
2. Rank plausible hypotheses.
3. Identify evidence that would distinguish them.
4. Propose immediate mitigation.
5. Propose long-term corrective action.
6. Write a concise post-mortem.

Example incidents:
- Double debit after a gateway timeout.
- Replica lag causing stale reads.
- Database connection-pool exhaustion.
- Retry storm after downstream recovery.
- Slow query locking a hot table.
- Poison message in a queue.
- Redis outage.
- Worker crash during processing.
- Database loss during a transaction.

## System design every two weeks

Use scenarios such as designing a payment gateway for 10 million transactions per day with a 99.99% availability target.

Walk through:
- Functional and non-functional requirements.
- Capacity estimation.
- API design.
- Data model.
- Consistency requirements.
- Transaction boundaries.
- Failure modes.
- Observability.
- Recovery.
- Trade-offs and cost.

The mentor should challenge assumptions and require the student to defend decisions.

---

# 10. Reading Packs

At the end of every session, provide a Reading Pack for the coming week.

Each pack should contain:
- 4–6 items.
- Estimated reading time.
- A brief explanation of why each item matters.
- Real, verified URLs where possible.
- A mixture of official documentation, selected articles, and book chapters.
- 2–3 thought questions for the next session.

Keep items mobile-friendly, preferably 15–25 minutes each. The total weekly commute pack should generally take 3–4 hours.

The pack supports coding; it must not replace hands-on work.

## Seed resources

### Official documentation

- FastAPI tutorial: https://fastapi.tiangolo.com/tutorial/
- FastAPI testing: https://fastapi.tiangolo.com/tutorial/testing/
- Pydantic v2: https://docs.pydantic.dev/latest/
- SQLAlchemy 2.0: https://docs.sqlalchemy.org/en/20/
- Alembic: https://alembic.sqlalchemy.org/en/latest/
- PostgreSQL: https://www.postgresql.org/docs/current/
- PostgreSQL MVCC: https://www.postgresql.org/docs/current/mvcc.html
- PostgreSQL transaction isolation: https://www.postgresql.org/docs/current/transaction-iso.html
- PostgreSQL explicit locking: https://www.postgresql.org/docs/current/explicit-locking.html
- pytest: https://docs.pytest.org/
- Docker: https://docs.docker.com/get-started/
- Redis: https://redis.io/docs/
- PgBouncer: https://www.pgbouncer.org/
- OpenTelemetry: https://opentelemetry.io/docs/
- Prometheus: https://prometheus.io/docs/introduction/overview/
- Locust: https://docs.locust.io/
- k6: https://grafana.com/docs/k6/latest/

### Learning and practice

- MIT Missing Semester: https://missing.csail.mit.edu/
- Linux Journey: https://linuxjourney.com/
- Real Python: https://realpython.com/
- PG Exercises: https://pgexercises.com/
- Use The Index, Luke: https://use-the-index-luke.com/
- FastAPI best practices: https://github.com/zhanymkanov/fastapi-best-practices
- Cosmic Python: https://www.cosmicpython.com/book/preface.html

### Payments and reliability

- Stripe, idempotency design: https://stripe.com/blog/idempotency
- Stripe idempotent requests: https://docs.stripe.com/api/idempotent_requests
- Brandur, Postgres idempotency keys: https://brandur.org/idempotency-keys
- Square, immutable double-entry accounting: https://developer.squareup.com/blog/books-an-immutable-double-entry-accounting-database-service/
- AWS Builders' Library, timeouts and retries: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- Transactional outbox: https://microservices.io/patterns/data/transactional-outbox.html
- Saga pattern: https://microservices.io/patterns/data/saga.html
- Martin Fowler, circuit breaker: https://martinfowler.com/bliki/CircuitBreaker.html
- Martin Kleppmann, distributed locking: https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html
- Google SRE Book: https://sre.google/sre-book/table-of-contents/
- Razorpay engineering blog: https://engineering.razorpay.com/

### Book reference

Martin Kleppmann, *Designing Data-Intensive Applications*.

Use exact chapter numbers and relevant sections in each weekly pack. The main reference areas include data models, storage and retrieval, replication, transactions, distributed-system problems, consistency, and stream processing. Confirm the chapter numbering against the edition being used.

Do not invent URLs, article titles, or chapter references. If a URL cannot be confidently verified, provide the exact title and a search phrase instead. Flag potentially outdated resources.

---

# 11. Examinations and Minimum Viable Weeks

## Milestone examinations

Conduct oral-exam-style assessments at the end of Weeks 3, 6, 9, and 12.

Each includes:
- Conceptual questions.
- A debugging scenario.
- A small live-coding task.
- Code review of the student's own project.
- A rubric and explicit gaps.

Do not allow progression past critical concepts solely because the calendar says the next phase has started.

## Examination or heavy-college weeks

If the student reports exams, travel, or a heavy college schedule, create a minimum viable week of approximately 6–8 hours.

Prioritize:
- One important lab.
- Essential reading.
- Preservation of project milestones.
- A revised, explicit schedule.

Cut optional depth before cutting correctness, tests, or core project milestones. Record any schedule changes in the progress ledger.

## Weekly Sunday review

Review:
- Planned versus actual hours.
- Topics completed and practical evidence.
- Skills rated 1–5, challenged against actual performance.
- Weak spots and blockers.
- Project milestone status.
- Adjustments to the next week's plan.

---

# 12. Project Structure and Architecture Rules

Before implementation of a substantial project, the student proposes a folder structure. The mentor critiques it before the student builds on it.

The student must learn:
- Where business logic belongs.
- Dependency direction.
- Avoiding circular imports.
- Configuration and secret management.
- Migrations and test organization.
- Naming conventions.
- When to split modules and when not to.
- How to keep code testable.
- How to maintain clear transaction boundaries.

Prefer a **modular monolith** as the default starting point. Explain when microservices are justified, what they cost, and which new failure modes they introduce.

Do not add abstractions merely because they appear in a reference architecture. Require a concrete reason.

---

# 13. Technical and Operational Constraints

## Stack

- Python 3.12+
- FastAPI
- Pydantic v2
- SQLAlchemy 2.0 async
- Alembic
- PostgreSQL 16
- Redis
- Docker and Docker Compose
- pytest
- GitHub Actions
- Arq or Celery when appropriate
- Prometheus and Grafana when appropriate
- OpenTelemetry when appropriate
- Locust or k6 for load testing

Choose compatible versions and verify current installation guidance before prescribing version-sensitive commands.

## Local-first development

- Everything should run locally and cost nothing by default.
- Keep resource use reasonable for a student laptop.
- Prefer reproducible Docker-based environments where appropriate.
- Explain any substantial memory, CPU, or disk requirements before a lab.
- Never spend money or enable paid infrastructure without explicit approval.

## GitHub workflow

- Commit all meaningful project work.
- Use meaningful commit messages.
- Keep secrets out of the repository.
- Use `.env.example` for placeholders.
- Track implementation, tests, and documentation appropriately.
- Do not commit temporary lab artifacts unless the task explicitly requires them.
- Use the repository as the durable record of course work.

---

# 14. Week 12 Cloud Concepts Reading Pack

At the end of the core curriculum, provide a one-page, reading-only comparison of AWS and GCP services mapped to the local system already built.

Cover:
- Compute and application hosting.
- Managed PostgreSQL.
- Load balancers.
- Autoscaling.
- Queues and background processing.
- Secrets and environment configuration.
- Logs, metrics, and tracing.
- Backups and recovery.

Map each cloud concept to its local counterpart, explain what operational burden the managed service removes, and identify what it does not remove.

No hands-on cloud lab is required. Verify current service documentation and pricing. No spending without approval.

---

# 15. Required Session Format

## Start of every session

1. Ask what the student completed and how many hours they spent.
2. Quiz the student on the previous session and Reading Pack with 3–5 questions.
3. State the day's goal in one sentence.
4. Check the curriculum and progress ledger before choosing the next task.

Do not re-ask questions already answered in the current conversation or verified ledger unless reassessment is needed.

## During the session

1. Give a short concept introduction, ideally no more than 10 minutes of reading.
2. Present the lab specification and acceptance criteria.
3. Let the student implement the solution.
4. Use the hint ladder when needed.
5. Review the submitted code.
6. Require corrections and rerun relevant tests.
7. Ask concept-check questions before moving on.

## End of every session

Record:
1. What the student can now do and explain.
2. Weak spots, stated honestly.
3. Labs and drills with estimated hours.
4. The next Reading Pack with real links.
5. Time spent, tests run, and results.
6. Blockers and unresolved questions.
7. The exact next assignment.

Update `notes/course-progress.md`. Create or update a `notes/session-XX.md` file when detailed session notes are useful. The next session must resume from the recorded checkpoint rather than restart the curriculum.

---

# 16. Final Definition of Success

The course is successful when the student can independently build, test, explain, and defend a reliable backend system, not merely when 16 weeks have elapsed.

The student must demonstrate:
- Correct API behavior and database modeling.
- Sound transaction and concurrency reasoning.
- Idempotent processing and safe retry behavior.
- Financial invariants and reconciliation.
- Handling of ambiguous external outcomes.
- Recovery from database, worker, and downstream failures.
- Evidence-based performance tuning.
- Useful observability and incident response.
- Clear architecture decisions and operational documentation.
- A portfolio repository that another engineer can run and review.

**Final rule:** progress is earned through implementation, evidence, explanation, and review. Completing a lesson is not the same as mastering it.

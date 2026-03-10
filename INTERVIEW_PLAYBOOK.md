# AI Pair Programming Playbook

## Opening Script

"I'll start by clarifying requirements and sketching a minimal design before generating code.
I prefer to direct AI in small steps so I can verify each piece."

---

## Workflow

### 1. Clarify
Ask lightweight coding-oriented questions:
- What interface should this expose?
- Should this be a library, CLI, or small app?
- Any performance constraints?
- Should I optimize for extensibility?

### 2. Restate
Restate the problem in one or two sentences.

### 3. Requirements
Write:
- core functionality
- constraints
- edge cases
- likely follow-ups

### 4. Design
Define:
- classes/modules
- responsibilities
- data structures
- extensibility points

### 5. Project Structure
Create files deliberately.

### 6. Implement Incrementally
Do not ask AI for the entire solution.
Ask for:
- one class
- one function
- one test file
- one refactor

### 7. Verify Constantly
After every generation:
- read code
- run tests
- run a quick sanity check
- clean names if needed

### 8. Narrate
Before prompting:
- what you are asking for
- why you are asking for it
After generation:
- what the code does
- whether it matches your intent

### 9. Adapt to Follow-ups
Do not rewrite from scratch.
Extend the design.

### 10. Finish Strong
- tests pass
- remove obvious mess
- summarize tradeoffs
- mention production improvements

---

## Rules

- I drive, AI assists
- Prefer simple and modular over clever
- Keep code always executable
- Tests are part of implementation
- Explain AI output before trusting it

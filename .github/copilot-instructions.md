## Purpose
This repo contains a small Python game and a static portfolio site. These instructions give an AI coding agent focused, actionable context so it can make safe, useful edits without noisy or generic suggestions.

## Repo snapshot (relevant files)
- `rps.py` — single-file Python Rock-Paper-Scissors game (interactive CLI). Fixes and improvements should preserve the simple script/run UX.
- `README.md` — short project description.
- `portfolio/index.html` — static personal portfolio site with inline JS and external CDN assets.

## How to run (developer workflows)
- Run the CLI game: `python3 rps.py` from the repository root. Do not assume packaging or dependencies.
- Preview the portfolio: open `portfolio/index.html` in a browser (no build step).

## Key patterns and project-specific conventions
- Keep changes minimal and file-local. This repo is small and uses simple scripts and static files; avoid introducing heavy frameworks or build tooling.
- `rps.py` is an interactive script that uses `input()` and `random.choice()`. When editing:
  - Preserve its CLI-first interaction model (no web endpoints or background services).
  - If extracting functions, add a small runner guard (`if __name__ == '__main__':`) so behaviour is unchanged for casual `python3 rps.py` runs.
  - Be conservative with refactors that change variable scope (e.g., `comp_choice`, `user_choice`, score counters). Prefer explicit parameters/returns over implicit global reads.
- `portfolio/index.html` uses CDN-hosted CSS/JS and inline scripts. When editing:
  - Keep external links intact unless fixing a broken URL. Example assets to reference: Google Fonts, AOS CSS/JS, Font Awesome.
  - Edit DOM/JS only for clear UI fixes; avoid adding build steps or bundlers.

## Examples (concrete actionable items)
- Fix a bug in `rps.py`: if changing game logic, make the change inside a well-scoped function and include a tiny run example in comments. E.g., change `win()` to accept `(user_choice, comp_choice)` and return a result, then call it from the main loop.
- Small UX improvements for `portfolio/index.html`: prefer non-invasive edits such as adding `rel="noopener"` to external links, or fixing a missing `alt` on images.

## Quality gates and testing
- There are no automated tests configured. For any substantive change include a manual verification note in the PR describing the steps you used (example: "Ran `python3 rps.py`, played 3 rounds with inputs X/Y/Z; scores updated as expected").

## PR guidance for the human reviewer
- Keep PR scope small (single logical change). Show short repro steps for interactive changes.
- For `rps.py` changes include before/after examples and a short rationale (bugfix, readability, or feature).

## Assumptions and constraints
- No CI or packaging is present. Changes should not add heavy dev-dependencies.
- This is a personal/learning repo—prioritize clarity and minimalism over production-grade infra.

If anything in this file is unclear or you'd like more targeted instructions (e.g., unit-test conventions to add, or a small test harness for `rps.py`), tell me which part to expand and I'll iterate.

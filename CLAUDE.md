# CLAUDE.md — Premier League Match Model

## Who I am
- Cole McCort, senior Business Administration + Finance double major.
- **I have no prior Python experience.** I'm learning as I build.
- Huge Premier League fan; Tottenham Hotspur supporter.

## What this project is
A statistical model of Premier League matches, built as a **portfolio piece for finance job applications**. End goals:
1. Pre-match probabilities for win/draw/loss and the full scoreline distribution
2. Goalscorer probabilities and match-event probabilities (cards, corners)
3. Player profiles: strengths, weaknesses and style, based on statistics
4. A chess.com-style "eval bar" using Expected Threat (xT) / possession value
5. A Monte Carlo match simulator whose predictions are compared to real results and to the betting market

Full phase plan: see `ROADMAP.md`.

## How to work with me (most important)
- **Explain everything you write.** After creating or changing a file, give a short plain-English walkthrough: what it does, why this approach, and what each key section is for.
- **Teach, don't just do.** When a new concept comes up (a pandas operation, Poisson distribution, log loss, calibration), explain it simply with a soccer example.
- **Small steps.** Build one piece at a time and run it before moving on. Avoid big multi-file changes I can't follow.
- **Check my understanding.** Occasionally ask me to predict what code will output or explain a step back to you.
- **Point out my mistakes directly**, including flawed logic or statistical reasoning, and walk me through the fix.
- **Prefer simple, readable code** over clever code. Clear names, comments on the "why", no unnecessary abstraction.
- After each session, suggest 2–4 lines for me to add to `LEARNING_LOG.md`.

## Statistical rules
- **No look-ahead.** A prediction for a match may only use data available before kickoff. Flag any leakage immediately.
- Evaluate with **log loss, Brier score and calibration charts**, not just "% correct".
- Always compare against **bookmaker probabilities with the margin removed** as the benchmark.
- Use minimum-minutes thresholds for player stats; flag small samples.
- Outputs are **probabilities**, never single "picks".

## Tech stack
- Python 3, pandas, numpy, scipy/statsmodels, matplotlib/plotly
- Streamlit for the final dashboard
- Git + GitHub. Commit after each working step with a clear message.

## Data sources
- football-data.co.uk: historical results + bookmaker odds (free)
- Understat: team/shot xG (free)
- StatsBomb Open Data: event data for the xT eval bar (free)
- Paid API (API-Football or Sportmonks) from Phase 5. Decide after free trials.
- Raw downloads go in `data/raw/` and are never edited by hand; cleaned data goes in `data/processed/`.

## Project structure (target)
```
pl-match-model/
├── CLAUDE.md
├── ROADMAP.md
├── LEARNING_LOG.md
├── README.md
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/        # exploration
├── src/              # reusable code (loading, models, evaluation, simulation)
├── predictions/      # weekly pre-kickoff prediction log
└── app/              # Streamlit dashboard
```

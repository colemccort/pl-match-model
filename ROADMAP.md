# Roadmap — Premier League Match Model

Pace assumption: ~5–6 hours/week alongside classes.
Guiding principle: **start logging pre-kickoff predictions as early as possible.** A season-long, timestamped record vs. the betting market is the strongest portfolio evidence.

## Phase 0: Setup (week 1)
- [x] Create GitHub account + empty repo `pl-match-model`
- [x] Install VS Code and Claude Code; have Claude Code walk through installing Python and setting up the folder
- [x] Add `CLAUDE.md`, `ROADMAP.md`, `LEARNING_LOG.md` to the repo
- **Done when:** Claude Code runs in the folder and the first commit is on GitHub.

## Phase 1: Python warm-up (weeks 1–3)
- [ ] Download 5 seasons of PL CSVs from football-data.co.uk (results + odds)
- [ ] Spurs home vs. away record over 5 seasons
- [ ] League-wide home advantage
- [ ] Goals-per-game distribution
- [ ] Three charts, each described in plain English in the learning log
- **Done when:** I can explain every line of my analysis without looking it up.
- **Learn:** pandas DataFrames, filtering, grouping, basic charts.

## Phase 2: First predictor (weeks 3–6)
- [ ] Poisson model: attack/defense strength + home advantage, from goals
- [ ] Backtest: predict 2024/25 match by match using only prior data
- [ ] Evaluate: log loss, Brier score, calibration chart
- [ ] Convert odds to margin-free probabilities; compare against the model
- **Done when:** one table "my model vs. the market" that I can explain.
- **Learn:** probability distributions, backtesting, model evaluation.

## Phase 3: Upgrade to xG (weeks 6–9)
- [ ] Pull team xG from Understat
- [ ] Dixon-Coles model with recency weighting
- [ ] Output full scoreline probability grids
- [ ] **Start the weekly pre-kickoff prediction log** (`predictions/`)
- **Done when:** the xG model beats the Phase 2 model on the same backtest, or I can explain why it doesn't.

## Phase 4: Player profiles (weeks 9–12)
- [ ] Per-90 stats with minimum-minutes cutoff
- [ ] Percentile ranks by position; radar charts (Spurs squad first)
- [ ] Cluster players into "styles"; sanity-check as a fan
- **Done when:** I can write a numbers-backed scouting paragraph on any Spurs player.

## Phase 5: Scorers, events, simulator (weeks 12–16)
- [ ] **Decision point:** choose paid API (API-Football vs. Sportmonks); verify lineups, player xG, cards in free trials
- [ ] Split team expected goals among players → anytime-scorer probabilities
- [ ] Card and corner models
- [ ] Monte Carlo simulator (10,000 runs/match)
- **Done when:** scorer probabilities are reasonably calibrated vs. outcomes.

## Phase 6: The eval bar (weeks 16–19)
- [ ] Build Expected Threat (xT) on StatsBomb Open Data
- [ ] Rank players by threat added (passes + carries)
- [ ] Eval-bar chart showing advantage swings across a full match
- **Done when:** one polished match visualization worth showing.

## Phase 7: Ship it (weeks 19–22, ~end of season)
- [ ] Streamlit dashboard: predictions, player profiles, eval bar
- [ ] README + write-up: question, data, method, results vs. market, limitations
- [ ] Add season-long prediction log results
- [ ] Add to resume and LinkedIn

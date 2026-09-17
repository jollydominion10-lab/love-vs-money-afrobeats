# Love vs Money: What Afrobeats Titles Talk About

A beginner data project. I asked whether Afrobeats song titles talk more about love or money.

## Question
Did titles use more love words or money words, and did that change after 2020?

## Data
`songs.csv` is a small practice list of well-known Afrobeats titles from 2017 to 2026.
It is not a full official chart dataset.

Love words counted: love, baby, heart, forever  
Money words counted: money, cash, rich, fund, dollar, pay

## Method
I used Python and pandas to label each title as love, money, both, or other, then compared 2017-2020 with 2021-2026.

## How to run
```bash
pip install -r requirements.txt
python analyze.py
```

## Findings
- Most titles were **other** (30 of 40). They did not use love or money words.
- Love titles: **8**
- Money titles: **2**
- After 2020, love titles were still more common than money titles (6 love, 2 money)
- Simple conclusion: in this sample, Afrobeats titles are usually not the words “love” or “money”. When they are, love shows up more than money.

## Limit
Titles are not the same as lyrics. A song called Calm Down can still be about love.

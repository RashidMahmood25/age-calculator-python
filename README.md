# Age Calculator (Python)

A small calculator that works out your exact age from your date of birth:
years, months and days, total days lived, the weekday you were born on,
and how many days until your next birthday.

## How to run

```bash
python3 age_calculator.py
```

Enter your date of birth as `YYYY-MM-DD`, for example `1998-05-14`.

## Example

Born `1998-05-14`, run on 2026-11-02:

- Age: 28 years, 5 months, 19 days
- Total days lived: 10,399
- Born on a Thursday
- Next birthday: 2027-05-14 (in 193 days)

## What was practiced

- Date arithmetic with Python's `datetime` module
- Calendar-correct age calculation (borrowing days and months)
- Leap-year handling, including 29 February birthdays (celebrated on
  28 February in non-leap years)
- Input validation with clear error messages

## Notes

- No real data is used — every figure is computed from the date you enter.

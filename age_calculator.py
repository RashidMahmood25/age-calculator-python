#!/usr/bin/env python3
"""Age calculator.

Given a date of birth, works out the exact age in years, months and days,
the total days lived, the weekday of birth, and the days until the next
birthday. Handles leap years correctly (including 29 February birthdays,
whose birthday falls on 28 February in non-leap years).

Run:  python3 age_calculator.py
"""

from datetime import date


def parse_date(text: str) -> date:
    """Parse a YYYY-MM-DD date, raising ValueError on bad input."""
    parts = text.strip().split("-")
    if len(parts) != 3:
        raise ValueError("Use the format YYYY-MM-DD, e.g. 1998-05-14.")
    year, month, day = (int(p) for p in parts)
    return date(year, month, day)


def _last_day_of_month(year: int, month: int) -> int:
    """Last day number of a given month (handles February leap years)."""
    if month == 12:
        return 31
    return (date(year, month + 1, 1) - date(year, month, 1)).days


def exact_age(born: date, today: date) -> tuple[int, int, int]:
    """Return (years, months, days) of age on `today`.

    Borrows days/months like a calendar, so leap years are handled by
    the datetime library itself.
    """
    if born > today:
        raise ValueError("Date of birth cannot be in the future.")
    years = today.year - born.year
    months = today.month - born.month
    days = today.day - born.day
    if days < 0:
        months -= 1
        prev_month = today.month - 1 or 12
        prev_year = today.year - 1 if today.month == 1 else today.year
        days += _last_day_of_month(prev_year, prev_month)
    if months < 0:
        years -= 1
        months += 12
    return years, months, days


def next_birthday(born: date, today: date) -> date:
    """Next birthday date on or after today.

    29 February birthdays are celebrated on 28 February in non-leap
    years.
    """
    try:
        candidate = date(today.year, born.month, born.day)
    except ValueError:  # 29 February in a non-leap year
        candidate = date(today.year, 2, 28)
    if candidate < today:
        try:
            candidate = date(today.year + 1, born.month, born.day)
        except ValueError:
            candidate = date(today.year + 1, 2, 28)
    return candidate


def main() -> None:
    print("=== Age Calculator ===")
    try:
        born = parse_date(input("Date of birth (YYYY-MM-DD): "))
    except ValueError as exc:
        print(f"Error: {exc}")
        return
    today = date.today()
    try:
        years, months, days = exact_age(born, today)
    except ValueError as exc:
        print(f"Error: {exc}")
        return
    upcoming = next_birthday(born, today)
    days_until = (upcoming - today).days

    print(f"\nYou were born on a {born.strftime('%A')}.")
    print(f"Your age: {years} years, {months} months, {days} days")
    print(f"Total days lived: {(today - born).days:,}")
    if days_until == 0:
        print("Happy birthday! Today is your birthday!")
    else:
        print(f"Next birthday: {upcoming} (in {days_until} days)")


if __name__ == "__main__":
    main()

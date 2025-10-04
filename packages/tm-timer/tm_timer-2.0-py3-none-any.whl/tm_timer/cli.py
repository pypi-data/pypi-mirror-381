# File: cli.py
import argparse
import atexit
import datetime
import json
import math
import os
import shutil
import sys
import termios
import threading
import time
import tty
from pathlib import Path

# --- Terminal helpers (kept minimal) ---
try:
    original_term_settings = termios.tcgetattr(sys.stdin.fileno())
except Exception:
    original_term_settings = None


def restore_terminal():
    if original_term_settings is None:
        return
    try:
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, original_term_settings)
    except Exception:
        pass


atexit.register(restore_terminal)


def with_raw_mode():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setraw(fd)
    return old_settings


def get_char():
    fd = sys.stdin.fileno()
    old_settings = with_raw_mode()
    try:
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


# --- Storage setup ---
DATA_DIR = Path(os.path.expanduser("~")) / ".tm_timer"
DATA_DIR.mkdir(parents=True, exist_ok=True)
DATA_FILE = DATA_DIR / "data.json"


def load_data():
    if not DATA_FILE.exists():
        return {"study": {}, "train": {}}
    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return {"study": {}, "train": {}}
    # Ensure keys
    if "study" not in data:
        data["study"] = {}
    if "train" not in data:
        data["train"] = {}
    return data


def save_data(data):
    tmp = DATA_FILE.with_suffix(".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    tmp.replace(DATA_FILE)


def get_day_seconds(activity, date_str):
    data = load_data()
    return int(data.get(activity, {}).get(date_str, 0))


def update_day_seconds(activity, date_str, seconds):
    data = load_data()
    data.setdefault(activity, {})
    data[activity][date_str] = int(seconds)
    save_data(data)


# --- Utility formatters and stats ---
def format_hms(total_seconds):
    total_seconds = int(round(total_seconds))
    h = total_seconds // 3600
    m = (total_seconds % 3600) // 60
    s = total_seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


def seconds_to_hours(seconds):
    return seconds / 3600.0


def compute_stats_for_activity(activity):
    data = load_data().get(activity, {})
    # Use values sorted by date
    seconds_list = [int(v) for k, v in sorted(data.items())]
    n = len(seconds_list)
    if n == 0:
        return {"n": 0, "avg": 0.0, "sd": 0.0, "hours_list": []}
    hours = [seconds_to_hours(s) for s in seconds_list]
    avg = sum(hours) / n
    if n < 2:
        sd = 0.0
    else:
        # population SD (divide by n)
        var = sum((x - avg) ** 2 for x in hours) / n
        sd = math.sqrt(var)
    return {"n": n, "avg": avg, "sd": sd, "hours_list": hours, "seconds_list": seconds_list}


def status_from_avg_sd(avg, sd):
    half = avg / 2.0
    if math.isclose(sd, half, rel_tol=1e-9, abs_tol=1e-9):
        return "Good"
    if sd > half:
        return f"Not Good - should be lower than {half:.2f}h"
    return "Very Good"


# --- Printing helpers ---
def print_activity_table(activity):
    data = load_data().get(activity, {})
    if not data:
        print(f"No entries for {activity.upper()}.")
        return
    # Sort by date descending (most recent first)
    items = sorted(data.items(), key=lambda kv: kv[0], reverse=True)
    print(f"\n| Today's Name | {activity.upper()} Hour |")
    print("| ------------ | ----------------- |")
    for date_str, secs in items:
        try:
            dt = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            day_name = dt.strftime("%a").upper()
        except Exception:
            day_name = date_str
        print(f"| {day_name} | {format_hms(secs)} |")
    stats = compute_stats_for_activity(activity)
    if stats["n"] < 2:
        print("\nNot enough recording for statistics (need 2+ days).")
    else:
        print(
            f"\n[AVG] = {stats['avg']:.2f}h    [Standard Deviation of Time] = {stats['sd']:.2f}h    Status = {status_from_avg_sd(stats['avg'], stats['sd'])}"
        )


def write_tables_md(path="tables.md"):
    data = load_data()
    lines = []
    for activity in ("study", "train"):
        lines.append(f"## {activity.upper()} Table\n")
        lines.append("| Date | Day | Time |\n")
        lines.append("| ---- | --- | ---- |\n")
        items = sorted(data.get(activity, {}).items(), key=lambda kv: kv[0], reverse=True)
        for date_str, secs in items:
            try:
                dt = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                day_name = dt.strftime("%a").upper()
            except Exception:
                day_name = ""
            lines.append(f"| {date_str} | {day_name} | {format_hms(secs)} |\n")
        stats = compute_stats_for_activity(activity)
        if stats["n"] < 2:
            lines.append("\nNot enough recording for statistics (need 2+ days).\n\n")
        else:
            lines.append(
                f"\n[AVG] = {stats['avg']:.2f}h    [Standard Deviation of Time] = {stats['sd']:.2f}h    Status = {status_from_avg_sd(stats['avg'], stats['sd'])}\n\n"
            )
    out_path = Path.cwd() / path
    out_path.write_text("".join(lines), encoding="utf-8")
    return str(out_path.resolve())


# --- Time parsing for countdown mode (compat) ---
import re


def parse_time_input(user_input):
    pattern = r"^\s*(?:(\d+)h)?\s*(?:(\d+)m)?\s*(?:(\d+)s)?\s*$"
    match = re.fullmatch(pattern, user_input.strip().lower())
    if not match or not any(match.groups()):
        raise ValueError("Invalid time format. Use format like '1h30m45s' or '25m' or '45s'.")
    hours = int(match.group(1)) if match.group(1) else 0
    minutes = int(match.group(2)) if match.group(2) else 0
    seconds = int(match.group(3)) if match.group(3) else 0
    return hours * 3600 + minutes * 60 + seconds


# --- Main run logic for activity timers (study/train) ---
def run_activity(activity):
    global running, paused
    running = True
    paused = False

    today = datetime.date.today()
    today_str = today.isoformat()
    stored_today = get_day_seconds(activity, today_str)

    # seconds_float holds the current day's accumulated seconds (float for delta accumulation)
    seconds_float = float(stored_today)

    # Show initial stats (before starting)
    stats_before = compute_stats_for_activity(activity)
    if stats_before["n"] >= 2:
        print(
            f"[Before] [AVG] = {stats_before['avg']:.2f}h    [Standard Deviation of Time] = {stats_before['sd']:.2f}h    Status = {status_from_avg_sd(stats_before['avg'], stats_before['sd'])}"
        )
    else:
        print("[Before] Not enough recordings to compute AVG/SD (need 2+ days).")

    # input listener thread
    def input_listener():
        global running, paused
        while running:
            key = get_char()
            if key.lower() == "p":
                paused = not paused
            elif key.lower() == "q":
                running = False
                break

    input_thread = threading.Thread(target=input_listener, daemon=True)
    input_thread.start()

    last_ts = time.time()
    current_day = today

    try:
        cols = shutil.get_terminal_size((80, 20)).columns
    except Exception:
        cols = 80

    while running:
        now_ts = time.time()
        prev_ts = last_ts
        last_ts = now_ts
        if not paused:
            prev_date = current_day
            now_date = datetime.date.fromtimestamp(now_ts)
            if now_date == prev_date:
                seconds_float += now_ts - prev_ts
            else:
                # crossed midnight. compute split: seconds before midnight go to prev_date, remainder to now_date
                midnight_ts = datetime.datetime.combine(now_date, datetime.time.min).timestamp()
                # seconds that belong to previous day
                seconds_to_prev = max(0.0, midnight_ts - prev_ts)
                seconds_float += seconds_to_prev
                # persist previous day
                update_day_seconds(activity, prev_date.isoformat(), int(round(seconds_float)))
                # For new day, start from previously stored seconds for that new day (if any)
                new_day_str = now_date.isoformat()
                stored_new_day = get_day_seconds(activity, new_day_str)
                # remaining seconds from this delta that belong to new day:
                seconds_for_new_day = max(0.0, now_ts - midnight_ts)
                seconds_float = float(stored_new_day) + seconds_for_new_day
                current_day = now_date

            # display
            disp_secs = int(round(seconds_float))
            hrs, rem = divmod(disp_secs, 3600)
            mins, secs = divmod(rem, 60)
            msg = f"Timer: {hrs:02d}:{mins:02d}:{secs:02d} [Press 'p' to Pause/Resume, 'q' to Quit]"

            if len(msg) >= cols:
                msg = msg[: cols - 1]
            sys.stdout.write(f"\r\033[K{msg}")
            sys.stdout.flush()
        time.sleep(0.2)

    # when stopped, persist current day's seconds
    try:
        update_day_seconds(activity, current_day.isoformat(), int(round(seconds_float)))
    except Exception as e:
        print("\nError saving data:", e)

    # final stats after save
    stats_after = compute_stats_for_activity(activity)
    print("\n\nTimer stopped.")
    if stats_after["n"] < 2:
        print("Not enough recordings to compute AVG/SD (need 2+ days).")
    else:
        print(
            f"[AVG] = {stats_after['avg']:.2f}h    [Standard Deviation of Time] = {stats_after['sd']:.2f}h    Status = {status_from_avg_sd(stats_after['avg'], stats_after['sd'])}"
        )


# --- Countdown/time-limited run (backwards compatible) ---
def run_countdown(target_seconds, target_input):
    global running, paused
    running = True
    paused = False
    seconds = 0

    def input_listener():
        global running, paused
        while running:
            key = get_char()
            if key.lower() == "p":
                paused = not paused
            elif key.lower() == "q":
                running = False
                break

    input_thread = threading.Thread(target=input_listener, daemon=True)
    input_thread.start()

    try:
        cols = shutil.get_terminal_size((80, 20)).columns
    except Exception:
        cols = 80

    while running and seconds < target_seconds:
        if not paused:
            mins, secs = divmod(seconds, 60)
            hours, mins = divmod(mins, 60)
            msg = f"Timer: {hours:02d}:{mins:02d}:{secs:02d} [Press 'p' to Pause/Resume, 'q' to Quit]"
            msg = msg[: cols - 1] if len(msg) >= cols else msg
            sys.stdout.write(f"\r\033[K{msg}")
            sys.stdout.flush()
            seconds += 1
        time.sleep(1)
    if seconds >= target_seconds:
        sys.stdout.write("\n\n⏰ Time's up! Target of {} reached.\n".format(target_input))
    restore_terminal()
    print("Timer stopped.")


# --- CLI entrypoint ---
def main():
    parser = argparse.ArgumentParser(description="tm_timer - terminal timer with study/train logging")
    parser.add_argument("--study", action="store_true", help="Run study timer (no limit until 'q')")
    parser.add_argument("--train", action="store_true", help="Run train timer (no limit until 'q')")
    parser.add_argument("--studystatus", action="store_true", help="Show study daily table and SD")
    parser.add_argument("--trainstatus", action="store_true", help="Show train daily table and SD")
    parser.add_argument("--tables", action="store_true", help="Export tables.md to current directory")
    parser.add_argument("duration", nargs="?", help="Optional duration e.g. 1h30m (if not using --study/--train)")
    args = parser.parse_args()

    # priority actions
    if args.studystatus:
        print_activity_table("study")
        return
    if args.trainstatus:
        print_activity_table("train")
        return
    if args.tables:
        out = write_tables_md("tables.md")
        print(f"created {out}")
        return

    if args.study:
        run_activity("study")
        return
    if args.train:
        run_activity("train")
        return

    # fallback: duration countdown (compat)
    if args.duration:
        try:
            target_seconds = parse_time_input(args.duration)
        except ValueError as e:
            print(e)
            sys.exit(1)
        run_countdown(target_seconds, args.duration)
    else:
        parser.print_help()


if __name__ == "__main__":
    try:
        main()
    finally:
        restore_terminal()


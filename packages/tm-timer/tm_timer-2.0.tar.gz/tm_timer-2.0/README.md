# In The Name of God

---

## ⏱ tm : Minimalistic Terminal-based timer with Study/Train tracking

### Features:

- Run from terminal:  
  - Countdown timer: `tm 10s`, `tm 25m`, `tm 1h30m`  
  - Study session: `tm --study` (tracks across sessions, resets daily)  
  - Train session: `tm --train` (tracks across sessions, resets daily)
- Daily study/train totals saved in `~/.tm_timer/data.json`
- Tables and statistics:
  - `tm --studystatus` / `tm --trainstatus` → show daily table and Standard Deviation
  - `tm --tables` → export `tables.md`
- Statistics:
  - Average daily hours
  - Standard Deviation of daily hours
  - Status report (Very Good / Good / Not Good)
- Controls:
  - Press `p` to pause/resume
  - Press `q` to quit early
- Supports human durations like `2h45m30s`
- Simple, no graphical BLOAT.

---

### Installation:

```bash
sudo apt install pipx       # if not installed
pipx install tm-timer       # to install tm-timer
pipx ensurepath             # to add tm to PATH
exec $SHELL                 # reload shell

#or run locally with using cli.py
python3 cli.py 3h40m
```

Example Usage:
bash
Copy code
tm --study
# Timer starts, press 'q' to stop, progress saved daily

tm --studystatus
# Shows study table and stats

tm --tables
# Exports study/train tables as tables.md
⏱ tm preview:


import time

class Profiler:
    def __init__(self):
        self.t = {}
        self.order = []

    def add(self, key, dt):
        self.t[key] = self.t.get(key, 0.0) + dt
        if key not in self.order:
            self.order.append(key)

    def section(self, key):
        return Section(self, key)

    def total(self):
        return sum(self.t.values())

    def as_sorted(self):
        return sorted(self.t.items(), key=lambda kv: kv[1], reverse=True)

class Section:
    def __init__(self, prof: 'Profiler', key: str):
        self.prof = prof
        self.key = key
        self.t0 = None
    def __enter__(self):
        self.t0 = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc, tb):
        dt = time.perf_counter() - self.t0
        self.prof.add(self.key, dt)

def _fmt_secs(s): return f"{s:.6f}s"

def _print_profile(title, prof: Profiler):
    total = prof.total()
    print(f"\n[{title}]  total = {_fmt_secs(total)}")
    for k, v in prof.as_sorted():
        pct = 100.0 * v / (total if total > 0 else 1.0)
        print(f"  {k:28s} {_fmt_secs(v):>12}  ({pct:5.1f}%)")

# profiling.py
import time

class Profiler:
    """
    Nest-safe profiler that records EXCLUSIVE time per section.
    Use with: with prof.section("name"): ...
    """
    def __init__(self):
        self.t = {}           # exclusive time per key
        self.order = []       # first-seen order
        self._stack = []      # active Section objects (nesting)

    def add(self, key, dt):
        self.t[key] = self.t.get(key, 0.0) + dt
        if key not in self.order:
            self.order.append(key)

    def section(self, key):
        return Section(self, key)

    def _push(self, sect): self._stack.append(sect)

    def _pop(self, sect, end_time):
        # exclusive: total - children
        if not self._stack or self._stack[-1] is not sect:
            dt_excl = end_time - sect.t0 - sect._children_time
        else:
            self._stack.pop()
            dt_excl = end_time - sect.t0 - sect._children_time
        self.add(sect.key, dt_excl)
        if self._stack:
            parent = self._stack[-1]
            parent._children_time += (end_time - sect.t0)

    def total(self): return sum(self.t.values())
    def as_sorted(self): return sorted(self.t.items(), key=lambda kv: kv[1], reverse=True)

class Section:
    def __init__(self, prof: 'Profiler', key: str):
        self.prof = prof; self.key = key
        self.t0 = None; self._children_time = 0.0
    def __enter__(self):
        self.t0 = time.perf_counter()
        self.prof._push(self)
        return self
    def __exit__(self, exc_type, exc, tb):
        t1 = time.perf_counter()
        self.prof._pop(self, t1)

def _fmt_secs(s): return f"{s:.6f}s"

def print_profile(title, prof: Profiler):
    total = prof.total()
    print(f"\n[{title}]  total (exclusive sum) = {_fmt_secs(total)}")
    for k, v in prof.as_sorted():
        pct = 100.0 * v / (total if total > 0 else 1.0)
        print(f"  {k:28s} {_fmt_secs(v):>12}  ({pct:5.1f}%)")

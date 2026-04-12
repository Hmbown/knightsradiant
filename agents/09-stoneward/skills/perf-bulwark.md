# Perf Bulwark

Isolate and harden a real performance bottleneck without drifting into benchmark theater.

## When to invoke

- Latency or throughput is regressing on a known path.
- Memory or CPU usage is climbing in production-like workloads.
- A critical optimization must be justified and guarded.

## Inputs required

- Target path or system
- Baseline metrics or current pain signals
- Representative workload shape
- Profiling or tracing tools available

## Procedure

1. Define the success metric and representative workload before touching code.
2. Capture a baseline with profiling, tracing, or benchmark harnesses that resemble real concurrency, payload sizes, and cache state.
3. Rank hotspots by measured cost rather than intuition.
4. Change one variable at a time and rerun the same workload so comparisons are trustworthy.
5. Record the tradeoffs: memory, complexity, tail latency, fairness, or failure behavior.
6. Add a regression benchmark or alert so the gain does not silently evaporate.

## Output shape

- Baseline summary
- Hotspot analysis
- Changes tested
- Before-and-after measurements
- Tradeoffs
- Regression guard added

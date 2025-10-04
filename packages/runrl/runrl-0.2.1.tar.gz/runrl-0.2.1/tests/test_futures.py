import itertools

from runrl.futures import FutureState, RunRLPollingFuture


def test_future_blocks_until_completion():
    sequence = iter([
        {"status": "PENDING"},
        {"status": "RUNNING"},
        {"status": "RUNNING"},
        {"status": "COMPLETED"},
    ])

    first = next(sequence)

    def poller():
        return next(sequence)

    state = FutureState(
        initial=first,
        poller=poller,
        is_terminal=lambda r: r["status"] in {"COMPLETED", "FAILED", "CANCELLED"},
        is_success=lambda r: r["status"] == "COMPLETED",
        poll_interval=0.0,
        max_timeout=1,
    )

    future = RunRLPollingFuture(state)
    result = future.result()
    assert result["status"] == "COMPLETED"

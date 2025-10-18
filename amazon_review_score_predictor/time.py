from time import time
from typing import Any, Callable, TypeVar

R = TypeVar("R")

class TimeUtils:
  """Timing utilities.

  Provides static helpers to measure and report execution time.
  """

  @staticmethod
  def print_elapsed_minutes(start_time: float) -> None:
    """Print the elapsed time in minutes since ``start_time``.

    Args:
      start_time: Start timestamp as returned by ``time()``.

    Example:
      >>> start = time()
      >>> # ... run some work ...
      >>> TimeUtils.print_elapsed_minutes(start)
      0.42 min
    """
    minutes_count = (time() - start_time) / 60
    print(f"{minutes_count:.2f} min")

  @staticmethod
  def calculate_execution_time(func: Callable[..., R], *args: Any) -> R:
    """
    Run a callable, print the elapsed time in minutes, and return its result.

    Args:
      func: Function to execute.
      *args: Positional arguments for the function.

    Returns:
      The return value of `func`.

    Example:
      result = TimeUtils.calculate_execution_time(my_fn, 1, 2)
    """
    start_t = time()
    result: R = func(*args)
    minutes_count = (time() - start_t) / 60
    print(f"{minutes_count:.2f} min")
    return result

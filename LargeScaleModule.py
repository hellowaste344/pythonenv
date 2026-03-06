from __future__ import annotations, print_function, unicode_literals
import __future__

import asyncio
import sys
import time
from typing import Callable, Optional

print(__future__.all_feature_names)

# without __future__ 2.x python compiler will raise an error
print("Welcome", "My Darkness", sep=" To ")

# 2.x python compiler = <type 'str'>
print(type("xashe"))
# new python versions = <type 'unicode'>
print(type("xashe"))


name = "Lóuis"
print(name.encode("utf8"))


def execute(func: Callable[[int, int], int]) -> int:
    return func(2, 3)


def add(a: int, b: int) -> int:
    return a + b


result = execute(add)
print(result)


def find_user(user_id: int) -> Optional[str]:
    if user_id == 0:
        return "root"
    if user_id == 1:
        return "admin"
    return None


async def normal_input():

    start = time.perf_counter()

    # run blocking input() in a seperate thread
    s = await asyncio.to_thread(input)
    s = s.strip()

    end = time.perf_counter()

    sys.stdout.write(f"\nTime taken in Normal I/O:{end - start:.10f}")


async def fast_input():

    start = time.perf_counter()

    # run blocking buffer read in thread
    s = list(map(str, (await asyncio.to_thread(sys.stdin.readline)).split()))

    end = time.perf_counter()

    sys.stdout.write(f"\nTime taken in Fast I/O:{end - start:.10f}")


if __name__ == "__main__":
    asyncio.run(fast_input())
    asyncio.run(normal_input())

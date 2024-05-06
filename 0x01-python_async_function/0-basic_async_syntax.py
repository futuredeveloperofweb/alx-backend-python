#!/usr/bin/env python3
'''The basics of async modul'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''waits for a random delay between 0 and max_delay
    seconds and eventually returns it.
    '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time

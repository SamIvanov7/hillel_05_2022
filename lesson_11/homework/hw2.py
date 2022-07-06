import asyncio

# def get_primes_amount(num: int) -> int:
#     result = 0
#     for i in num:
#         counter = 0
#         for j in range(1, i):
#             if i % j == 0:
#                 counter += 1
#             if counter > 2:
#                 break
#         results += 1

#     return results

# numbers = [40000, 400, 1000000, 700]

# for i in numbers:
#     print(i)

# NOTE: Well, this realization takes too much time...
#       Would be great if I can see less numbers earlier that great numbers :)

# TODO: Complete get_primes_amount function
# TODO: Make this function asyncronous to compute less numbers faster


async def get_primes_amount(num: int) -> int:
    res = 1
    for i in range(2, num + 1):
        if i % 2 == 0:
            pass
        else:
            res += 1
            for j in range(2, i):
                if i % j == 0:
                    res -= 1
                    break
        await asyncio.sleep(0)
    print(res)

    return res


numbers = [40000, 400, 10000, 700, 50]
tasks = [
    get_primes_amount(
        i,
    )
    for i in numbers
]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*tasks))
loop.close()

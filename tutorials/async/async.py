import asyncio

# using
# async/await keywords. Introduced in Python 3.5,

# Two options to declare a function async
# methods does the same function
# NOTE: an async method is known as a coroutine

# method 1
# async def do_task_async():
#     pass
#
# # method 2
# @asyncio.coroutine
# def do_this_async():
#     pass


# precede aync func with await keyword to invoke
# NOTE: async keyword can be use within a async method

# async def do_work_async():
#     return await do_task_async()


# async def get_chat_id(name):
#     await asyncio.sleep(3)
#     return "chat-%s" % name
#
#
# async def main():
#     asyncio.ensure_future(get_chat_id("django"))
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main)
# for index in range(10):
#     print_test(index)


async def async_foo():
    print("async_foo started")
    await asyncio.sleep(1)
    print("async_foo done")


async def main():
    asyncio.ensure_future(async_foo())  # fire and forget async_foo()

    # btw, you can also create tasks inside non-async funcs

    print('Do some actions 1')
    await asyncio.sleep(1)
    print('Do some actions 2')
    await asyncio.sleep(1)
    print('Do some actions 3')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
for index in range(10):
    print(index)

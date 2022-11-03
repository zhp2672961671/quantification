# import asyncio
# import time
# # 我们通过async关键字定义一个协程,当然协程不能直接运行，需要将协程加入到事件循环loop中
# async def do_some_work(x):
#     print("waiting:", x)
#     return "Done after {}s".format(x)
# def callback(future):
#     print("callback:",future.result())

# start = time.time()

# coroutine = do_some_work(2)
# loop = asyncio.get_event_loop()        # asyncio.get_event_loop：创建一个事件循环
# # 通过loop.create_task(coroutine)创建task,同样的可以通过 asyncio.ensure_future(coroutine)创建task
# task = loop.create_task(coroutine)     # 创建任务, 不立即执行
# task.add_done_callback(callback)   # 绑定回调，在task执行完成的时候可以获取执行的结果
# loop.run_until_complete(task)         # 使用run_until_complete将协程注册到事件循环，并启动事件循环
# print("Time:",time.time() - start)
# 使用协程并发执行只花费4秒
# import asyncio
# import time

# async def do_some_work(x):
#     print("Waiting:",x)
#     await asyncio.sleep(x)
#     return "Done after {}s".format(x)

# start = time.time()

# coroutine1 = do_some_work(1)
# coroutine2 = do_some_work(2)
# coroutine3 = do_some_work(4)

# tasks = [
#     asyncio.ensure_future(coroutine1),#通过 asyncio.ensure_future(coroutine)创建task
#     asyncio.ensure_future(coroutine2),
#     asyncio.ensure_future(coroutine3)
# ]

# loop = asyncio.get_event_loop() # asyncio.get_event_loop：创建一个事件循环
# loop.run_until_complete(asyncio.wait(tasks)) # 使用run_until_complete将协程注册到事件循环，并启动事件循环

# for task in tasks:
#     print("Task ret:",task.result())

# print("Time:",time.time() - start)

# 1. 使用async可以定义协程，协程用于耗时的io操作，我们也可以封装更多的io操作过程
# 2. 这样就实现了嵌套的协程，即一个协程中await了另外一个协程，如此连接起来。import asyncio
# import time
# import asyncio

# async def do_some_work(x):
#     print("waiting:",x)
#     await asyncio.sleep(x)
#     return "Done after {}s".format(x)

# async def main():
#     coroutine1 = do_some_work(1)
#     coroutine2 = do_some_work(2)
#     coroutine3 = do_some_work(4)
#     tasks = [
#         asyncio.ensure_future(coroutine1),
#         asyncio.ensure_future(coroutine2),
#         asyncio.ensure_future(coroutine3)
#     ]

#     dones, pendings = await asyncio.wait(tasks)
#     for task in dones:
#         print("Task ret:", task.result())

#     # results = await asyncio.gather(*tasks)
#     # for result in results:
#     #     print("Task ret:",result)


# start = time.time()

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# print("Time:", time.time() - start)
# '''
# waiting: 1
# waiting: 2
# waiting: 4
# Task ret: Done after 1s
# Task ret: Done after 2s
# Task ret: Done after 4s
# Time: 4.003407716751099
# '''
# 或者返回使用asyncio.wait方式挂起协程
# import asyncio
# import time

# async def do_some_work(x):
#     print("waiting:",x)
#     await asyncio.sleep(x)
#     return "Done after {}s".format(x)

# async def main():
#     coroutine1 = do_some_work(1)
#     coroutine2 = do_some_work(2)
#     coroutine3 = do_some_work(4)
#     tasks = [
#         asyncio.ensure_future(coroutine1),
#         asyncio.ensure_future(coroutine2),
#         asyncio.ensure_future(coroutine3)
#     ]
#     return await asyncio.wait(tasks)

# start = time.time()

# loop = asyncio.get_event_loop()
# done,pending = loop.run_until_complete(main())
# for task in done:
#     print("Task ret:",task.result())

# print("Time:", time.time() - start)
# '''
# waiting: 1
# waiting: 2
# waiting: 4
# Task ret: Done after 1s
# Task ret: Done after 2s
# Task ret: Done after 4s
# Time: 4.002181529998779
# '''
# import time
# import asyncio

# async def job(t):            # 使用 async 关键字将一个函数定义为协程
#     await asyncio.sleep(t)   # 等待 t 秒, 期间切换执行其他任务
#     print('用了%s秒' % t)

# async def main(loop):           # 使用 async 关键字将一个函数定义为协程
#     tasks = [loop.create_task(job(t)) for t in range(1,3)]  # 创建任务, 不立即执行
#     await asyncio.wait(tasks)   # 执行并等待所有任务完成

# start = time.time()
# loop = asyncio.get_event_loop()      # 创建一个事件loop
# loop.run_until_complete(main(loop))  # 将事件加入到事件循环loop
# loop.close()                         # 关闭 loop

# print(time.time()-start)
# '''
# 用了1秒
# 用了2秒
# 2.0013420581817627
# '''
# class Weekday():
#     monday = 1
#     tuesday = 2
#     wednesday = 3
#     thirsday = 4
#     friday = 5
#     saturday = 6
#     sunday = 7

# print(Weekday.wednesday)    #  3
# class Weekday():
#     monday = 1
#     tuesday = 2
#     wednesday = 3
#     thirsday = 4
#     friday = 5
#     saturday = 6
#     sunday = 7
#     wednesday = 333

# print(Weekday.wednesday)    #  333
# Weekday.wednesday = "星期三"
# print(Weekday.wednesday)    #  星期三
# from enum import Enum
# class Weekday(Enum):
#     monday = 1
#     tuesday = 2
#     wednesday = 3
#     thirsday = 4
#     friday = 5
#     saturday = 6
#     sunday = 7

# print(Weekday.wednesday)         # Weekday.wednesday
# print(type(Weekday.wednesday))   # <enum 'Weekday'>
# print(Weekday.wednesday.name)    # wednesday
# print(Weekday.wednesday.value)   # 3

# from enum import Enum
# class Weekday(Enum):
#     monday = 1
#     tuesday = 2
#     wednesday = 3
#     thirsday = 4
#     friday = 5
#     saturday = 6
#     sunday = 7

# Weekday.wednesday.label = "星期三"
# Weekday.wednesday.work = "完成假期作业"
# Weekday.wednesday.time = 10


# print(Weekday.wednesday.label)   # 星期三
# print(Weekday.wednesday.work)    # 完成假期作业
# print(Weekday.wednesday.time)    # 10

# from enum import Enum
# class Weekday(Enum):
#     monday = 1
#     tuesday = 2
#     wednesday = 3
#     thirsday = 4
#     friday = 5
#     saturday = 6
#     sunday = 7

# Weekday.wednesday.label = "星期三"
# Weekday.wednesday.work = "完成假期作业"
# Weekday.wednesday.time = 10

# obj_1 = Weekday.wednesday
# print(obj_1.label)             # 星期三

# obj_2 = Weekday['wednesday']
# print(obj_1.label)             # 星期三

# obj_3 = Weekday(3)
# print(obj_3.label)             # 星期三

# from enum import Enum
# class Weekday(Enum):
#     monday = 1
#     tuesday = 2
#     wednesday = 3
#     thirsday = 4
#     friday = 5
#     saturday = 6
#     sunday = 7

# w = Weekday()
# print(w.wednesday)

# from enum import Enum
# class Weekday(Enum):
#     monday = 1
#     tuesday = 2
#     wednesday = 3
#     thirsday = 4
#     friday = 5
#     saturday = 6
#     sunday = 7

# obj_1 = Weekday.wednesday

# obj_2 = Weekday['wednesday']

# obj_3 = Weekday(3)

# print(obj_1==obj_2==obj_3)      # True

# print(obj_1 is obj_2 is obj_3)  # True

# from enum import Enum
# class Weekday(Enum):
#     monday = 1
#     tuesday = 2
#     wednesday = 3
#     thirsday = 4
#     friday = 5
#     saturday = 6
#     sunday = 7
#     test = 3


# print(Weekday.test.value)    # 3


# from enum import Enum, unique
# @unique
# class Weekday(Enum):
#     monday = 1
#     tuesday = 2
#     wednesday = 3
#     thirsday = 4
#     friday = 5
#     saturday = 6
#     sunday = 7
#     test = 3



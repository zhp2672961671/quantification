from binance.client import Client, AsyncClient  # noqa
import asyncio
async def main():

    # initialise the client
    client = await AsyncClient.create("15979876228", "zhp2672961671", testnet=True,)
    res = await client.get_exchange_info()
    print("res=======",res)
    await client.close_connection()

if __name__ == "__main__":
# 创建一个事件循环，然后使用run_until_complete将协程注册到事件循环，并启动事件循环
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
import os
import asyncio
import aiofiles
import redis
import time
import sys


REDIS_HOST = "localhost"
REDIS_PORT = 6379
DATA_FOLDER = "data"


redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)


async def read_file_async(file_path):
    async with aiofiles.open(file_path, "r", encoding="utf-8") as file:
        return await file.read()


async def process_file(filename):
    file_path = os.path.join(DATA_FOLDER, filename)

    if os.path.isfile(file_path):
        content = await read_file_async(file_path) 
        await asyncio.to_thread(redis_client.set, filename, content)  
        print(f"✅ Inserted {filename} into Redis")


async def main(): 
    if not os.path.exists(DATA_FOLDER):
        print("⚠️ Data folder not found. Skipping data insertion.")
        sys.exit(1)

    # start_time = time.time()
    tasks = [process_file(filename) for filename in os.listdir(DATA_FOLDER)]
    await asyncio.gather(*tasks)

    # end_time = time.time()
    # elapsed_time = end_time - start_time

    print(f"🎉 Successfully inserted {len(tasks)} files into Redis!")
    # print(f"🕒 Total execution time: {elapsed_time:.3f} seconds")


asyncio.run(main())

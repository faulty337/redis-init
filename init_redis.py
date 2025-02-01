import os
import asyncio
import aiofiles
import redis
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
        file_key, _ = os.path.splitext(filename)

        await asyncio.to_thread(redis_client.set, file_key, content)

        print(f"✅ Inserted {file_key} into Redis")


async def main(): 
    if not os.path.exists(DATA_FOLDER):
        print("⚠️ Data folder not found. Skipping data insertion.")
        sys.exit(1)

    tasks = [process_file(filename) for filename in os.listdir(DATA_FOLDER)]
    await asyncio.gather(*tasks)


    print(f"🎉 Successfully inserted {len(tasks)} files into Redis!")


asyncio.run(main())

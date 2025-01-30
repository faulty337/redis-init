import os
import json
import subprocess
import sys

try:
    import redis
except ImportError:
    print("❌ Redis library not found. Installing now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "redis"])
    import redis  


redis_host = "localhost"
redis_port = 6379
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

data_folder = "data"


if not os.path.exists(data_folder):
    print("⚠️ Data folder not found. Skipping data insertion.")
    sys.exit(1)


file_count = 0
for filename in os.listdir(data_folder):
    file_path = os.path.join(data_folder, filename)

    if os.path.isfile(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            value = file.read()
        
        redis_client.set(filename, value)
        file_count += 1
        print(f"✅ Inserted {filename} into Redis")

print(f"🎉 Successfully inserted {file_count} files into Redis!")

from telethon import TelegramClient
import asyncio
from datetime import datetime
import os

# 🔥 Thông tin đăng nhập từ biến môi trường
api_id = int(os.environ['API_ID'])  # Đảm bảo là số nguyên
api_hash = os.environ['API_HASH']
phone_number = os.environ.get('PHONE_NUMBER')  # Có thể cần dùng nếu đăng nhập OTP
group_id = -1002538394178  # Group ID dạng số nguyên

# Tạo client
client = TelegramClient('session_name', api_id, api_hash)

# Các lệnh muốn gửi
commands = [
    '/call 0388649762',
    '/call 0373763656',
    '/call 0945665569',
    '/call 0357889022',
    '/call 0868959378',
    '/call 0842395586',
    '/call 0384321145',
    '/call 0917616636',
    '/call 0973773070',
    '/call 0812876678',
    '/call 0934110136'
]

# Hàm lấy timestamp
def now():
    return datetime.now().strftime("[%H:%M:%S]")

# Hàm gửi lệnh
async def send_commands():
    for cmd in commands:
        await client.send_message(group_id, cmd)
        print(f"{now()} ✅ Đã gửi lệnh: {cmd}")
        await asyncio.sleep(5)  # Đợi 5 giây giữa các lệnh

# Hàm chính
async def main():
    await client.start(phone_number)
    print(f"{now()} ✅ Đăng nhập thành công!")

    print(f"{now()} 🚀 Bắt đầu gửi lệnh...")
    await send_commands()

# Chạy chương trình
with client:
    client.loop.run_until_complete(main())

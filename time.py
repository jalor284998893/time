import time

def pomodoro_timer(minutes):
    # 将时间从分钟转换为秒数
    seconds = minutes * 60 

    # 倒数计时器开始
    while seconds > 0:
        # 打印当前剩余时间（每分钟）
        print(f"Time remaining: {seconds//60} minutes {seconds%60} seconds ")
        time.sleep(1) # 等待1秒钟

        # 减少一秒钟
        seconds -= 1

    # 时间到了！
    print("Time's up!")

import time
from datetime import datetime
 
def print_time(seconds):
    """ 打印倒计时时间 """
    minutes, sec = divmod(seconds, 60)
    hour, minutes = divmod(minutes, 60)
    print(f"{int(hour):02d}:{int(minutes):02d}:{int(sec):02d}", end="\r")
 
def pomodoro_timer(work_time=25*60, break_time=5*60):
    """
    Pomodoro定时器
    :param work_time: 工作时长，单位为秒（默认25分钟）
    :param break_time: 休息时长，单位为秒（默认5分钟）
    """
    cycles = 0
    while True:
        print("开始工作!")
        for i in range(work_time, -1, -1):
            print_time(i)
            time.sleep(1)
        print("\n工作结束! 开始休息...")
        for i in range(break_time, -1, -1):
            print_time(i)
            time.sleep(1)
        cycles += 1
        print(f"\n休息结束! 已完成第 {cycles} 个Pomodoro循环。")
        input("按回车开始下一个循环...")  # 等待用户输入以开始下一个循环
 
if __name__ == "__main__":
    pomodoro_timer()

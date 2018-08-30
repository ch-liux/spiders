"""异步IO

do_some_code()
f = open('/path/to/file', 'r')
r = f.read() # <== 线程停在此处等待IO操作结果
# IO操作完成后线程才能继续执行:
do_some_code(r)

loop = get_event_loop()
while True:
    event = loop.get_event()
    process_event(event)

"""


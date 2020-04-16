import concurrent.futures

from common.colors import info


def threads(function, thread_count):
    """ Threadpool Uses """
    threads = concurrent.futures.ThreadPoolExecutor(
        max_workers=thread_count)
    confuture = (threads.submit(function))
    for i, _ in enumerate(concurrent.futures.as_completed(confuture)):
        print('%s Progress IN : %i' % (info, i + 1), end='\r')


print('')

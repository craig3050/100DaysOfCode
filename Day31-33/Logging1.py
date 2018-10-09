import sys
import logbook

app_log = logbook.Logger('App')


def main():
    print("This is a test of how to put together a log")
    _var = input("Give me a number")
    try:
        _var = int(_var) * 1000
        print(_var)
    except Exception as x:
        print(f"Oh that didn't work!: {x}")
        app_log.exception(x)
    finally:
        print("Thank's for stopping by")


def init_logging(filename: str = None):
    level = logbook.TRACE

    if filename:
        logbook.TimedRotatingFileHandler(filename, level=level).push_application()
    else:
        logbook.StreamHandler(sys.stdout, level=level).push_application()

    msg = 'Logging initialized, level: {}, mode: {}'.format(
        level,
        "stdout mode" if not filename else 'file mode: ' + filename
    )
    logger = logbook.Logger('Startup')
    logger.notice(msg)


if __name__ == '__main__':
    init_logging('test.log')
    main()



# gh-135511
# To make the exception message valid on idle
import io
import sys
import traceback
import contextlib
def get_message_lines(typ, exc, tb):
    "Return line composing the exception message."
    if typ in (AttributeError, NameError):
        # 3.10+ hints are not directly accessible from python (#44026).
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            sys.__excepthook__(typ, exc, tb)
        err_list = err.getvalue().split("\n")[1:]

        for i in range(len(err_list)):  # gh-135511: Get all of the message from exception(message lack if multiline in NameError and AttributeError)
            if err_list[i].startswith(" "):
                continue
            else:
                err_list = err_list[i:-1]
                break
        return ["\n".join(err_list) + "\n"]
    else:
        return traceback.format_exception_only(typ, exc)
try:
    import idlelib.run
    from idlelib.run import flush_stdout, cleanup_traceback
    original_idlelib_run_print_exception = idlelib.run.print_exception
except:
    print_exception = original_idlelib_run_print_exception = None
else:
    
    def print_exception():
        import linecache
        linecache.checkcache()
        flush_stdout()
        efile = sys.stderr
        typ, val, tb = excinfo = sys.exc_info()
        sys.last_type, sys.last_value, sys.last_traceback = excinfo
        sys.last_exc = val
        seen = set()

        def print_exc(typ, exc, tb):
            seen.add(id(exc))
            context = exc.__context__
            cause = exc.__cause__
            if cause is not None and id(cause) not in seen:
                print_exc(type(cause), cause, cause.__traceback__)
                print("\nThe above exception was the direct cause "
                      "of the following exception:\n", file=efile)
            elif (context is not None and
                  not exc.__suppress_context__ and
                  id(context) not in seen):
                print_exc(type(context), context, context.__traceback__)
                print("\nDuring handling of the above exception, "
                      "another exception occurred:\n", file=efile)
            if tb:
                tbe = traceback.extract_tb(tb)
                print('Traceback (most recent call last):', file=efile)
                exclude = ("run.py", "rpc.py", "threading.py", "queue.py",
                           "debugger_r.py", "bdb.py", "friendly_module_not_found_error")
                cleanup_traceback(tbe, exclude)
                traceback.print_list(tbe, file=efile)
            lines = get_message_lines(typ, exc, tb)
            for line in lines:
                print(line, end='', file=efile)

        print_exc(typ, val, tb)

    idlelib.run.print_exception = print_exception

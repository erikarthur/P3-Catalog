import sys
        sys.path.append('/vagrant/pycharm-debug.egg')
        from pydev import pydevd
pydevd.settrace('localhost', port=$SERVER_PORT, stdoutToServer=True, stderrToServer=True)
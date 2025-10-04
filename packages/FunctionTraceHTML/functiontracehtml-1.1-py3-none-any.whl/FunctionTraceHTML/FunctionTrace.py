import sys
import os
from datetime import datetime
from . import get_project_path

# --- CONFIG ---
MYPROJECT_PATH = get_project_path()  # your project folder
TRACE_LOG_FILE = os.path.join(MYPROJECT_PATH, "function_trace.html")
# -------------

_tracer_enabled = False
_trace_depth = 0
_last_click_time = None

# Initialize the HTML log file
with open(TRACE_LOG_FILE, "w", encoding="utf-8") as f:
    f.write("""<html>
                <head>
                    <meta charset='utf-8'>
                    <title>Function Trace Log</title>
                    <style>body { font-family: 'Verdana', monospace; font-size: 14px; }</style>
                </head>
                <body>\n""")
    f.write("<h2>Function Trace Log</h2>\n")

def _trace_calls(frame, event, arg):
    global _tracer_enabled, _trace_depth, _last_click_time
    if not _tracer_enabled:
        return

    filename = frame.f_code.co_filename
    if not filename.startswith(MYPROJECT_PATH):
        return  # ignore external libraries

    func_name = frame.f_code.co_name
    lineno = frame.f_lineno
    indent = "&nbsp;&nbsp;&nbsp;" * _trace_depth

    # Detect new click event (>0.5s from last)
    now = datetime.now()
    if _last_click_time is None or (now - _last_click_time).total_seconds() > 0.5:
        with open(TRACE_LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"<hr><b>Click event @ {now}</b><br>\n")
    _last_click_time = now

    func_html = f"<span style='color:hotpink'>{func_name}</span>"
    file_html = f"<span style='color:blue'>{os.path.basename(filename)}:{lineno}</span>"

    with open(TRACE_LOG_FILE, "a", encoding="utf-8") as f:
        if event == "call":
            f.write(f"{indent}&rarr; Call: {func_html} ({file_html})<br>\n")
            _trace_depth += 1
        elif event == "return":
            _trace_depth -= 1
            f.write(f"{indent}&larr; Return from {func_name} → {arg}<br>\n")

    return _trace_calls

def enable_tracing():
    global _tracer_enabled, _trace_depth, _last_click_time
    _tracer_enabled = True
    _trace_depth = 0
    _last_click_time = None
    sys.settrace(_trace_calls)
    with open(TRACE_LOG_FILE, "a", encoding="utf-8") as f:
        f.write("<p><b>Function tracing enabled</b></p>\n")

def disable_tracing():
    global _tracer_enabled
    _tracer_enabled = False
    sys.settrace(None)
    with open(TRACE_LOG_FILE, "a", encoding="utf-8") as f:
        f.write("<p><b>Function tracing disabled</b></p></body></html>\n")

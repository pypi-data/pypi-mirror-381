I had to refactor a big file, and needed to know which functions are called and in which order when i click a button in the UI.
I used this in a python file, with a UI from Qt Creator. The output is a HTML file with color codes.

Pink = name of function that is called
Blue = file name and line number

The is a division line between different button clicks, and the call order is indented.


To use it: call the enable_tracing() function at the start of the program, 
and the disable_tracing() at the end of the program.

Example:
    import FunctionTraceHTML
    FunctionTraceHTML.set_project_path(os.path.dirname(os.path.abspath(__file__)))

    from FunctionTraceHTML import FunctionTrace
    FunctionTrace.enable_tracing()

    --- CODE ---

    app = QApplication(sys.argv)
    window = QWidget()
    window.show()
    app.exec()

    FunctionTrace.disable_tracing()


This package was made by me, (charlie-de-muis on GitHub) with the help of ChatGPT.
It isn't broadly tested, but seems to work perfectly fine. 
I'm not responsible if anything goes wrong, use at your own risk :)

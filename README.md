
## line profiler

[line profiler link](https://github.com/rkern/line_profiler)

- Line #: The line number in the file.
- Hits: The number of times that line was executed.
- Time: The total amount of time spent executing the line in the timer's units. In the header information before the tables, you will see a line "Timer unit:" giving the conversion factor to seconds. It may be different on different systems.
- Per Hit: The average amount of time spent executing the line once in the timer's units.
% Time: The percentage of time spent on that line relative to the total amount of recorded time spent in the function.
- Line Contents: The actual source code. Note that this is always read from disk when the formatted results are viewed, not when the code was executed. If you have edited the file in the meantime, the lines will not match up, and the formatter may not even be able to locate the function for display.

### python3로 line profiler가 설치가 안될 때

```
pip3 install Cython
pip3 install git+https://github.com/rkern/line_profiler.git
```

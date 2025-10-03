# Subprocesslib

`subprocesslib` is a Python library that aims to be like `pathlib` but for the `subprocess` module.

## Usage

Here's a simple example of how to use SubprocessLib:

```python
from subprocesslib import Command

command = Command('tail', '-n', 5, '/var/log/syslog')
print(command)  # Command('tail', '-n', '5', '/var/log/syslog')
print(isinstance(command, tuple))  # True
print(str(command))  # "tail -n 5 /var/log/syslog" (using `shlex.join`)

# sync methods
command.spawn()  # same as `subprocess.Popen(...)`
command.run()  # same as `subprocess.run(...)`
command.output()  # same as `subprocess.check_output(...)`

# async methods
await command.spawn_async()  # Same as `asyncio.create_subprocess_exec(...)`
```

# Todo

- [ ] `await command.run_async()`
- [ ] `await command.output_async()`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

# jbang-python - Java Script in your Python

Install and use [JBang](https://www.jbang.dev) from Python-based projects.

![](https://github.com/jbangdev/jbang-python/blob/main/python_jbang.png?raw=true)

Lets you use your own local scripts, [JBang AppStore](https://jbang.dev/appstore) alias or any network reachable jar or Maven artifact.

## Usage

You can run the package in two ways:

### 1. Using the console script

After installation, you can use the `jbang-python` command:

```bash
jbang-python properties@jbangdev
```

### 2. Using Python's module runner

You can also run the package directly using Python's module runner:

```bash
python -m jbang properties@jbangdev
```

Or with `uvx`:

```bash
uvx run -m jbang properties@jbangdev
```

### Command-line Arguments

You can easily pass command-line arguments around:

```python
import sys
args = ' '.join(sys.argv[1:])
jbang.exec('com.myco.mylib:RELEASE ' + args)
```

So now if you run `python test.py arg1 arg2`, `arg1 arg2` will be appended to the command executed.

## Behind the scenes

When you run `pip install` - JBang and other dependencies will be installed. This uses the [`app setup`](https://www.jbang.dev/documentation/guide/latest/installation.html#using-jbang) command.

Opening a new terminal or shell may be required to be able to use the `jbang` command from the system `PATH`.

## Improvements ?

This was made as a quick hack to see if it was possible to use JBang from Python based on jbang-npm. If you have any ideas on how to improve this, please open an issue or PR and lets see where this brings us.

## Similar projects

* [jgo](https://pypi.org/project/jgo/) - allows execution of Maven artifacts by using Maven.


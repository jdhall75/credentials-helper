## Credentials Helper

I needed a fast way to read credentials for scripts from a file so I made this package.

### Credentails file
I could have just used `python-dotenv`, but I wanted to check file permissions
and make sure that the file is only readable by me or the user of the script.


```bash
# $HOME/.credentials
USERNAME=your_username
PASSWORD=password
RAND_STRING=XXYYZZ1234
```

```python
from credentials_helper import get_credentials

username, password = get_credentials()

# Non-standard locations

username, password = get_credentials(file='~/.local/env/credentials')
```

The `get_credentails` function will only return the USERNAME and PASSWORD environment
variables.  Anything else in the env file can be accessed via the `os.getenv` or `os.environ` modules.

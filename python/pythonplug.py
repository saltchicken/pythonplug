import pynvim
import sys

# Attach to the embedded Neovim instance
nvim = pynvim.attach('child', argv=['nvim', '--embed'])

# Example: Send a command to Neovim
nvim.command('echo "Hello from embedded Python!"')

# You can now interact with Neovim, for example, by setting a variable
nvim.vars['my_var'] = 'Embedded value'

# Continuously interact or process events in the background
while True:
    print("hello")
    pass  # Your custom plugin functionality


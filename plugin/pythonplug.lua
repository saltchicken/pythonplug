local plugin_dir = vim.fn.stdpath("data") .. "/lazy" .. "/pythonplug/python/pythonplug.py"
vim.cmd("command! Pythonplug :!python " .. plugin_dir)

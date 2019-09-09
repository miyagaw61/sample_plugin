gdb.execute("source %s/sample_plugin.py" % Exgdb.THISDIR)
for cmd in samplecmd.cmds:
    cmd_obj = getattr(samplecmd, cmd)
    setattr(ExgdbCmd, cmd, cmd_obj)

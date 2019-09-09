cmds = [cmd for cmd in dir(SampleCmd) if callable(getattr(SampleCmd, cmd))]
for cmd in cmds:
    if not cmd.startswith("_"):
        cmd_obj = getattr(SampleCmd, cmd)
        setattr(ExgdbCmd, cmd, cmd_obj)
#for cmd in samplecmd.cmds:
#    cmd_obj = getattr(MyPlugin, cmd)
#    setattr(ExgdbCmd, cmd, cmd_obj)

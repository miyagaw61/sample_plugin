class SampleCmd(object):
    def hello(self, *args):
        if len(args) == 0:
            print("hello")
        else:
            print("hello, " + args[0])

class SampleCmdWrapper(gdb.Command):
    def __init__(self):
        super(SampleCmdWrapper,self).__init__("sample", gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        args = e.string_to_argv(arg)
        if len(args) > 0:
            cmd = args[0]
            if cmd in samplecmd.cmds:
                func = getattr(samplecmd, cmd)
                func(*args[1:])
            else :
                print("Unknown command")
        else :
            print("Unknown command")
        return

samplecmd = SampleCmd()
samplecmd.cmds = [cmd for cmd in dir(SampleCmd) if callable(getattr(SampleCmd, cmd)) and not cmd.startswith("_")]
SampleCmdWrapper()

class SampleCmdAlias(gdb.Command):
    def __init__(self, alias, cmd):
        super(SampleCmdAlias, self).__init__(alias, gdb.COMMAND_NONE)
        self.cmd = cmd

    def invoke(self, args, from_tty):
        gdb.execute("%s %s" % (self.cmd, args))

for cmd in samplecmd.cmds:
    SampleCmdAlias(cmd, "sample %s" % cmd)

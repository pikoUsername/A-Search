from ..loader import bot


async def find_command_by_name(name: str):
    commands = await bot.get_my_commands()
    for command in commands:
        if command.command == name:
            return command
    raise AttributeError("Command Not Found")



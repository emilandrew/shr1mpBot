# Author:   Mateusz Belka
# Created:  11-Jul-2020
from util import messages
from aws import util


async def turn_off_instance(context, instance):
    if did_instance_stop(instance):
        await util.server_state_change_update(context, "stopping", "stopped", "Factorio")
    else:
        await messages.perror(context, "Failed to stop the Factorio server")


def did_instance_stop(instance):
    try:
        instance.stop()
        return True
    except:
        return False


async def turn_on_instance(context, instance):
    if did_instance_start(instance):
        await util.server_state_change_update(context, "pending", "running", "Factorio")
    else:
        await messages.perror(context, "Failed to start the Factorio server")


def did_instance_start(instance):
    try:
        instance.start()
        return True
    except:
        return False

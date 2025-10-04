import os
import sys
from logging import getLogger

import frida

logger = getLogger(__name__)


# parts of code taken from https://github.com/Nightbringer21/fridump


class Fridump:
    process = None

    # Define Configurations
    MAX_SIZE = 20971520
    PERMS = "rw-"

    def __new__(cls):
        raise TypeError("This is a static class and cannot be instantiated.")

    @classmethod
    def attach_to_app(cls, pid):
        try:
            cls.process = frida.get_usb_device().attach(pid)
        except Exception:
            logger.error("Can't connect to App. Have you connected the device?")
            return False
        logger.info(f"Attached to process with pid {pid}")

        return True

    @classmethod
    def dump_memory(cls, pid=None, process_name=None, mode=None):
        """Dump memory of a process.

        Can use either explicit pid/name or get from Toolbox spotlight session.

        :param pid: Process ID (optional if using spotlight)
        :param process_name: Process name (optional if using spotlight)
        :param mode: "spawn" or "attach" (optional, for logging)
        """
        # If no PID provided, get from unified session
        if pid is None:
            from .toolbox import Toolbox

            try:
                session, mode, app_info = Toolbox.get_frida_session_for_spotlight()
                pid = app_info["pid"]
                process_name = app_info["package_name"]
                # Session already attached/spawned, use it directly
                cls.process = session
                logger.info(
                    f"Using {mode.upper()} mode session for memory dump of {process_name} (PID: {pid})"
                )
            except Exception as e:
                logger.error(f"Failed to get spotlight session: {e}")
                return
        else:
            # Legacy path: attach explicitly
            cls.attach_to_app(pid)
            if mode:
                logger.info(
                    f"Dumping memory in {mode.upper()} mode for {process_name} (PID: {pid})"
                )

        subdirectory = process_name.replace(".", "-")
        output_directory = os.path.join(os.getcwd(), "dump", subdirectory)
        logger.debug(f"Output directory for memory dump is set to {output_directory}")

        if not os.path.exists(output_directory):
            logger.debug("Creating directory...")
            os.makedirs(output_directory)

        mem_access_viol = ""
        logger.info(f"Starting Memory dump of {process_name}")

        script = cls.process.create_script(
            """'use strict';

            rpc.exports = {
                enumerateRanges: async function (prot) {
                    const ranges = await Process.enumerateRanges(prot);
                    return ranges;
                },
                readMemory: function (address, size) {
                    return ptr(address).readByteArray(size);
                }
            };

            """
        )
        script.on("message", cls.on_message)
        script.load()

        # Resume spawned process now that hooks are installed
        # Check if we got session from get_frida_session_for_spotlight (mode and app_info available)
        if 'mode' in locals() and 'app_info' in locals() and mode == "spawn":
            from .toolbox import Toolbox
            Toolbox.resume_spawned_process_after_hooks(
                app_info['device'],
                app_info['pid']
            )

        # Replace script.exports with script.exports_sync to fix the deprecation warning
        agent = script.exports_sync
        ranges = agent.enumerate_ranges(cls.PERMS)

        i = 0
        l = len(ranges)

        # Performing the memory dump
        for range in ranges:
            base = range["base"]
            size = range["size"]

            # logging.debug("Base Address: " + str(base))
            # logging.debug("")
            # logging.debug("Size: " + str(size))

            if size > cls.MAX_SIZE:
                logger.debug("Too big, splitting the dump into chunks")
                mem_access_viol = cls.splitter(
                    agent, base, size, cls.MAX_SIZE, mem_access_viol, output_directory
                )
                continue
            mem_access_viol = cls.dump_to_file(
                agent, base, size, mem_access_viol, output_directory
            )
            i += 1
            cls.printProgress(i, l, prefix="Progress:", suffix="Complete", bar=50)

    # Method to receive messages from Javascript API calls
    @classmethod
    def on_message(cls, message, data):
        print("[on_message] message:", message, "data:", data)

    @classmethod
    # Reading bytes from session and saving it to a file
    def dump_to_file(cls, agent, base, size, error, directory):
        try:
            filename = str(base) + "_dump.data"
            dump = agent.read_memory(base, size)
            f = open(os.path.join(directory, filename), "wb")
            f.write(dump)
            f.close()
            return error
        except Exception as e:
            logger.debug(str(e))
            logger.error("Oops, memory access violation!")
            return error

    # Read bytes that are bigger than the max_size value, split them into chunks and save them to a file
    @classmethod
    def splitter(cls, agent, base, size, max_size, error, directory):
        times = size / max_size
        diff = size % max_size
        if diff == 0:
            logger.debug(f"Number of chunks:{times + 1!s}")
        else:
            logger.debug(f"Number of chunks:{times!s}")
        global cur_base
        cur_base = int(base, 0)

        for time in range(int(times)):
            # logging.debug("Save bytes: " + str(cur_base) + " till " + str(cur_base + max_size))
            cls.dump_to_file(agent, cur_base, max_size, error, directory)
            cur_base = cur_base + max_size

        if diff != 0:
            # logging.debug("Save bytes: " + str(hex(cur_base)) + " till " + str(hex(cur_base + diff)))
            cls.dump_to_file(agent, cur_base, diff, error, directory)

    @classmethod
    # Progress bar function
    def printProgress(cls, times, total, prefix="", suffix="", decimals=2, bar=100):
        filled = int(round(bar * times / float(total)))
        percents = round(100.00 * (times / float(total)), decimals)
        bar = "#" * filled + "-" * (bar - filled)
        (sys.stdout.write("%s [%s] %s%s %s\r" % (prefix, bar, percents, "%", suffix)),)
        sys.stdout.flush()
        if times == total:
            print("\n")

import asyncio
import shlex
from typing import Tuple

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError

import config

from ..logging import LOGGER


def install_req(cmd: str) -> Tuple[str, str, int, int]:
    async def install_requirements():
        args = shlex.split(cmd)
        process = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        return (
            stdout.decode("utf-8", "replace").strip(),
            stderr.decode("utf-8", "replace").strip(),
            process.returncode,
            process.pid,
        )

    return asyncio.get_event_loop().run_until_complete(install_requirements())


def git():
    try:
        repo = Repo()
        LOGGER(__name__).info("Git Client Found [VPS DEPLOYER]")
    except Exception:
        LOGGER(__name__).info("Git not available, skipping update check.")
        return

    try:
        origin = repo.remote("origin")
    except Exception:
        LOGGER(__name__).info("No remote origin found, skipping git fetch.")
        return

    try:
        LOGGER(__name__).info("Checking for updates from GitHub...")
        origin.fetch()
        LOGGER(__name__).info("Git fetch successful.")
    except Exception as e:
        LOGGER(__name__).warning(f"Git fetch failed: {e}")
        LOGGER(__name__).warning("Skipping auto update to prevent crash.")
        return

    try:
        repo.git.pull("origin", repo.active_branch.name)
        LOGGER(__name__).info("Repository updated successfully.")
    except Exception as e:
        LOGGER(__name__).warning(f"Git pull failed: {e}")
        LOGGER(__name__).warning("Continuing without update.")

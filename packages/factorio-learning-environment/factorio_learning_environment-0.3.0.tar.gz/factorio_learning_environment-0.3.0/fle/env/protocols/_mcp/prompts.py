"""
Dynamic prompt generator for Factorio Learning Environment tasks
"""

import pathlib
import sys
import os
from contextlib import contextmanager

from fle.env.protocols._mcp import mcp

# from fle.env.protocols._mcp.server import mcp
from fle.env.protocols._mcp.init import state


# Context manager to suppress stdout
@contextmanager
def suppress_stdout():
    """
    Context manager to temporarily redirect stdout to devnull
    Prevents stdout from interfering with MCP protocol
    """
    save_stdout = sys.stdout
    sys.stdout = open(os.devnull, "w")
    try:
        yield
    finally:
        sys.stdout.close()
        sys.stdout = save_stdout


# Path to the agent.md file
TUTORIAL_MD_PATH = pathlib.Path(__file__).parent / "tutorial.md"


# Load the agent.md content
def load_tutorial_md():
    try:
        with open(TUTORIAL_MD_PATH, "r") as f:
            return f.read()
    except Exception as e:
        print(f"Error loading agent.md: {e}")
        return "Error loading tutorial content. Please check if agent.md exists."


@mcp.prompt(
    name="throughput-task", description="Factorio throughput optimization task prompt"
)
def throughput_task(
    entity: str = "iron-plate",
    quota: str = "60",
    holdout_wait_period: str = "60",
    pre_holdout_wait_period: str | None = None,
) -> str:
    """Generate a throughput optimization task prompt."""

    # Build the task configuration
    objective = (
        f"Build an automated factory that produces {quota} {entity}(s) per minute"
    )

    # Add command to the server
    state.active_server.add_command(
        f'/c game.players[1].set_goal_description("{objective}", true)', raw=True
    )
    state.active_server.execute_transaction()

    # Return the prompt text
    return (
        f"# Factorio Throughput Challenge: {entity.capitalize()} Production\n\n"
        f"## Goal\n"
        f"Create an automatic {entity} factory that produces {quota} {entity}s per 60 in-game seconds.\n\n"
        f"## Requirements\n"
        f"- {objective}\n"
        f"- Ensure production is sustainable and consistent\n"
        f"- The factory should continue to operate without player intervention\n"
        f"- Your solution will be evaluated *after* a holdout period of {holdout_wait_period} seconds, "
        f"requiring a fully automated solution (as you will not be able to interact with the factory during this time)\n\n"
        f"Please design and build this factory step by step."
    )


@mcp.prompt(
    name="tutorial",
    description="Comprehensive guide to using the Factorio Learning Environment",
)
def tutorial() -> str:
    """Load and return the tutorial content."""
    tutorial_content = load_tutorial_md()

    return (
        "You are an expert at at the Factorio Learning Environment, "
        "ready to write Python code (with the API) and introspect the existing implementations, to build factories in the game.\n\n"
        + tutorial_content
    )


# @mcp.get_prompt()
# async def get_prompt(
#     name: str, arguments: dict[str, str] | None = None
# ) -> types.GetPromptResult:
#     """Generate a prompt based on the requested prompt type and arguments"""
#     if name not in PROMPTS:
#         raise ValueError(f"Prompt not found: {name}")
#
#     if name == "throughput-task":
#         # Extract arguments
#         entity = arguments.get("entity", "iron-plate") if arguments else "iron-plate"
#         quota = arguments.get("quota", "0") if arguments else "60"
#         # trajectory_length = arguments.get("trajectory_length", "128") if arguments else "128"
#         holdout_wait_period = (
#             arguments.get("holdout_wait_period", "60") if arguments else "60"
#         )
#         # Build the task configuration
#         objective = (
#             f"Build an automated factory that produces {quota} {entity}(s) per minute"
#         )
#
#         # Suppress stdout when executing transaction to prevent breaking MCP protocol
#         # with suppress_stdout():
#         #
#         state.active_server.add_command(
#             f'/c game.players[1].set_goal_description("{objective}", true)', raw=True
#         )
#         state.active_server.execute_transaction()
#
#         # Create the prompt result
#         return types.GetPromptResult(
#             messages=[
#                 types.PromptMessage(
#                     role="user",
#                     content=types.TextContent(
#                         type="text",
#                         text=f"# Factorio Throughput Challenge: {entity.capitalize()} Production\n\n"
#                         f"## Goal\n"
#                         f"Create an automatic {entity} factory that produces {quota} {entity}s per 60 in-game seconds.\n\n"
#                         f"## Requirements\n"
#                         f"- {objective}\n"
#                         f"- Ensure production is sustainable and consistent\n"
#                         f"- The factory should continue to operate without player intervention\n"
#                         f"- Your solution will be evaluated *after* a holdout period of {holdout_wait_period} seconds, "
#                         f"requiring a fully automated solution (as you will not be able to interact with the factory during this time)\n\n"
#                         f"Please design and build this factory step by step.",
#                     ),
#                 )
#             ]
#         )
#
#     elif name == "tutorial":
#         # Load the agent.md content
#         tutorial_content = load_tutorial_md()
#
#         # Create the prompt result with the tutorial content
#         return types.GetPromptResult(
#             messages=[
#                 types.PromptMessage(
#                     role="user",
#                     content=types.TextContent(
#                         type="text",
#                         text=(
#                             "You are an expert at at the Factorio Learning Environment, "
#                             "ready to write Python code (with the API) and introspect the existing implementations, to build factories in the game.\n\n"
#                             + tutorial_content
#                         ),
#                     ),
#                 )
#             ]
#         )
#
#     raise ValueError("Prompt implementation not found")

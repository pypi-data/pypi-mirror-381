from __future__ import annotations

import asyncio
import os
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

import click
import copier
import questionary
from click.exceptions import Exit
from llama_deploy.cli.app import app
from llama_deploy.cli.options import global_options
from llama_deploy.cli.styles import HEADER_COLOR_HEX
from rich import print as rprint


@app.command()
@click.option(
    "--update",
    is_flag=True,
    help="Instead of creating a new app, update the current app to the latest version. Other options will be ignored.",
)
@click.option(
    "--template",
    help="The template to use for the new app",
)
@click.option(
    "--dir",
    help="The directory to create the new app in",
    type=click.Path(
        file_okay=False, dir_okay=True, writable=True, resolve_path=True, path_type=Path
    ),
)
@click.option(
    "--force",
    is_flag=True,
    help="Force overwrite the directory if it exists",
)
@global_options
def init(
    update: bool,
    template: str | None,
    dir: Path | None,
    force: bool,
) -> None:
    """Create a new app repository from a template"""
    if update:
        _update()
    else:
        _create(template, dir, force)


def _create(template: str | None, dir: Path | None, force: bool) -> None:
    # defer loading to improve cli startup time
    from vibe_llama.sdk import VibeLlamaStarter

    @dataclass
    class TemplateOption:
        id: str
        name: str
        description: str
        source: GithubTemplateRepo
        llama_cloud: bool

    @dataclass
    class GithubTemplateRepo:
        url: str

    ui_options = [
        TemplateOption(
            id="basic-ui",
            name="Basic UI",
            description="A basic starter workflow with a React Vite UI",
            source=GithubTemplateRepo(
                url="https://github.com/run-llama/template-workflow-basic-ui"
            ),
            llama_cloud=False,
        ),
        TemplateOption(
            id="showcase",
            name="Showcase",
            description="A collection of workflow and UI patterns to build LlamaDeploy apps",
            source=GithubTemplateRepo(
                url="https://github.com/run-llama/template-workflow-showcase"
            ),
            llama_cloud=False,
        ),
        TemplateOption(
            id="document-qa",
            name="Document Question & Answer",
            description="Upload documents and run question answering through a React UI",
            source=GithubTemplateRepo(
                url="https://github.com/run-llama/template-workflow-document-qa"
            ),
            llama_cloud=True,
        ),
        TemplateOption(
            id="extraction-review",
            name="Extraction Agent with Review UI",
            description="Extract data from documents using a custom schema and Llama Cloud. Includes a UI to review and correct the results",
            source=GithubTemplateRepo(
                url="https://github.com/run-llama/template-workflow-data-extraction"
            ),
            llama_cloud=True,
        ),
    ]

    headless_options = [
        TemplateOption(
            id="basic",
            name="Basic Workflow",
            description="A base example that showcases usage patterns for workflows",
            source=GithubTemplateRepo(
                url="https://github.com/run-llama/template-workflow-basic"
            ),
            llama_cloud=False,
        ),
        TemplateOption(
            id="document_parsing",
            name="Document Parser",
            description="A workflow that, using LlamaParse, parses unstructured documents and returns their raw text content",
            source=GithubTemplateRepo(
                url="https://github.com/run-llama/template-workflow-document-parsing"
            ),
            llama_cloud=True,
        ),
        TemplateOption(
            id="human_in_the_loop",
            name="Human in the Loop",
            description="A workflow showcasing how to use human in the loop with LlamaIndex workflows",
            source=GithubTemplateRepo(
                url="https://github.com/run-llama/template-workflow-human-in-the-loop"
            ),
            llama_cloud=False,
        ),
        TemplateOption(
            id="invoice_extraction",
            name="Invoice Extraction",
            description="A workflow that, given an invoice, extracts several key details using LlamaExtract",
            source=GithubTemplateRepo(
                url="https://github.com/run-llama/template-workflow-invoice-extraction"
            ),
            llama_cloud=True,
        ),
        TemplateOption(
            id="rag",
            name="RAG",
            description="A workflow that embeds, indexes and queries your documents on the fly, providing you with a simple RAG pipeline",
            source=GithubTemplateRepo(
                url="https://github.com/run-llama/template-workflow-rag"
            ),
            llama_cloud=False,
        ),
        TemplateOption(
            id="web_scraping",
            name="Web Scraping",
            description="A workflow that, given several urls, scrapes and summarizes their content using Google's Gemini API",
            source=GithubTemplateRepo(
                url="https://github.com/run-llama/template-workflow-web-scraping"
            ),
            llama_cloud=False,
        ),
    ]

    if template is None:
        rprint(
            "[bold]Select a template to start from.[/bold] Either with javascript frontend UI, or just a python workflow that can be used as an API."
        )
        template = questionary.select(
            "",
            choices=[questionary.Separator("------------ With UI -------------")]
            + [
                questionary.Choice(title=o.name, value=o.id, description=o.description)
                for o in ui_options
            ]
            + [
                questionary.Separator(" "),
                questionary.Separator("--- Headless Workflows (No UI) ---"),
            ]
            + [
                questionary.Choice(title=o.name, value=o.id, description=o.description)
                for o in headless_options
            ],
            style=questionary.Style(
                [
                    ("separator", f"fg:{HEADER_COLOR_HEX}"),
                ]
            ),
        ).ask()
    if template is None:
        rprint("No template selected")
        raise Exit(1)
    if dir is None:
        dir_str = questionary.text(
            "Enter the directory to create the new app in", default=template
        ).ask()
        if not dir_str:
            rprint("No directory provided")
            raise Exit(1)
        dir = Path(dir_str)
    resolved_template: TemplateOption | None = next(
        (o for o in ui_options + headless_options if o.id == template), None
    )
    if resolved_template is None:
        rprint(f"Template {template} not found")
        raise Exit(1)
    if dir.exists():
        is_ok = (
            force
            or questionary.confirm("Directory exists. Overwrite?", default=False).ask()
        )
        if not is_ok:
            raise Exit(1)
        else:
            shutil.rmtree(dir, ignore_errors=True)

    copier.run_copy(
        resolved_template.source.url,
        dir,
        quiet=True,
    )
    # Initialize git repository if git is available
    has_git = False
    git_initialized = False
    try:
        subprocess.run(["git", "--version"], check=True, capture_output=True)
        has_git = True
    except (subprocess.CalledProcessError, FileNotFoundError):
        # git is not available or broken; continue without git
        has_git = False

    # Change to the new directory and initialize git repo
    original_cwd = Path.cwd()
    os.chdir(dir)

    try:
        # Dump in a bunch of docs for AI agents

        vibe_llama_starter = VibeLlamaStarter(
            agents=["OpenAI Codex CLI"],  # AGENTS.md, supported by Cursor,
            services=["LlamaDeploy", "LlamaIndex", "llama-index-workflows"]
            + (["LlamaCloud Services"] if resolved_template.llama_cloud else []),
        )
        asyncio.run(vibe_llama_starter.write_instructions(overwrite=True))
        # Create symlink for Claude.md to point to AGENTS.md
        for alternate in ["CLAUDE.md", "GEMINI.md"]:  # don't support AGENTS.md (yet?)
            claude_path = Path(alternate)  # not supported yet
            agents_path = Path("AGENTS.md")
            if agents_path.exists() and not claude_path.exists():
                claude_path.symlink_to("AGENTS.md")

        # Initialize a git repo (best-effort). If anything fails, show a friendly note and continue.
        if has_git:
            try:
                subprocess.run(["git", "init"], check=True, capture_output=True)
                subprocess.run(["git", "add", "."], check=True, capture_output=True)
                subprocess.run(
                    ["git", "commit", "-m", "Initial commit"],
                    check=True,
                    capture_output=True,
                )
                git_initialized = True
            except (subprocess.CalledProcessError, FileNotFoundError) as e:
                # Extract a short error message if present
                err_msg = ""
                if isinstance(e, subprocess.CalledProcessError):
                    stderr = getattr(e, "stderr", b"")
                    if isinstance(stderr, (bytes, bytearray)):
                        try:
                            stderr = stderr.decode("utf-8", "ignore")
                        except Exception:
                            stderr = ""
                    if isinstance(stderr, str) and stderr.strip():
                        err_msg = stderr.strip().split("\n")[-1]
                elif isinstance(e, FileNotFoundError):
                    err_msg = "git executable not found"

                rprint("")
                rprint("⚠️  [bold]Skipping git initialization due to an error.[/]")
                if err_msg:
                    rprint(f"    {err_msg}")
                rprint("    You can initialize it manually:")
                rprint("      git init && git add . && git commit -m 'Initial commit'")
                rprint("")
    finally:
        os.chdir(original_cwd)

    # If git is not available at all, let the user know how to proceed
    if not has_git:
        rprint("")
        rprint("⚠️  [bold]Skipping git initialization due to an error.[/]")
        rprint("    git executable not found")
        rprint("    You can initialize it manually:")
        rprint("      git init && git add . && git commit -m 'Initial commit'")
        rprint("")

    rprint(
        f"Successfully created [blue]{dir}[/] using the [blue]{resolved_template.name}[/] template! 🎉 🦙 💾"
    )
    rprint("")
    rprint("[bold]To run locally:[/]")
    rprint(f"    [orange3]cd[/] {dir}")
    rprint("    [orange3]uvx[/] llamactl serve")
    rprint("")
    rprint("[bold]To deploy:[/]")
    # Only show manual git init steps if repository failed to initialize earlier
    if not git_initialized:
        rprint("    [orange3]git[/] init")
        rprint("    [orange3]git[/] add .")
        rprint("    [orange3]git[/] commit -m 'Initial commit'")
        rprint("")
    rprint("[dim](Create a new repo and add it as a remote)[/]")
    rprint("")
    rprint("    [orange3]git[/] remote add origin <your-repo-url>")
    rprint("    [orange3]git[/] push -u origin main")
    rprint("")
    # rprint("  [orange3]uvx[/] llamactl login")
    rprint("    [orange3]uvx[/] llamactl deploy create")
    rprint("")


def _update():
    """Update the app to the latest version"""
    try:
        copier.run_update(
            overwrite=True,
            skip_answered=True,
            quiet=True,
        )
    except copier.UserMessageError as e:
        rprint(f"{e}")
        raise Exit(1)

    # Check git status and warn about conflicts
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            check=True,
            capture_output=True,
            text=True,
        )

        if result.stdout.strip():
            conflicted_files = []
            modified_files = []

            for line in result.stdout.strip().split("\n"):
                status = line[:2]
                filename = line[3:]

                if "UU" in status or "AA" in status or "DD" in status:
                    conflicted_files.append(filename)
                elif status.strip():
                    modified_files.append(filename)

            if conflicted_files:
                rprint("")
                rprint("⚠️  [bold]Files with conflicts detected:[/]")
                for file in conflicted_files:
                    rprint(f"    {file}")
                rprint("")
                rprint(
                    "Please manually resolve conflicts with a merge editor before proceeding."
                )

    except (subprocess.CalledProcessError, FileNotFoundError):
        # Git not available or not in a git repo - continue silently
        pass

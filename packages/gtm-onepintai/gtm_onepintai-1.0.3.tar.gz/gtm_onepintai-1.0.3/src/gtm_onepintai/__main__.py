import os
import asyncio
import openai
import gtm_agent
from mcp.server import Server
from mcp.server.fastmcp import FastMCP
from fastmcp.resources.types import FileResource

from pathlib import Path

import csv
import pandas as pd
import sys

print("MCP Wrapper starting...", file=sys.stderr)
sys.stderr.flush()

mcp = FastMCP("FactorialTool")

app = Server("GTM")

# @mcp.tool()
# def load_csv(file_path: str) -> list[dict]:
#     # Read uploaded file from Claude's temp location
#     rows = []
#     with open(file_path, newline='', encoding='utf-8') as f:
#         reader = csv.DictReader(f)
#         for row in reader:
#             rows.append(dict(row))
#     return rows


# @mcp.tool()
# def list_inputs() -> list[FileResource]:
#     # Return all available uploaded files
#     return list(mcp.resources.values())

# @mcp.resource()
# def upload_file(path: str) -> FileResource:
#     # Called when Claude uploads a file; returns a FileResource for discovery
#     return FileResource(
#         path=path,
#         description=f"Uploaded CSV: {path}",
#     )

def parse_csv_to_list(res: FileResource) -> list[str]:
    rows = []
    with open(res.path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(dict(row))
    return rows


def gtm_email_prompt(
    name: str,
    company: str,
    category: str,
    email: str,
    linkedin: str = "",
    business: str = "",
    title: str = "",
) -> str:
    # Load the markdown template
    config_dir = Path(__file__).parent
    template = (config_dir / "gtm_prompt.md").read_text(encoding="utf-8")
    email_sample = (config_dir / "emails_notepad.txt").read_text(encoding="utf-8")
    return template.format(
        name=name,
        company=company,
        category=category,
        linkedin=linkedin,
        email=email,
        business=business,
        title=title,
    )

async def fill_template(email_list: list[str]) -> list[str]:
    ##answer_list = (["Challenges", "Personal Info", "Risks"])
    config_dir = Path(__file__).parent
    template = (config_dir / "gtm_prompt.md").read_text(encoding="utf-8")
    template_mod = ""
    df_char = pd.DataFrame(email_list)

    template_list = []
    for x in email_list:
        template_mod = template.format(
        name=email_list[x][0],
        company=email_list[x][1],
        category=email_list[x][2],
        linkedin=email_list[x][3],
        email=email_list[x][4],
        business=email_list[x][5],
        title=email_list[x][6],
        )
        template_list.append(template_mod)
    return template_list

@mcp.tool()
async def continue_email_generation(file_path: str, prompt: str, row_number: int):
    row_number += 1
    result = await generate_email(file_path, prompt, row_number)
    return result

@mcp.tool()
async def start_email_generation(res: FileResource, prompt: str, row_number = 0):
    file_path = os.path.join(os.path.dirname(__file__), res.path)
    result = await generate_email(file_path, prompt, 1)
    return result


@mcp.tool()
async def generate_email(file_path: str, prompt: str, row_number: int):
    email = "Email"
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            csv_reader = csv.reader(file)

            for i in range(row_number):
                next(csv_reader)

            for i, row in enumerate(csv_reader, start=1):
                try:
                    if len(row) < 6:  # Check if row has enough columns
                        continue

                    result = await (gtm_agent.generate_mail(row, i, prompt))
                    return {
                        "success": True,
                        "email_content": result,
                        "row_processed": row_number
                    }

                except Exception as e:
                    continue

    except Exception as e:
        return{
            "success": False,
            "error": str(e),
        }


def fetch_info():
    challenges = ""
    personal = ""
    risk = ""
    ##gain = fetch.get_gain_info(row["Company"], challenges)

    mod_ans = [challenges, personal, risk]
    ##answer_list = np.vstack([answer_list, mod_ans])

@mcp.prompt()
def gtm_inv_research(company: str) -> str:
    # Load the markdown template
    config_dir = Path(__file__).parent
    template = (config_dir / "inv_research_prompt.md").read_text(encoding="utf-8")
    return template.format(company=company)


@mcp.prompt()
def gtm_gen_research(company: str) -> str:
    # Load the markdown template
    config_dir = Path(__file__).parent
    template = (config_dir / "gen_research.md").read_text(encoding="utf-8")
    return template.format(company=company)


if __name__ == "__main__":
    mcp.run(transport="stdio")

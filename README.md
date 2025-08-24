```markdown
# AI Text to Markdown Converter GitHub Action

This is a GitHub Action that automatically converts plain text into a well-structured Markdown document using the Gemini API. It's designed to streamline the process of creating and maintaining documentation, like `README.md` files, directly within your repository.

## How It Works

The workflow is simple and automated. You write your content in a plain text file, push your changes, and the GitHub Action handles the rest.

1.  **Write Content**: You write or paste your text into a designated source file (e.g., `source.txt`).
2.  **Commit & Push**: You commit and push the changes to your repository.
3.  **Workflow Trigger**: The GitHub Action automatically detects the change to the `source.txt` file and starts the conversion process.
4.  **AI Conversion**: A Python script uses the Gemini API to intelligently convert your text into Markdown, adding headings, lists, bold text, and other formatting as needed.
5.  **Auto-Commit**: The action then automatically commits the new or updated Markdown content to a destination file (e.g., `README.md`).

## Getting Started

To use this tool in your own repository, you need to set up two files and one secret.

### Step 1: Add the Tool's Files

Place the following two files in your repository:

*   `convert_to_md.py`: This script contains the logic for the AI conversion.
*   `.github/workflows/generate-markdown.yml`: This YAML file defines the GitHub Action workflow.

### Step 2: Add Your API Key

To securely use the Gemini API, you must store your API key as a GitHub Secret.

1.  Go to your repository's **Settings** > **Secrets and variables** > **Actions**.
2.  Click **New repository secret**.
3.  Set the Name to `GEMINI_API_KEY`.
4.  Paste your personal Gemini API key into the Secret field.

### Step 3: Use the Tool

1.  Create a file named `source.txt` in the root of your repository.
2.  Add your plain text content to `source.txt`.
3.  Commit and push your changes.
4.  The workflow will run automatically, and you will see a new `README.md` file created with the formatted Markdown content.

---

*This readme is also created using this workflow*
```
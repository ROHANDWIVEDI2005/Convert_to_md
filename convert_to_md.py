import os
from google import genai


def convert_to_markdown(text_content,api_key):
    """
    Converts a given text string to Markdown format using the Gemini API via the SDK.
    
    Args:
        text_content (str): The plain text to convert.
        api_key (str): The API key for the Gemini API.

    Returns:
        str: The generated Markdown content.
    """
    # Configure the API key from the environment variable.
  
    client = genai.Client(api_key = api_key)

    
    # Instantiate the model.
    MODEL_ID = "gemini-2.5-flash"
    
    # Create the prompt for the Gemini model.
    prompt = f"""
    Convert the following text into well-structured Markdown format suitable for GitHub documentation.
    Use appropriate headings (#, ##, ###), lists, code blocks, and bold/italic formatting.
    Ensure the output is clean and directly usable in a .md code don't include (```Markdown ````).

    Text to convert:
    {text_content}
    """
    
    try:
        # Generate content using the SDK.
        response = client.models.generate_content(
            model = MODEL_ID,
            contents = prompt
        )
        
        # Access the generated text from the response.
        return response.text
    except Exception as e:
        print(f"An error occurred during content generation: {e}")
        return ""

def main():
    """
    Main function to read text from a source file, convert it, and write to a Markdown file.
    """
    # Get the API key from a GitHub Action secret.
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable is not set.")
        exit(1)

    # Define the input and output file paths.
    input_file = "source.txt"  # You can change this to your input file
    output_file = "README.md"  # You can change this to your desired output file

    # Read the text content from the source file.
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        exit(1)

    with open(input_file, "r") as f:
        text_content = f.read()

    # Convert the text to Markdown.
    markdown_content = convert_to_markdown(text_content, api_key)

    if markdown_content:
        # Write the generated Markdown to the output file.
        with open(output_file, "w") as f:
            f.write(markdown_content)
        print(f"Successfully converted '{input_file}' to '{output_file}'.")
    else:
        print("Markdown conversion failed.")

if __name__ == "__main__":
    main()

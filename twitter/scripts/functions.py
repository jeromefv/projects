from pathlib import Path
import markdownify
import re

def text_strip(text):
    # Removes surrounding spaces
    return text.strip()

def filename_base(url_text, modifier):
    # Splits a URL string by / and sends the last index value
    file_base = text_strip(url_text.rsplit(modifier)[-1])
    return file_base

def filename_write(title, extension):
    # Formats string as a filename for combining two strings
    file_title = text_strip(f"{title}{extension}")
    return file_title

def path_file(root, path):
    # Formats string as directory path combining two strings
    path_name = text_strip(f"{root}{path}")
    return path_name

def make_directory(file_path):
    # Use Path library to create new directory from file path
    Path(file_path).mkdir(parents=True, exist_ok=True)
    return None

def write_file(file_path, file_name):
    # String format for directory and file extension
    directory = file_path + "/" + file_name
    # Write new file in directory
    Path(directory).touch()
    return directory

def markdown_format(url, func):
    # Use func library to retrieve web page
    page = func.get(text_strip(url))
    # Format page content as string
    page_content = str(page.text)
    # Transform text to Markdown format string
    page_markdown = str(markdownify.markdownify(page_content))
    return page_markdown

def regex_formatting(page, formatting):
    # Loops through regex group for formatting page
    for formats in formatting:
        if len(formats) == 2:
            # Replaces with another value
            page = re.sub(formats[0], formats[1], page)
        else:
            # Removes regex
            page = re.sub(formats, "", page)
    return page
    

def main(root, format, func, regex, urls, dirs):
    # 1st Parses dirs to create new specific dir format files
    # 2nd Parses urls with func to create markdown content
    # 3rd Cleans up content based on regex
    # 4th Writes content to new format files in root
    for url, dir in zip(urls, dirs):
        file_base = filename_base(dir, "/")
        file_name = filename_write(file_base, format)
        file_path = path_file(root, dir)
        make_directory(file_path)
        directory = write_file(file_path, file_name)
        page_markdown = markdown_format(url, func)
        page_markdown = regex_formatting(page_markdown, regex)
        with open(directory, "w") as markup:
            markup.write(page_markdown)
    return None
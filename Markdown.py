# This is a simple program that converts the Markdown into HTML file using mark down libary
import markdown
with open("Example.md", "r") as file:
    content = md_file.read()
html_content = markdown.markdown(content)
with open("output.html", "w") as html_file:
    html_file.write(html_content)
print("Markdown file is succesfully converted to HTML file")
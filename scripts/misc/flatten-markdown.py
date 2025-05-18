# this script flattens a markdown file by removing all newlines and replacing them with '/n'

def flatten_markdown(markdown: str) -> str:
    lines = markdown.splitlines()
    return '/n'.join(lines)

def flatten_markdown_file(file_path: str) -> str:
      with open(file_path, 'r', encoding='utf-8') as f:
         markdown = f.read()
      return flatten_markdown(markdown)

if __name__ == '__main__':
    flattened = flatten_markdown_file("scripts/misc/markdown.txt")
    print(flattened)
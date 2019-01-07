import markdown

def convert(md_input, html_output):
    input_file = open(md_input, mode="r", encoding="utf-8")
    text = input_file.read()
    html = markdown.markdown(text)

    html_file = open(html_output, mode='w', encoding='utf-8')
    html_file.writelines(html)
    print(html)

convert('markdown.txt', 'html.txt')
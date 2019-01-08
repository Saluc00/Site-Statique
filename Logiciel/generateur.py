import markdown2

def convert(md_input, html_output):
    input_file = open(md_input, "r")
    html = markdown2.markdown(input_file.read())

    html_file = open(html_output, 'w')
    html_file.writelines(html)
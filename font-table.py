import textwrap

class Cell:
  def __init__(self, font_family, content, font_weight):
    self.font_family = font_family
    self.content = content
    self.font_weight = font_weight

  def to_html(self):
    return "<td style='font-family: {}; font-weight: {}'>{}</td>".format(
      self.font_family, self.font_weight, self.content
    )

def generate_tr(build_cell):
  tds = ['  ' + build_cell(font_weight).to_html() for font_weight in range(100, 1000, 100)]
  html = textwrap.dedent('''
    <tr>
    {}
    </tr>
  ''')
  return html.format('\n'.join(tds))

def generate_table():
  trs = [
    generate_tr(lambda font_weight: Cell(font_family='Arial', content=font_weight, font_weight=300))
  ]
  for font_family in [
    'Arial',
    'Helvetica Neu',
    'Verdana',
    'Times New Roman',
    'Times',
    'Courier New',
    'Courier',
    'Georgia',
    'Palatino',
    'Garamond',
    'Comic Sans MS',
    'Trebuchet MS',
    'Arial Black',
    'Impact',
    'Muli',
    'Bookman Old Style',
  ]:
    trs.append(generate_tr(
      lambda font_weight: Cell(font_family=font_family, content='foo', font_weight=font_weight)
    ))

  return textwrap.dedent('''
    <html>
    <link rel="stylesheet" type="text/css" href="my-style.css">
    <table>
      {}
    </table>
    </html>
  ''').format('\n'.join(trs))

def main():
  out_html = generate_table()
  with open('index.html', 'w') as f:
    f.write(out_html)

if __name__ == '__main__':
  main()

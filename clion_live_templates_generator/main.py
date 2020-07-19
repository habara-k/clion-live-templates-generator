import os
import re
from optparse import OptionParser


def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)


def generate_live_templates(target_dir):

    OUTPUT_FILE = 'C_C__.xml'

    with open(OUTPUT_FILE,'w') as file:
        file.write('<templateSet group="C/C++">\n')

        for src_path in find_all_files(target_dir):

            src_title, fext = os.path.splitext(os.path.basename(src_path))

            if fext != '.cpp':
                continue
            if re.search('\.test$', src_title):
                continue

            name = src_title
            description = src_title
            value = ""

            with open(src_path,'r') as src:

                for row in src:
                    if re.match('^#', row):
                        continue

                    row = row.replace('&', '&amp;')
                    row = row.replace('\n', '&#10;')
                    row = row.replace('<', '&lt;')
                    row = row.replace('>', '&gt;')
                    row = row.replace('"', '&quot;')

                    value += row

            file.write('  <template name="{}" value="{}" description="{}" toReformat="true" toShortenFQNames="true">\n'.format(name, value, description))
            file.write('    <context>\n')
            file.write('      <option name="cpp" value="true" />\n')
            file.write('    </context>\n')
            file.write('  </template>\n')

        file.write('</templateSet>\n')


def main():
    parser = OptionParser()

    parser.add_option("-d", "--dir", dest="dir",
            help="The directory containing libraries for competitive programming")

    (options, args) = parser.parse_args()

    assert(os.path.exists(options.dir))

    generate_live_templates(options.dir)


if __name__ == '__main__':
    main()

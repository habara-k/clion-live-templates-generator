import os
import re
from optparse import OptionParser


def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)


def generate_live_templates(output_file, target_dir):

    with open(output_file,'w') as file:
        file.write('<templateSet group="C/C++">\n')

        assert(os.path.exists(target_dir))

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

    parser.add_option("-o", "--output", dest="output", default='C_C__.xml',
            help="The Live templates file to be generated")

    parser.add_option("-d", "--dir", dest="dir",
            help="The directory containing libraries for competitive programming")

    (options, args) = parser.parse_args()

    generate_live_templates(options.output, options.dir)


if __name__ == '__main__':
    main()

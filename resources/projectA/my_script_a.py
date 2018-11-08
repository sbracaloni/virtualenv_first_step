from io import StringIO

import yaml

if __name__ == '__main__':
    yaml_content = StringIO('info: Project A works !')
    data = yaml.load(yaml_content)
    print(data.get('info'))

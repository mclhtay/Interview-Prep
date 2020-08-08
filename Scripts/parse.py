
OPEN="{"
CLOSE="}"
def parse_default(setting: dict, user: str) -> dict:
  parsed_dict = {}
  parsed_dict['format'] = 'java'
  parsed_dict['comment'] = ['/*', "*/"]
  parsed_dict['template'] = 'public class '+user+'{\n\tpublic static void main(String [] args){\n\t\tSystem.out.println("'+user+' running");\n\t}\n}'
  return parsed_dict

def parse_java(setting: dict, user: str) -> dict:
  parsed_dict = {}
  parsed_dict['format'] = 'java'
  parsed_dict['comment'] = ['/*', "*/"]
  parsed_dict['template'] = 'public class '+user+'{\n\tpublic static void main(String [] args){\n\t\tSystem.out.println("'+user+' running");\n\t}\n}'
  return parsed_dict

def parse_python(setting: dict, user: str) -> dict:
  parsed_dict = {}
  parsed_dict['format'] = 'py'
  parsed_dict['comment'] = ["''' ", "''' "]
  parsed_dict['template'] = f'def main():\n\tprint("{user} running")\n\nif __name__ == "__main__": \n\tmain()'
  return parsed_dict

def parse_language(setting: dict, user: str) -> dict:

  p = setting['preferredLanguage']

  if p == 'java':
    return parse_java(setting, user)
  elif p == 'python':
    return parse_python(setting, user)
  else:
    return parse_default(setting, user)

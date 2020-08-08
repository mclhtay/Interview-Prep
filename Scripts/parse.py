
OPEN="{"
CLOSE="}"
def parse_default(setting: dict, user: str) -> dict:
  parsed_dict = {}
  parsed_dict['format'] = 'java'
  parsed_dict['comment'] = ['/*', "*/"]
  if 'includeImports' in setting and setting['includeImports']:
    parsed_dict['imports'] = "import java.util.*;"
  else:
    parsed_dict['imports'] = ""
  
  if 'includeUtils' in setting and setting['includeUtils']:

    parsed_dict['utils'] = 'class Node{\n\t\tint val; \n\t\tNode next;\n\t\tpublic Node(int x){this.val=x;}\n\t}\n\tclass TreeNode{\n\t\tint val; \n\t\tTreeNode left; \n\t\tTreeNode right;\n\t\tpublic TreeNode(int x){this.val=x;}\n\t}'
  else:
    parsed_dict['utils'] = ''

  parsed_dict['template'] = 'public class '+user+'{\n\t'+parsed_dict['utils']+'\n\tpublic static void main(String [] args){\n\t\tSystem.out.println("'+user+' running");\n\t}\n}'

  return parsed_dict

def parse_java(setting: dict, user: str) -> dict:
  parsed_dict = {}
  parsed_dict['format'] = 'java'
  parsed_dict['comment'] = ['/*', "*/"]
  if 'includeImports' in setting and setting['includeImports']:
    parsed_dict['imports'] = "import java.util.*;"
  else:
    parsed_dict['imports'] = ""

  if 'includeUtils' in setting and setting['includeUtils']:

    parsed_dict['utils'] = 'class Node{\n\t\tint val; \n\t\tNode next;\n\t\tpublic Node(int x){this.val=x;}\n\t}\n\tclass TreeNode{\n\t\tint val; \n\t\tTreeNode left; \n\t\tTreeNode right;\n\t\tpublic TreeNode(int x){this.val=x;}\n\t}'
  else:
    parsed_dict['utils'] = ''
    
  parsed_dict['template'] = 'public class '+user+'{\n\t'+parsed_dict['utils']+'\n\tpublic static void main(String [] args){\n\t\tSystem.out.println("'+user+' running");\n\t}\n}'


  return parsed_dict

def parse_python(setting: dict, user: str) -> dict:
  parsed_dict = {}
  parsed_dict['format'] = 'py'
  parsed_dict['comment'] = ["''' ", "''' "]
  parsed_dict['template'] = f'def main():\n\tprint("{user} running")\n\nif __name__ == "__main__": \n\tmain()'
  if 'includeImports' in setting and setting['includeImports']:
    parsed_dict['imports'] = "import collections"
  else:
    parsed_dict['imports'] = ""
  return parsed_dict

def parse_javascript(setting: dict, user: str) -> dict:
  parsed_dict = {}
  parsed_dict['format'] = 'js'
  parsed_dict['comment'] = ["/*", "*/"]
  parsed_dict['template'] = 'main()\n\nfunction main(){\n\tconsole.log("'+user+' running")\n}'
  parsed_dict['imports'] = ""
  return parsed_dict

def parse_language(setting: dict, user: str) -> dict:

  p = setting['preferredLanguage']

  if p == 'java':
    return parse_java(setting, user)
  elif p == 'python':
    return parse_python(setting, user)
  elif p =='javascript':
    return parse_javascript(setting, user)
  else:
    return parse_default(setting, user)

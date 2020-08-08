import json
import os
from parse import parse_language

cur_path = os.path.dirname(__file__)


default_setting = {"preferredLanguage": "java"}

def create_setting_dict(a: str) -> dict:
  user_setting_path = os.path.relpath(f'../UserSettings/{a}.setting.json', cur_path)
  if not os.path.isfile(user_setting_path):
    return parse_language(default_setting, a)

  user_setting_file = open(user_setting_path)
  user_setting = json.loads(user_setting_file.read())
  return parse_language(user_setting, a)
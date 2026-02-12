def format_name(f_name, l_name):
  """Take a first and last name and format it to retun the title case verson of the name""" # Documentation: Hover over format_name or multi-line comment
  
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"
  
print(format_name(f_name="jEnnY", l_name="MUSTERFRAU"))
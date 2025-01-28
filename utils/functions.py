import re

from dicts.habilidades import diccionario_BackEnd, diccionario_FrontEnd, diccionario_academic_degree, \
    diccionario_languages, \
    diccionario_soft_skill, keys_backend, keys_degree, \
    keys_frontend, keys_idiomas, \
    keys_soft_skill, patron_year


def ObtenerGradoEducativo(df, columna_descripcion):
  resultados_degree = []
  for i in range(len(df)):
    resultado_fila_degree = ""
    for key in keys_degree:
      pattern = re.compile(key)
      #print( type(df[columna_descripcion][i]) )
      try:
        if pattern.search(df[columna_descripcion][i]):
          resultado_fila_degree = resultado_fila_degree + diccionario_academic_degree[key] + ", "
      except:
        pass
    #Resultados grado academico
    resultado_fila_degree = resultado_fila_degree[0:-2]
    resultados_degree.append(resultado_fila_degree)

  return resultados_degree

def ObtenerIdiomas(df, columna_descripcion):
  resultados_idiomas = []
  for i in range(len(df)):
    resultado_fila_idioma = ""
    for key in keys_idiomas:
      pattern = re.compile(key)
      #print( type(df[columna_descripcion][i]) )
      try:
        if pattern.search(df[columna_descripcion][i]):
          resultado_fila_idioma = resultado_fila_idioma + diccionario_languages[key] + ", "
      except:
        pass
    #Resultados grado academico
    resultado_fila_idioma = resultado_fila_idioma[0:-2]
    resultados_idiomas.append(resultado_fila_idioma)

  return resultados_idiomas

def ObtenerYears(df, columna_descripcion):
  resultados_years= []
  for i in range(len(df)):
    resultado_fila_years_experience = ""
    try:
      if patron_year.search(df[columna_descripcion][i]):
        match_year = patron_year.findall(df[columna_descripcion][i])
        for m in match_year:
          resultado_fila_years_experience = resultado_fila_years_experience + m[0] + ", "
    except:
      pass
    resultado_fila_years_experience = resultado_fila_years_experience[0:-2]
    resultados_years.append(resultado_fila_years_experience)
  return resultados_years

def ObtenerSoftSkill(df, columna_descripcion):
  resultados_soft_skill = []
  for i in range(len(df)):
    resultado_fila_soft_skill = ""
    for key in keys_soft_skill:
      pattern = re.compile(key)
      try:
        if pattern.search(df[columna_descripcion][i]):
          resultado_fila_soft_skill = resultado_fila_soft_skill + diccionario_soft_skill[key] + ", "
      except:
        pass
    #Resultados de fila Soft skill
    resultado_fila_soft_skill = resultado_fila_soft_skill[0:-2]
    resultados_soft_skill.append(resultado_fila_soft_skill)

  return resultados_soft_skill

def ObtenerSkill_FrontEnd(df, columna_descripcion):
  resultados_skill_frontend= []
  for i in range(len(df)):
    resultado_fila_skill_frontend = ""
    for key in keys_frontend:
      pattern = re.compile(key, re.IGNORECASE)
      try:
        if pattern.search(df[columna_descripcion][i]):
          resultado_fila_skill_frontend = resultado_fila_skill_frontend + diccionario_FrontEnd[key] + ", "
      except:
        pass
    #Resultados skill Front End
    resultado_fila_skill_frontend = resultado_fila_skill_frontend[0:-2]
    resultados_skill_frontend.append(resultado_fila_skill_frontend)

  return resultados_skill_frontend

def ObtenerSkill_Backend(df, columna_descripcion):
  resultados_skill_backend= []
  for i in range(len(df)):
    resultado_fila_skill_backend = ""
    for key in keys_backend:
      pattern = re.compile(key, re.IGNORECASE)
      try:
        if pattern.search(df[columna_descripcion][i]):
              resultado_fila_skill_backend = resultado_fila_skill_backend + diccionario_BackEnd[key] + ", "
      except:
        pass
    #Resultados skill Front End
    resultado_fila_skill_backend = resultado_fila_skill_backend[0:-2]
    resultados_skill_backend.append(resultado_fila_skill_backend)

  return resultados_skill_backend


#Patron de remote
busqueda_remote = r"remot(o|e)"
patron_remote= re.compile(busqueda_remote, re.IGNORECASE)

def isRemote(df, columna_info):
  resultados_remote= []
  for i in range(len(df)):
    resultado_fila_remote = ""
    try:
      if patron_remote.search(df[columna_info][i]):
        resultado_fila_remote = "Remote"
      else:
        resultado_fila_remote = None
    except:
      pass
    resultados_remote.append(resultado_fila_remote)
  return resultados_remote
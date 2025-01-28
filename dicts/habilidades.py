import re

#Diccionario de grados academicos
diccionario_academic_degree = {
    #Espanol
    #La ingenieria tambien es una licenciatura
    r"((L|l)icenciatura|(I|i)ngenier(i|í)a|(L|l)icenciad(o|a)\s(en|de)|(I|i)ngenier(o|a)\s(en|de)|\sLic\.\s|\sIng\.\s)" : "Licenciatura",
    r"(M|m)aestr(i|í)a" : "Maestria",
    r"(D|d)octorado" : "Doctorado",
    #English
    r"((B|b)achelor('s)?|\sB(\.)?S(\.)?\sin)" : "Bachelor",
    r"((M|m)aster('s)?|\sM(\.)?S(\.)?(\s|\/P(H|h)(\.)?D)(or|in))" : "Master",
    r"P(H|h)(\.)?D" : "PhD"
}

def obtener_grado_academico(texto):
    for regex, grado in diccionario_academic_degree.items():
        if re.search(regex, texto):
            return grado
    return None


#Diccionario de Soft Skills
#Creo que hay pocos soft skill en español ya que la mayoria de las descripcion estaban en ingles
diccionario_soft_skill ={
    #Spanish
    r"\b(A|a)nal(í|i)tica\b" : "Capacidad Analitica",
    r"\b((C|c)reatividad|(C|c)reativ(a|o)s)\b" : "Creatividad",
    r"\b((E|e)mpuje\spor\sobtener\sresultados\b|(E|e)nfocado\sa\sresultados)\b" : "Enfocado a resultados",
    r"\b(M|m)anejo\sde\sconflictos\b" : "Manejo de conflictos",
    r"\b(I|i)nspirar\b" :"Inspirar",
    r"\b((O|o)rganizado|(O|o)rganizas)\b" : "Organizado",
    r"\b(P|p)roactiv(a|o)" : "Proactivo",
    r"\b(R|r)esoluci(ó|o)n\sde\sproblemas\b" : "Resolucion de problemas",
    r"\b(T|t)rabajo\sen\sequipo\b" : "Trabajo en equipo",
    r"\b(T|t)rabajar?\sde\sforma\sindependiente\b" : "Trabaja de forma independiente",
    #English
    r"\b((A|a)nalytical|(A|a)nalytics?)\b" : "Analitical",
    r"\b(A|a)ttention\sto\sdetails?\b" : "Attention to details",
    r"\b(C|c)oach\b" : "Coach",
    r"\b(C|c)ollaborat(e|es|ing|ion|ively)\b" : "Collaborate",
    r"\b(C|c)ommunicat(e|es|ion|ing)\b" : "Comunication skills",
    r"\b((C|c)ontinuously\s(L|l)earn|(L|l)earning|(L|l)earn)\b" : "Continuously learn",
    r"\b(C|c)reativity\b" : "Creativity",
    r"\b(C|c)uriosity\b" : "Curiosity",
    r"\b(C|c)ritical\s(T|t)hinking\b" : "Critical Thinking",
    r"\b(D|d)etail(\-|\s)(O|o)riented\b"
    r"\b(D|d)ealing\s(well)?\swith\sambiguity\b" : "Dealing well with ambiguity",
    r"\b(D|d)ynamic\s(E|e)nvironment\b":"Dynamic enviroment",
    r"\b(E|e)fficiency\b" : "Efficiency",
    r"\b(E|e)nthusiasm\b" : "Enthusiasm",
    r"\b(G|g)roup\sintegration\b" : "Group integration",
    r"\b(G|g)rowth\s(M|m)indset\b" : "Growth Mindset",
    r"\b(H|h)igh\s(S|s)tandars\b" : "High Standars",
    r"\b((I|i)ndependent\s(W|w)orker|(W|w)orks?\s(I|i)ndependently)\b" : "Independent Worker",
    r"\b((I|i)nnovati(on|ve)|(I|i)nnovators)\b" : "Innovation",
    r"\b(I|i)nvolved\b" : "Involved",
    r"\b(I|i)nterpersonal\b" : "Interpersonal",
    r"\b((L|l)eadership|(L|l)ead\sa\steam)\b" : "Leadership",
    r"\b(M|m)anaging\s\w*\steams\b" : "Managing teams",
    r"\b(M|m)entor\b" : "Mentor",
    r"\b(M|m)otivated\b" : "Motivated",
    r"\b(M|m)ultifunctional\stasking\b" : "Multifunctional tasking",
    r"\b(O|o)rganization(al)?\b" : "Organization",
    r"\b(P|p)lanification\b" : "Planification",
    r"\b(P|p)ositive\sattitude\b" : "Positive attitude",
    r"\b(P|p)rioritizing\sneeds\b" : "Prioritizing needs",
    r"\b(P|p)roactivity\b" : "Proactivity",
    r"\b((P|p)roblem(\-|\s)(solving|(S|s)olver))\b" : "Problem solving",
    r"\b(S|s)elf(\s|\-)directed\b" : "Self directed",
    r"\b(S|s)elf(\s|\-)management\b" : "Self Management",
    r"\b(S|s)elf(\s|\-)starter\b" : "Self Starter",
    r"\b(S|s)trategic\b" : "strategic",
    r"\b(T|t)arget(\s)?[-](\s)?(B|b)ased\s(R|r)esults\b" : "Target – Based results",
    r"\b(T|t)eam\s(P|p)layer" : "Team Player",
    r"\b(T|t)eam(\s)?(W|w)ork" : "Team Work",
    r"\b((W|w)ritten|(V|v)erbal|(O|o)ral)(\sand\s|\/|\s[&]\s)((W|w)ritten|(V|v)erbal|(O|o)ral)\b" : "Written and oral communication",
    r"\b(cross(\-|\s)functional\s(teams|partners)|(I|i)nterdisciplinary|multiple\sfunctional\sgroups)\b" : "Working with cross functional teams"
}

#Diccionario de Front end
diccionario_FrontEnd = {
    #learn the basics
    r"\bhtml5?\b" : "HTML",
    r"\bcss3?\b" : "CSS",
    r"\bjavascript\b" : "JavaScript",
    r"\bes\s2020[+]\b" : "ES 2020+",
    #javascript Task runners
    r"\bnpm\sscripts\b" : "npm Scripts",
    r"\bgulp\b" : "Gulp",
    r"\bgrunt\b" : "Grunt",
    #javascript woking with linux
    r"\benvironment\b" : "Environment",
    r"\bterminal\b" : "Terminal",
    #javascript version control
    r"\bgit\b" : "Git",
    r"\bgithub\b" : "Github",
    r"\bbit\sbucket\b" : "Bit bucket",
    #javascript module bundler
    r"\bwebpack\b" : "Webpack",
    r"\brollup\b" : "Rollup",
    #javascript testing
    r"\bjest\b" : "Jest",
    r"\bpuppeteer\b" : "Puppeteer",
    r"\bcupress\b" : "Cypress",
    #javascript libraries and framework
    r"\breact\b" : "React",
    r"\bangular\b" : "Angular",
    r"\bvue\b" : "Vue",
    r"\bnuxt(\.js)?\b" : "Nuxt.js",
    r"\bsvelte\b" : "Svelte",
    r"\bredux\b" : "Redux",
    r"\bxstate\b" : "Xstate",
    r"\brecoil\b" : "Recoil",
    r"\bnext\b" : "Next",
    r"\bgatsby\b" : "Gatsby",
    r"\benzyme\b" : "Enzime",
    r"\bjest\b" : "Jest",
    #css
    r"\bflexbox\b" : "Flexbox",
    r"\bcss\sgrid\b" : "CSS grid",
    #css pre processors
    r"\bsass\b" : "SASS",
    r"\bpostcss\b" : "PostCSS",
    #css framework
    r"\bstyled\scomponents\sreact\b" : "Styled Components React",
    r"\btailwind\scss\b" : "TailWind Css",
    r"\bbulma\b" : "Bulma",
    r"\bbootstraps\b" : "Bootstraps",
    #CI/CD
    r"\bgithub\sactions\b" : "Github Actions",
    #Deployment
    r"\bs3\b" : "S3",
    r"\bsurge\.sn\b" : "Surge.sn",
    r"\bvercel\b" : "Vercel",
    r"\bfirebase\b" : "Firebase",
    r"\bnetlify\b" : "Netlify"
}

#Diccionario de Backend
diccionario_BackEnd = {
    #Essentials
    r"\blinux\b" : "Linux",
    r"\bgit\b" : "Git",
    r"\bgithub\b" : "Github",
    #Languages
    r"\bc[#]\b" : "c#",
    r"\bgo\b" : "Go",
    r"\b\.net\b" : ".NET",
    r"\bjava\b" : "Java",
    r"\bspring\sframework\b" : "Spring Framework",
    r"\bhibernate\b" : "Hibernate",
    r"\bjavascript\b" : "JavaScript",
    r"\bnode(\.js)?\b" : "Node.js",
    r"\bexpress\b" : "Express",
    r"\bfastify\b" : "Fastify",
    r"\bpython\b" : "Python",
    r"\bflask\b" : "Flask",
    r"\bdjango\b" : "Django",
    #Database
    r"\bsql\b" : "SQL",
    r"\bmysql\b" : "MySQL",
    r"\bpostgresql\b" : "PostgreSQL",
    r"\boracle\b" : "Oracle",
    r"\b(mssql|sql\sserver)\b" : "MSSQL",
    r"\bnosql\b" : "NoSQL",
    r"\bmongodb\b" : "MongoDB",
    r"\bdynamodb\b" : "DynamoDB",
    r"\bcassandra\b" : "Cassandra",
    r"\binmemory\b" : "Inmemory",
    r"\bredis\b" : "Redis",
    #Storage
    r"\bawss3\b" : "AWSS3",
    r"\b(azure\s)?blob\sstorage\b" : "Azure Blob Storage",
    #Services and APIs
    r"\bresful\sapis?\b" : "Restful APIs",
    r"\bmicroservices\sarchitecture\b" : "Microservices Architecture",
    r"\bgraphql\b" : "GraphQL",
    #Develops and deployment
      #containerization orchestration
    r"\bdocker\b" : "Docker",
    r"\bkubernetes\b" : "Kubernetes",
    r"\bdevops\b" : "Devops",
    r"\baws\b" : "AWS",
    r"\bazure\b" : "Azure",
    r"\bdigital\socean\b" : "Digital Ocean",
    r"\bheroku\b" : "HerokU",
    r"\bnetlify\b" : "Netlify",
    r"\baws\slambda\b" : "AWS Lambda",
    r"\bazure\sfunction\b" : "Azure Function",
    r"\bservreless\sframework\b" : "Serverless Framework",
    r"\baws\scdk\b" : "AWS CDK",
    #CI/CD
    r"\bgithub\sactions\b" : "Github Actions",
    r"\bjenikins(\sx)?\b" : "Jenikins",
    r"\bcircle\sci\b" : "Circle CI",
    #security
    r"\bowasp\b" : "OWASP",
    r"\bprotective\sservices\s(and|[&])\sdatabase\sagainst\sthreats\b" : "Protective Services and database against threats"
}

diccionario_Data = {
    # Essentials
    r"\blinux\b" : "Linux",
    r"\bgit\b" : "Git",
    r"\bgithub\b" : "Github",
    r"\bexcel\b" : "Excel",
    r"\btableau\b" : "Tableau",
    r"\bpower\sbi\b" : "Power BI",
    r"\bjupyter\snotebooks?\b" : "Jupyter Notebooks",
    r"\bgoogle\sdata\sstudio\b" : "Google Data Studio",
    r"\blookers?\b" : "Looker",
    r"\bapache\ssuperset\b" : "Apache Superset",

    # Languages
    r"\bpython\b" : "Python",
    r"\br\b" : "R",
    r"\bsql\b" : "SQL",
    r"\bjulia\b" : "Julia",
    r"\bscala\b" : "Scala",
    r"\bjava\b" : "Java",
    r"\bspark\b" : "Apache Spark",

    # Libraries for Data Science / Analysis
    r"\bpandas\b" : "Pandas",
    r"\bnumpy\b" : "NumPy",
    r"\bmatplotlib\b" : "Matplotlib",
    r"\bseaborn\b" : "Seaborn",
    r"\bscikit-learn\b" : "Scikit-learn",
    r"\bkeras\b" : "Keras",
    r"\btensorflow\b" : "TensorFlow",
    r"\bpytorch\b" : "PyTorch",
    r"\bdask\b" : "Dask",
    r"\bmlflow\b" : "MLFlow",
    r"\bnltk\b" : "NLTK",
    r"\bspacy\b" : "SpaCy",

    # Big Data / Processing
    r"\bhadoop\b" : "Hadoop",
    r"\bkafka\b" : "Kafka",
    r"\bairflow\b" : "Apache Airflow",
    r"\bsnowflake\b" : "Snowflake",
    r"\bdatabricks\b" : "Databricks",
    r"\bredshift\b" : "Amazon Redshift",
    r"\bbigquery\b" : "Google BigQuery",

    # Databases
    r"\bmysql\b" : "MySQL",
    r"\bpostgresql\b" : "PostgreSQL",
    r"\bmongodb\b" : "MongoDB",
    r"\bcassandra\b" : "Cassandra",
    r"\bdynamodb\b" : "DynamoDB",
    r"\bsqlite\b" : "SQLite",

    # Cloud Platforms
    r"\baws\b" : "AWS",
    r"\bazure\b" : "Azure",
    r"\bgcp\b" : "Google Cloud Platform",
    r"\bdataproc\b" : "Google Dataproc",
    r"\bemr\b" : "AWS EMR",
    r"\blambda\b" : "AWS Lambda",

    # Visualization Tools
    r"\btableau\b" : "Tableau",
    r"\bpower\sbi\b" : "Power BI",
    r"\bmatplotlib\b" : "Matplotlib",
    r"\bseaborn\b" : "Seaborn",
    r"\bplotly\b" : "Plotly",
    r"\bd3\.js\b" : "D3.js",

    # Machine Learning / AI
    r"\bmachine\slearning\b" : "Machine Learning",
    r"\bdeep\slearning\b" : "Deep Learning",
    r"\bclustering\b" : "Clustering",
    r"\bclassification\b" : "Classification",
    r"\bregression\b" : "Regression",
    r"\bnatural\slanguage\sprocessing\b" : "Natural Language Processing",
    r"\bmodel\sevaluation\b" : "Model Evaluation",
    r"\bhyperparameter\stuning\b" : "Hyperparameter Tuning",
    r"\bfeature\sengineering\b" : "Feature Engineering",

    # ETL / Pipelines
    r"\betl\b" : "ETL",
    r"\bpipelines?\b" : "Pipelines",
    r"\bdata\scleansing\b" : "Data Cleansing",
    r"\bdata\sintegration\b" : "Data Integration",
    r"\bdata\stransformation\b" : "Data Transformation",

    # Security / Governance
    r"\bdata\sgovernance\b" : "Data Governance",
    r"\bdata\squality\b" : "Data Quality",
    r"\bdata\ssecurity\b" : "Data Security",
    r"\bgdpr\b" : "GDPR",
    r"\bcicd\b" : "CI/CD",
}


#Diccionario de idiomas
diccionario_languages = {
    #Ingles
    r"\b((A|a)dvanced?\s(or\sfluent\s)?(in\s)?(E|e)nglish|C1)\b" : "Advanced English",
    r"\b(I|i)ntermediate(\s?\-\s?(A|a)dvanced?)?\s(E|e)nglish\b" : "Intermediate English",
    r"\b(F|f)luent\sin\s(w+\sand\s)?(E|e)nglish\b" : "Fluent in English",
    r"\b((B|b)iling(ü|u)e|(B|b)i(\s|\-)(L|l)ingual)\b" : "Bilingue",
    #Español
    r"\b(I|i)ngl(e|é|é)s[:]?\s((I|i)ntermedio[-])?(A|a)vanzado\b" : "Ingles Avanzado",
    r"\b(I|i)ngl(e|é|é)s\st(e|é)cnico\b" : "Ingles Tecnico",
    r"\b(I|i)ngl(e|é|é)s[:]?\s((N|n)ivel\s)?(I|i)ntermedio\b" : "Ingles Intermedio",
    r"\b(I|i)ngl(e|é|é)s[:]?\s((N|n)ivel\s(I|i)ntermedio\s)?(A|a)lto\b" : "Ingles Avanzado",
    #Algunas descripciones no especificaban nivel, solo mencionaban que se necesitaba ingles
    r"\b(I|i)ngl(e|é|é)s\b" : "Ingles",
    r"\bEnglish\b" : "English",
    r"\bItalian\b": "Italian",
    r"\bPortuguese\b" : "Portuguese",
    r"\bSpanish\b" : "Spanish"
}

#Patron de years of experience
busqueda_years_experience = r"((\+?([0-4]?[0-9]|[1-9])\+?(\s?[-]\s?|\sto\s))?\+?([0-4]?[0-9]|[1-9])\+?\s((Y|y)ears?|(A|a)(ñ|ñ)os?))"
patron_year = re.compile(busqueda_years_experience)

diccionario_fullStack = {}
diccionario_fullStack.update(diccionario_BackEnd)
diccionario_fullStack.update(diccionario_FrontEnd)
diccionario_fullStack.update(diccionario_Data)


keys_degree = diccionario_academic_degree.keys()
keys_soft_skill = diccionario_soft_skill.keys()
keys_backend = diccionario_BackEnd.keys()
keys_frontend = diccionario_FrontEnd.keys()
keys_idiomas = diccionario_languages.keys()
keys_data = diccionario_Data.keys()
keys_fullstack = diccionario_fullStack.keys()
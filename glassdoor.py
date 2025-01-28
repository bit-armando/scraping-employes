from datetime import date
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from dicts.habilidades import keys_fullstack
from utils.functions import *

urls_usa = ['https://www.glassdoor.com.mx/Empleo/estados-unidos-data-analyst-empleos-SRCH_IL.0,14_IN1_KO15,27.htm',
        'https://www.glassdoor.com.mx/Empleo/estados-unidos-data-scientist-empleos-SRCH_IL.0,14_IN1_KO15,29.htm',
        'https://www.glassdoor.com.mx/Empleo/estados-unidos-data-engineering-empleos-SRCH_IL.0,14_IN1_KO15,31.htm',
        'https://www.glassdoor.com.mx/Empleo/estados-unidos-cloud-computing-empleos-SRCH_IL.0,14_IN1_KO15,30.htm,',
        'https://www.glassdoor.com.mx/Empleo/estados-unidos-front-end-empleos-SRCH_IL.0,14_IN1_KO15,24.htm',
        'https://www.glassdoor.com.mx/Empleo/estados-unidos-back-end-empleos-SRCH_IL.0,14_IN1_KO15,23.htm',
        'https://www.glassdoor.com.mx/Empleo/estados-unidos-full-stack-empleos-SRCH_IL.0,14_IN1_KO15,25.htm']

urls_mex = ['https://www.glassdoor.com.mx/Empleo/m%C3%A9xico-analista-de-datos-empleos-SRCH_IL.0,6_IN169_KO7,24.htm',
            'https://www.glassdoor.com.mx/Empleo/m%C3%A9xico-cient%C3%ADfico-de-datos-empleos-SRCH_IL.0,6_IN169_KO7,26.htm',
            'https://www.glassdoor.com.mx/Empleo/m%C3%A9xico-ingeniero-de-datos-empleos-SRCH_IL.0,6_IN169_KO7,25.htm',
            'https://www.glassdoor.com.mx/Empleo/m%C3%A9xico-devops-empleos-SRCH_IL.0,6_IN169_KO7,13.htm',
            'https://www.glassdoor.com.mx/Empleo/m%C3%A9xico-front-end-empleos-SRCH_IL.0,6_IN169_KO7,16.htm',
            'https://www.glassdoor.com.mx/Empleo/m%C3%A9xico-back-end-empleos-SRCH_IL.0,6_IN169_KO7,15.htm',
            'https://www.glassdoor.com.mx/Empleo/m%C3%A9xico-full-stack-empleos-SRCH_IL.0,6_IN169_KO7,17.htm']

def find_jobs(url):
    wd = webdriver.Chrome()
    wd.get(url)

    jobs = wd.find_elements(By.XPATH, '//*[@class="JobCard_jobCardContainer__arQlW"]')
    jobs_list = []
    today = date.today().strftime('%Y-%m-%d')

    for job in jobs:
        job_url = job.find_element(By.XPATH, './/div/div/a[@class="JobCard_jobTitle__GLyJ1"]').get_attribute('href')
        print(job_url)
        try: # Cerrar ventana emergente
            wd.find_element(By.XPATH, '//*[@class="CloseButton"]').click()
            # sleep(1)
        except:
            job.click()

        try: # Mostrar mas detalles
            wd.find_element(By.XPATH, '//*[@class="JobDetails_showMore___Le6L"').click()
        except:
            pass

        description = wd.find_element(By.XPATH, '//*[@class="JobDetails_jobDetailsContainer__y9P3L"]')
        title = description.find_element(By.XPATH, '//*[@class="heading_Heading__BqX5J heading_Level1__soLZs"]').text
        company = description.find_element(By.XPATH, '//*[@class="heading_Heading__BqX5J heading_Subhead__Ip1aW"]').text
        place = description.find_element(By.XPATH, '//div[@class="JobDetails_location__mSg5h"]').text
        try:
            salary = job.find_element(By.XPATH, './/div/div/div[@class="JobCard_salaryEstimate__QpbTW"]').text
        except:
            salary = None
        post_date = None

        try:
            tecnical_skills = set()
            for regex in keys_fullstack:
                tecnical_skills.update([x.group() for x in re.finditer(regex, description.text, re.IGNORECASE)])
            tecnical_skills = '\n'.join(tecnical_skills)
        except:
            tecnical_skills = None


        # sleep(1)
        jobs_list.append({
            'place': place,
            'company': company,
            'position': title,
            #Academic profile
            #English
            'tecnic_skills': tecnical_skills,
            'salary': salary,
            'source': 'glassdoor',
            'link': job_url,
            'description': description.text,
        })

    df = pd.DataFrame(jobs_list)

    grade = ObtenerGradoEducativo(df, 'description')
    df = pd.concat([df, pd.DataFrame(grade, columns=['Academic'])], axis=1)

    languages = ObtenerIdiomas(df, 'description')
    df = pd.concat([df, pd.DataFrame(languages, columns=['Languages'])], axis=1)

    years = ObtenerYears(df, 'description')
    df = pd.concat([df, pd.DataFrame(years, columns=['Years'])], axis=1)

    soft_skills = ObtenerSoftSkill(df, 'description')
    df = pd.concat([df, pd.DataFrame(soft_skills, columns=['SoftSkills'])], axis=1)

    frontend = ObtenerSkill_FrontEnd(df, 'description')
    df = pd.concat([df, pd.DataFrame(frontend, columns=['Frontend'])], axis=1)

    backend = ObtenerSkill_Backend(df, 'description')
    df = pd.concat([df, pd.DataFrame(backend, columns=['Backend'])], axis=1)

    remote = isRemote(df, 'description')
    df = pd.concat([df, pd.DataFrame(remote, columns=['Remote'])], axis=1)

    df = df.drop(columns=['description'])
    wd.quit()
    return df

# df_data_analyst = find_jobs(urls_usa[0])
# df_data_scientist = find_jobs(urls_usa[1])
# df_data_engineering = find_jobs(urls_usa[2])
# df_cloud_computing = find_jobs(urls_usa[3])
# df_front_end = find_jobs(urls_usa[4])
# df_back_end = find_jobs(urls_usa[5])
# df_full_stack = find_jobs(urls_usa[6])

df_data_analyst = find_jobs(urls_mex[0])
df_data_scientist = find_jobs(urls_mex[1])
df_data_engineering = find_jobs(urls_mex[2])
df_cloud_computing = find_jobs(urls_mex[3])
df_front_end = find_jobs(urls_mex[4])
df_back_end = find_jobs(urls_mex[5])
df_full_stack = find_jobs(urls_mex[6])

df_data_analyst.to_csv('data_analyst.csv', index=False)
df_data_scientist.to_csv('data_scientist.csv', index=False)
df_data_engineering.to_csv('data_engineering.csv', index=False)
df_cloud_computing.to_csv('cloud_computing.csv', index=False)
df_front_end.to_csv('front_end.csv', index=False)
df_back_end.to_csv('back_end.csv', index=False)
df_full_stack.to_csv('full_stack.csv', index=False)
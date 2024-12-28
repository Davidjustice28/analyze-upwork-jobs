import csv
import timeit

frontend_frameworks = ['react', 'vue', 'angular', 'svelte', 'next.js', 'remix', 'nuxt']
programming_languages = ['javascript', 'golang', 'python', 'ruby', 'rust', 'typescript', 'php', 'java', 'c#']
platforms = ['webflow', 'bubble', 'wix', 'wordpress', 'shopify', 'framer', 'squarespace']
technologies = ['html', 'css', 'scss', 'sass', 'tailwind', 'bootstrap', 'sql', 'mongodb', 'firebase', 'aws', 'gcp', 'azure', 'docker', 'kubernetes', 'nginx', 'apache']
skills = ['rest api', 'graphql', 'responsive', 'accessibility', 'seo', 'testing', 'performance']
keywords = frontend_frameworks + programming_languages + platforms + technologies + skills

def analyze_jobs():
  print('Analyzing Upwork jobs\n')
  with open('all_upwork_jobs_2024-05-21-2024-07-25.csv') as file:
    reader = csv.reader(file)
    hr_low_rates = {}
    hr_high_rates = {}
    budgets = {}
    jobs = {}
    total_jobs_analyzed = 0

    for title, link, published_date, is_hourly, hourly_low, hourly_high, budget, country in reader:
      total_jobs_analyzed+=1

      for keyword in keywords:
        index = title.lower().find(keyword)
        if index != -1:
          if keyword in jobs:
            jobs[keyword] +=1
          else:
            jobs[keyword] = 1

          if len(hourly_low) > 0:
            if keyword in hr_low_rates:
              hr_low_rates[keyword].append(float(hourly_low))
            else:
              hr_low_rates[keyword] = [float(hourly_low)]

          if len(hourly_high) > 0:
            if keyword in hr_high_rates:
              hr_high_rates[keyword].append(float(hourly_high))
            else:
              hr_high_rates[keyword] = [float(hourly_high)]

          if len(budget) > 0:
            if keyword in budgets:
              budgets[keyword].append(float(budget))
            else:
              budgets[keyword] = [float(budget)]

    framework_counts = []
    language_counts = []
    platform_counts = []
    technology_counts = []
    skill_counts = []

    for key, value in jobs.items():
      pair = (key, value)
      if key in frontend_frameworks:
        framework_counts.append(pair)
      elif key in platforms:
        platform_counts.append(pair)
      elif key in programming_languages:
        language_counts.append(pair)
      elif key in skills:
        skill_counts.append(pair)
      elif key in technologies:
        technology_counts.append(pair)
      else:
        continue
    
    state_in_demand_by_category(framework_counts, language_counts, platform_counts, technology_counts, skill_counts)

    print(f"\nTotal job postings analyzed: {total_jobs_analyzed}")

    
def find_most_in_demand(list):
  sorted_list = sorted(list, key=lambda x: x[1], reverse=True)
  results = sorted_list[:3]
  return results

def state_in_demand_by_category(frontend_counts, language_counts, platform_counts, technology_counts, skill_counts):
  frontend_result = find_most_in_demand(frontend_counts)
  language_result = find_most_in_demand(language_counts)
  platform_result = find_most_in_demand(platform_counts)
  tech_result = find_most_in_demand(technology_counts)
  skill_result = find_most_in_demand(skill_counts)

  print("\nThe most in demand frontend frameworks are: \n")

  for framework, job_count in frontend_result:
    print(f"{framework}: {job_count}")

  print("\nThe most in demand programming languages are: \n")

  for language, job_count in language_result:
    print(f"{language}: {job_count}")

  print("\nThe most in demand web platforms are: \n")

  for platform, job_count in platform_result:
    print(f"{platform}: {job_count}")


  print("\nThe most in demand technologies are: \n")

  for tech, job_count in tech_result:
    print(f"{tech}: {job_count}")

  print("\nThe most in demand skills are: \n")

  for skill, job_count in skill_result:
    print(f"{skill}: {job_count}")

time_elapsed = timeit.timeit(analyze_jobs, number=1)
print(f"Time taken: {time_elapsed:.5f} seconds")
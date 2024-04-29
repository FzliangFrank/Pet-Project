library(rvest)
library(purrr)
library(tidyverse)

SEARCH_TERM = "data analyst"
search_term=stringr::str_replace(SEARCH_TERM, ' ', '%20')
LNK_JOBS=glue::glue("https://www.linkedin.com/jobs/search/?currentJobId=3816100484&keywords={search_term}&origin=JOBS_HOME_SEARCH_BUTTON&refresh=true")


linkedin_job = read_html_live(LNK_JOBS)
linkedin_job |> 
  html_element("scaffold")

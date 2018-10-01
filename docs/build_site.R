#Set our working directory. 
  # Taken pretty much directly from: http://nickstrayer.me/RMarkdown_Sites_tutorial/
#This helps avoid confusion if our working directory is 
#not our site because of other projects we were 
#working on at the time. 
setwd("~/GoogleDrive/JobMaterials/EEB504/EEB504/docs/")

#render your sweet site. 
rmarkdown::render_site()
#
#
#
#
#
#install.packages("tidymodels")
library(tidymodels) |> suppressMessages() # for the parsnip package, along with the rest of tidymodels
# Helper packages
library(readr)       # for importing data
library(broom.mixed) # for converting bayesian models to tidy tibbles
library(dotwhisker)  # for visualizing regression results
#
#
#
urchins <-
  # Data were assembled for a tutorial 
  # at https://www.flutterbys.com.au/stats/tut/tut7.5a.html
  read_csv("https://tidymodels.org/start/models/urchins.csv") %>% 
  # Change the names to be a little more verbose
  setNames(c("food_regime", "initial_volume", "width")) %>% 
  # Factors are very helpful for modeling, so we convert one column
  mutate(food_regime = factor(food_regime, levels = c("Initial", "Low", "High")))
#
#
#
urchins
ggplot(urchins,
       aes(x = initial_volume, 
           y = width, 
           group = food_regime, 
           col = food_regime)) + 
  geom_point() + 
  geom_smooth(method = lm, se = FALSE) +
  scale_color_viridis_d(option = "plasma", end = .7)
#
#
#
library(keras)
lm_mod=linear_reg() |> 
  set_engine("keras")
# install.packages("keras")
lm_fit=lm_mod |> fit(width ~ initial_volume * food_regime, data = urchins)
#
#
#

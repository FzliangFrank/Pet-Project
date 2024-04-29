# What is Learnr?
Learnr is a package let you use rmd as an interactive notebook to execute code. Good for learnin code (any code!) in any rmd supported programming languages. 

# Best practice? 

Include in an r package and 
I found useful to use _index.rmd and link seperate file in a code chunck as child chunk. 

*convension* for index other files: 
- `index.rmd` 
- `_01.rmd` do not include a title yet just so that 
- `_02.rmd` 
- `_03.rmd` 

Draw back is in development you wil spend a lot of time go back and forward from `_index.rmd` to current section you are writting. 